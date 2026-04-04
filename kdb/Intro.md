Introduction

KCML has a built in relational database called the KCML Database or **KDB** which is accessed through a database API implemented using the [CALL](mk:@MSITStore:kcmlrefman.chm::/CALL.htm) verb. This same API can also be used to provide uniform access to third party databases such as Oracle.

Features

- Relational, all joins are dynamic
- Supports both SQL access and direct rowset access to data
- Uses native operating system files rather than raw disk partitions
- Optional word search indexing on any column
- BLOB or binary large object support for multimedia. There can be multiple BLOBs per row
- Supports ODBC allowing open access to data from Windows clients.
- Date and user stamping for auditing
- Table sizes are limited only by physical disk space
- Snapshot backup facility
- XML serialization support

Unlike other databases, KDB is implemented largely in the individual KCML processes using a modicum of shared memory for inter process communication. There is no central database instance (though there will be at least one logging daemon) so the startup time after a reboot is very quick. Tables manage their own metadata.
