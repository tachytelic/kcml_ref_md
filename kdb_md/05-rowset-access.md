# KDB Rowset Access — Sequential and Direct Reads

## Overview

Once a table is open on a handle, rows can be read in two ways:

1. **Sequential access** — traverse rows in index order using `KI_START` / `KI_START_BEG` to position, then `KI_READ_NEXT` repeatedly
2. **Direct access by ROWID** — use `KI_READ_PTR` to load a specific row by its 6-byte ROWID token

---

## KI_START

Sets the current sequential pointer **before** the row indexed by the supplied key. A subsequent `KI_READ_NEXT` will read the first row with a key **greater than or equal to** the supplied key.

```
CALL KI_START handle, key$, path TO ki_status
```

| Parameter | Purpose |
|-----------|---------|
| `handle` | Open table handle |
| `key$` | The key value to position at (need not exist in the index) |
| `path` | Index path number (1-based). Negative path positions **after** the key for reverse traversal |
| `ki_status` | Always succeeds if the table is open |

**Forward traversal (most common):**
```kcml
: DIM ki_key$64
: ki_key$ = ALL(HEX(00))
: CALL KI_START handle, ki_key$, 1 TO ki_status
```

**Reverse traversal:**
```kcml
: REM Position after the key — subsequent KI_READ_NEXT on negative path reads backwards
: CALL KI_START handle, ki_key$, -1 TO ki_status
```

Do not change direction without re-issuing `KI_START` — the definition of "current row" is the row last read, not the row about to be read.

---

## KI_START_BEG

Positions the sequential pointer at the very beginning of the index (before the first row). This is the standard way to start a full table scan.

```
CALL KI_START_BEG handle, path TO ki_status
```

```kcml
: CALL KI_START_BEG handle, 1 TO ki_status
```

---

## KI_READ_NEXT

Reads the next sequential row from the index path.

```
CALL KI_READ_NEXT handle, path, ki_sym TO ki_status, ki_dataptr$, ki_key$
```

| Parameter | Purpose |
|-----------|---------|
| `handle` | Open table handle |
| `path` | Index path (positive = forward, negative = reverse, 0 = continue same direction as `KI_START`) |
| `ki_sym` | `SYM()` of the row buffer — pre-compute before the loop, do not pass `SYM()` inline |
| `ki_status` | Returns 0 on success, 2 at EOF, non-zero on error |
| `ki_dataptr$` | Must be declared as exactly 6 bytes |
| `ki_key$` | Receives the key value of the row read |

**Important rules:**
- Declare `ki_dataptr$` as exactly 6 bytes: `DIM ki_dataptr$6`
- Pre-assign `ki_sym = SYM(rec$)` before the loop — do not pass `SYM(rec$)` inline
- If `ki_sym` is 0, the data is not read but `ki_key$` and `ki_dataptr$` are still updated (useful for key-only scans, followed by `KI_READ_PTR`)
- Status 2 = EOF (normal end), 0 = success

**Complete sequential read example:**
```kcml
: DIM handle, ki_status, ki_sym, ki_dataptr$6, ki_key$64
: DIM rec$512, count

: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END

: CALL KI_OPEN handle, "/data/CUSTFILE", "R" TO ki_status
: IF ki_status <> 0 THEN $END

: CALL KI_START_BEG handle, 1 TO ki_status
: ki_sym = SYM(rec$)
: count = 0

: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN DO
:     count++
:     PRINT "Row "; count; ": Key=["; STR(ki_key$, 1, 10); "]"
:   END DO
: UNTIL ki_status <> 0

: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
: $END
```

**Partial key scan — read only rows starting with a prefix:**
```kcml
: DIM prefix$10
: prefix$ = "AB"
: CALL KI_START handle, prefix$, 1 TO ki_status
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status <> 0 THEN BREAK
:   IF STR(ki_key$, 1, 2) <> "AB" THEN BREAK
:   PRINT STR(ki_key$, 1, 20)
: UNTIL FALSE
```

---

## KI_READ_PTR

Reads a row directly by its ROWID, bypassing the index. This is fast — no index lookup required.

```
CALL KI_READ_PTR handle, rowid$, ki_sym TO ki_status
```

Returns `KE_NOTFOUND` if the ROWID is invalid or the row has been deleted.

```kcml
: DIM rowid$6
: REM rowid$ was obtained from a previous KI_READ_NEXT call
: CALL KI_READ_PTR handle, rowid$, ki_sym TO ki_status
: IF ki_status <> 0 THEN PRINT "Row not found"
```

**Key-only scan then fetch by ROWID:**
```kcml
: REM Pass ki_sym = 0 to KI_READ_NEXT to skip data read, just get key + rowid
: CALL KI_READ_NEXT handle, 1, 0 TO ki_status, ki_dataptr$, ki_key$
: REM ki_dataptr$ now holds the ROWID — use it to fetch the full row
: CALL KI_READ_PTR handle, ki_dataptr$, ki_sym TO ki_status
```

---

## KI_BIND_COL

Binds a KCML program variable to a specific column in an open rowset. After binding, whenever the current row changes (following `KI_READ_NEXT`, `KI_FETCH`, etc.) the bound variable is automatically updated.

```
CALL KI_BIND_COL handle, col, SYM(var$) TO ki_status
```

`col` can be a column ordinal (integer, counted from 1) or a column name string.

**Important limitation (verified by testing):** Binding by column name only works on **type 7 KDB tables** created with `CREATE TABLE` (which have an embedded schema). On legacy type 6 and earlier KISAM files, `KI_BIND_COL` with a column name returns status 18 (not available) and the variable will not be populated. For those files, use `STR(rec$, start, length)` to extract fields directly by byte offset.

Binding by column ordinal (integer) may work on both type 6 and type 7 tables.

```kcml
: REM Type 7 KDB table - bind by column name works
: CALL KI_OPEN handle, "GB_00_users", "R" TO ki_status
: CALL KI_BIND_COL handle, "userid", SYM(userid$) TO ki_status
: CALL KI_BIND_COL handle, "username", SYM(username$) TO ki_status
: CALL KI_START_BEG handle, 1 TO ki_status
: REPEAT
:   CALL KI_READ_NEXT handle, 1, 0 TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN PRINT userid$; " - "; username$
: UNTIL ki_status <> 0
```

```kcml
: REM Legacy type 6 KISAM file - use STR() with byte offsets instead
: CALL KI_OPEN handle, "/data/S_STOK01", "R" TO ki_status
: CALL KI_START_BEG handle, 1 TO ki_status
: DIM part$15, desc$30
: ki_sym = SYM(rec$)
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN DO
:     part$ = STR(rec$, 20, 15)
:     desc$ = STR(rec$, 36, 30)
:     PRINT part$; " - "; desc$
:   END DO
: UNTIL ki_status <> 0
```

On `KI_WRITE` / `KI_REWRITE`, the contents of bound variables are written back into the row buffer. For BLOB columns, the BLOB itself is fetched or written automatically.

---

## KI_FLD

Initialises field symbols in the current program's symbol table corresponding to columns in a type 7 table. Each field symbol defines an offset into the row buffer and a data type, usable with `FLD()` for data-aware access.

```
CALL KI_FLD handle, prefix$, BYREF reclen, BYREF cols TO ki_status
```

| Parameter | Purpose |
|-----------|---------|
| `handle` | Open table handle (table must have been created with `CREATE TABLE`) |
| `prefix$` | Prefix to prepend to column names (replaces any IPREFIX on the table if supplied) |
| `reclen` | Returns the recommended row buffer size |
| `cols` | Returns the number of columns initialized |

For a table created as:
```sql
CREATE TABLE XX00test (name VARCHAR(10), deptno NUMERIC(4)) IPREFIX 'XX_'
```

Calling `KI_FLD(h, "", reclen, cols)` initialises field symbols `.XX_name$` and `.XX_deptno`.

Calling `KI_FLD(h, "ZZ_", reclen, cols)` initialises `.ZZ_name$` and `.ZZ_deptno` instead.

```kcml
: DIM rec$512, reclen, cols
: CALL KI_FLD handle, "", reclen, cols TO ki_status
: REM Now .XX_name$ and .XX_deptno are available as field symbols
: CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
: PRINT FLD(.XX_name$); " dept "; FLD(.XX_deptno)
```

`KI_FLD` can also be used with SQL query result sets after `KI_PREPARE`.
