Implementation

Attaching to Oracle

It is not necessary to perform a CREATE DATABASE for Oracle as there is a built in database name of "oracle8". In a future version of KCML multiple databses will be supported. A [KI_CONNECT](tmp/KI_CONNECT.htm) call using the database name "oracle8" must be used to log into the Oracle database and get a connection number for later use. This will load a shared library containing Oracle support routines. A licence file entry in your KCML licence file is needed to permit the use of this library.

When a table is opened it must be done on a handle allocated to that connection so that KCML knows to access Oracle and not the native database. The userid and password fields will be required for Oracle. Generally you will want to have one secret special user with read and write permission for programatic access so that normal users do not have write access to tables under their own accounts.

Functionality supported

- CREATE DATABASE does not apply.
- There is only one Oracle database supported with the special name *oracle8*.
- Table spaces are not supported at this time. All tables go in one tablespace.
- TIME stamp and USER stamp columns are not supported.
- KI_READ_HOLD_NEXT is not supported.
- Word search indices are support but very inefficiently.

Creating tables

Tables are created in the usual way with CREATE TABLE and CREATE INDEX. KCML will convert the native SQL grammar into the Oracle dialect. The table schema is preserved and can be recovered with KI_DESCRIBE_COL.

Opening tables

At the time the table is opened by [KI_OPEN](tmp/KI_OPEN.htm) KCML will import index and dictionary information from the Oracle data dictionary. Path numbers will be given to the indices on the basis of the order they appear in the dictionary that is in index name order. Note that Oracle table names are not in a tree structure though they can be modified by an owner prefix. Each table opened will consume two Oracle cursors. You may need to tune the maximum number of concurrent cursors to be at least twice the number of tables that will be open at any time.

Sequential access

To process a table sequentially you must call [KI_START](tmp/KI_START.htm) or [KI_START_BEG](tmp/KI_START_BEG.htm). This causes KCML to issue a SELECT \* statement for all the columns in that table ordered by the appropriate key path. The columns are bound to internal KCML buffers. For each subsequent [KI_READ_NEXT](tmp/KI_READ_NEXT.htm) a fetch will be issued which copies the data into the bound buffers. KCML will then pack the row buffer passed in the call using standard KCML data types. Therefore the fact that Oracle uses different data types is transparent to the KCML program and no code needs to be changed to move a table from KCML to Oracle.

For rowset operations that traverse one table sequentially joining a second table manually as it were by doing a [KI_START](tmp/KI_START.htm) on the second table there can be problems with performance on big tables. This is particularly acute when the join key has multiple segments as is normally the case. The Oracle optimise will always perform a table scan when presented with an open ended start operation like this and therefore to avoid significant delays in producing the first row you should consider recoding using SQL directly to achieve the join or use [KI_START_ON](tmp/KI_START_ON.htm) which limits the result set to only those rows that match one or more key segments exactly. In general KI_START_ON should always be used in prference to KI_START if the circumstances permit.

Random access and updates

To read a table randomly KCML will issue a SELECT\* and an immediate fetch, possibly with a row lock for a [KI_READ_HOLD](tmp/KI_READ_HOLD.htm). A [KI_REWRITE](tmp/KI_REWRITE.htm) does a SELECT FOR UPDATE. A [KI_UNLOCK](tmp/KI_UNLOCK.htm) will be ignored and you should instead rollback the transaction with [KI_ROLLBACK](tmp/KI_ROLLBACK.htm) if that is appropriate.

The rowid variable *ki_dataptr\$* returned from many library functions that identifies a row must be at least 16 bytes to hold an Oracle ROWID.

Performance

To get good performance it is essential to enclose updates inside a transaction delimited by [KI_BEGIN](tmp/KI_BEGIN.htm) and [KI_COMMIT](tmp/KI_COMMIT.htm) statements. KCML will auto-commit if the database is changed outside an explicit transaction but the overhead for this in Oracle is prohibitive.

To further improve performance updates can be coded directly in Oracle PL/SQL and executed using [KI_PREPARE](tmp/KI_PREPARE.htm), [KI_EXECUTE](tmp/KI_EXECUTE.htm) and [KI_FETCH](tmp/KI_FETCH.htm) statements. This should be done for programs that batch update tables.

In general Oracle will perform significantly slower than the same operation applied to a native KCML database. This will be most apparent on updates. This is due to extra overhead in compiling and optimising dynamic SQL, binding columns unnecessarily, executing SQL in an non optimal way, and transactional costs.
