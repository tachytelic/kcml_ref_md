# KDB Handles and Connections

## KI_ALLOC_HANDLE

Allocates a rowset handle for use in opening a table or issuing a query.

```
CALL KI_ALLOC_HANDLE handle, conn TO newhand, ki_status
```

| Parameter | Purpose |
|-----------|---------|
| `handle` | Allocation mode (see below) |
| `conn` | Connection number (use `1` for the default KISAM connection) |
| `newhand` | Returns the allocated handle number |
| `ki_status` | Returns 0 on success |

**Allocation modes for `handle`:**

| Value | Meaning |
|-------|---------|
| Positive integer | Close any existing handle at that slot and assign it |
| `_KDB_AUTO_HANDLE` (= `0`) | Auto-allocate from the lowest free handle in the pool |
| `_KDB_TEMP_HANDLE` (= `-1`) | Auto-allocate from the highest free handle; marked as temporary — automatically closed on `LOAD` or `RUN` or `KI_CLEAR_HANDLES` |

The most common usage in standalone scripts is `_KDB_AUTO_HANDLE` (pass `0`):

```kcml
: DIM handle, ki_status
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END
```

Handles allocated with `KI_ALLOC_HANDLE` should be freed with `KI_FREE_HANDLE` when done.

---

## KI_FREE_HANDLE

Frees the memory associated with a handle previously allocated by `KI_ALLOC_HANDLE`. The table or file on the handle **must** already be closed with `KI_CLOSE` before calling this.

```
CALL KI_FREE_HANDLE handle TO ki_status
```

```kcml
: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
```

---

## KI_CLEAR_HANDLES

Closes and frees all temporary auto-allocated handles (those allocated with `_KDB_TEMP_HANDLE`). Normally not needed explicitly as temporary handles are implicitly closed on `RUN` or `LOAD`.

```
CALL KI_CLEAR_HANDLES TO ki_status
```

---

## KI_INITIALISE

Truncates a table to zero rows. The table must already be open in exclusive (`"X"`) or unchecked (`"U"`) mode.

```
CALL KI_INITIALISE handle TO ki_status
```

```kcml
: CALL KI_OPEN handle, "/path/to/TABLE", "X" TO ki_status
: IF ki_status <> 0 THEN $END
: CALL KI_INITIALISE handle TO ki_status
: CALL KI_CLOSE handle TO ki_status
```

---

## Status Codes

Common status values returned in `ki_status`:

| Value | Meaning |
|-------|---------|
| `0` | Success |
| `1` | Not found (key not in index) |
| `2` | EOF — no more rows |
| Non-zero | Error — check with `KI_ERROR` or `KI_ERROR_TEXT` |

---

## Typical Handle Lifecycle (Standalone Script)

Connection 1 is auto-created as KISAM on script start — no `KI_ALLOC_CONNECT` needed for default file access.

```kcml
: DIM handle, ki_status, rec$512, ki_sym, ki_dataptr$6, ki_key$64, count

: REM Allocate handle on connection 1 (auto-KISAM)
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END

: REM Open table
: CALL KI_OPEN handle, "/data/MYTABLE", "R" TO ki_status
: IF ki_status <> 0 THEN $END

: REM Position to start
: CALL KI_START_BEG handle, 1 TO ki_status

: REM Read loop
: ki_sym = SYM(rec$)
: count = 0
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN count++
: UNTIL ki_status <> 0 OR count >= 100

: REM Close and free
: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
: $END
```
