pltlist (UNIX/DOS)

General Form:\
\

pltlist \[-cdnp\] \[-f mask \] platter\

The pltlist utility lists on its standard output the catalogue of a platter image in a similar form to the LIST DCT command.

The parameters used with pltlist are as follows:

|  |  |
|----|----|
| -c | If '-c' specified then the Index size, End catalogue Area, and current End for the platter are displayed at the beginning of the list. |
| -d | If '-d' is specified, then only data files are listed. |
| -n | Causes only file names to be listed, one to a line. |
| -p | If '-p' is specified, then only program files are listed. |
| -f mask | The '-f' mask option limits output to those files matching the specified pattern. The pattern matching is limited, and does not allow true grep-like patterns. |

Example:

pltlist -dc -f 'SORT\*' D10.plt

This will list the names, sizes, and start positions of all the files starting 'SORT' in the platter image 'D10.plt'.
