LIMITS

------------------------------------------------------------------------

General Form:\
\
.      LIMITS \#stream, \[filename, \] start, end, current \[ ,status\]\
\
Where:\
\
     start, end, current, status      = numeric receiver variables\
\

------------------------------------------------------------------------

The LIMITS statement is used to obtain information about cataloged files within a platter image or native files.

If a filename is specified then LIMITS will return the start sector, end sector, and the number of sectors used for the specified file. The used return variable is optional. If the used parameter is not specifed performance will be improved as KCML then avoids a disk access to read the system end block where the used count is held. If a fourth return variable is specified then LIMITS will return the current status of the file. If the specified file does not exist and the status return variable has been omitted then an error will occur.

If no filename is specified, then a stream number must be specified instead of a device address, the information will then be returned for the file currently open on that stream. No status information can be obtained when specifying a stream number. If the stream points to a native operating system file previously opened with the [OPEN \#](OPENhash.htm) statement then the start parameter will always be zero, the size of the file in bytes is returned as the end parameter and the current position is also expressed in bytes. If the file is OPENed in append mode (See [OPEN#](OPENhash.htm) for more information) then LIMITS will not return reliable information. In this case [SEEK \#n, END](SEEKhash.htm) should be used.

The status codes are:

| Value | Meaning                                |
|-------|----------------------------------------|
| -2    | Scratched data file                    |
| -1    | Scratched program                      |
| 0     | File not found                         |
| 1     | Program file                           |
| 2     | Data file                              |
| 3     | Directory                              |
| 4     | Unix special file or device. E.g. FIFO |

When operating on a native file, the statement will always return zero for the start.

Syntax examples:

LIMITS \#1,start1, end1, used1\
LIMITS "FRED", start_1, end_1\
LIMITS \<fnm\$\>, st, ed
