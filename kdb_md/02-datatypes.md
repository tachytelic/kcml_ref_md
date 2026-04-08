# KDB Data Types

## SQL Type Mapping

This table shows the mapping between SQL data types used in `CREATE TABLE` statements and the internal dictionary type codes used in legacy KCML files.

The `SIGNED` / `UNSIGNED` attributes can override defaults. Packed numbers are assumed SIGNED. Integers are assumed UNSIGNED.

`prec` = total digits; `scale` = digits after decimal point.

| Dict code | SQL type | Purpose |
|-----------|----------|---------|
| `C` | `VARCHAR(len)` | Character strings of any size. NULL if first byte is `0xFF` or `0x00` |
| `P` | `NUMERIC(prec[, scale])` | KCML packed decimal numbers. NULL if first byte is `0xFF` |
| `B` | `INTEGER[(size)]` | Binary integers, 1–4 bytes. Cannot be NULL |
| `N` | `INTEGER(4)` | Internal 4-byte integer representation. Cannot be NULL, not portable |
| `J` | `DATE` | Julian date stored as 3-byte unsigned integer. Zero = NULL |
| `D` | `OLD_DATE` | Old date representation — no longer used |
| `H` | `HEX(len)` | Binary data rendered as hex digits. Almost obsolete |
| `F` | `BIT` | Logical/flag: synthetic type for single-byte `Y`/`N`/blank columns |
| `G` | `BOOL` | Boolean — `Y`/`1` or `N`/`0` held as single byte |
| `L` | `BCDDATE` | 3-byte `YYMMDD` or 4-byte `CCYYMMDD` packed BCD date |
| `K` | `DECIMAL(prec[, scale])` | IBM packed (BCD) numbers |
| `T` | `TIME` | Seconds since midnight (local) as 3-byte unsigned integer |
| `M` | `TIMESTAMP` | Milliseconds since 00:00 GMT year 0000, 6-byte unsigned integer |
| `O` | `BLOB` | Binary Large Object |
| `Q` | `CBLOB` | Character BLOB |

### Notes on specific types

**VARCHAR**: Fixed-length and space-padded in KCML. `LEN()` returns content length excluding trailing spaces.

**NUMERIC / DECIMAL**: Packed numeric types (`P` = KCML native packed, `K` = IBM packed BCD). Use `HEXUNPACK` to read these from legacy files. See the decode pattern below.

**DATE (Julian)**: The `J` type stores the Julian day number as a 3-byte unsigned integer. Zero means NULL. KCML's date functions handle conversion automatically.

**BCDDATE (`L` type)**: Used in many legacy Kerridge applications. 4-byte variant stores `CCYYMMDD` as binary-coded decimal. To display as DD/MM/YYYY:
```kcml
: DIM hex$12, date$10
: HEXUNPACK STR(rec$, 82, 4) TO hex$
: date$ = STR(hex$, 7, 2) & "/" & STR(hex$, 5, 2) & "/" & STR(hex$, 1, 4)
```

**IBM Packed Decimal (`K` type, also `I` in legacy DD files)**: Each byte holds two BCD digits (nibbles). The last nibble is the sign: `C` = positive, `D` = negative, `F` = unsigned. Use `UNPACK` with the matching image string — this works directly on IBM BCD format and is verified on real KISAM files:

```kcml
: REM 8-byte field, 6 decimal places = 15 total digits (9 integer + 6 decimal)
: DIM packed$8, val
: packed$ = STR(rec$, start_offset, 8)
: UNPACK (#########.######) packed$ TO val
```

The image must match the field's precision. For a field with `n` total digits and `s` scale: `n - s` `#` characters, a `.`, then `s` `#` characters.

If needed as a fallback (e.g. to inspect the raw BCD or handle unusual sign codes), the manual approach using HEXUNPACK:
```kcml
: DIM hex$20, valstr$20, sign$1, val
: HEXUNPACK packed$ TO hex$
: sign$ = STR(hex$, 16, 1)
: valstr$ = STR(hex$, 1, 9) & "." & STR(hex$, 10, 6)
: CONVERT valstr$ TO val
: IF sign$ == "D" THEN val = -val
```

**Note on type conversion:** `VAL(str$, n)` in KCML reads `n` bytes of `str$` as a **binary integer** (inverse of `BIN(`) — it does NOT parse ASCII decimal text. Use `CONVERT str$ TO num` for parsing ASCII number strings.

---

## Legacy File Types

KDB table storage has evolved through several file format versions. KCML 6.x can read and write all earlier formats.

| File type | KCML version | Details |
|-----------|-------------|---------|
| 1 | 2.0 | Obsolete |
| 2 | 2.0 | Obsolete |
| 3 | 3.0 | Effectively obsolete — auto-converted to type 4 if accessed by later KCML |
| 4 | 3.1 | Fixed size, limited index size |
| 5 | 3.2 | Fixed size, larger index size |
| 6 | 5.0 | Extents, unlimited index/data size, word search indexing |
| 7 | 6.0 | Page-structured, embedded schema, BLOB support, requires KDB connection |

**Type 7** is the current format (KCML 6.x). It uses 8KB pages containing data or index blocks. Key differences from earlier types:
- Non-unique indices are not supported — all indices must be unique
- Word search index blocks are in the same file as data
- BLOBs are stored in the same file
- Requires a KDB database connection (cannot be used with the default connection 0)
- Schema is embedded in the table file itself

**Converting legacy files:**
- Types 3–6: use `krebuild` to convert in-place up to type 6
- Type 6 → type 7: use `kconvert` (creates a new file)

---

## Binary Large Objects (BLOBs)

BLOBs are streams of binary data of arbitrary size stored in type 7 tables.

- BLOBs are **not** stored inline in the row — the row column holds a 6-byte **BID** (BLOB Identifier)
- Multiple BLOB columns per row are allowed
- One BLOB cannot be associated with more than one row or column
- BLOBs were introduced with type 7 tables

### Declaring a BLOB column

```sql
CREATE TABLE Movies (
    FILM     VARCHAR(30),
    RELDATE  DATE,
    STAR     VARCHAR(30),
    TRAILER  BLOB
)
```

### BLOB API

| Call | Purpose |
|------|---------|
| `KI_BLOB_GET` | Retrieve BLOB data by BID |
| `KI_BLOB_SET` | Insert or update BLOB data |

### BLOB workflow for inserting a new row with a BLOB

```
1. INSERT row with NULL BLOB column (KI_WRITE with null BID)
2. Call KI_BLOB_SET with the row buffer and BLOB data — this saves the BLOB,
   allocates a BID, and updates the row internally
3. The lock remains set — finally call KI_UNLOCK or KI_REWRITE
```

Setting a BLOB column to zero and rewriting the row automatically deletes the previously associated BLOB.

If a row is deleted, associated BLOBs are automatically deleted by the database.

Data binding for forms will transmit a BLOB to a control automatically (pictures as JPG/PNG etc.).
