# KDB Transactions

## Overview

KISAM transactions guarantee that several changes to several KCML tables are **atomic** — either all changes succeed or none do.

- `KI_BEGIN` marks the start of a transaction. From this point, all updates go to an in-memory buffer, not to the tables.
- `KI_COMMIT` writes all buffered changes to the actual tables. If the journal is enabled, the buffer is copied to the journal log first.
- `KI_ROLLBACK` discards the buffer — all changes since `KI_BEGIN` are abandoned.

Transactions and the journal are independent features — transactions can be used without a journal.

---

## Transaction API

| Call | Purpose |
|------|---------|
| `KI_BEGIN` | Start a transaction |
| `KI_COMMIT` | Commit all changes since `KI_BEGIN` |
| `KI_ROLLBACK` | Discard all changes since `KI_BEGIN` |
| `KI_SET_MODE` | Configure transaction and locking mode programmatically |

**Basic transaction pattern:**
```kcml
: CALL KI_BEGIN TO ki_status
: IF ki_status <> 0 THEN $END

: REM ... perform reads, writes, rewrites ...

: REM If all OK, commit
: CALL KI_COMMIT TO ki_status
: IF ki_status <> 0 THEN DO
:   CALL KI_ROLLBACK TO ki_status
:   PRINT "Transaction failed, rolled back"
: END DO
```

---

## Locking Modes

Locking is configured via `krecover -x` or `KI_SET_MODE`. The `-x` flag is a bit field:

| Bit | Value | Meaning |
|-----|-------|---------|
| 0 | `0x01` | KISAM transaction logging ON |
| 1 | `0x02` | Check that tables are locked before writing |
| 2 | `0x04` | Take transaction system lock |
| 3 | `0x08` | Take KISAM logging system lock |
| 4 | `0x10` | ERR if transaction locking is off |
| 5 | `0x20` | Automatic `KI_ROLLBACK` on error |

Recommended locking mode for most use: `-x 0x23` — enables transaction logging with locking checks and automatic rollback on error.

**Two extreme locking strategies:**
- **Application-managed locks:** Application code explicitly locks all tables before `KI_BEGIN` and keeps them locked until after `KI_COMMIT`. Requires application code changes.
- **System lock:** A lock is taken on the KISAM log file at `KI_BEGIN` and released after `KI_COMMIT` or `KI_ROLLBACK`. Only one transaction can execute system-wide at a time — very coarse but requires no application code changes.

**Better middle-ground:** Locks taken by application code are recorded and automatically deferred until `KI_COMMIT` or `KI_ROLLBACK`. This makes migration of existing code easier.

---

## Enabling Transactions Without the Journal

If you want transaction behaviour without the performance overhead of the journal:

```kcml
: DIM mode, oldMode, ki_status
: mode = VAL(HEX(23))
: CALL KI_SET_MODE, 1, mode TO oldMode, ki_status
```

In this mode KISAM performs all transaction operations except writing to the log. If the locking mode is not the coarse log-file lock, `krecover` and its shared memory are not required.

---

## Restrictions

- **No nested transactions.** A second `KI_BEGIN` before a `KI_COMMIT` or `KI_ROLLBACK` gives error `KE_TRANSSYNTAX` (31).
- **Buffer size limit.** If the in-memory transaction buffer overflows, an update will fail with `KE_TRANSSIZE` (32). This typically happens if `KI_BEGIN` is called without a matching `KI_COMMIT`/`KI_ROLLBACK`.
- **Not suitable for whole-table updates.** Bulk operations that affect many rows should not be wrapped in transactions.
- **Table open/close is not permitted within a transaction.** All tables needed must be opened before `KI_BEGIN` and closed after `KI_COMMIT`/`KI_ROLLBACK`. This restriction may be relaxed in future.
- Not appropriate for: `KI_OPEN`, `KI_CLOSE`, `KI_CREATE`, `KI_BU_CREATE`, `KI_GROW`, `KI_EXTEND`

---

## Additional Transaction Features

**Plain file updates within transactions:** `KI_BU_CREATE`, `KI_BU_OPEN`, `KI_BU_READ`, `KI_BU_WRITE` allow plain (non-KDB) files to be updated and included in the journal log / transaction.

**Automatic rollback:** Can be enabled via `krecover -x` or `KI_SET_MODE`. If an error occurs during a transaction, changes are automatically rolled back.

**Manual sync:** `KI_LOG_SYNC` issues a `sync()` and marks the sync in the log. This is an expensive call.

**KLOGKEY environment variable:** For development with multiple KCML journal systems, set `KLOGKEY` to a unique 4-character string (default `"KLOG"`) to keep shared memory and semaphores separate.
