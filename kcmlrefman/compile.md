compile

General Form:\
\
<img src="bitmaps/compile.gif" data-border="0" width="461" height="43" />

This command (which on Unix is actually a link to the [kcml](kcml.htm) program) creates compiled and [LOAD](LOAD.htm)able KCML programs from their ASCII source equivalents. On operating systems which do not support links it can be invoked with the '-c' switch to [kcml](kcml.htm). It can compile programs into a platter or leave then as separate files in a directory of the native file system. It can be used to convert the '.SRC' files produced by the NPL de-compiler into compiled KCML programs.

Each source specifier may be a file, a wild card specifier such as '\*.SRC' or directory name. If a directory is specified as the source, the destination must then be a directory or a platter if the '-w' is specified. Only files with names of the form '*base*.asc' or '*base*.SRC' will be compiled; the corresponding output file will have a name '*base*'.

Each individually named source file will be compiled into the target directory or onto a platter image file if '-w' was used. Each source directory will be recursively examined for '.asc' or '.SRC' files; the directory hierarchy will be reproduced in the output. For example, 'compile SOURCE D99' would compile 'SOURCE/GO/MENU.SRC' into 'D99/GO/MENU'. All output directories will be created as needed.

The parameters available to the *compile* utility are as follows:

| Switch | Purpose |
|----|----|
| -b *maxexp* | If this option is specified, all expressions \> '1E*maxexp*' will be consistently changed to '1E*maxexp*' in the compiled program. For example if '-b 30' was specified the statement 'Q9=1E99' would be changed to 'Q9=1E30'. This is only required on certain older processors that cannot hold large exponential floating point numbers greater than 1E34 (e.g. VAX, Pyramid and CCI 6/32). |
| -d | If the '-d' option is used, source files will be removed if the program compiles correctly. |
| -e *sectors* | The '-e' option should only be used if '-w' has already been specified. The '-e' option instructs *compile* to add the specified number of sectors to the file before it is placed onto the specified platter. A Wang BASIC-2 header and trailer is also added to the file before it is added to the platter. |
| -i *index* | The '-i' option should only be used if the '-w' option has already been specified. The '-i' option instructs *compile* to create a platter with the specified number of index sectors, before any files are compiled onto it. By default the platter will be created with 43 index sectors. |
| -r | Existing files will not be overwritten unless the '-r' option is used. No attempt will be made to overwrite existing directories to create files or vice versa. |
| -s | If the '-s' option is specified, any [REM](REM.htm) text will be removed from the compiled program, this performs the same function as a '[SAVE](SAVE.htm) \<R\>"PROG1"' from within KCML. |
| -v | If the '-v' option is used, the names of files are displayed as they are compiled. |
| -w *platter* | If the '-w' option is specified, *compile* will create a platter with the specified name and compile the programs onto the platter. This can be used in conjunction with the '-e' and '-i' options. |
| ! | Specifying the '!' parameter will prompt for a password with which it will scramble all of the specified programs (See [SELECT PASSWORD](SELECT_PASSWORD.htm)). |

Examples:

compile -vs ACCOUNTS/SOURCE ACCOUNTS/PROGS

This will compile all ASCII source files in and below the directory 'ACCOUNTS/SOURCE' into separate programs in the directory 'ACCOUNTS/PROGS', keeping the same subdirectory structure. All REMrem text will be removed. No existing files in 'ACCOUNTS/PROGS' will be overwritten. Only errors will be reported.

compile -v -w D11.bs2 -i 253 \*.SRC \>/tmp/log 2\>&1

In this example all the files ending in '.SRC' in the current directory will be compiled and added to the platter image file 'D11.bs2'. If that file did not exist it will be created with an index size of 253 sectors. The list of files compiled and any error messages produced in the compilation are routed to the file '/tmp/log'. Because '-r' was not specified existing files already in the platter image will not be overwritten but a message will be written to the log file.

Compatibility notes:

The ability to compile programs onto platters was introduced in release 3.00.00.

See also:

[ucompile](ucompile.htm), [kcml](kcml.htm), [\$COMPILE]($COMPILE.htm)
