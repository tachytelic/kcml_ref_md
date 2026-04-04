KI_PREPARE

This parses the SQL statement in sql\$ generating an execution plan which is stored against the handle. This can then be executed with [KI_EXECUTE](KI_EXECUTE.htm). The number of columns in any result set is returned in the optional count which will be zero if there is no result set, as in a DELETE or UPDATE.

Like [KI_SQL](KI_SQL.htm) if a negative handle number is passed then functionallity is restricted to SELECT.

Note: A KI_PREPARE/KI_EXECUTE/KI_FETCH block **MUST** be followed by a [KI_CLOSE](KI_CLOSE.htm) before the handle can be re-used to parse another SQL statement or open a table.
