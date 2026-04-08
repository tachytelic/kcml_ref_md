# KDB Reference Documentation

KDB (KCML Database), also known as KISAM, is the built-in relational database system for KCML. This reference covers the API, SQL dialect, utilities, and operational concepts.

Oracle support is intentionally excluded from this documentation.

## Files

| File | Contents |
|------|---------|
| [01-introduction.md](01-introduction.md) | Overview, database structure, connections, handles, rowsets, ROWIDs |
| [02-datatypes.md](02-datatypes.md) | SQL type mapping, legacy file types, BLOB support |
| [03-handles-connections.md](03-handles-connections.md) | KI_ALLOC_HANDLE, KI_FREE_HANDLE, KI_CLEAR_HANDLES, KI_INITIALISE |
| [04-open-close-create.md](04-open-close-create.md) | KI_OPEN, KI_CLOSE, KI_CREATE, KI_SIZE_FILE |
| [05-rowset-access.md](05-rowset-access.md) | KI_START, KI_START_BEG, KI_READ_NEXT, KI_READ_PTR, KI_BIND_COL, KI_FLD |
| [06-sql-api.md](06-sql-api.md) | KI_PREPARE, KI_EXECUTE, KI_FETCH, KI_TABLES, KI_COLUMNS |
| [07-ddl.md](07-ddl.md) | CREATE/DROP DATABASE, TABLE, INDEX, TABLESPACE, WORD INDEX; ALTER TABLE |
| [08-dml.md](08-dml.md) | SELECT, INSERT, UPDATE, DELETE, SQL in programs |
| [09-sql-functions.md](09-sql-functions.md) | Set, string, numeric, date, system functions |
| [10-transactions.md](10-transactions.md) | KI_BEGIN, KI_COMMIT, KI_ROLLBACK, locking modes |
| [11-journaling.md](11-journaling.md) | Journal setup, krecover daemon, crash recovery examples |
| [12-permissions.md](12-permissions.md) | Permissions table structure, KCML 5 sources.txt |
| [13-utilities.md](13-utilities.md) | kconvdd, kconvert, krebuild, krecover, kverify |
| [14-reserved-words.md](14-reserved-words.md) | Complete SQL reserved word list |
| [demo-db-operations.kcml](demo-db-operations.kcml) | **Working KCML demo** — all common DB operations in one script |

## Quick Reference — Common Patterns

### Read all rows from a KISAM file (no SQL)
```kcml
: DIM handle, ki_status, ki_sym, ki_dataptr$6, ki_key$64, rec$512, count
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: CALL KI_OPEN handle, "/full/path/to/FILE", "R" TO ki_status
: CALL KI_START_BEG handle, 1 TO ki_status
: ki_sym = SYM(rec$)
: count = 0
: REPEAT
:   CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
:   IF ki_status == 0 THEN count++
: UNTIL ki_status <> 0
: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
```

### Execute SQL and fetch results
```kcml
: DIM handle, ki_status, colcount, rowcount, reclen, sql$256, rowbuf$512
: CALL KI_ALLOC_HANDLE 0, 1 TO handle, ki_status
: sql$ = "SELECT color, quantity FROM SL00test ORDER BY color"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: MAT REDIM rowbuf$reclen
: REPEAT
:   CALL KI_FETCH handle, SYM(rowbuf$) TO ki_status
:   REM process rowbuf$ here
: UNTIL ki_status <> 0
: CALL KI_CLOSE handle TO ki_status
: CALL KI_FREE_HANDLE handle TO ki_status
```

### Execute non-SELECT SQL (INSERT/UPDATE/DELETE)
```kcml
: sql$ = "UPDATE SL00test SET quantity = 0 WHERE color = 'red'"
: CALL KI_PREPARE handle, sql$ TO ki_status, colcount
: CALL KI_EXECUTE handle TO ki_status, rowcount, reclen
: CALL KI_CLOSE handle TO ki_status
```

## Key Rules

- Always `KI_CLOSE` before `KI_FREE_HANDLE`
- Always `KI_CLOSE` after a `KI_PREPARE`/`KI_EXECUTE`/`KI_FETCH` block before reusing the handle
- Use `KI_OPEN handle, file$, mode$` (3 params) — the 4-param form causes S24 panic in KCML 6.x
- Pre-assign `ki_sym = SYM(rec$)` before a read loop — do not pass `SYM()` inline
- `ki_dataptr$` must be exactly 6 bytes
- Status 0 = success, 2 = EOF (normal), non-zero = error
