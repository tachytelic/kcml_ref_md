# KDB — Introduction and Overview

## What is KDB?

KDB (KCML Database) is the built-in relational database system for KCML. It is also known as **KISAM** (KCML Indexed Sequential Access Method) and is accessed through a database API using the `CALL` verb.

### Key Features

- Relational — all joins are dynamic
- Supports both SQL access and direct rowset access to data
- Uses native operating system files rather than raw disk partitions
- Optional word search indexing on any column
- BLOB (Binary Large Object) support for multimedia — multiple BLOBs per row
- Date and user stamping for auditing
- Table sizes limited only by physical disk space
- Snapshot backup facility
- XML serialisation support
- No central database instance — implemented in individual KCML processes with shared memory for IPC

---

## Database Structure

There can be more than one KDB database on a server. The overall schema is held in the KCML configuration repository (`kconf.xml` in the KCML install directory).

Each database has:
- A **catalog** table — lists the tables in the database
- An optional **permissions** table

Each table is a native OS file containing its own self-descriptive metadata (columns, properties, and all index blocks).

Tables are associated with **tablespaces**, which map to OS directories. Tablespaces are created with `CREATE TABLESPACE` and referenced when creating tables.

---

## Connections

KCML supports simultaneous access to multiple databases through connection handles.

All KCML processes are connected by default to a schema-less default database on **connection zero**. This connection is available without any explicit `KI_CONNECT` call and is what most standalone scripts use.

To access a named KDB database explicitly you must:
1. Allocate a connection handle with `KI_ALLOC_CONNECT`
2. Connect with `KI_CONNECT`
3. Allocate rowset handles with `KI_ALLOC_HANDLE` on that connection

For the common case of reading existing KISAM files from scripts, connection 1 is auto-created as KISAM on script start — no `KI_ALLOC_CONNECT` is needed.

---

## Handles

Handles are opaque numeric tokens used to hold state for an open rowset or connection. When a table or query result set is opened, a handle number is assigned. This handle is passed to all subsequent API calls.

Two kinds of handle:
- **Connection handles** — allocated by `KI_ALLOC_CONNECT`, identify a database connection
- **Rowset handles** — allocated by `KI_ALLOC_HANDLE`, identify an open table or query result set

As of KCML 6.20, handle numbers are non-zero positive large integers (opaque tokens), not the small sequential integers of earlier versions.

---

## Rowsets

A rowset is a collection of rows from a table, accessed via a handle. You can:
- Access rows **sequentially** using an index (via `KI_START` + `KI_READ_NEXT`)
- Access rows **directly** by ROWID (via `KI_READ_PTR`)
- Traverse rows in natural order without an index using `KI_READ_RAW`

SQL query results are also considered rowsets, though random and indexed access is not available on them — only sequential `KI_FETCH`.

When a row is read it populates a **row buffer**. Fields within the row buffer are accessed using `FLD()` operators or by binding variables with `KI_BIND_COL`.

---

## Row Identifiers (ROWID)

Each row has a unique **ROWID** — an opaque token returned by read operations. The ROWID can be used later to reload or update that specific row directly without index traversal.

ROWID size depends on the connection:
- Default connection: up to 4 bytes
- KDB connection (type 7 tables): 6 bytes

Always declare `rowid$` as at least 6 bytes when working with type 7 tables:

```kcml
: DIM rowid$6
```

Use `KI_INFO` to query the actual size from the connection if needed.
