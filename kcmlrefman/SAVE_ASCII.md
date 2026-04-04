SAVE ASCII <span style="font-size: 16pt ; ">command</span>

------------------------------------------------------------------------

General Form:\
\
     SAVE ASCII filename \[,start_line\] \[,\[ end_line\]\]\
\

------------------------------------------------------------------------

The SAVE ASCII command saves the program in memory to a program file in ASCII form rather than compiled form. It is a command and is not programmable.

The start and end line number parameters operate the same as with the [SAVE](SAVE.htm) statement.

ASCII files are files that can be used by Unix/DOS utilities such as the editors ed or vi. The output resembles that of [LIST D](LIST.htm). The file names are created in the current working directory irrespective of any [SELECT \#0](SELECT_DISK.htm) or [SELECT DISK](SELECT_DISK.htm). However, full Unix/DOS pathnames are allowed. If the file already exists, the original file is overwritten.

Syntax examples:

SAVE ASCII "/tmp/PROG.asc"     \
SAVE ASCII "temp_file.asc"

See also:

[LOAD ASCII](LOAD_ASCII.htm)

 
