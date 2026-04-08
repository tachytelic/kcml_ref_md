# KDB SQL API — Prepare, Execute, Fetch

## Overview

SQL statements are executed in KCML using a three-step process:

1. **`KI_PREPARE`** — parse and compile the SQL statement into a query plan
2. **`KI_EXECUTE`** — execute the prepared query plan
3. **`KI_FETCH`** — retrieve result rows one at a time (for SELECT)

After use, the handle **must** be closed with `KI_CLOSE` before it can be reused.

---

## KI_PREPARE

Parses an SQL statement and generates an execution plan stored against the handle. Returns the number of columns in the result set (zero for non-SELECT statements like DELETE or UPDATE).

```
CALL KI_PREPARE handle, sql$ TO ki_status, colcount
```

| Parameter | Purpose |
|-----------|---------|
| `handle` | Allocated handle (from `KI_ALLOC_HANDLE`) |
| `sql$` | The SQL statement string |
| `ki_status` | 0 on success |
| `colcount` | Number of result columns (0 for non-SELECT) |

The prepare phase can be expensive as KCML optimises the query plan. Use **parameters** (`?` tokens) to reuse a prepared plan with different values without recompiling. Parameters are positional, counted left to right.

```kcml
: DIM sql$128, ki_status, colcount
: sql$ = "SELECT color, quantity FROM SL00test WHERE color = ?"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
```

---

## KI_EXECUTE

Executes the SQL statement previously prepared on the same handle.

```
CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
```

| Parameter | Purpose |
|-----------|---------|
| `ki_status` | 0 if rows are available, `KE_ENDOFFILE_` if no rows |
| `rowcount` | For UPDATE/DELETE/INSERT: count of affected rows. For SELECT: always 0 |
| `reclen` | Length of the row buffer needed for `KI_FETCH` |

For SELECT: rows are returned by successive `KI_FETCH` calls until `KE_ENDOFFILE_` is returned. If no rows match, the initial `KI_EXECUTE` itself returns `KE_ENDOFFILE_`.

```kcml
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status <> 0 THEN DO
:   PRINT "No results or error: "; ki_status
:   CALL KI_CLOSE handle TO ki_status
:   $END
: END DO
```

---

## KI_FETCH

Returns the next row from a result set established by `KI_EXECUTE`, `KI_TABLES`, or `KI_COLUMNS`.

```
CALL KI_FETCH handle, SYM(buf$) TO ki_status
```

The buffer `buf$` must be large enough to hold the row (use `reclen` from `KI_EXECUTE`).

```kcml
: MAT REDIM rowbuf$reclen
: REPEAT
:   CALL KI_FETCH handle, SYM(rowbuf$) TO ki_status
:   IF ki_status == 0 THEN DO
:     PRINT STR(rowbuf$, 1, 20)
:   END DO
: UNTIL ki_status <> 0
: CALL KI_CLOSE handle TO ki_status
```

---

## Complete SELECT Example

```kcml
: DIM handle, ki_status, colcount, rowcount, reclen
: DIM sql$256, rowbuf$512, color$10, qty

: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END

: sql$ = "SELECT color, quantity FROM SL00test ORDER BY color"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: IF ki_status <> 0 THEN $END

: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status <> 0 THEN DO
:   CALL KI_CLOSE handle TO ki_status
:   $END
: END DO

: REM Bind result columns to variables
: CALL KI_BIND_COL handle, 1, SYM(color$) TO ki_status
: CALL KI_BIND_COL handle, 2, SYM(qty) TO ki_status

: MAT REDIM rowbuf$reclen
: REPEAT
:   CALL KI_FETCH handle, SYM(rowbuf$) TO ki_status
:   IF ki_status == 0 THEN PRINT color$; " = "; qty
: UNTIL ki_status <> 0

: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
: $END
```

---

## Complete INSERT / UPDATE / DELETE Example

For non-SELECT statements, `rowcount` from `KI_EXECUTE` tells you how many rows were affected:

```kcml
: DIM handle, ki_status, colcount, rowcount, reclen
: DIM sql$256

: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END

: sql$ = "INSERT INTO SL00test (color, quantity) VALUES ('blue', 99)"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: IF ki_status <> 0 THEN $END

: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Inserted "; rowcount; " row(s)"

: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status

: REM Now update it
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: sql$ = "UPDATE SL00test SET quantity = 50 WHERE color = 'blue'"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Updated "; rowcount; " row(s)"
: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
: $END
```

---

## KI_TABLES

Generates a result set containing information about all tables available in the database. The handle must be allocated with `KI_ALLOC_HANDLE`.

```
CALL KI_TABLES handle TO ki_status
```

Use `KI_FETCH` to iterate the results:

```kcml
: DIM tblrow$100
: CALL KI_TABLES handle TO ki_status
: REPEAT
:   CALL KI_FETCH handle, SYM(tblrow$) TO ki_status
:   IF ki_status == 0 THEN PRINT tblrow$
: UNTIL ki_status <> 0
: CALL KI_CLOSE handle TO ki_status
```

---

## KI_COLUMNS

Sets up a virtual result set enumerating the columns for a specified table. Use `KI_FETCH` to iterate.

```
CALL KI_COLUMNS handle, tablename$ TO ki_status
```

The result set contains at minimum: column 1 = column name.

```kcml
: DIM colrow$100
: CALL KI_COLUMNS handle, "SL00test" TO ki_status
: REPEAT
:   CALL KI_FETCH handle, SYM(colrow$) TO ki_status
:   IF ki_status == 0 THEN PRINT colrow$
: UNTIL ki_status <> 0
: CALL KI_CLOSE handle TO ki_status
```

---

## Important Rules

1. A `KI_PREPARE` / `KI_EXECUTE` / `KI_FETCH` block **MUST** be followed by a `KI_CLOSE` before the handle can be reused for another SQL statement or table open.
2. Always `KI_CLOSE` before `KI_FREE_HANDLE`.
3. `KI_PREPARE` can be called with a negative handle number to restrict to SELECT-only statements.
