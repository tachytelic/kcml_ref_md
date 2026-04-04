KI_FETCH

This function returns the next row from a result set established on the handle by [KI_EXECUTE](KI_EXECUTE.htm), [KI_TABLES](KI_TABLES.htm) or [KI_COLUMNS](KI_COLUMNS.htm). The data is put into the buffer whose SYM() is passed in *sym*. This buffer must be large enough.

Note: A KI_PREPARE/KI_EXECUTE/KI_FETCH block **MUST** be followed by a [KI_CLOSE](KI_CLOSE.htm) before the handle can be re-used to parse another SQL statement or open a table.
