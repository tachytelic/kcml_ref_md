#!/usr/bin/env python3
"""
Kerridge ERP MCP Server
Exposes live ERP data from KISAM K-Open 3 files via KCML query programs.

Tools:
  find_customer     - search customers by name fragment
  get_orders        - list orders for a customer account
  get_order_detail  - full order detail with line and pick status

Transport modes:

  stdio (Claude Desktop local config):
    python3 server.py

  HTTP/SSE (Claude Desktop via SSH tunnel or network):
    python3 server.py --http --port 8765

    Claude Desktop config (claude_desktop_config.json):
      {
        "mcpServers": {
          "kerridge-erp": {
            "url": "http://localhost:8765"
          }
        }
      }

    SSH tunnel (run on your LOCAL machine):
      ssh -L 8765:localhost:8765 user@erpserver
"""

import argparse
import json
import subprocess
import sys
import uuid
import queue
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# ── Configuration ─────────────────────────────────────────────────────────────

KCML_BIN   = "/usr/lib/kcml/kcml"
UF_JSON_SO = str(Path(__file__).parent.parent / "UFN/json_escape/uf_json.so")
KCML_DIR   = Path(__file__).parent / "kcml"

SOP_DIR      = "/user1/kopen/sop"
ACCOUNTS_DIR = "/user1/kopen/accounts"

# ── KCML runner ───────────────────────────────────────────────────────────────

def run_kcml(script: str, *args: str, timeout: int = 30):
    script_path = KCML_DIR / script
    cmd = [KCML_BIN, "-x", UF_JSON_SO, "-p", str(script_path)] + list(args)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"KCML script {script} timed out after {timeout}s")

    output = result.stdout.strip()
    if not output:
        raise RuntimeError(f"KCML script {script} produced no output (exit {result.returncode})")

    try:
        data = json.loads(output)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON from {script}: {e}\nOutput: {output[:300]}")

    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(data["error"])

    return data

# ── Tool implementations ───────────────────────────────────────────────────────

def find_customer(name: str) -> str:
    if not name or not name.strip():
        return json.dumps({"error": "name parameter is required"})
    try:
        return json.dumps(run_kcml("find_customer.src", ACCOUNTS_DIR, name.strip()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_orders(account: str) -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    try:
        return json.dumps(run_kcml("get_orders.src", SOP_DIR, account.strip().upper()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_order_detail(order: str) -> str:
    if not order or not order.strip():
        return json.dumps({"error": "order parameter is required"})
    try:
        return json.dumps(run_kcml("get_order_detail.src", SOP_DIR, order.strip()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

# ── MCP tool definitions ───────────────────────────────────────────────────────

TOOLS = [
    {
        "name": "find_customer",
        "description": (
            "Search the Kerridge ERP customer master (SALLED01) for customers "
            "whose name contains the given fragment. Case-insensitive. "
            "Returns account code, name, current balance, credit limit, and "
            "whether the account is on stop. Use this first to look up a "
            "customer account code before calling get_orders."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Name fragment, e.g. 'smith' or 'namco'"}
            },
            "required": ["name"],
        },
    },
    {
        "name": "get_orders",
        "description": (
            "Return all active sales orders for a customer account code from "
            "the Kerridge ERP order header file (OEHDR01). Shows order number, "
            "date, customer reference, delivery name/postcode, and order value."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string", "description": "Customer account code, e.g. 'P6750'"}
            },
            "required": ["account"],
        },
    },
    {
        "name": "get_order_detail",
        "description": (
            "Return full detail for a single sales order: header, all lines "
            "with part number, description, unit of measure, price, and pick "
            "status (qty_picked vs qty_outstanding from OEPIK01)."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "order": {"type": "string", "description": "Sales order number, e.g. '700002'"}
            },
            "required": ["order"],
        },
    },
]

TOOL_FNS = {
    "find_customer":    lambda a: find_customer(a.get("name", "")),
    "get_orders":       lambda a: get_orders(a.get("account", "")),
    "get_order_detail": lambda a: get_order_detail(a.get("order", "")),
}

# ── JSON-RPC message handler ───────────────────────────────────────────────────

def handle_message(msg: dict):
    method = msg.get("method")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "kerridge-erp", "version": "1.0.0"},
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS}}

    if method == "tools/call":
        params    = msg.get("params", {})
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})
        if tool_name not in TOOL_FNS:
            return {"jsonrpc": "2.0", "id": msg_id,
                    "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}}
        try:
            output = TOOL_FNS[tool_name](tool_args)
        except Exception as e:
            output = json.dumps({"error": str(e)})
        return {
            "jsonrpc": "2.0", "id": msg_id,
            "result": {"content": [{"type": "text", "text": output}], "isError": False},
        }

    if method == "ping":
        return {"jsonrpc": "2.0", "id": msg_id, "result": {}}

    if msg_id is not None:
        return {"jsonrpc": "2.0", "id": msg_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"}}
    return None

# ── stdio transport ────────────────────────────────────────────────────────────

def run_stdio():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        response = handle_message(msg)
        if response is not None:
            print(json.dumps(response), flush=True)

# ── HTTP / SSE transport ───────────────────────────────────────────────────────
#
# Claude Desktop HTTP-MCP protocol:
#   GET  /sse              → long-lived SSE stream; first event announces POST endpoint
#   POST /messages?sessionId=X → JSON-RPC request; response sent back via SSE stream
#   GET  /health           → {"status":"ok"}
#
# Each SSE client gets a session id and a queue. The POST handler looks up the
# queue by session id and pushes the JSON-RPC response onto it; the SSE handler
# drains the queue and writes events to the open connection.

# session_id -> queue.Queue
_sessions: dict[str, queue.Queue] = {}
_sessions_lock = threading.Lock()


class MCPHandler(BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        pass  # suppress request log

    # ── GET ──────────────────────────────────────────────────────────────────

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/health":
            self._json_response(200, {"status": "ok"})
            return

        if parsed.path == "/sse":
            self._handle_sse()
            return

        self.send_response(404)
        self.end_headers()

    def _handle_sse(self):
        session_id = str(uuid.uuid4())
        q: queue.Queue = queue.Queue()
        with _sessions_lock:
            _sessions[session_id] = q

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Tell the client where to POST requests
        endpoint = f"/messages?sessionId={session_id}"
        self._sse_write(f"event: endpoint\ndata: {endpoint}\n\n")

        # Stream responses until client disconnects
        try:
            while True:
                try:
                    payload = q.get(timeout=15)
                    if payload is None:          # shutdown signal
                        break
                    data = json.dumps(payload)
                    self._sse_write(f"event: message\ndata: {data}\n\n")
                except queue.Empty:
                    self._sse_write(": ping\n\n")  # keepalive comment
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            with _sessions_lock:
                _sessions.pop(session_id, None)

    def _sse_write(self, text: str):
        self.wfile.write(text.encode())
        self.wfile.flush()

    # ── POST ─────────────────────────────────────────────────────────────────

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != "/messages":
            self.send_response(404)
            self.end_headers()
            return

        params = parse_qs(parsed.query)
        session_id = (params.get("sessionId") or [""])[0]

        with _sessions_lock:
            q = _sessions.get(session_id)

        if q is None:
            self._json_response(400, {"error": f"Unknown sessionId: {session_id}"})
            return

        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length)

        # Acknowledge immediately — response comes via SSE
        self.send_response(202)
        self.send_header("Content-Length", "0")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Process in a thread so we don't block the HTTP server
        def process():
            try:
                msg = json.loads(body)
            except json.JSONDecodeError:
                return
            response = handle_message(msg)
            if response is not None:
                q.put(response)

        threading.Thread(target=process, daemon=True).start()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    # ── helpers ───────────────────────────────────────────────────────────────

    def _json_response(self, code: int, data):
        payload = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(payload))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(payload)


def run_http(port: int):
    server = HTTPServer(("0.0.0.0", port), MCPHandler)
    print(f"Kerridge ERP MCP server listening on port {port}", file=sys.stderr, flush=True)
    print(f"SSE endpoint : http://localhost:{port}/sse", file=sys.stderr, flush=True)
    print(f"Health check : http://localhost:{port}/health", file=sys.stderr, flush=True)
    server.serve_forever()

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kerridge ERP MCP Server")
    parser.add_argument("--http", action="store_true", help="HTTP/SSE mode (default: stdio)")
    parser.add_argument("--port", type=int, default=8765, help="HTTP port (default 8765)")
    args = parser.parse_args()

    if args.http:
        run_http(args.port)
    else:
        run_stdio()
