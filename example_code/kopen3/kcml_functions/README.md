# kcml_functions — Native KCML DB Extraction Programs

This directory contains KCML programs that extract business documents directly
from KISAM K-Open 3 database files, bypassing spool text parsing entirely.
Each program reads structured binary data from the relevant B-tree DB files and
emits a single JSON object to stdout, ready for submission to Power Automate.

This approach is more reliable than scraping fixed-width spool text — the data
comes straight from the ERP source of truth with correct types, clean strings,
and no dependency on print layout or page formatting.

---

## Environment

Programs require the KCML runtime wrapper and the `JSON_ESCAPE` user function:

```bash
/usr/local/bin/kcml -x /usr/lib/kcml/uf_json.so -p <program.src> [args...]
```

- `/usr/local/bin/kcml` — wrapper script that sets `MAC_ADDRESS`, `SPOOF_HOSTNAME`,
  and `LD_PRELOAD` before exec'ing the 32-bit KCML binary
- `/usr/lib/kcml/uf_json.so` — 32-bit shared library providing the `JSON_ESCAPE`
  user function (compiled from `kcml_ufn/json_escape/uf_json.c`)

---

## KISAM database reference

Field offsets for all 113 K-Open 3 tables are documented in
`../datadict/*.md`, generated from the live `.DD` data dictionary files by
`../SPOOLMAST/dd_reader.py`. The ODRWCAT B-tree catalogue (at
`/user1/kopen/datadict/ODRWCAT`) is the authoritative mapping of logical table
names to physical data file paths and DD file paths.

All offsets are **1-based** as required by KCML `STR()` and `UNPACK` expressions.

Binary integer fields use `UNPACK (########) STR(rec$, off, len)` for plain
integers and `UNPACK (#########.######) STR(rec$, off, len)` for fields with
6 implied decimal places (monetary values and quantities).

Date fields (type D) are 4-byte packed BCD in `CCYYMMDD` order; decode with
`HEXUNPACK` then rearrange digits.

### KCML syntax note

**Never put a colon `:` in a REM statement.** KCML treats the colon as a
statement separator even inside a REM line, causing a syntax error. Use a dash
`-` instead; e.g. `REM Phase 1 - description` not `REM Phase 1: description`.

---

## Programs

### pik_to_json.src

Extracts a picking note from the Order Entry DB files.
See [pik_to_json.md](pik_to_json.md) for full details.

**Arguments:** `<sop_dir>` `<picking_note_number>`

```bash
kcml -x /usr/lib/kcml/uf_json.so -p pik_to_json.src /user1/kopen/sop 114315
```

**DB files used:** `OEPIK01`, `OEHDR01`, `OEENT01`

---

### inv_to_json.src

Extracts a sales invoice from the Order Entry and Sales Ledger DB files.
See [inv_to_json.md](inv_to_json.md) for full details.

**Arguments:** `<sop_dir>` `<accounts_dir>` `<invoice_number>`

```bash
kcml -x /usr/lib/kcml/uf_json.so -p inv_to_json.src /user1/kopen/sop /user1/kopen/accounts 153132
```

**DB files used:** `SALINV01`, `OEPIK01`, `OEHDR01`, `SALLED01`, `OEENT01`

---

## Integration with process_spool.py

`process_spool_v2/process_spool.py` calls these programs via `call_kcml()`.
The `KCML_PROGRAMS` dict maps a document category (derived from the SPOOLMAST
stationery field) to the `.src` filename:

```python
KCML_PROGRAMS = {
    "picking_note": "pik_to_json.src",
    "invoice":      "inv_to_json.src",
}
```

The document reference (picking note number, invoice number, etc.) is extracted
from the SPOOLMAST `description` field for the relevant stationery type.

---

## Adding a new program

1. Create a `.src` file in this directory
2. Accept the DB directory path(s) via `$ARG(1)` / `$ARG(2)` and the document
   reference as the final argument
3. Build DB file paths by concatenating the directory with the table name,
   e.g. `pik_file$ = sop_dir$ & "/OEPIK01"`
4. Use `KI_ALLOC_HANDLE`, `KI_OPEN`, `KI_START` / `KI_START_BEG`, and
   `KI_READ_NEXT` to navigate the B-tree files
5. Use `KI_START` for direct key lookups (when you know the key value) and
   `KI_START_BEG` + scan loop for searches on non-key fields
6. Emit a JSON object to stdout; use `CALL JSON_ESCAPE` for all string values
7. Create a companion `.md` file documenting the tables, fields, and output schema
8. Add an entry to `KCML_PROGRAMS` in `process_spool_v2/process_spool.py`
9. Update this README
