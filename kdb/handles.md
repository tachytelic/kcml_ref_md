Handles

Handles are used to hold information about a [rowset](rowsets.htm) or a [connection](connection.htm). They are represented in KCML programs by non-zero numbers that act as opaque tokens. When a rowset or connection is opened a handle number is associated with it which KCML uses internally to find the state of the resource. When the rowset or connection is no longer required the handle should be closed.

Connection handles are allocated initially by [KI_ALLOC_CONNECT](tmp/KI_ALLOC_CONNECT.htm) whereas rowset handles are allocated with [KI_ALLOC_HANDLE](tmp/KI_ALLOC_HANDLE.htm) once a connection has been established.

Rowset handle are allocated from a pool of [\_KDB_MAX_HANDLES](mk:@MSITStore:kcmlrefman.chm::/tmp/KdbConstantsHelp.htm) handles that can be open simultaneously. A programmer can either nominate the handle number to be used or allow KCML to choose one in which case the handle can be a temporary one that will be automatically closed on the next LOAD or CLEAR.

Handles can be converted to small integers in the range 1 to \_KDB_MAX_HANDLES using [KI_INFO](tmp/KI_INFO.htm).
