#!/usr/bin/env python3
"""
dd_reader.py — Parse KISAM data-dictionary (.DD) files and write one Markdown
doc per table into <project_root>/datadict/.

Usage:
    python3 dd_reader.py [--dd-dir DIR] [--out-dir DIR]

Defaults:
    --dd-dir   /user1/kopen/datadict
    --out-dir  <directory of this script>/../datadict

The file format (verified against OEPIK01/OEHDR01/OEENT01 field offsets):

  KISAM .DD file layout
  ─────────────────────
  • First 0x4800 (18432) bytes: file header / index blocks (not decoded here)
  • From 0x4800 onward: sequential 64-byte field records until rec[1] == 0x00

  Each 64-byte field record
  ─────────────────────────
  [0]      : 0x00  (reserved / separator)
  [1:21]   : field name, 20 chars, right-padded with spaces
  [21]     : field type  'C'=Character  'D'=Date  'I'=Binary/Integer
                         'P'=IBM Packed  'N'=Numeric
  [22:25]  : offset from record start, big-endian 3-byte uint (1-based)
  [25:28]  : field length in bytes, big-endian 3-byte uint
  [28]     : decimal places (0 for non-numeric)
  [29]     : signed flag  0x01 = signed, 0x00 = unsigned
  [30]     : ODBC-updatable  'Y' or 'N'
  [31:64]  : space padding
"""

import argparse
import os
import struct
import sys
from pathlib import Path

# ── Constants ──────────────────────────────────────────────────────────────────

DD_DIR  = Path("/user1/kopen/datadict")
SCRIPT  = Path(__file__).resolve()
OUT_DIR = SCRIPT.parent.parent / "datadict"

FIELD_START = 0x4800
REC_SIZE    = 64

TYPE_NAMES = {
    'C': 'Character',
    'D': 'Date',
    'I': 'Binary',
    'P': 'Packed',
    'N': 'Numeric',
}

# ── ODRWCAT catalogue ──────────────────────────────────────────────────────────
# Authoritative source: dump_odrwcat.src run against live ODRWCAT B-tree.
# Key   = DD file stem (no path, no .DD extension)
# Value = dict with:
#   descriptions : list of display names from ODRWCAT field 11 (offset 249)
#   data_files   : list of physical data file paths from ODRWCAT field 2 (offset 37)
# Multiple entries occur when the same DD file describes several logical tables
# that share a physical data file (e.g. SMSC*.DD covers Co 01 and Co 02).

CATALOGUE = {
    "ACCD0101":  {"descriptions": ["Area Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0201":  {"descriptions": ["Business type (SIC) codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0301":  {"descriptions": ["Customer Class Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0401":  {"descriptions": ["Enquiry Source Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0501":  {"descriptions": ["Representative Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0601":  {"descriptions": ["Job Title Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0701":  {"descriptions": ["Account Type Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0801":  {"descriptions": ["Category Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD0901":  {"descriptions": ["EC Member Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD1001":  {"descriptions": ["EC Intra-stat Member Code Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD1101":  {"descriptions": ["Diary Category Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5101":  {"descriptions": ["Currency Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5201":  {"descriptions": ["VAT Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5301":  {"descriptions": ["Terms Table Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5401":  {"descriptions": ["Department Split Table Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5501":  {"descriptions": ["Cashbook Transaction Type Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5601":  {"descriptions": ["Cashbook Analysis Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5701":  {"descriptions": ["MA Department Split Table Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ACCD5801":  {"descriptions": ["MA Period Split Table Co 01"],
                  "data_files":   ["/user1/kopen/accounts/ACCODE01"]},
    "ANALYS01":  {"descriptions": ["NL Transactions file Co 01", "NL ARCHIVES"],
                  "data_files":   ["/user1/kopen/accounts/ANALYS01",
                                   "/user1/kopen/archive/NL01/20150930.EOM/ANALYS01"]},
    "ANALYS02":  {"descriptions": ["NL Transactions file Co 02"],
                  "data_files":   ["/user1/kopen/accounts/ANALYS02"]},
    "BSALOC01":  {"descriptions": ["Batch/Serial Allocations file Co 01"],
                  "data_files":   ["/user1/kopen/bas/BSALOC01"]},
    "BSHDR01":   {"descriptions": ["Batch/Serial Header file Co 01"],
                  "data_files":   ["/user1/kopen/bas/BSHDR01"]},
    "BSLOG01":   {"descriptions": ["Batch/Serial Log file Co 01"],
                  "data_files":   ["/user1/kopen/bas/BSLOG01"]},
    "CBAAUT01":  {"descriptions": ["CB Auto Postings Analysis file Co 01"],
                  "data_files":   ["/user1/kopen/accounts/CBAAUT01"]},
    "CBANAL01":  {"descriptions": ["Cashbook analysis file Co 01"],
                  "data_files":   ["/user1/kopen/accounts/CBANAL01"]},
    "CBAUTO01":  {"descriptions": ["CB Automatic Postings file Co 01"],
                  "data_files":   ["/user1/kopen/accounts/CBAUTO01"]},
    "CBBANK01":  {"descriptions": ["Cashbook bank a/c file Co 01"],
                  "data_files":   ["/user1/kopen/accounts/CBBANK01"]},
    "CBITEM01":  {"descriptions": ["Cashbook Transactions Co 01"],
                  "data_files":   ["/user1/kopen/accounts/CBITEM01"]},
    "CPENT01":   {"descriptions": ["SL Contract price entries file Co 01"],
                  "data_files":   ["/user1/kopen/cprice/CPENT01"]},
    "CPENT02":   {"descriptions": ["SL Contract price entries file Co 02"],
                  "data_files":   ["/user1/kopen/cprice/CPENT02"]},
    "CPHDR01":   {"descriptions": ["SL Contract price header file Co 01"],
                  "data_files":   ["/user1/kopen/cprice/CPHDR01"]},
    "CPHDR02":   {"descriptions": ["SL Contract price header file Co 02"],
                  "data_files":   ["/user1/kopen/cprice/CPHDR02"]},
    "NLDEPT01":  {"descriptions": ["NL Department Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/NOMINL01"]},
    "NLDEPT02":  {"descriptions": ["NL Department Codes Co 02"],
                  "data_files":   ["/user1/kopen/accounts/NOMINL02"]},
    "NLEXP01":   {"descriptions": ["NL Expense Codes Co 01"],
                  "data_files":   ["/user1/kopen/accounts/NOMINL01"]},
    "NLEXP02":   {"descriptions": ["NL Expense Codes Co 02"],
                  "data_files":   ["/user1/kopen/accounts/NOMINL02"]},
    "OEENT01":   {"descriptions": ["Sales Order entry file Co 01"],
                  "data_files":   ["/user1/kopen/sop/OEENT01"]},
    "OEENT02":   {"descriptions": ["Sales Order entry file Co 02"],
                  "data_files":   ["/user1/kopen/sop/OEENT02"]},
    "OEHDR01":   {"descriptions": ["Sales Order Header file Co 01"],
                  "data_files":   ["/user1/kopen/sop/OEHDR01"]},
    "OEHDR02":   {"descriptions": ["Sales Order Header file Co 02"],
                  "data_files":   ["/user1/kopen/sop/OEHDR02"]},
    "OEMIA01":   {"descriptions": ["Monthly Intake Analysis file Co 01"],
                  "data_files":   ["/user1/kopen/sop_sa/OEMIA01"]},
    "OEMIA02":   {"descriptions": ["Monthly Intake Analysis file Co 02"],
                  "data_files":   ["/user1/kopen/sop_sa/OEMIA02"]},
    "OEMSA01":   {"descriptions": ["Monthly Sales Analysis File Co 01"],
                  "data_files":   ["/user1/kopen/sop_sa/OEMSA01"]},
    "OEMSA02":   {"descriptions": ["Monthly Sales Analysis File Co 02"],
                  "data_files":   ["/user1/kopen/sop_sa/OEMSA02"]},
    "OEPIK01":   {"descriptions": ["Order picking notes Co 01"],
                  "data_files":   ["/user1/kopen/sop/OEPIK01"]},
    "OEPIK02":   {"descriptions": ["Order picking notes Co 02"],
                  "data_files":   ["/user1/kopen/sop/OEPIK02"]},
    "PCCNENT01": {"descriptions": ["Purchase consignment entries Co 01"],
                  "data_files":   ["/user1/kopen/pop/PCCNENT01"]},
    "PCCNENT02": {"descriptions": ["Purchase consignment entries Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCCNENT02"]},
    "PCCNHDR01": {"descriptions": ["Purchase consignment headers Co 01"],
                  "data_files":   ["/user1/kopen/pop/PCCNHDR01"]},
    "PCCNHDR02": {"descriptions": ["Purchase consignment headers Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCCNHDR02"]},
    "PCDRY02":   {"descriptions": ["Purchase Control Diary Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCDRY02"]},
    "PCENT01":   {"descriptions": ["Purchase entries file Co 01"],
                  "data_files":   ["/user1/kopen/pop/PCENT01"]},
    "PCENT02":   {"descriptions": ["Purchase entries file Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCENT02"]},
    "PCHDR01":   {"descriptions": ["Purchase Header file Co 01"],
                  "data_files":   ["/user1/kopen/pop/PCHDR01"]},
    "PCHDR02":   {"descriptions": ["Purchase Header file Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCHDR02"]},
    "PCSUP01":   {"descriptions": ["Supplier file Co 01"],
                  "data_files":   ["/user1/kopen/pop/PCSUP01"]},
    "PCSUP02":   {"descriptions": ["Supplier file Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCSUP02"]},
    "PCVSI01":   {"descriptions": ["Purchase VSI File Co 01"],
                  "data_files":   ["/user1/kopen/pop/PCVSI01"]},
    "PCVSI02":   {"descriptions": ["Purchase VSI File Co 02"],
                  "data_files":   ["/user1/kopen/pop/PCVSI02"]},
    "PGCALL01":  {"descriptions": ["Prospect Calls file Co 01"],
                  "data_files":   ["/user1/kopen/prospect/PGCALL01"]},
    "PGCALL02":  {"descriptions": ["Prospect Calls file Co 02"],
                  "data_files":   ["/user1/kopen/prospect/PGCALL02"]},
    "PGCNCT01":  {"descriptions": ["Prospecting Contact file Co 01"],
                  "data_files":   ["/user1/kopen/prospect/PGCNCT01"]},
    "PGCNCT02":  {"descriptions": ["Prospecting Contact file Co 02"],
                  "data_files":   ["/user1/kopen/prospect/PGCNCT02"]},
    "PGCUST01":  {"descriptions": ["Prospect Details Co 01"],
                  "data_files":   ["/user1/kopen/prospect/PGCUST01"]},
    "PGCUST02":  {"descriptions": ["Prospect Details file Co 02"],
                  "data_files":   ["/user1/kopen/prospect/PGCUST02"]},
    "PPENT02":   {"descriptions": ["PL Contract Price Entries file Co 02"],
                  "data_files":   ["/user1/kopen/cprice/PPENT02"]},
    "PPHDR02":   {"descriptions": ["PL Contract Price Header file Co 02"],
                  "data_files":   ["/user1/kopen/cprice/PPHDR02"]},
    "PREGLN01":  {"descriptions": ["Purchase Register Lines Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PREGLN01"]},
    "PREGLN02":  {"descriptions": ["Purchase Register Lines Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PREGLN02"]},
    "PURDRY01":  {"descriptions": ["Purchase Ledger Diary File Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PURDRY01"]},
    "PURDRY02":  {"descriptions": ["Purchase Ledger Diary File Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PURDRY02"]},
    "PURINV01":  {"descriptions": ["Purchase Ledger Transactions Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PURINV01"]},
    "PURINV02":  {"descriptions": ["Purchase Ledger Transactions Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PURINV02"]},
    "PURLED01":  {"descriptions": ["Purchase Ledger Supplier file Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PURLED01"]},
    "PURLED02":  {"descriptions": ["Purchase Ledger Supplier file Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PURLED02"]},
    "PURLOG01":  {"descriptions": ["Purchase Ledger Paid Transactions Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PURLOG01"]},
    "PURLOG02":  {"descriptions": ["Purchase Ledger Paid Transactions Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PURLOG02"]},
    "PURREG01":  {"descriptions": ["Purchase ledger inv register Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PURREG01"]},
    "PURREG02":  {"descriptions": ["Purchase ledger inv register Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PURREG02"]},
    "PURXTA01":  {"descriptions": ["Purchase Ledger Extra Fields Co 01"],
                  "data_files":   ["/user1/kopen/accounts/PURXTA01"]},
    "PURXTA02":  {"descriptions": ["Purchase Ledger Extra Fields Co 02"],
                  "data_files":   ["/user1/kopen/accounts/PURXTA02"]},
    "REJECT01":  {"descriptions": ["Rejection analysis Co 01"],
                  "data_files":   ["/user1/kopen/pop/REJECT01"]},
    "REJECT02":  {"descriptions": ["Rejection analysis Co 02"],
                  "data_files":   ["/user1/kopen/pop/REJECT02"]},
    "RWINDX":    {"descriptions": ["Report Writer Report List File"],
                  "data_files":   ["/user1/kopen/datadict/RWINDX"]},
    "SALDRY01":  {"descriptions": ["Sales Ledger Diary File Co 01"],
                  "data_files":   ["/user1/kopen/accounts/SALDRY01"]},
    "SALDRY02":  {"descriptions": ["Sales Ledger Diary File Co 02"],
                  "data_files":   ["/user1/kopen/accounts/SALDRY02"]},
    "SALINV01":  {"descriptions": ["Sales Ledger Transactions Co 01"],
                  "data_files":   ["/user1/kopen/accounts/SALINV01"]},
    "SALINV02":  {"descriptions": ["Sales Ledger Transactions Co 02"],
                  "data_files":   ["/user1/kopen/accounts/SALINV02"]},
    "SALLED01":  {"descriptions": ["Sales Ledger Customer File Co 01"],
                  "data_files":   ["/user1/kopen/accounts/SALLED01"]},
    "SALLED02":  {"descriptions": ["Sales Ledger Customer File Co 02"],
                  "data_files":   ["/user1/kopen/accounts/SALLED02"]},
    "SALLOG01":  {"descriptions": ["Sales Ledger Paid Transactions Co 01"],
                  "data_files":   ["/user1/kopen/accounts/SALLOG01"]},
    "SALLOG02":  {"descriptions": ["Sales Ledger Paid Transactions Co 02"],
                  "data_files":   ["/user1/kopen/accounts/SALLOG02"]},
    "SALXTA01":  {"descriptions": ["Sales Ledger Extra Fields Co 01"],
                  "data_files":   ["/user1/kopen/accounts/SALXTA01"]},
    "SALXTA02":  {"descriptions": ["Sales Ledger Extra Fields Co 02"],
                  "data_files":   ["/user1/kopen/accounts/SALXTA02"]},
    "SMSC01":    {"descriptions": ["Location Descriptions Co 01",
                                   "Location Descriptions Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_MISC01",
                                   "/user1/kopen/stock/S_MISC02"]},
    "SMSC03":    {"descriptions": ["Representatives Co 01",
                                   "Representatives Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_MISC01",
                                   "/user1/kopen/stock/S_MISC02"]},
    "SMSC04":    {"descriptions": ["WO Cost Codes Co 01",
                                   "WO Cost Codes Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_MISC01",
                                   "/user1/kopen/stock/S_MISC02"]},
    "SMSC05":    {"descriptions": ["Resource Types Co 01",
                                   "Resource Types Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_MISC01",
                                   "/user1/kopen/stock/S_MISC02"]},
    "SMSC06":    {"descriptions": ["Reject Reason Codes Co 01",
                                   "Reject Reason Codes Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_MISC01",
                                   "/user1/kopen/stock/S_MISC02"]},
    "S_LOCN01":  {"descriptions": ["Locational Stock File Co 01"],
                  "data_files":   ["/user1/kopen/stock/S_LOCN01"]},
    "S_LOCN02":  {"descriptions": ["Locational Stock File Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_LOCN02"]},
    "S_LOG01":   {"descriptions": ["Stock Log file Co 01"],
                  "data_files":   ["/user1/kopen/stk_log/S_LOG01"]},
    "S_LOG02":   {"descriptions": ["Stock Log file Co 02"],
                  "data_files":   ["/user1/kopen/stk_log/S_LOG02"]},
    "S_PGRP01":  {"descriptions": ["Product Groups Co 01"],
                  "data_files":   ["/user1/kopen/stock/S_PGRP01"]},
    "S_PGRP02":  {"descriptions": ["Product Groups Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_PGRP02"]},
    "S_STOK01":  {"descriptions": ["Stock file Co 01"],
                  "data_files":   ["/user1/kopen/stock/S_STOK01"]},
    "S_STOK02":  {"descriptions": ["Stock file Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_STOK02"]},
    "S_TEXT01":  {"descriptions": ["Stock Additional Text Co 01"],
                  "data_files":   ["/user1/kopen/stk_text/S_TEXT01"]},
    "S_TEXT02":  {"descriptions": ["Stock Additional Text Co 02"],
                  "data_files":   ["/user1/kopen/stk_text/S_TEXT02"]},
    "S_TRNS01":  {"descriptions": ["In Transit file Co 01"],
                  "data_files":   ["/user1/kopen/stock/S_TRNS01"]},
    "S_TRNS02":  {"descriptions": ["In Transit file Co 02"],
                  "data_files":   ["/user1/kopen/stock/S_TRNS02"]},
    "z_SALLED01":{"descriptions": ["z_SalesLedgerCustomerFile01"],
                  "data_files":   ["/user1/kopen/accounts/SALLED01"]},
}

# Module prefixes → human-readable module name (used as fallback for unlisted files)
MODULE_PREFIXES = [
    ("ACCD",    "General Codes — shared code/lookup table"),
    ("ANALYS",  "Nominal Ledger (NL) — analysis / archive"),
    ("BS",      "Batch/Serial tracking"),
    ("CBAAUT",  "Cashbook (CB) — auto-postings analysis"),
    ("CBANAL",  "Cashbook (CB) — analysis"),
    ("CBAUTO",  "Cashbook (CB) — automatic postings"),
    ("CB",      "Cashbook (CB)"),
    ("CPENT",   "Sales Ledger (SL) — contract price entries"),
    ("CPHDR",   "Sales Ledger (SL) — contract price headers"),
    ("NL",      "Nominal Ledger (NL)"),
    ("OEENT",   "Order Entry (OE) — order line entries"),
    ("OEHDR",   "Order Entry (OE) — order headers"),
    ("OEMIA",   "Order Entry (OE) — monthly intake analysis"),
    ("OEMSA",   "Order Entry (OE) — monthly sales analysis"),
    ("OEPIK",   "Order Entry (OE) — picking notes"),
    ("PCCN",    "Purchase Ledger (PL) — consignments"),
    ("PCDRY",   "Purchase Ledger (PL) — control diary"),
    ("PCENT",   "Purchase Ledger (PL) — entries"),
    ("PCHDR",   "Purchase Ledger (PL) — purchase headers"),
    ("PCSUP",   "Purchase Ledger (PL) — supplier master"),
    ("PCVSI",   "Purchase Ledger (PL) — VSI file"),
    ("PG",      "Prospect/CRM module"),
    ("PPENT",   "Purchase Ledger (PL) — contract price entries"),
    ("PPHDR",   "Purchase Ledger (PL) — contract price headers"),
    ("PREGLN",  "Purchase Ledger (PL) — register lines"),
    ("PURDRY",  "Purchase Ledger (PL) — diary"),
    ("PURINV",  "Purchase Ledger (PL) — invoices / transactions"),
    ("PURLED",  "Purchase Ledger (PL) — supplier ledger"),
    ("PURLOG",  "Purchase Ledger (PL) — paid transactions log"),
    ("PURREG",  "Purchase Ledger (PL) — invoice register"),
    ("PURXTA",  "Purchase Ledger (PL) — extra fields"),
    ("REJECT",  "Rejection analysis"),
    ("RWINDX",  "Report Writer — report index"),
    ("SALDRY",  "Sales Ledger (SL) — diary"),
    ("SALINV",  "Sales Ledger (SL) — invoices / transactions"),
    ("SALLED",  "Sales Ledger (SL) — customer master"),
    ("SALLOG",  "Sales Ledger (SL) — paid transactions log"),
    ("SALXTA",  "Sales Ledger (SL) — extra fields"),
    ("SMSC",    "Stock Miscellaneous Codes"),
    ("S_LOCN",  "Stock — locational stock"),
    ("S_LOG",   "Stock — transaction log"),
    ("S_PGRP",  "Stock — product groups"),
    ("S_STOK",  "Stock master file"),
    ("S_TEXT",  "Stock — additional text"),
    ("S_TRNS",  "Stock — in-transit file"),
]


# ── Parser ─────────────────────────────────────────────────────────────────────

def parse_dd(path: Path) -> list[dict]:
    """Return a list of field dicts from a .DD file."""
    data = path.read_bytes()
    fields = []
    off = FIELD_START
    while off + REC_SIZE <= len(data):
        rec = data[off : off + REC_SIZE]
        if rec[1] == 0x00:
            break
        name    = rec[1:21].decode("latin1").rstrip()
        ftype   = chr(rec[21])
        foffset = struct.unpack(">I", b"\x00" + rec[22:25])[0]
        flength = struct.unpack(">I", b"\x00" + rec[25:28])[0]
        fdec    = rec[28]
        fsigned = bool(rec[29])
        fodbc   = chr(rec[30]) == "Y"
        fields.append({
            "name":      name,
            "type":      ftype,
            "type_name": TYPE_NAMES.get(ftype, ftype),
            "offset":    foffset,
            "length":    flength,
            "decimals":  fdec,
            "signed":    fsigned,
            "odbc":      fodbc,
        })
        off += REC_SIZE
    return fields


# ── Module inference ───────────────────────────────────────────────────────────

def infer_module(table_name: str) -> str:
    upper = table_name.upper()
    for prefix, desc in MODULE_PREFIXES:
        if upper.startswith(prefix):
            return desc
    return "Unknown module"


# ── Markdown writer ────────────────────────────────────────────────────────────

def write_md(out_path: Path, table_name: str, fields: list[dict]) -> None:
    cat       = CATALOGUE.get(table_name, {})
    descs     = cat.get("descriptions", [])
    dfiles    = cat.get("data_files",   [])
    module    = infer_module(table_name)
    company   = ""
    if table_name[-2:].isdigit():
        company = f"Company {int(table_name[-2:]):02d}"

    lines = []

    # ── Header ────────────────────────────────────────────────────────────────
    lines.append(f"# {table_name}")
    lines.append("")

    if len(descs) == 1:
        lines.append(f"**Description:** {descs[0]}")
    elif descs:
        lines.append("**Descriptions** (this DD file serves multiple logical tables):")
        for d in descs:
            lines.append(f"- {d}")
    else:
        lines.append("**Description:** *(not found in KISAM catalogue)*")

    lines.append("")
    lines.append(f"**Module:** {module}")
    if company:
        lines.append(f"**Company:** {company}")

    if len(dfiles) == 1:
        lines.append(f"**Data file:** `{dfiles[0]}`")
    elif dfiles:
        lines.append("**Data files:**")
        for df in dfiles:
            lines.append(f"- `{df}`")

    lines.append(f"**Field count:** {len(fields)}")
    if fields:
        max_off = max(f["offset"] + f["length"] - 1 for f in fields)
        lines.append(f"**Record length (approx):** {max_off} bytes")
    lines.append("")

    # ── Field table ───────────────────────────────────────────────────────────
    lines.append("## Fields")
    lines.append("")
    lines.append("| # | Name | Type | Offset | Length | Dec | Signed | ODBC |")
    lines.append("|---|------|------|-------:|-------:|:---:|:------:|:----:|")

    for i, f in enumerate(fields, 1):
        dec  = str(f["decimals"]) if f["decimals"] else ""
        sgn  = "Y" if f["signed"] else ""
        odbc = "Y" if f["odbc"]   else ""
        lines.append(
            f"| {i} | {f['name']} | {f['type_name']} "
            f"| {f['offset']} | {f['length']} | {dec} | {sgn} | {odbc} |"
        )

    lines.append("")

    # ── KCML reference block ──────────────────────────────────────────────────
    lines.append("## KCML field reference")
    lines.append("")
    lines.append("Copy-paste offsets for use in KCML `STR()` / `UNPACK` expressions.")
    lines.append("Offsets are 1-based as required by KCML.")
    lines.append("")
    lines.append("```")
    lines.append(f"REM {table_name} field offsets")
    for f in fields:
        lines.append(
            f"REM   {f['name']:<28}  {f['type']}"
            f"  off={f['offset']:>4}  len={f['length']:>4}"
            + (f"  dec={f['decimals']}" if f["decimals"] else "")
        )
    lines.append("```")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dd-dir",  default=str(DD_DIR),  help="Directory containing .DD files")
    parser.add_argument("--out-dir", default=str(OUT_DIR), help="Output directory for .md files")
    args = parser.parse_args()

    dd_dir  = Path(args.dd_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    dd_files = sorted(dd_dir.glob("*.DD"))
    if not dd_files:
        print(f"No .DD files found in {dd_dir}", file=sys.stderr)
        sys.exit(1)

    ok = errors = 0
    for dd_path in dd_files:
        table_name = dd_path.stem
        try:
            fields = parse_dd(dd_path)
            out_path = out_dir / f"{table_name}.md"
            write_md(out_path, table_name, fields)
            print(f"  {table_name:<14}  {len(fields):>3} fields  →  {out_path.name}")
            ok += 1
        except Exception as e:
            print(f"  ERROR {table_name}: {e}", file=sys.stderr)
            errors += 1

    print(f"\n{ok} tables written to {out_dir}  ({errors} errors)")


if __name__ == "__main__":
    main()
