Transactions

KISAM transactions guarantee that several changes to several KCML tables are atomic. The KISAM [journal](journal.htm) guarantees the logging of whole KISAM transactions. It is intended to preserve the consistency of KISAM databases. It has an advantage over just the KISAM journal that in addition to guaranteed internal consistency of KCML tables transactions between KCML tables are also guaranteed. The start of a KISAM transaction is marked by a call to [KI_BEGIN](tmp/KI_BEGIN.htm). From this point onwards all transactions are made to an in memory buffer. No updates are made to the KCML tables. The end of the transaction is marked by a call to either [KI_COMMIT](tmp/KI_COMMIT.htm) or [KI_ROLLBACK](tmp/KI_ROLLBACK.htm). [KI_ROLLBACK](tmp/KI_ROLLBACK.htm) throws away the buffer. [KI_COMMIT](tmp/KI_COMMIT.htm) makes all the changes to all the KCML tables. If the KISAM journal exists and is enabled [KI_COMMIT](tmp/KI_COMMIT.htm) copies the buffer to the journal log before doing the updates to the KCML tables.

Locking

Various modes of locking can be set with *krecover -x* or [KI_SET_MODE](tmp/KI_SET_MODE.htm). There are two extremes of locking. One is that locking is expected to be done by the application code. This means that locks should be taken on all the KCML tables before the transaction, and not removed until after a [KI_COMMIT](tmp/KI_COMMIT.htm). This may require application code changes. The other extreme of locking takes a lock on the KISAM log file at a [KI_BEGIN](tmp/KI_BEGIN.htm) and releases it after a [KI_COMMIT](tmp/KI_COMMIT.htm) or [KI_ROLLBACK](tmp/KI_ROLLBACK.htm). This form of locking means that there can only be one transaction executed on the system at a time. It is very coarse but is done by the KISAM transaction logging code and requires no application code changes.

A better solution than these two extremes is available. This should make migration of existing application code to the use of transactions easier. In this mode, locks taken by the application code are implemented and recorded. When the application releases these locks KISAM does not release the locks but records the fact. When a [KI_COMMIT](tmp/KI_COMMIT.htm) or [KI_ROLLBACK](tmp/KI_ROLLBACK.htm) has been executed the locks taken and released in the transaction are released.

Restrictions

There is a compiled in maximum size to the transaction buffer. If a [KI_BEGIN](tmp/KI_BEGIN.htm) is executed by accident without a matching [KI_COMMIT](tmp/KI_COMMIT.htm) or [KI_ROLLBACK](tmp/KI_ROLLBACK.htm), or too many updates are attempted then an update will fail with a KE_TRANSSIZE (32) error. KISAM transaction logging is not of much use for whole table type updates. These could be re-executed in the event of a system crash anyway. To enable transaction logging [KI_BEGIN](tmp/KI_BEGIN.htm), [KI_COMMIT](tmp/KI_COMMIT.htm) and [KI_ROLLBACK](tmp/KI_ROLLBACK.htm) calls should be added to the application programs. In addition [krecover](krecover.htm) should be started with the appropriate flags to select transaction logging and its locking mode.

It is not possible to nest transactions. Issuing a second [KI_BEGIN](tmp/KI_BEGIN.htm) before a [KI_COMMIT](tmp/KI_COMMIT.htm) or [KI_ROLLBACK](tmp/KI_ROLLBACK.htm) gives a KE_TRANSSYNTAX (31) error.

[KI_OPEN](tmp/KI_OPEN.htm), [KI_CLOSE](tmp/KI_CLOSE.htm), [KI_CREATE](tmp/KI_CREATE.htm), [KI_BU_CREATE](tmp/KI_BU_CREATE.htm), [KI_GROW](tmp/KI_GROW.htm) and [KI_EXTEND](tmp/KI_EXTEND.htm) are currently not permitted within transactions. All the tables required for a transaction must be opened sometime before the [KI_BEGIN](tmp/KI_BEGIN.htm) and closed sometime after the [KI_COMMIT](tmp/KI_COMMIT.htm) or [KI_ROLLBACK](tmp/KI_ROLLBACK.htm). The reason for this is that the journal mechanism depends on the file descriptors remaining unchanged. This restriction may be relaxed in the future.

Additional Functionality

In addition to KCML tables, it may be necessary to update plain files and have these changes included in the journal log and/or in transactions. For this purpose [KI_BU_CREATE](tmp/KI_BU_CREATE.htm), [KI_BU_OPEN](tmp/KI_BU_OPEN.htm), [KI_BU_READ](tmp/KI_BU_READ.htm) and [KI_BU_WRITE](tmp/KI_BU_WRITE.htm) have been added.

A feature of some DBMS is automatic rollback. If there is an error in the course of a transaction then the changes made in the transaction are automatically rolled back. This can be enabled in KISAM through *krecover -x* or [KI_SET_MODE](tmp/KI_SET_MODE.htm)

There is also a [KI_LOG_SYNC](tmp/KI_LOG_SYNC.htm) call which can be used to issue a sync() and mark the sync in the log in the normal way. This is an expensive call.

For development it may be desirable to have several different KCML database journal systems. The [KLOGKEY](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#KLOGKEY) environment parameter can be used to keep these systems separate. It must be exactly 4 characters long. It's value is used as the key for the shared memory and semaphore that control the journal system. It's default value is "KLOG", 0x424C4F47. For more information see [KCML environment variables](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm)

Security

The device driver entry points */dev/kisamlogread* and */dev/kisamlogwrite* give access to the raw disk partition that is used for the KISAM journal. This partition contains a copy of all the data written to KCML tables, while the journal has been enabled. In order to maintain security of the information written to KCML tables these devices should only be readable by privileged users. All users must be able to write to the writing device.

Transaction Logging Without the Journal

The KISAM journal has an obvious performance overhead. Every write requires a physical write to the journal log. Some situations require the functionality of transactions, but do not want the performance overhead of the KISAM journal. This is catered for by having KISAM perform all the operations explained above, except actually writing to the log. In addition, if the chosen locking mode is not the coarse KISAM log lock, then [krecover](krecover.htm) and its shared memory segment are not required. KISAM transaction logging without the KISAM journal can be enabled by with [KI_SET_MODE](tmp/KI_SET_MODE.htm).

Setting Up Transaction Locking

If the KISAM journal is being used then transaction logging can be enabled with [krecover](krecover.htm). A useful locking mode could be enabled by adding a *-x 0x23* argument. This enables transaction logging with locking checks and automatic rollback on error. The *-x* argument is a bit field where,

|      |                                                       |
|------|-------------------------------------------------------|
| 0x01 | KISAM transaction logging ON                          |
| 0x02 | check that tables are locked                          |
| 0x04 | take transaction system lock                          |
| 0x08 | take KISAM logging system lock                        |
| 0x10 | ERR if transaction locking is off                     |
| 0x20 | automatic [KI_ROLLBACK](tmp/KI_ROLLBACK.htm) on error |

If the KISAM journal is not being used then transaction logging can be programmatically enabled with the following code


    mode = VAL(HEX(23))
    CALL KI_SET_MODE, 1, mode, TO oldMode, ki_status
