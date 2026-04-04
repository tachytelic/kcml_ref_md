Row identifiers

A row in a table is uniquely identified by a rowid which is an opaque token. Many KDB API calls, such as [KI_READ](tmp/KI_READ.htm), will return a rowid together with the row buffer. This rowid can be later used to update the row or to reload it afresh.

The size of the rowid token depends on the database connection. On the default connection you should be prepared to accept up to 4 bytes while on a KDB is 6 bytes. To be certain you are using the right size you should use [KI_INFO](tmp/KI_INFO.htm) to query the connection and get the size from that.
