# KDB Data Definition Language (DDL)

DDL statements define the structure of the database and its components. They are executed via `KI_PREPARE` / `KI_EXECUTE` like any other SQL.

---

## CREATE DATABASE

```sql
CREATE DATABASE database_name
TYPE KDB|VIRTUAL
DEFAULT TABLESPACE tablespace_name
[DESCRIPTION string]
[WITH PERMISSIONS]
```

Creates a new database entry in `kconf.xml`. If type is `KDB`, a catalog table named `DATABASE_NAME_CAT.kdb` is created in the `system` tablespace (which must already exist). No catalog is created for a `VIRTUAL` database.

The `WITH PERMISSIONS` clause creates a permissions file named `DATABASE_NAME_PERMS.kdb` in the `system` tablespace.

The KCML installer creates a default virtual database called `system` with a `system` tablespace as a subdirectory of the KCML install directory.

**Examples:**
```sql
CREATE DATABASE test TYPE KDB DEFAULT TABLESPACE temp DESCRIPTION 'Test database'
CREATE DATABASE boot TYPE VIRTUAL DEFAULT TABLESPACE SYSTEM DESCRIPTION 'Bootstrap connection'
```

---

## DROP DATABASE

```sql
DROP DATABASE database_name
```

Drops a database by removing it from `kconf.xml`, its catalog, and permissions file (if any). A non-virtual database can only be dropped if all its tables have already been dropped.

---

## CREATE TABLESPACE

```sql
CREATE [GLOBAL | LOCAL] TABLESPACE tablespacename location TYPE {TREE | FLAT | TEMPORARY}
```

Creates a tablespace — a named mapping to an OS directory. If the directory doesn't exist it is created. The location may contain environment variables.

| Type | Meaning |
|------|---------|
| `FLAT` | All tables in one directory |
| `TREE` | Hierarchical — table name is broken into subdirectories (e.g. `NL_01_example` → `NL/01/NL_01_example.kdb`) |
| `TEMPORARY` | For temporary tables |

`GLOBAL` tablespaces are usable by all databases; `LOCAL` only by the database the statement was issued against. Default is `GLOBAL`.

**Examples:**
```sql
CREATE TABLESPACE disk2 '/disk2' TYPE FLAT
CREATE GLOBAL TABLESPACE tmp '/tmp' TYPE TEMPORARY
CREATE LOCAL TABLESPACE Data1 'C:\Comm8\Data1' TYPE TREE
CREATE LOCAL TABLESPACE MyTables '$HOME/tables' TYPE FLAT
```

---

## CREATE TABLE

```sql
CREATE TABLE tablename (coldesc [, coldesc] ...) [tableparm [, tableparm] ...]
```

### Column description (`coldesc`)

```sql
colname datatype [ALIAS colname] [STARTBYTE integer]
    [DISPLAY 'image'] [SIGNED|UNSIGNED]
    [OCCURS integer] [RANGE(from,to)] [TOTALLED]
    [PRIORITY(u,d,p)] [NAME 'string'] [SPECIAL 'string']
    [PREVAL integer] [POSTVAL integer]
    [VALIDATE C|R|U|V|T 'string']
    [SEQUENCE integer] [OVERLAPS colname [BY integer]]
    [[NOT] NULL] [DEFAULT number|'string'|NULL|USER]
```

### Table parameters (`tableparm`)

| Parameter | Meaning |
|-----------|---------|
| `NAME 'string'` | Descriptive name for the table |
| `ROWS integer` | Maximum rows in first extent (default 100) |
| `RECLEN integer` | Row length in bytes (deduced from columns if omitted) |
| `EXTENT integer` | Auto-extension percentage (0–155) |
| `TYPE integer` | File format type: 3, 4, 5, 6, or 7 (default 7) |
| `PACKING integer` | Index block packing % (50–100; default 50, or 75 for type 7) |
| `BLOCKLEN integer` | Index block size in 256-byte units (2, 4, or 8; for type 7: page size in KB, 8–64) |
| `PATH 'string'` | Explicit file path for the table |
| `TABLESPACE 'string'` | Create table in the named tablespace |
| `SERIAL mode [colname]` | Serial number column: `A` = automatic, `M` = manual, `N` = none; column must be `INTEGER(4)` |
| `DATESTAMP colname` | (Type 7 only) Column for automatic date-stamping; must be `INTEGER(4)` |
| `USERSTAMP colname` | (Type 7 only) Column for automatic user-stamping; must be `VARCHAR` < 255 bytes |
| `IPREFIX 'string'` | (Type 7 only) Prefix applied by `KI_FLD` when its prefix parameter is blank |
| `CASE 'string'` | Column name style for ODBC access: `SHORT`, `LONG`, `SHORT_UPPER`, etc. |
| `UPDATE 'string'` | ODBC update mode: `Y` or `N` (default `Y`) |

**Examples:**
```sql
CREATE TABLE SL00test (color VARCHAR(10), quantity NUMERIC(8))
CREATE TABLE SL00test (color VARCHAR(10), quantity NUMERIC(8)) TABLESPACE mydata
CREATE TABLE SL00trans (pid INTEGER(4), fname VARCHAR(20), sname VARCHAR(20),
    created DATE) TYPE 7, IPREFIX 'SL_', TABLESPACE data1
```

---

## ALTER TABLE

Only supported for **type 7** tables.

```sql
ALTER TABLE tablename col_action (col_description [, col_description ...])
```

| Action | Effect |
|--------|--------|
| `ADD` | Add columns at end of row (initialised to zeroes / spaces for VARCHAR) |
| `DROP` | Remove columns (cannot drop serialized, BLOB_ID, or indexed columns) |
| `MODIFY` | Change column attributes (type cannot change; size can only increase; indexed columns cannot be modified) |
| `RENAME` | Rename a column (`old_name new_name` — cannot rename serialized columns) |

**Examples:**
```sql
ALTER TABLE XX00test ADD (newcol VARCHAR(10))
ALTER TABLE XX00test MODIFY (newcol VARCHAR(20) NAME 'New column')
ALTER TABLE XX00test RENAME (newcol oldcol)
ALTER TABLE XX00test DROP (oldcol)
```

---

## DROP TABLE

```sql
DROP TABLE tablename [FROM CATALOGUE]
```

Deletes the named table and all its indices. With `FROM CATALOGUE`, only removes the catalog entry without deleting the physical file.

**Example:**
```sql
DROP TABLE SL00trans
```

---

## CREATE INDEX

All KDB indices **must be unique**.

```sql
CREATE UNIQUE INDEX indexname ON tablename (colname [ASC|DESC] [, colname ...])
```

The index name should be the table name with a suffix of `_Axx` where `xx` is the path number (01–18). Up to 8 columns per index.

`DESC` is defined but not supported in KCML 5.

**Example:**
```sql
CREATE UNIQUE INDEX SL00trans_A1 ON SL00trans (fname, sname)
CREATE UNIQUE INDEX SL00trans_A2 ON SL00trans (pid)
```

---

## DROP INDEX

```sql
DROP INDEX indexname
```

Deletes the named index from its table.

**Example:**
```sql
DROP INDEX SL00test_A1
```

---

## CREATE WORD INDEX

Word search indices allow full-text searching on VARCHAR, INTEGER, or NUMERIC columns.

```sql
CREATE WORD INDEX wsindexname ON tablename
(colname [, colname ...]) ORDER BY indexname
[MAX integer] [MIN integer] [NONALPHA 'string'] [NOISE 'filename']
```

| Parameter | Meaning |
|-----------|---------|
| `MAX` | Maximum word length to index (default 8, max 16) |
| `MIN` | Minimum word length to index (default 3, min 2) |
| `NONALPHA` | Non-alphabetic characters to include in words (e.g. digits for numeric fields) |
| `NOISE` | Path to XML noise words file (words to force include/exclude) |

The index name should be the table name with suffix `_Wx` where `x` is 1–4. The `ORDER BY` clause names an existing ordinary index that defines the return order.

**Example:**
```sql
CREATE WORD INDEX SL00trans_W1 ON SL00trans (fname, sname)
    ORDER BY SL00trans_A1 MAX 15, MIN 5
```

---

## DROP WORD INDEX

```sql
DROP WORD INDEX indexname
```

**Example:**
```sql
DROP WORD INDEX SL00test_W1
```

---

## Executing DDL from KCML Code

DDL statements are executed the same way as DML — via `KI_PREPARE` / `KI_EXECUTE`:

```kcml
: DIM handle, ki_status, colcount, rowcount, reclen, sql$256

: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: IF ki_status <> 0 THEN $END

: sql$ = "CREATE TABLE SL00test (color VARCHAR(10), quantity NUMERIC(8)) TYPE 7, TABLESPACE data1"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: IF ki_status <> 0 THEN PRINT "Prepare failed: "; ki_status
: IF ki_status <> 0 THEN $END

: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Table created"
: CALL KI_CLOSE handle TO ki_status

: REM Create the index
: sql$ = "CREATE UNIQUE INDEX SL00test_A1 ON SL00test (color)"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: IF ki_status == 0 THEN PRINT "Index created"
: CALL KI_CLOSE handle TO ki_status

: CALL KI_FREE_HANDLE handle TO ki_status
: $END
```
