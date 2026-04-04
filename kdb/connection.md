Connections

KCML supports simultaneous access to multiple databases through the use of connection [handles](handles.htm). All KCML processes are connected by default to a simple schema-less default database on connection zero. This connection number can be used without explicitely calling [KI_CONNECT](tmp/KI_CONNECT.htm).

To access a KDB or Oracle database you must make an explicit [KI_CONNECT](tmp/KI_CONNECT.htm) call having first allocated a handle with [KI_ALLOC_CONNECT](tmp/KI_ALLOC_CONNECT.htm). This connection handle is then used to allocate the rowset handles necessary to open a table or execute a query.
