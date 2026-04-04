COPY

------------------------------------------------------------------------

General Form:\
\
     COPY filename TO filename\
\

------------------------------------------------------------------------

The COPY statement is used to copy native files from one location to another. This statement should be used instead of shelling out to a native operating system copy command.

The COPY statement will generate an error if the directory exists or if the specified path is not valid. Such recoverable errors can be trapped with the ERROR DO ... END DO statement.

Note that this statement works with respect to the current working directory, not the directory specified by a select disk.

Syntax examples:

COPY FileName\$ TO "PROGS"\
COPY "/tmp/PROG1" TO "/user1/backup"

See also:

[MOVE](MOVE.htm), [REMOVE](REMOVE.htm)
