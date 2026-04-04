KI_EXECUTE

This function executes an SQL statement previously prepared by [KI_PREPARE](KI_PREPARE.htm) on the same handle. If rows are affected by the statement, such as in an UPDATE, then a count of the rows will be returned. For SELECT this rowcount will always be zero, rows can be returned using calls to [KI_FETCH](KI_FETCH.htm) until KE_ENDOFFILE\_ is returned. However, if no rows will be returned the initial KI_EXECUTE will return KE_ENDOFFILE\_.

Note: A KI_PREPARE/KI_EXECUTE/KI_FETCH block **MUST** be followed by a [KI_CLOSE](KI_CLOSE.htm) before the handle can be re-used to parse another SQL statement or open a table.
