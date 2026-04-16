#!/usr/bin/env python3
"""
Kerridge ERP MCP Server
Exposes live ERP data from KISAM K-Open 3 files via KCML query programs.

Tools:
  find_customer     - search customers by name fragment
  get_orders        - list orders for a customer account
  get_order_detail  - full order detail with line and pick status

Usage (stdio mode, for Claude Desktop):
  python3 server.py

Usage (HTTP/SSE mode, for multi-user network access):
  python3 server.py --http --port 8765
"""

import argparse
import json
import subprocess
import sys
import os
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

KCML_BIN    = "/usr/lib/kcml/kcml"
UF_JSON_SO  = str(Path(__file__).parent.parent / "UFN/json_escape/uf_json.so")
KCML_DIR    = Path(__file__).parent / "kcml"

SOP_DIR      = "/user1/kopen/sop"
ACCOUNTS_DIR = "/user1/kopen/accounts"

# ── KCML runner ───────────────────────────────────────────────────────────────

def run_kcml(script: str, *args: str, timeout: int = 30) -> dict | list:
    """
    Run a KCML script with the JSON_ESCAPE UFN loaded.
    Returns parsed JSON output, or raises RuntimeError on failure.
    """
    script_path = KCML_DIR / script
    cmd = [KCML_BIN, "-x", UF_JSON_SO, "-p", str(script_path)] + list(args)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError(f"KCML script {script} timed out after {timeout}s")

    output = result.stdout.strip()
    if not output:
        raise RuntimeError(f"KCML script {script} produced no output (exit {result.returncode})")

    try:
        data = json.loads(output)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"KCML script {script} produced invalid JSON: {e}\nOutput: {output[:500]}")

    if isinstance(data, dict) and "error" in data:
        raise RuntimeError(data["error"])

    return data

# ── Tool implementations ───────────────────────────────────────────────────────

def find_customer(name: str) -> str:
    """
    Search for customers by name fragment (case-insensitive).
    Returns a JSON array of matching customers with account code, name,
    current balance, credit limit, and on-stop flag.
    """
    if not name or not name.strip():
        return json.dumps({"error": "name parameter is required"})
    try:
        results = run_kcml("find_customer.src", ACCOUNTS_DIR, name.strip())
        return json.dumps(results, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})


def get_orders(account: str) -> str:
    """
    Return all active orders for a customer account code.
    Each order shows order number, date, customer reference,
    delivery name/postcode, and order value.
    """
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    try:
        results = run_kcml("get_orders.src", SOP_DIR, account.strip().upper())
        return json.dumps(results, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})


def get_order_detail(order: str) -> str:
    """
    Return full detail for a single order including all lines, quantities,
    prices, and pick status (picked vs still outstanding) from OEPIK01.
    """
    if not order or not order.strip():
        return json.dumps({"error": "order parameter is required"})
    try:
        result = run_kcml("get_order_detail.src", SOP_DIR, order.strip())
        return json.dumps(result, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

# ── MCP protocol ──────────────────────────────────────────────────────────────

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
                "name": {
                    "type": "string",
                    "description": "Name fragment to search for, e.g. 'smith' or 'acme'",
                }
            },
            "required": ["name"],
        },
    },
    {
        "name": "get_orders",
        "description": (
            "Return all active sales orders for a customer account code from "
            "the Kerridge ERP order header file (OEHDR01). Shows order number, "
            "date, customer reference, delivery name and postcode, and order value. "
            "Use find_customer first if you only have a customer name."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {
                    "type": "string",
                    "description": "Customer account code, e.g. 'AC001' or 'P6750'",
                }
            },
            "required": ["account"],
        },
    },
    {
        "name": "get_order_detail",
        "description": (
            "Return full detail for a single sales order: header fields plus "
            "every order line with part number, description, unit of measure, "
            "price, qty to follow, qty picked, and qty still outstanding. "
            "Pick status comes from OEPIK01 — qty_picked > 0 means the line "
            "has been assigned to a picking note; qty_outstanding > 0 means "
            "items are still waiting to be picked."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "order": {
                    "type": "string",
                    "description": "Sales order number, e.g. '700002'",
                }
            },
            "required": ["order"],
        },
    },
]

TOOL_FNS = {
    "find_customer":   lambda args: find_customer(args.get("name", "")),
    "get_orders":      lambda args: get_orders(args.get("account", "")),
    "get_order_detail":lambda args: get_order_detail(args.get("order", "")),
}


def handle_message(msg: dict) -> dict | None:
    method = msg.get("method")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "kerridge-erp", "version": "1.0.0"},
            },
        }

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {"tools": TOOLS},
        }

    if method == "tools/call":
        params   = msg.get("params", {})
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})

        if tool_name not in TOOL_FNS:
            return {
                "jsonrpc": "2.0",
                "id": msg_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"},
            }

        try:
            output = TOOL_FNS[tool_name](tool_args)
        except Exception as e:
            output = json.dumps({"error": str(e)})

        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "content": [{"type": "text", "text": output}],
                "isError": False,
            },
        }

    # Unknown method — return error for requests, ignore for notifications
    if msg_id is not None:
        return {
            "jsonrpc": "2.0",
            "id": msg_id,
            "error": {"code": -32601, "message": f"Method not found: {method}"},
        }
    return None


def run_stdio():
    """Run in stdio mode (for Claude Desktop local config)."""
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


def run_http(port: int):
    """Run in HTTP/SSE mode (for multi-user network access)."""
    try:
        from http.server import BaseHTTPRequestHandler, HTTPServer
        import threading
    except ImportError:
        print("HTTP mode requires Python standard library (http.server)", file=sys.stderr)
        sys.exit(1)

    class MCPHandler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # suppress access log

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            body   = self.rfile.read(length)
            try:
                msg = json.loads(body)
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                return

            response = handle_message(msg)
            payload  = json.dumps(response).encode() if response else b"{}"
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(payload))
            self.end_headers()
            self.wfile.write(payload)

        def do_GET(self):
            if self.path == "/health":
                payload = b'{"status":"ok"}'
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", len(payload))
                self.end_headers()
                self.wfile.write(payload)
            else:
                self.send_response(404)
                self.end_headers()

    server = HTTPServer(("0.0.0.0", port), MCPHandler)
    print(f"Kerridge ERP MCP server listening on port {port}", file=sys.stderr)
    server.serve_forever()


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kerridge ERP MCP Server")
    parser.add_argument("--http", action="store_true", help="Run in HTTP mode instead of stdio")
    parser.add_argument("--port", type=int, default=8765, help="HTTP port (default 8765)")
    args = parser.parse_args()

    if args.http:
        run_http(args.port)
    else:
        run_stdio()
