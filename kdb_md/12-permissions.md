# KDB Permissions

## Overview

KDB supports optional permissions-based security at the database level. When a database is created with the `WITH PERMISSIONS` clause, a permissions table is created that controls which users can access which tables at what priority level.

Permissions are **not** checked for tables in FLAT tablespaces. If the connection is made by the `dbauser` (the user who executed `CREATE DATABASE`), priority `9` is returned for all tables regardless of the permissions table.

```sql
CREATE DATABASE mydb TYPE KDB DEFAULT TABLESPACE data WITH PERMISSIONS
```

---

## KDB 6 Permissions Table Structure

The permissions table (`DATABASE_NAME_PERMS.kdb`) has this structure:

```sql
CREATE TABLE perms (
    USERID    VARCHAR(16)  NAME 'User Id',
    MODULE    VARCHAR(2)   NAME 'Module',
    COMPANY   VARCHAR(2)   NAME 'Company',
    BRANCH    VARCHAR(4)   NAME 'Branch',
    TABLENAME VARCHAR(35)  NAME 'Tablename',
    PRIORITY  VARCHAR(1)   NAME 'Priority',
    CANUPDATE VARCHAR(1)   NAME 'Can Update',
    XFLAG     VARCHAR(1)   NAME 'Xflag'
) NAME 'Permissions'

CREATE UNIQUE INDEX perms_A1 ON perms
    (USERID, MODULE, COMPANY, BRANCH, TABLENAME, PRIORITY, CANUPDATE, XFLAG)
```

The table is **not** listed in the catalog. It is the application's responsibility to populate it.

---

## KCML 5 Permissions Table Structure

Older KCML 5 databases used a simpler permissions structure with an overlapping KEY field:

```sql
CREATE TABLE perms (
    "KEY"      VARCHAR(12)  NAME 'Key',
    "USER"     VARCHAR(8)   OVERLAPS "KEY" OFFSET 1  NAME 'User ID',
    "MODULE"   VARCHAR(2)   OVERLAPS "KEY" OFFSET 9  NAME 'Module',
    "COMPANY"  VARCHAR(2)   OVERLAPS "KEY" OFFSET 11 NAME 'Company',
    "PRIORITY" VARCHAR(1)   NAME 'Priority'  VALIDATE C '123456789'
) NAME 'Permissions'

CREATE UNIQUE INDEX perms_A1 ON perms ("KEY")
```

Note the quoted column names to avoid conflicts with SQL reserved words.

In early KCML 5 the USER column was `VARCHAR(5)`. The `LongUserNames` keyword in the sources file (or `Rev8Perms` in KCML 5) controlled whether 5-character or 8-character user IDs were in use.

---

## KCML 5 Database Schema (sources.txt)

In KCML 5, the database schema was defined in a `sources.txt` file (similar to a Windows INI file). Comments start with `#`. Blank lines and extra whitespace are ignored. Not case sensitive.

**Supported keywords:**

| Keyword | Meaning |
|---------|---------|
| `Description` | Description of the database |
| `Catalog` | Path to the catalog table (required to define a database) |
| `Optimization` | SQL optimisation level 0–9 (default 9) |
| `Permissions` | Path to the permissions table |
| `LongUserNames` | `true`/`false` — 8-character or 5-character user IDs |
| `ShortName` | `true`/`false` — how column names are returned from data dictionary |
| `TraceFile` | Log file path for debugging |
| `TraceLevel` | Trace verbosity 0–9 (0 = off) |
| `Update` | `true`/`false` — whether INSERT/UPDATE/CREATE/DROP are allowed |
| `Workspace` | Directory for temporary sort tables |

**Example sources.txt:**
```
# This is a comment

[General]
Workspace = /user8/tmp

[Autoline]
Catalog = /user1/home/catfile
Permissions = /user1/home/perms
```

In KCML 6, this configuration moved to `kconf.xml` and is managed through SQL DDL (`CREATE DATABASE`, `CREATE TABLESPACE`).
