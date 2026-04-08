# KDB Data Manipulation Language (DML)

## What is SQL?

SQL (Structured Query Language) is the standard language for querying and modifying relational database data. KCML's implementation is based on the X/Open SQL CAE specification (SQL92) plus Microsoft ODBC 2.0 extensions.

There are two categories of statements:
- **DDL** (Data Definition Language) — `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE`, `CREATE INDEX`, etc.
- **DML** (Data Manipulation Language) — `SELECT`, `INSERT`, `UPDATE`, `DELETE`

The KDB schema is maintained exclusively through SQL DDL. DML is optional — direct rowset API calls (`KI_READ_NEXT`, `KI_WRITE`, etc.) can also be used.

**Column names and IPREFIX:** If a table was created with an `IPREFIX`, column names must be qualified with that prefix in DML (but not in DDL or `KI_BIND_COL`):
```sql
-- Table created with: IPREFIX 'CG_'
SELECT CG_PID, CG_SNAME FROM CGR_TMP
```

---

## SELECT

```sql
SELECT [ALL | DISTINCT] selectlist
FROM tablelist
[WHERE condition]
[GROUP BY expression [, expression] ...]
[HAVING condition]
[UNION [ALL] [subquery]]
[ORDER BY {expression | position} [ASC|DESC] ...]
```

Where `selectlist` is:
```sql
{ * | table.* | expression [AS alias] [, expression [AS alias]] ... }
```

And `tablelist` is:
```sql
table [alias] [, table [alias]] ...
```

| Component | Purpose |
|-----------|---------|
| `table` | A named table in the database |
| `alias` | Alternative name for a table or expression |
| `expression` | Column, literal, built-in function, or arithmetic expression |
| `subquery` | Another SELECT statement |
| `condition` | Logical expression; columns, functions, parameters or literals; connected with `AND` / `OR` |
| `position` | Ordinal position in selectlist for ORDER BY (counted from 1) |

**Examples:**
```sql
SELECT * FROM SL00trans
SELECT color, qty*10, UCASE(description) FROM SL00trans ORDER BY 1
SELECT color, COUNT(*), SUM(quantity) FROM SL00test GROUP BY color
SELECT * FROM SL00trans WHERE color='red' AND quantity > 0
SELECT fname, sname FROM SL00trans WHERE fname LIKE 'Smi%' ORDER BY sname
```

---

## INSERT

```sql
INSERT INTO table [(column [, column] ...)]
{VALUES (expression [, expression] ...) | subquery}
```

Values can be literals, expressions, functions, or `?` parameters. If column names are listed, values must match them. If no column list is given, values must match all columns in order.

A subquery can supply multiple rows in a single INSERT.

**Examples:**
```sql
INSERT INTO XX00test VALUES(1, 'red')
INSERT INTO XX00test (quantity, color) VALUES (5, 'green')
INSERT INTO SL00trans (pid, fname, sname) VALUES (?, ?, ?)
INSERT INTO archive_table SELECT * FROM SL00trans WHERE created < '2020-01-01'
```

**From KCML code:**
```kcml
: DIM sql$256, ki_status, colcount, rowcount, reclen
: DIM color$10, qty

: color$ = "blue"
: qty = 42

: sql$ = "INSERT INTO SL00test (color, quantity) VALUES ('" & color$ & "', " & qty & ")"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Inserted "; rowcount; " row(s)"
: CALL KI_CLOSE handle TO ki_status
```

---

## UPDATE

```sql
UPDATE tablename SET column=expression [, column=expression] ...
[WHERE condition]
```

Updates specified columns in all rows meeting the WHERE condition. If no WHERE clause, all rows are updated.

**Examples:**
```sql
UPDATE SL00test SET quantity = 0 WHERE color = 'red'
UPDATE SL00test SET quantity = quantity + 1
UPDATE SL00trans SET batchdate = '1999-10-31'
```

**From KCML code:**
```kcml
: sql$ = "UPDATE SL00test SET quantity = 0 WHERE color = 'red'"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Updated "; rowcount; " row(s)"
: CALL KI_CLOSE handle TO ki_status
```

---

## DELETE

```sql
DELETE FROM table [WHERE condition]
```

Deletes all rows meeting the condition. Without WHERE, deletes all rows.

**Examples:**
```sql
DELETE FROM SL00test WHERE color = 'red'
DELETE FROM SL00test
```

**From KCML code:**
```kcml
: sql$ = "DELETE FROM SL00test WHERE quantity = 0"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Deleted "; rowcount; " row(s)"
: CALL KI_CLOSE handle TO ki_status
```

---

## Using Parameters (?) in SQL

Parameters replace literal constants, allowing a query plan to be reused with different values without recompiling. Parameters are represented by `?` and are positional (left to right).

Each `?` must be bound to a KCML variable using `KI_BIND_PARAM` before `KI_EXECUTE`.

```sql
SELECT * FROM TESTTAB WHERE cost = ? OR color = ?
INSERT INTO YY01test VALUES (?, ?, ?, ?)
```

---

## Using SQL in a Program — Full Pattern

```kcml
: DIM handle, ki_status, colcount, rowcount, reclen, sql$256

: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END

: REM ---- SELECT ----
: sql$ = "SELECT color, quantity FROM SL00test ORDER BY color"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: IF ki_status <> 0 THEN $END

: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status <> 0 THEN DO
:   CALL KI_CLOSE handle TO ki_status
:   $END
: END DO

: DIM rowbuf$512
: MAT REDIM rowbuf$reclen

: DIM color$10, qty
: CALL KI_BIND_COL handle, 1, SYM(color$) TO ki_status
: CALL KI_BIND_COL handle, 2, SYM(qty) TO ki_status

: REPEAT
:   CALL KI_FETCH handle, SYM(rowbuf$) TO ki_status
:   IF ki_status == 0 THEN PRINT color$; " qty="; qty
: UNTIL ki_status <> 0

: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
: $END
```
