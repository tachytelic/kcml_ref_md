# Kerridge ERP MCP Server

An MCP (Model Context Protocol) server that exposes live data from a Kerridge K-Open 3 ERP system to AI assistants such as Claude. Each tool runs a KCML script that reads directly from the live KISAM binary files — no database export, no sync, no middleware.

---

## Architecture

```
Claude (MCP client)
    │
    │  JSON-RPC (stdio or HTTP/SSE)
    ▼
server.py  ──►  kcml/get_orders.src    ──►  /user1/kopen/sop/OEHDR01       (live KISAM file)
               kcml/get_invoices.src   ──►  /user1/kopen/accounts/SALINV01
               kcml/find_stock.src     ──►  /user1/kopen/stock/S_STOK01
               kcml/get_part_sales.src ──►  /user1/kopen/sop_sa/OEMSA01
               ...etc
```

- **Transport**: stdio (local) or HTTP/SSE (`--http --port <n>`)
- **Runtime**: KCML 6.9, `/usr/lib/kcml/kcml`
- **JSON helper**: `uf_json.so` UFN for `JSON_ESCAPE` (path configured in `server.py`)
- **No dependencies** beyond Python 3 stdlib and the KCML interpreter

---

## Quick start

### stdio mode (Claude Desktop, local machine)

```bash
python3 server.py
```

Claude Desktop `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "kerridge-erp": {
      "command": "python3",
      "args": ["/path/to/mcp_server/server.py"]
    }
  }
}
```

### HTTP/SSE mode (remote server / SSH tunnel)

On the ERP server:
```bash
python3 server.py --http --port 8765
```

On your local machine (SSH tunnel):
```bash
ssh -L 8765:localhost:8765 user@erpserver
```

Claude Desktop `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "kerridge-erp": {
      "url": "http://localhost:8765"
    }
  }
}
```

---

## Tools

### Customer tools

| Tool | Input | Description |
|------|-------|-------------|
| `find_customer` | `name` (fragment) | Case-insensitive name search in `SALLED01`. Returns account code, balance, credit limit, on-stop flag. |
| `get_customer` | `account` | Direct lookup by account code. Same fields. |

### Order tools

| Tool | Input | Description |
|------|-------|-------------|
| `get_orders` | `account` | All active sales orders for an account from `OEHDR01`. Order number, date, customer ref, delivery name/postcode, value. |
| `get_order_detail` | `order` | Full order: header + all lines with part, description, UOM, price, pick status (`OEHDR01` + `OEENT01` + `OEPIK01`). |

### Invoice tools

| Tool | Input | Description |
|------|-------|-------------|
| `get_invoices` | `account` | All open invoices from `SALINV01`. Invoice number, date, due date, net, VAT, gross, customer ref. |
| `get_invoice` | `invoice` | Single invoice lookup by invoice number. |

### Stock tools

| Tool | Input | Description |
|------|-------|-------------|
| `get_stock_item` | `part` | Direct lookup in `S_STOK01`. Description, UOM, product group, sell price, qty in stock, qty allocated, qty free. |
| `find_stock` | `description` (fragment) | Case-insensitive description search. Up to 50 matches. |
| `get_part_orders` | `part` | All sales order lines where this part has `qty_to_follow > 0` (`OEENT01` + `OEHDR01`). Shows which orders the allocated stock is committed to, plus picking note if one has been raised. |
| `get_account_sales` | `account`, `months` (opt, default 12) | Invoiced sales history for a customer account from `OEMSA01`. Uses the account-keyed index (path 2) — fast. Returns each sale line: date, part, description, rep, order, qty, sales value, cost, customer ref. Sorted most-recent first, capped at 500 lines. |
| `get_part_sales` | `part`, `months` (opt, default 12) | Invoiced sales history for a part from `OEMSA01`. Uses the part-keyed index (path 1) — fast. Returns each sale line: date, account, rep, order, qty, sales value, cost, customer ref. Sorted most-recent first, capped at 500 lines. |

### Purchase order tools

| Tool | Input | Description |
|------|-------|-------------|
| `get_purchase_orders` | `part` | All purchase order lines for this part from `PCENT01`. Shows `po_number`, `date_expected`, `originally_expected`, `last_advice_date`, `qty_required`, `qty_received`, `qty_outstanding`. Outstanding lines sorted first. |
| `get_purchase_order` | `po` | Full detail for a single PO from `PCHDR01` + `PCENT01`. Header: supplier name/code, country, order date, buyer, delivery address/postcode. Lines: part, description, expected dates, qty required/received/outstanding, unit price. |

### Picking tools

| Tool | Input | Description |
|------|-------|-------------|
| `get_picking_note` | `note` | Full picking note from `OEPIK01` + `OEHDR01` + `OEENT01`. Header, delivery address, all lines with qty to pick and qty to follow. |

### Credit control tools

| Tool | Input | Description |
|------|-------|-------------|
| `list_balances` | *(none)* | All accounts with non-zero balance from `SALLED01`, sorted largest first. |
| `list_overdue` | *(none)* | All accounts with invoices past due date from `SALINV01`, sorted by overdue total descending. Includes oldest due date and on-stop flag. |

---

## Typical workflows

**Customer enquiry by name**
```
find_customer("smith") → get_orders("S1234") → get_order_detail("700123")
```

**Invoice / credit control**
```
find_customer("acme") → get_invoices("A5678") → get_invoice("713001")
list_overdue() → get_invoices("T0001")
```

**Stock availability + inbound**
```
find_stock("ethernet cable") → get_stock_item("88504040")
get_stock_item("88504040")    → get_part_orders("88504040")     [what orders need it]
get_stock_item("88504040")    → get_purchase_orders("88504040") [when is it due in]
get_purchase_orders("88504040") → get_purchase_order("64577")  [full PO detail]
```

**Sales history / margin analysis**
```
get_part_sales("88504040")            [last 12 months — who bought it, qty, value, cost]
get_part_sales("88504040", months=24) [extend window to 2 years]
get_account_sales("B1350")            [everything this account bought in the last year]
find_customer("namco") → get_account_sales("Z8009") [customer lookup then full history]
```

**Warehouse / picking**
```
get_picking_note("355918")
get_order_detail("700123")    [shows pick status per line]
```

---

## File layout

```
mcp_server/
├── server.py               # MCP server — JSON-RPC handler, tool registry, KCML runner
└── kcml/                   # One KCML script per tool
    ├── find_customer.src
    ├── get_customer.src
    ├── get_orders.src
    ├── get_order_detail.src
    ├── get_invoices.src
    ├── get_invoice.src
    ├── get_stock_item.src
    ├── find_stock.src
    ├── get_part_orders.src
    ├── get_account_sales.src
    ├── get_part_sales.src
    ├── get_purchase_orders.src
    ├── get_purchase_order.src
    ├── get_picking_note.src
    ├── list_balances.src
    └── list_overdue.src
```

---

## ERP file locations (configured in `server.py`)

| Variable | Path | Used by |
|----------|------|---------|
| `SOP_DIR` | `/user1/kopen/sop` | Orders, picking |
| `SOP_SA_DIR` | `/user1/kopen/sop_sa` | Sales analysis (OEMSA01) |
| `ACCOUNTS_DIR` | `/user1/kopen/accounts` | Invoices, customers |
| `STOCK_DIR` | `/user1/kopen/stock` | Stock master |
| `POP_DIR` | `/user1/kopen/pop` | Purchase orders |

---

## Adding a new tool

1. Write `kcml/<toolname>.src` — reads KISAM file(s), prints JSON to stdout
2. Add a Python function in `server.py` calling `run_kcml("toolname.src", DIR, args...)`
3. Add a tool definition to the `TOOLS` list
4. Add an entry to `TOOL_FNS`

The KCML scripts all follow the same pattern: open file → sequential scan or keyed lookup → print JSON → close. See `get_stock_item.src` for a simple direct lookup, `list_overdue.src` for a multi-phase aggregation example.

---

## Dependencies

- Python 3 (stdlib only — `subprocess`, `json`, `argparse`, `http.server`)
- `/usr/lib/kcml/kcml` — KCML 6.9 interpreter
- `/root/kcml_ref_md/UFN/json_escape/uf_json.so` — `JSON_ESCAPE` user function
