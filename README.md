# KCML Reference Documentation

This repository contains reference documentation and a Claude Code skill for **KCML** (Kerridge Computer Macro Language), a multi-platform 4GL descended from Wang BASIC-2.

## What is KCML?

KCML is an incremental compiler combining the best features of compiled and interpreted languages. Originally developed by Kerridge Computer Company in 1985 to succeed the Wang 2200 BASIC-2 system, KCML has evolved into a modern Rapid Application Development (RAD) environment used by 80,000+ end users worldwide for commercial ERP applications.

### Key Features

- **Cross-platform** — Programs and data files run unchanged across Windows, Linux, AIX, HP-UX, Solaris, and more
- **Multi-user** — True multi-user with automatic file/record locking and unique terminal numbering
- **Built-in database** — Integrated KISAM B-tree database with SQL and direct ISAM operations
- **Client-server** — Designed for wide area networks; KClient provides a GUI forms and text client
- **GUI and text** — Supports both modern forms-based interfaces and traditional text terminals

---

## Repository Structure

```
kcmlrefman_md/          # Full language reference — 393 markdown files (primary source)
.github/skills/
  kcml-coding/
    SKILL.md            # Claude Code skill — quick reference and coding guide
    references/         # Detailed topic reference files
kcml_executor/          # Local KCML execution helpers
```

### `kcmlrefman_md/` — Language Reference (393 files)

The complete KCML language reference, converted from the original HTML help files to clean markdown. Covers:

- All statements, functions, operators, and system variables
- Control flow, data types, string and numeric functions
- File I/O (sequential, random, KISAM/KDB)
- Error handling (TRY/CATCH, ON ERROR, TRAP)
- GUI forms (DEFFORM, DEFEVENT, controls)
- COM, CORBA, and SOAP object integration
- XML (DOM and SAX via Xerces)
- Text terminals (VT100, VT220, Wyse, KClient, TERMINFO)
- Tutorials (files, sorting, Unicode, shell, configuration)
- Admin utilities (bkstat, tik, compile, kat, kconf, bkstat)
- ASP/multi-tenant deployment

### `.github/skills/kcml-coding/` — Claude Code Skill

A Claude Code skill that enables Claude to write, test, and debug KCML code:

- `SKILL.md` — Quick reference covering syntax rules, common patterns, and execution
- `references/` — Detailed topic files: data types, arrays, control flow, string functions, date functions, error handling, subroutines, screen I/O, and more

### `mcp_server/` — Kerridge ERP MCP Server

A Model Context Protocol server that exposes Kerridge K-Open 3 ERP data to AI assistants. Reads KISAM binary files directly — no middleware required.

**Invoice tools:**
- `get_invoices` — list open invoices for an account (SALINV01)
- `get_invoice` — look up a single invoice by document number (SALINV01)
- `get_invoice_detail` — full invoice with delivery/invoice address, all lines, net/gross/VAT, and carrier description (SALINV01 + OEHDR01 + OEENT01 + S_MISC01)
- `get_paid_invoices` — paid invoices for an account with date filter

**Order tools:**
- `get_orders` — list open orders for an account (OEHDR01)
- `get_order_detail` — full order header with address and all lines (OEHDR01 + OEENT01)
- `get_part_orders` — all open orders containing a specific part (OEENT01 + OEHDR01)
- `get_picking_note` — picking note detail by note number (OEPIK01 + OEENT01)

**Customer tools:**
- `get_customer` — account master including address, terms, sales rep (OECUS01)
- `find_customer` — search accounts by name fragment

**Stock tools:**
- `get_stock_item` — single part lookup: description, price, qty, free stock (S_STOK01)
- `find_stock` — search parts by description fragment
- `get_account_sales` — YTD/MTD sales by account (OEMSA01)
- `get_part_sales` — sales history by part number (OEMSA01)

**Other:**
- `list_overdue` — accounts with overdue balances
- `list_balances` — all account balances
- `add_account_note` — append a note to an account record

### `kcml_executor/` — Execution Helpers

Scripts for running KCML code locally during development and testing.

---

## Using the Claude Code Skill

The skill at `.github/skills/kcml-coding/SKILL.md` gives Claude everything needed to write correct KCML:

- Syntax rules (DIM, string sizing, array indexing, script mode)
- Common pitfalls (blank lines in `-p` mode, `:` in REMs, `HEX(22)` for quotes)
- Execution instructions for local testing
- KISAM file access patterns
- DEFFORM / DEFEVENT patterns

For any language detail not in the skill, Claude can consult `kcmlrefman_md/`.

---

## Language Quick Reference

| Area | Key files in `kcmlrefman_md/` |
|------|-------------------------------|
| Statements A–Z | `ABS(.md`, `DIM.md`, `FOR.md`, `IF.md`, `PRINT.md`, `SELECT*.md`, … |
| Control flow | `FOR.md`, `WHILE.md`, `REPEAT.md`, `IF.md`, `IFENDIF.md`, `DO.md` |
| String functions | `STR.md`, `LEN(.md`, `POS.md`, `RTRIM.md`, `LTRIM.md`, `VER.md` |
| Numeric functions | `ABS(.md`, `INT(.md`, `ROUND.md`, `SQR.md`, `SIN.md`, … |
| Date/time | `_DATE.md`, `_TIME.md`, `CONVERT_DATE.md`, `JulianDate.md`, `timezone.md` |
| File I/O | `OPENhash.md`, `READhash.md`, `WRITEhash.md`, `SEEKhash.md` |
| Error handling | `TRY.md`, `ERROR.md`, `ON_ERROR.md`, `TRAP.md`, `THROW.md` |
| Forms | `DEFFORM.md`, `DEFEVENT.md`, `DEFOBJ.md` |
| Objects/COM | `comintro.md`, `cominst.md`, `commethod.md`, `ObjCOM.md`, `ObjSoap.md` |
| System constants | `_PART.md`, `_TERM.md`, `_LINE.md`, `_GOLDKEY.md` |
| Utilities | `bkstat.md`, `compile.md`, `kat.md`, `tik.md`, `kconf.md` |
| Tutorials | `Tutorial*.md` (15 tutorials covering files, sorting, Unicode, and more) |

---

## Origin

The `kcmlrefman_md/` files were converted from the original KCML HTML help system to Markdown for improved accessibility, version control, and use as an AI coding assistant knowledge base.

## License

Please refer to Kerridge Commercial Systems for licensing information regarding KCML software and documentation.
