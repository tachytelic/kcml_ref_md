KI_READ_PTR

Reads a row with the specified ROWID directly into the row buffer. This is fast as it does not use any index. If the ROWID is invalid or if the row has been deleted then error code [KE_NOTFOUND](errorcodes.htm) will be returned.
