# ERP.md — Kerridge SOP ERP Reference

This file documents the specific file formats, field maps, and patterns for the Kerridge SOP ERP system running on this server. It is separate from CLAUDE.md (general KCML language patterns).

Key file paths:
- SOP files: `/user1/kopen/sop/`
- Stock files: `/user1/kopen/stock/`
- ERP programs: `/user1/kopen/D40/`

---

## ERP File Handle Map (gb_h array, from LIST DIM inside SOP menu)

The ERP keeps all files open in the `gb_h(255)` handle array. Key handles relevant to sales order processing:

| gb_h index | File | Notes |
|------------|------|-------|
| 50 | S_CON01 (PF controls) | Control records including PFN8 order number counter |
| 65 | OEHDR01 | Order header file |
| 66 | OEENT01 | Order entry lines file |
| 68 | OEMSA01 | Sales analysis (current) |
| 70 | OEMSA01 | Sales analysis (year) |

These handles are valid when attached via `SELECT @PART "KOPEN3GB"`. From a standalone script, open the files directly with `KI_OPEN`.

---

## OEHDR01 — Sales Order Header File

> **Note:** Direct creation of order records by writing raw bytes to OEHDR01/OEENT01 was attempted but abandoned — the resulting records are too sparse compared to what the ERP UI produces (many fields unpopulated, no allocation, no stock commitment). Order creation requires the full ERP session context. The field maps below are retained for use by read tools.

### OE_P1/OE_P2 Field Map (from libOE DATA statement, 1-based index)

| Index | Start | Len | Content |
|-------|-------|-----|---------|
| 1  | 18  | 10  | order_no |
| 2  | 28  | 30  | account (account_10 + billing_10 + account_6 + 4 pad) |
| 3  | 58  | 24  | cus_ref |
| 4  | 82  | 32  | dates (8 × 4-byte packed BCD) |
| 5  | 114 | 150 | del_name + del_a1..a4 (5 × 30) |
| 6  | 264 | 150 | inv_name + inv_a1..a4 (5 × 30) |
| 7  | 414 | 20  | payment terms text |
| 8  | 434 | 1   | order type code (e.g. 'I') |
| 9  | 435 | 120 | — |
| 10 | 555 | 1   | currency code (space = base currency) |
| 11 | 556 | 1   | flag ('N') |
| 12 | 557 | 4   | code (e.g. "0051") |
| 13 | 561 | 24  | — |
| 14 | 585 | 1   | currency flag ('F') |
| 15 | 586 | 160 | BCD numeric fields (20 × 8 bytes) |
| 16 | 746 | 1   | **setup flags byte — bit 0x02 = header set up** |
| 17 | 747 | 2   | — |
| 18 | 749 | 24  | — |
| 19 | 783 | 24  | flag bytes ('N', 'Y', 'N', ...) |
| 20 | 807 | 192 | — |
| 21 | 999 | 64  | BCD numeric fields (8 × 8 bytes) |
| 31 | 1106 | 6  | 6-byte null field |

### OE_PX1/OE_PX2 Set 2 (from libOE)

| Index | Start | Len | Content |
|-------|-------|-----|---------|
| 3 | 775 | 4 | sm_number (packed 4-byte int, 0 for standard SOP) |
| 4 | 779 | 1 | SM type code (space for standard SOP) — checked for "Sales Management type" error |
| 5 | 780 | 1 | flag |
| 6 | 781 | 1 | flag |
| 7 | 782 | 1 | flag |

---

## OEENT01 — Sales Order Entry Lines File

### Key Structure (verified by KI_INFO)

Primary key (path 1) is 13 bytes: 10-byte order_no (ASCII, left-aligned, space-padded) + 3-byte line_seq (binary big-endian integer).

```kcml
REM Build key for order 719908, line 1:
ki_key$ = "719908    "    REM 10 chars, space-padded
STR(ki_key$, 11, 3) = BIN(1, 3)
CALL KI_READ h, ki_key$, 1, ki_sym TO ki_status, ki_dataptr$
```

### Field Map (from oe_k1/oe_k2, verified by LIST DIM)

| oe_k1 index | Offset | Len | Content |
|-------------|--------|-----|---------|
| 1  | 18  | 1  | line type ('P'=part, 'T'=text) |
| 2  | 19  | 24 | part_no (15 chars + padding) |
| 8  | 151 | 6  | UOM |
| 17 | 378 | 10 | order_no |
| 18 | 388 | 3  | line_seq (binary) |

Packed BCD fields (8 bytes, format `#########.######`, sign nibble `C`):
- Offset 186: qty_to_follow
- Offset 202: unit price

---

---

## ERP Wrapper Bug: ki_start_beg After EOF

After reading a KISAM file to EOF using the ERP global wrapper, `GOSUB 'ki_start_beg(handle, 1)` fails to reposition — it returns a non-zero status. The fix: capture the first record key before any EOF scan, then use `GOSUB 'ki_start(handle, first_key$, 1)` to restart.

`CALL KI_START_BEG handle, 1 TO ki_status` (direct KCML call, not the ERP wrapper) works correctly after EOF.

---

## ERP libKI Wrapper Notes

The ERP's `GOSUB 'ki_write(handle, sym)` wrapper (in GB/libKI) does the following before calling `CALL KI_WRITE`:
- Sets lock byte (offset 1) to `HEX(00)`
- Stamps USER_CREATE, USER_AMEND from `u6$(8)` (current user)
- Stamps DATE_CREATE, DATE_AMEND from `TODAYP$` (today's packed date)

Direct `CALL KI_WRITE h, SYM(rec$), 0 TO ki_status, ki_dataptr$` skips these stamps — set them manually if required.

Similarly, `GOSUB 'ki_rewrite` auto-stamps USER_AMEND/DATE_AMEND; direct `CALL KI_REWRITE` does not.
