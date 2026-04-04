## Error statement

The [ERROR](mk:@MSITStore:kcmlrefman.chm::/error.htm) statement modifies the behavior of the previous statement (which must exist) and is not a valid statement in its own right. **KCML** will indent the ERROR statement itself and subsequent statements until the start of the next line to make it plain that these statements form a group which will be skipped unless there is an error.

The error statement, if the error is not taken, performs a jump to the next program line. This can cause problems if line numbers are to be removed and it is recommended that the statement is replaced by the [ERROR DO](mk:@MSITStore:kcmlrefman.chm::/ERROR.htm) statement whenever possible.
