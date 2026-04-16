# SPOOLMAST — KISAM Catalogue and Data Dictionary Tools

This directory contains tools for interrogating the KISAM K-Open 3 internal
catalogue (`ODRWCAT`) and data dictionary (`.DD`) files.  The outputs feed
the `../datadict/` reference directory used by the KCML extraction programs.

---

## Files

### dd_reader.py

Reads every `.DD` file in the live K-Open 3 data dictionary directory and
writes one Markdown reference file per table into `../datadict/`.

**Usage:**

```bash
python3 dd_reader.py [--dd-dir DIR] [--out-dir DIR]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--dd-dir` | `/user1/kopen/datadict` | Directory containing the live `.DD` files |
| `--out-dir` | `../datadict` (relative to this script) | Where to write the generated `.md` files |

Each generated `.md` file contains a field table (name, type, offset, length,
decimal places, signed flag, ODBC-updatable flag) and a ready-to-paste KCML
field-offset reference block.

The script also embeds the `CATALOGUE` dict, which maps DD file stems to their
human-readable descriptions and physical data file paths.  This data was
obtained by running `dump_odrwcat.src` against the live `ODRWCAT` B-tree.

---

### dump_odrwcat.src

KCML program that performs a full sequential scan of the `ODRWCAT` B-tree
catalogue and prints one pipe-delimited line per record to stdout.

`ODRWCAT` is the authoritative index of all K-Open 3 tables — it maps each
logical table name to its physical data file path, DD file path, and display
description.

**Usage:**

```bash
kcml -p dump_odrwcat.src
```

The file is hardcoded to `/user1/kopen/datadict/ODRWCAT` (the standard
K-Open 3 install path).

**Output columns** (pipe-delimited, one row per catalogue entry):

| Col | ODRWCAT offset | Content |
|-----|---------------|---------|
| 1 | 2, len 35 | DD file stem (table name key) |
| 2 | 37, len 96 | Physical data file path |
| 3 | 133, len 96 | DD file path |
| 4 | 229, len 1 | Flag field |
| 5 | 230, len 1 | Flag field |
| 6 | 249, len 35 | Display description |
| 7 | 284, len 1 | Flag field |
| 8 | 285, len 10 | Additional field |

Redirect the output and paste into the `CATALOGUE` dict in `dd_reader.py`
when the catalogue needs refreshing.

---

### libRW.src

Source extract from the KISAM K-Open 3 Report Writer library (`GB/libRW`),
preserved here for reference.  It documents the internal KCML routines used
by K-Open 3 itself to manage the `ODRWCAT` catalogue, the `RWINDX` report
index, and the NRG (New Report Generator) parameter/index files.

This file is **not executed directly** — it is an excerpt from the live KISAM
source tree included here so the catalogue field offsets and B-tree layout are
documented alongside the tools that use them.

Key routines:

| Routine | Purpose |
|---------|---------|
| `open_rw_files` | Opens ODRWCAT and RWINDX; creates them if absent |
| `read_rw_catalogue` / `write_rw_catalogue` | Read/write ODRWCAT records |
| `read_rw_dd` / `write_rw_dd` | Read/write `.DD` field records |
| `open_nrg_files` | Opens NRGPARAM, NRGSINDX, NRGDICT for the NRG module |

The `DATA` statements starting at line 12004 are the authoritative catalogue
field offsets (matching the columns extracted by `dump_odrwcat.src`).

---

## Workflow — refreshing the datadict

1. Run `dump_odrwcat.src` on the K-Open 3 server to get a fresh catalogue dump.
2. Update the `CATALOGUE` dict in `dd_reader.py` if any table descriptions or
   data file paths have changed.
3. Run `dd_reader.py` to regenerate all files in `../datadict/`.
4. Commit the updated `../datadict/` files.
