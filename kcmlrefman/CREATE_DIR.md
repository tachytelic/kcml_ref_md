CREATE DIR

------------------------------------------------------------------------

General Form:\
\
     CREATE DIR dirname\
\

------------------------------------------------------------------------

The statement is used to create native operating system directories. This statement should always be used instead of shelling out to the native operating system equivalent, usually mkdir under Windows and UNIX.

The CREATE DIR statement will error if the directory exists or if the specified path is not valid. Such recoverable errors can be trapped with the [ERROR](ERROR.htm) [DO ... END DO](DO.htm) statement.

Note that the [REMOVE DIR](REMOVE_DIR.htm) statement is used to remove directories and the [MOVE](MOVE.htm) statement can be used to rename directories.

Examples:

CREATE DIR Directory\$\
CREATE DIR "/tmp/NewDir"

See also:

[REMOVE DIR](REMOVE_DIR.htm), [MOVE](MOVE.htm)
