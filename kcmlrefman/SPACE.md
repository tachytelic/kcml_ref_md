SPACE functions (obsolete)

General Form:\
\

SPACE\
SPACEF\
SPACEK\
SPACEP\
SPACEV\
SPACEW\

------------------------------------------------------------------------

These functions were originally used to return the space available to a program. They date from BASIC-2 with its fixed size memory allocations and are obsolete today with the large dynamic memory available to KCML. Where the function is only meaningful in the context of a fixed memory allocation KCML will return an arbitrary fixed value larger than it could be with BASIC-2.

Generally a KCML program can assume an unlimited amount of memory is available but there will be practical limitations set by the amount of paging space or perhaps a memory quota on Unix. These functions should not be used in new programs. To view how much memory is actually being used use the [LIST SPACE](LIST_SPACE.htm) command.

|  |  |
|----|----|
| SPACE | The available memory in the partition in bytes. Always returns 56k i.e. 57344 unless overridden by the [SPACE](EnvVars.htm) environment variable. |
| SPACEF | Available free space. Always returns 1MB i.e. 1048576 |
| SPACEK | The size of the fixed memory partition. As KCML partitions are dynamic this is fixed as either 99 or if the [SPACEK](EnvVars.htm) environment variable exists then its value. |
| SPACEP | The space available for programs. Always returns 57344. |
| SPACEV | The space available for data. Always returns 57344. |
| SPACEW | Available free space. Always returns 1MB i.e. 1048576 |

Syntax examples:

mem = SPACEK\*1024
