KI_BIND_COL

This function is used to bind a variable in a program to a column in a rowset open on *handle*. The column to be bound is specified by its column ordinal *col* which is counted from 1. String variables can be bound to any column with KCML handling any necessary conversions but numeric variables can only be bound to numeric columns.

Whenever the current row changes (following a [KI_FETCH](KI_FETCH.htm)) the bound variables associated with the handle through this call are updated auotomatically.

KI_BIND_COL can also be used to bind variables to columns in a KCML rowset on an open handle by name, eg. CALL KI_OPEN handle, "GB_00_users", "R" TO status CALL KI_BIND_COL handle, "userid", SYM(userid\$) TO status

On subsequent KI_READ's, KI_READ_NEXT's etc. (except KI_READ_RAW) the *userid\$* variable will be automatically filled in with the appropriate data from the row buffer. On KI_WRITE's and KI_REWRITE's the contents of the variable will be put into the row buffer.

If the bound column is a pointer to a BLOB then the BLOB itself will be fetched into the bound variable and the bound variable will be re-dimmed if it is not large enough, else it will be space padded. On a KI_WRITE/KI_REWRITE all bound BLOBs will be written/re-written, except if the buffer is blank filled, in which case the BLOBID is set to zeroes in the row buffer.
