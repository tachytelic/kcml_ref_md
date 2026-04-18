#!/usr/bin/env python3
"""
Kerridge ERP MCP Server
Exposes live ERP data from KISAM K-Open 3 files via KCML query programs.

Tools:
  find_customer        - search customers by name fragment
  get_customer         - direct customer lookup by account code
  get_orders           - list orders for a customer account
  get_order_detail     - full order detail with line and pick status
  get_invoices         - list open invoices for a customer account
  get_invoice          - direct invoice lookup by invoice number
  get_stock_item       - direct stock lookup by part number
  find_stock           - search stock by description fragment
  get_picking_note     - full picking note detail by note number
  list_balances        - all accounts with outstanding balance, sorted largest first
  get_part_orders      - all open orders containing a given part number
  get_account_sales    - invoiced sales history for an account (OEMSA01, fast keyed access)
  get_part_sales       - invoiced sales history for a part (OEMSA01, fast keyed access)
  get_purchase_orders  - all purchase order lines for a given part number
  get_purchase_order   - full detail for a single purchase order (header + lines)
  get_paid_invoices    - paid invoice history for a customer account (SALLOG01, keyed access)
  add_account_note     - write a diary note to a customer account (SALDRY01, creates new record)
  get_invoice_detail   - full invoice detail with delivery address and all lines (SALINV01+OEHDR01+OEENT01)
  get_spool_entry      - return spooler entry metadata and content by entry number (SPOOLMAST)
  create_order         - create a new sales order header + lines (OEHDR01 + OEENT01, allocates order number)

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
import os
import struct
import subprocess
import sys
import uuid
import queue
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

# ── Configuration ─────────────────────────────────────────────────────────────

KCML_BIN   = "/usr/lib/kcml/kcml"
UF_JSON_SO = str(Path(__file__).parent.parent / "UFN/json_escape/uf_json.so")
KCML_DIR   = Path(__file__).parent / "kcml"

SOP_DIR      = "/user1/kopen/sop"
SOP_SA_DIR   = "/user1/kopen/sop_sa"
ACCOUNTS_DIR = "/user1/kopen/accounts"
STOCK_DIR    = "/user1/kopen/stock"
POP_DIR      = "/user1/kopen/pop"
SPOOL_DIR    = "/user1/kopen/spool"

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

def get_customer(account: str) -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    try:
        return json.dumps(run_kcml("get_customer.src", ACCOUNTS_DIR, account.strip().upper()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

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

def get_invoices(account: str) -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    try:
        return json.dumps(run_kcml("get_invoices.src", ACCOUNTS_DIR, account.strip().upper()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_invoice(invoice: str) -> str:
    if not invoice or not invoice.strip():
        return json.dumps({"error": "invoice parameter is required"})
    try:
        return json.dumps(run_kcml("get_invoice.src", ACCOUNTS_DIR, invoice.strip()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_stock_item(part: str) -> str:
    if not part or not part.strip():
        return json.dumps({"error": "part parameter is required"})
    try:
        return json.dumps(run_kcml("get_stock_item.src", STOCK_DIR, part.strip().upper()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def find_stock(description: str) -> str:
    if not description or not description.strip():
        return json.dumps({"error": "description parameter is required"})
    try:
        return json.dumps(run_kcml("find_stock.src", STOCK_DIR, description.strip()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_picking_note(note: str) -> str:
    if not note or not note.strip():
        return json.dumps({"error": "note parameter is required"})
    try:
        return json.dumps(run_kcml("get_picking_note.src", SOP_DIR, note.strip()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def list_overdue() -> str:
    import datetime
    today = datetime.date.today().strftime("%Y%m%d")
    try:
        data = run_kcml("list_overdue.src", ACCOUNTS_DIR, today)
        if isinstance(data, list):
            data.sort(key=lambda x: x.get("overdue_gross", 0), reverse=True)
        return json.dumps(data, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_part_orders(part: str) -> str:
    if not part or not part.strip():
        return json.dumps({"error": "part parameter is required"})
    try:
        return json.dumps(run_kcml("get_part_orders.src", SOP_DIR, part.strip().upper()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_purchase_orders(part: str) -> str:
    if not part or not part.strip():
        return json.dumps({"error": "part parameter is required"})
    def _date_sort_key(d):
        # Convert DD/MM/YYYY -> YYYYMMDD for sortable string; missing dates sort last
        s = d.get("date_expected", "--/--/----")
        if len(s) == 10 and s[2] == "/" and s[5] == "/":
            return s[6:10] + s[3:5] + s[0:2]
        return "00000000"
    try:
        data = run_kcml("get_purchase_orders.src", POP_DIR, part.strip().upper())
        if isinstance(data, list):
            # Outstanding qty first, then by expected date descending
            data.sort(key=lambda x: (
                0 if x.get("qty_outstanding", 0) > 0 else 1,
                _date_sort_key(x),
            ), reverse=True)
        return json.dumps(data, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_account_sales(account: str, months: int = 12) -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=max(1, months) * 30)
    cutoff_str = cutoff.strftime("%Y%m%d")
    def _date_sort_key(d):
        s = d.get("date", "--/--/----")
        if len(s) == 10 and s[2] == "/" and s[5] == "/":
            return s[6:10] + s[3:5] + s[0:2]
        return "00000000"
    try:
        data = run_kcml("get_account_sales.src", SOP_SA_DIR, account.strip().upper(), cutoff_str)
        if isinstance(data, list):
            data.sort(key=_date_sort_key, reverse=True)
        return json.dumps(data, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_part_sales(part: str, months: int = 12) -> str:
    if not part or not part.strip():
        return json.dumps({"error": "part parameter is required"})
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=max(1, months) * 30)
    cutoff_str = cutoff.strftime("%Y%m%d")
    def _date_sort_key(d):
        s = d.get("date", "--/--/----")
        if len(s) == 10 and s[2] == "/" and s[5] == "/":
            return s[6:10] + s[3:5] + s[0:2]
        return "00000000"
    try:
        data = run_kcml("get_part_sales.src", SOP_SA_DIR, part.strip().upper(), cutoff_str)
        if isinstance(data, list):
            data.sort(key=_date_sort_key, reverse=True)
        return json.dumps(data, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_purchase_order(po: str) -> str:
    if not po or not po.strip():
        return json.dumps({"error": "po parameter is required"})
    try:
        return json.dumps(run_kcml("get_purchase_order.src", POP_DIR, po.strip()), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def add_account_note(account: str, text: str, category: str = "N") -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    if not text or not text.strip():
        return json.dumps({"error": "text parameter is required"})
    import datetime
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    time_str = now.strftime("%H%M")
    padded_text = text[:210].ljust(210)
    cat = (category.strip().upper() or "N")[:1]
    try:
        return json.dumps(run_kcml(
            "add_account_note.src",
            ACCOUNTS_DIR, account.strip().upper(), cat, padded_text, date_str, time_str
        ), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def get_paid_invoices(account: str, months: int = 12) -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=max(1, months) * 30)
    cutoff_str = cutoff.strftime("%Y%m%d")
    def _date_sort_key(d):
        s = d.get("date", "--/--/----")
        if len(s) == 10 and s[2] == "/" and s[5] == "/":
            return s[6:10] + s[3:5] + s[0:2]
        return "00000000"
    try:
        data = run_kcml("get_paid_invoices.src", ACCOUNTS_DIR, account.strip().upper(), cutoff_str)
        if isinstance(data, list):
            data.sort(key=_date_sort_key, reverse=True)
        return json.dumps(data, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

_SPOOL_REC_SIZE = 128
_SPOOL_STATUS   = {'1':'ON QUEUE','2':'PRINTING','3':'PRINTED','4':'ABORTED','5':'KEEP'}
_SPOOL_SYSTEM   = {'A':'Accounts','S':'Stock','P':'Sales','C':'Contract',' ':'Global'}

def _bcd_date(raw: bytes) -> str:
    h = raw.hex()
    return '' if h == '00000000' else f'{h[6:8]}/{h[4:6]}/{h[0:4]}'

def _bcd_time(raw: bytes) -> str:
    h = raw.hex()
    return '' if h == '000000' else f'{h[0:2]}:{h[2:4]}:{h[4:6]}'

def get_spool_entry(entry: int) -> str:
    try:
        path = os.path.join(SPOOL_DIR, 'SPOOLMAST')
        with open(path, 'rb') as f:
            data = f.read()
        next_free = struct.unpack('>I', data[0:4])[0]
        for i in range(1, next_free):
            rec = data[i * _SPOOL_REC_SIZE : (i + 1) * _SPOOL_REC_SIZE]
            if struct.unpack('>I', rec[0:4])[0] != entry:
                continue
            stat_byte = chr(rec[56])
            if stat_byte == '6':
                return json.dumps({"error": f"Entry {entry} has been purged"})
            filename = rec[4:16].decode('latin1').rstrip()
            meta = {
                'entry':       entry,
                'filename':    filename,
                'description': rec[16:46].decode('latin1').rstrip(),
                'stationery':  rec[46:56].decode('latin1').rstrip(),
                'status':      _SPOOL_STATUS.get(stat_byte, 'UNKNOWN'),
                'dateReq':     _bcd_date(rec[58:62]),
                'dateActual':  _bcd_date(rec[62:66]),
                'timeQueued':  _bcd_time(rec[66:69]),
                'timePrinted': _bcd_time(rec[69:72]),
                'user':        rec[72:76].decode('latin1').rstrip(),
                'operator':    rec[76:80].decode('latin1').rstrip(),
                'printer':     chr(rec[80]),
                'company':     rec[81:83].decode('latin1').rstrip(),
                'system':      _SPOOL_SYSTEM.get(chr(rec[83]), chr(rec[83]).strip()),
                'copies':      rec[84],
            }
            content_path = os.path.join(SPOOL_DIR, filename)
            try:
                with open(content_path, 'r', encoding='latin1') as cf:
                    meta['content'] = cf.read()
            except OSError as e:
                meta['content'] = None
                meta['content_error'] = str(e)
            return json.dumps(meta, indent=2)
        return json.dumps({"error": f"Entry {entry} not found in SPOOLMAST"})
    except OSError as e:
        return json.dumps({"error": str(e)})

def get_invoice_detail(doc: int) -> str:
    try:
        return json.dumps(run_kcml("get_invoice_detail.src", ACCOUNTS_DIR, SOP_DIR, str(doc), STOCK_DIR), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def list_balances() -> str:
    try:
        data = run_kcml("list_balances.src", ACCOUNTS_DIR)
        if isinstance(data, list):
            data.sort(key=lambda x: x.get("balance", 0), reverse=True)
        return json.dumps(data, indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

def create_order(
    account: str,
    lines: list,
    customer_ref: str = "",
    delivery_name: str = "",
    delivery_addr1: str = "",
    delivery_addr2: str = "",
    delivery_addr3: str = "",
) -> str:
    if not account or not account.strip():
        return json.dumps({"error": "account parameter is required"})
    if not lines:
        return json.dumps({"error": "at least one order line is required"})
    import datetime
    date_str = datetime.date.today().strftime("%Y%m%d")
    args = [
        SOP_DIR, STOCK_DIR,
        account.strip().upper(),
        (customer_ref or "")[:24],
        (delivery_name or "")[:30],
        (delivery_addr1 or "")[:30],
        (delivery_addr2 or "")[:30],
        (delivery_addr3 or "")[:30],
        date_str,
        str(len(lines)),
    ]
    for ln in lines:
        args.append(str(ln.get("part", "")).strip().upper()[:15])
        args.append(str(ln.get("qty", 1)))
        args.append(str(ln.get("price", 0)))
    try:
        return json.dumps(run_kcml("create_order.src", *args, timeout=30), indent=2)
    except RuntimeError as e:
        return json.dumps({"error": str(e)})

# ── MCP tool definitions ───────────────────────────────────────────────────────

TOOLS = [
    {
        "name": "get_customer",
        "description": (
            "Direct lookup of a single customer account by account code in the "
            "Kerridge ERP customer master (SALLED01). Returns name, current "
            "balance, credit limit, and on-stop status. Use this when you already "
            "have the account code. Use find_customer instead to search by name."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string", "description": "Customer account code, e.g. 'D2560'"}
            },
            "required": ["account"],
        },
    },
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
    {
        "name": "get_invoices",
        "description": (
            "Return all open invoices for a customer account code from the "
            "Kerridge ERP sales ledger (SALINV01). Shows invoice number, date, "
            "due date, net value, VAT, gross total, and customer reference. "
            "All invoices returned are outstanding (unpaid). Use find_customer "
            "first to get the account code if you only have a name."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string", "description": "Customer account code, e.g. 'D2560'"}
            },
            "required": ["account"],
        },
    },
    {
        "name": "get_invoice",
        "description": (
            "Look up a single invoice by invoice number from the Kerridge ERP "
            "sales ledger (SALINV01). Returns account code, type, date, due "
            "date, net, VAT, gross, and customer reference. Use this when the "
            "user quotes a specific invoice number."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "invoice": {"type": "string", "description": "Invoice number, e.g. '713773'"}
            },
            "required": ["invoice"],
        },
    },
    {
        "name": "get_stock_item",
        "description": (
            "Direct lookup of a single stock item by part number from the "
            "Kerridge ERP stock master (S_STOK01). Returns description, unit "
            "of measure, product group, selling price, qty in stock, qty "
            "allocated, and free stock. Use this when you already have the "
            "part number. Use find_stock to search by description."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "part": {"type": "string", "description": "Part number, e.g. '88600041'"}
            },
            "required": ["part"],
        },
    },
    {
        "name": "find_stock",
        "description": (
            "Search the Kerridge ERP stock master (S_STOK01) for parts whose "
            "description contains the given fragment. Case-insensitive. Returns "
            "part number, description, unit of measure, product group, selling "
            "price, and qty in stock. Returns up to 50 matches."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "description": {"type": "string", "description": "Description fragment, e.g. 'ethernet cable'"}
            },
            "required": ["description"],
        },
    },
    {
        "name": "list_overdue",
        "description": (
            "Return all customer accounts with invoices past their due date, "
            "sorted by total overdue amount descending. For each account shows "
            "the account code, customer name, total overdue gross (inc VAT), "
            "number of overdue invoices, oldest due date, and on-stop status. "
            "Use this for credit control — e.g. 'who has the largest overdue "
            "balances?' or 'show me all overdue accounts'."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "list_balances",
        "description": (
            "Return all customer accounts with a non-zero outstanding balance "
            "from the Kerridge ERP sales ledger master (SALLED01), sorted by "
            "balance descending (largest first). Shows account code, name, "
            "balance, credit limit, and on-stop status. Use this for credit "
            "control overviews — e.g. 'who owes the most?' or 'show me all "
            "accounts with outstanding balances'."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "get_purchase_orders",
        "description": (
            "Return all purchase order lines for a given part number from the "
            "Kerridge ERP purchase entries file (PCENT01). Shows the expected "
            "delivery date, original expected date, last advice date, qty "
            "required, qty received, and qty outstanding for each PO line. "
            "Outstanding POs (qty_outstanding > 0) are listed first. "
            "Use this to find when stock is due to arrive — e.g. after "
            "get_stock_item shows a part is out of stock or on backorder."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "part": {"type": "string", "description": "Part number, e.g. '88504040'"}
            },
            "required": ["part"],
        },
    },
    {
        "name": "get_account_sales",
        "description": (
            "Return the invoiced sales history for a customer account from the "
            "Kerridge ERP monthly sales analysis file (OEMSA01). Uses the "
            "account-keyed index (path 2) so it is fast — no full scan. "
            "Returns each sale line with date, part number, description, rep, "
            "order, qty, sales value, cost, order type, and customer reference. "
            "invoice_account is included when it differs from the delivery "
            "account (indicating a branch/group billing relationship). Results "
            "are sorted most recent first and capped at 500 lines. Default "
            "window is 12 months; pass months to override. Use this to answer: "
            "what has this customer bought, at what volumes and values, and "
            "what products do they re-order regularly?"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string",  "description": "Customer account code, e.g. 'B1350'"},
                "months":  {"type": "integer", "description": "How many months of history to return (default 12)"},
            },
            "required": ["account"],
        },
    },
    {
        "name": "get_part_sales",
        "description": (
            "Return the invoiced sales history for a given part number from the "
            "Kerridge ERP monthly sales analysis file (OEMSA01). Uses keyed "
            "access so it is fast even against the 600K+ record file. Returns "
            "each sale line with date, delivery account, invoice account (if "
            "different), sales rep, order number, qty, sales value, cost, "
            "order type, and customer reference. Results are sorted most recent "
            "first and capped at 500 lines. Default window is 12 months; pass "
            "months to override. Use this to answer: who is buying this part, "
            "at what volumes and prices, and what margin are we making?"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "part":   {"type": "string",  "description": "Part number, e.g. '88504040'"},
                "months": {"type": "integer", "description": "How many months of history to return (default 12)"},
            },
            "required": ["part"],
        },
    },
    {
        "name": "get_purchase_order",
        "description": (
            "Return full detail for a single purchase order from the Kerridge ERP "
            "purchase files (PCHDR01 + PCENT01). Shows the supplier name and code, "
            "order date, buyer, delivery address and postcode, and all order lines "
            "with part number, description, expected delivery date, original "
            "expected date, qty required, qty received, qty outstanding, and unit "
            "price. Use this after get_purchase_orders returns a po_number — e.g. "
            "to see all parts on a specific PO or to get the supplier details."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "po": {"type": "string", "description": "Purchase order number, e.g. '64577'"}
            },
            "required": ["po"],
        },
    },
    {
        "name": "get_invoice_detail",
        "description": (
            "Return full detail for a single invoice from the Kerridge ERP system. "
            "Looks up the invoice document number in SALINV01, retrieves the delivery "
            "and invoice addresses from the linked sales order in OEHDR01, and returns "
            "all invoice lines from OEENT01 with part, description, UOM, qty, unit "
            "price, and line total. Also returns calculated net, gross, and VAT totals, "
            "and a carrier field with the delivery service description (e.g. 'DHL "
            "International', 'Next Day By 17.30 pm'). "
            "The document number is the number printed top-right on the invoice "
            "(e.g. 714128 from '00714128'). Use get_invoice to search open invoices by "
            "this same number; use get_invoice_detail when you need the line-level breakdown."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "doc": {"type": "integer", "description": "Invoice document number, e.g. 714128"},
            },
            "required": ["doc"],
        },
    },
    {
        "name": "get_spool_entry",
        "description": (
            "Return the metadata and full text content of a Kerridge ERP spooler "
            "entry by its entry number. Looks up the entry in SPOOLMAST to get "
            "the description, status, dates, user, and printer, then reads the "
            "spool file itself and returns its content as a string. Use this when "
            "someone asks to see the output of a spooled report or job — e.g. a "
            "daybook, stock report, or verification listing."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "entry": {"type": "integer", "description": "Spooler entry number, e.g. 1496"},
            },
            "required": ["entry"],
        },
    },
    {
        "name": "add_account_note",
        "description": (
            "Add a diary note to a customer account in the Kerridge ERP Sales "
            "Ledger diary file (SALDRY01). The note appears immediately when "
            "staff open the account in the ERP. Use this to record call outcomes, "
            "payment promises, credit decisions, dispute details, or any other "
            "account activity. The note is timestamped with today's date and "
            "current time. Category codes: N=general note (default), "
            "P=phone call, C=credit decision. Text up to 210 characters."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account":  {"type": "string", "description": "Customer account code, e.g. 'Z9234'"},
                "text":     {"type": "string", "description": "Note text, up to 210 characters"},
                "category": {"type": "string", "description": "Category code: N=note (default), P=phone call, C=credit decision"},
            },
            "required": ["account", "text"],
        },
    },
    {
        "name": "get_paid_invoices",
        "description": (
            "Return the paid invoice history for a customer account from the "
            "Kerridge ERP Sales Ledger paid transactions file (SALLOG01). Uses "
            "keyed access positioned at the account, so it is fast. Returns each "
            "paid invoice or credit note with invoice date, paid date, net value, "
            "customer reference, cheque/payment reference, and days taken to pay. "
            "Results are sorted most recent first and capped at 500 records. "
            "Default window is 12 months; pass months to override. Use this to "
            "answer: when did this customer last pay, how long do they typically "
            "take to pay, what invoices have been settled, and by which cheque?"
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {"type": "string",  "description": "Customer account code, e.g. 'D2560'"},
                "months":  {"type": "integer", "description": "How many months of history to return (default 12)"},
            },
            "required": ["account"],
        },
    },
    {
        "name": "get_part_orders",
        "description": (
            "Find all open orders that have outstanding quantity for a given part "
            "number. Scans the Kerridge ERP order line file (OEENT01) for lines "
            "where qty_to_follow > 0, then looks up the order header (OEHDR01) "
            "and checks for any picking note (OEPIK01). Returns order number, "
            "account code, customer reference, delivery name, order date, "
            "qty_to_follow, picking note number (if raised), and qty on pick. "
            "Use this after get_stock_item shows allocated stock, to find which "
            "orders that stock is committed to."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "part": {"type": "string", "description": "Part number, e.g. '88504721'"}
            },
            "required": ["part"],
        },
    },
    {
        "name": "get_picking_note",
        "description": (
            "Return full detail for a picking note from the Kerridge ERP "
            "picking file (OEPIK01). Shows the picking note date, linked "
            "sales order, account, delivery address, and all line items with "
            "part number, description, qty to pick, and qty to follow. "
            "Use this to look up a physical picking note by its number."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "note": {"type": "string", "description": "Picking note number, e.g. '355918'"}
            },
            "required": ["note"],
        },
    },
    {
        "name": "create_order",
        "description": (
            "Create a new sales order in the Kerridge ERP system. Allocates the "
            "next order number from the PFN8 counter (S_CON01), writes the order "
            "header to OEHDR01, and writes one OEENT01 record per line. Returns "
            "the new order number. Use get_customer first to confirm the account "
            "code exists before calling this."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "account": {
                    "type": "string",
                    "description": "Customer account code, e.g. 'Z9010'"
                },
                "customer_ref": {
                    "type": "string",
                    "description": "Customer's own reference for this order (optional, max 24 chars)"
                },
                "delivery_name": {
                    "type": "string",
                    "description": "Delivery address name (max 30 chars)"
                },
                "delivery_addr1": {
                    "type": "string",
                    "description": "Delivery address line 1 (max 30 chars)"
                },
                "delivery_addr2": {
                    "type": "string",
                    "description": "Delivery address line 2 (max 30 chars, optional)"
                },
                "delivery_addr3": {
                    "type": "string",
                    "description": "Delivery address line 3 (max 30 chars, optional)"
                },
                "lines": {
                    "type": "array",
                    "description": "Order lines — at least one required",
                    "items": {
                        "type": "object",
                        "properties": {
                            "part":  {"type": "string",  "description": "Part number (max 15 chars)"},
                            "qty":   {"type": "number",  "description": "Quantity (whole or decimal)"},
                            "price": {"type": "number",  "description": "Selling price per unit"}
                        },
                        "required": ["part", "qty", "price"]
                    },
                    "minItems": 1
                },
            },
            "required": ["account", "lines"],
        },
    },
]

TOOL_FNS = {
    "get_customer":     lambda a: get_customer(a.get("account", "")),
    "find_customer":    lambda a: find_customer(a.get("name", "")),
    "get_orders":       lambda a: get_orders(a.get("account", "")),
    "get_order_detail": lambda a: get_order_detail(a.get("order", "")),
    "get_invoices":     lambda a: get_invoices(a.get("account", "")),
    "get_invoice":      lambda a: get_invoice(a.get("invoice", "")),
    "get_stock_item":   lambda a: get_stock_item(a.get("part", "")),
    "find_stock":       lambda a: find_stock(a.get("description", "")),
    "get_account_sales":   lambda a: get_account_sales(a.get("account", ""), int(a.get("months", 12))),
    "get_part_sales":      lambda a: get_part_sales(a.get("part", ""), int(a.get("months", 12))),
    "get_purchase_orders": lambda a: get_purchase_orders(a.get("part", "")),
    "get_purchase_order":  lambda a: get_purchase_order(a.get("po", "")),
    "add_account_note":    lambda a: add_account_note(a.get("account", ""), a.get("text", ""), a.get("category", "N")),
    "get_paid_invoices":   lambda a: get_paid_invoices(a.get("account", ""), int(a.get("months", 12))),
    "get_part_orders":     lambda a: get_part_orders(a.get("part", "")),
    "get_picking_note": lambda a: get_picking_note(a.get("note", "")),
    "get_invoice_detail": lambda a: get_invoice_detail(int(a.get("doc", 0))),
    "get_spool_entry":  lambda a: get_spool_entry(int(a.get("entry", 0))),
    "list_balances":    lambda a: list_balances(),
    "list_overdue":     lambda a: list_overdue(),
    "create_order":     lambda a: create_order(
        a.get("account", ""),
        a.get("lines", []),
        customer_ref=a.get("customer_ref", ""),
        delivery_name=a.get("delivery_name", ""),
        delivery_addr1=a.get("delivery_addr1", ""),
        delivery_addr2=a.get("delivery_addr2", ""),
        delivery_addr3=a.get("delivery_addr3", ""),
    ),
}

# ── JSON-RPC message handler ───────────────────────────────────────────────────

def handle_message(msg: dict):
    method = msg.get("method")
    msg_id = msg.get("id")

    if method == "initialize":
        return {
            "jsonrpc": "2.0", "id": msg_id,
            "result": {
                "protocolVersion": "2025-11-25",
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
_server_port = 8765  # updated by run_http()


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

        # Tell the client where to POST requests (full URL required by mcp-remote)
        host = self.headers.get("Host", f"localhost:{_server_port}")
        endpoint = f"http://{host}/messages?sessionId={session_id}"
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
    global _server_port
    _server_port = port
    server = ThreadingHTTPServer(("0.0.0.0", port), MCPHandler)
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
