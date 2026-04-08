# KDB Table Open, Close and Create

## KI_OPEN

Opens a table for rowset access. The handle must be supplied in all subsequent database calls referencing the table.

```
CALL KI_OPEN handle, file$, mode$ TO ki_status
```

| Parameter | Purpose |
|-----------|---------|
| `handle` | Handle allocated by `KI_ALLOC_HANDLE` |
| `file$` | Full path to the table file |
| `mode$` | Access mode string (see below) |
| `ki_status` | Returns 0 on success |

**Access modes:**

| Mode | Meaning |
|------|---------|
| `"R"` | Read only — always allowed regardless of other users' open mode |
| `"W"` | Read/write — allowed if no other user has the table open exclusively |
| `"X"` | Exclusive — guarantees no other user has the table open for writing |
| `"U"` | Unchecked — for utility programs that need to open regardless of state (e.g. repair) |

Write operations fail with `KE_BADFUNCTION` in `"R"` mode. Opening in `"W"` mode when another user holds it exclusively fails with `KE_ACCESS`. Re-opening an already open handle is permitted.

After an open, the sequential pointer is undefined. A `KI_START` or `KI_START_BEG` is required before any sequential read.

**Important: Use 3-parameter form in KCML 6.x:**
```kcml
: CALL KI_OPEN handle, "/full/path/to/FILENAME", "R" TO ki_status
```

Do NOT use the 4-parameter `KI_OPEN handle, stream, file$, mode$` form — this causes an S24 panic in KCML 6.x.

**Examples:**

```kcml
: REM Open for reading
: CALL KI_OPEN handle, "/data/CUSTFILE", "R" TO ki_status
: IF ki_status <> 0 THEN PRINT "Open failed: "; ki_status
: IF ki_status <> 0 THEN $END

: REM Open for read/write
: CALL KI_OPEN handle, "/data/CUSTFILE", "W" TO ki_status
```

---

## KI_CLOSE

Closes the table, flat file, or result set open on the handle, allowing the handle to be reused. The handle itself still exists and can be freed with `KI_FREE_HANDLE`.

Tables should be closed promptly to keep access control information up-to-date.

```
CALL KI_CLOSE handle TO ki_status
```

```kcml
: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
```

---

## KI_CREATE

Creates and opens a new legacy table (type 6 or earlier). **Not available for type 7 KDB tables** — use `CREATE TABLE` SQL instead.

```
CALL KI_CREATE handle, rows, rowlen, Type, keyspec$, packfactor, blocklen TO ki_status
```

| Parameter | Purpose |
|-----------|---------|
| `rows` | Maximum number of rows in the first extent |
| `rowlen` | Length of each row in bytes |
| `Type` | Table format type: use `6` unless backward compatibility is required |
| `keyspec$` | Array of up to 18 index definitions (33 bytes each), or `0` for unindexed |
| `packfactor` | Index block packing percentage: 50 for volatile tables, 100 for static |
| `blocklen` | Index block size in units of 256 bytes (2, 4, or 8) |

Each index definition in `keyspec$()` has this structure:
- Byte 1: `'Y'` or `'N'` — whether duplicates are permitted in this key path
- Bytes 2–33: Up to 8 segment specifiers, each 4 bytes:
  - 2 bytes: start of segment (binary, counted from 1)
  - 1 byte: length of segment (binary)
  - 1 byte: flag byte (must be `HEX(00)`)

To discover the required file size before creating, use `KI_SIZE_FILE`.

**Note:** `KI_CREATE` is for legacy type 6 and earlier tables only. Type 7 tables must be created via SQL `CREATE TABLE`.

---

## KI_SIZE_FILE

Returns the number of bytes (in 256-byte allocation units) required to create a table with the given specification. Same parameters as `KI_CREATE`.

```
CALL KI_SIZE_FILE rows, rowlen, Type, keyspec$, packfactor, blocklen TO size
```

Useful for pre-checking disk space before `KI_CREATE`.
