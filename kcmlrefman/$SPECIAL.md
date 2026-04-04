\$SPECIAL

------------------------------------------------------------------------

General Forms:\
\
1.      \$SPECIAL = alpha_expression\
\
2.      alpha_receiver = \$SPECIAL\
\

------------------------------------------------------------------------

The \$SPECIAL statement allows special versions of standard programs to be loaded from a standard directory. The special programs are saved in the directory with either a special suffix or in a special subdirectory. If \$SPECIAL ends in a slash character '/' (or '\\ for Windows), then \$SPECIAL will be considered as a *subdirectory*. Otherwise it will be considered as a filename *dot extension* To activate those programs in all subsequent [LOADs](LOAD.htm) a \$SPECIAL statement is executed. Thereafter [LOAD "PROG"](LOAD.htm) will first check to see if a file with a modified program name exists.\
For example:

| \$SPECIAL | Modified name |
|-----------|---------------|
| "ext"     | "PROG.ext"    |
| "subdir/" | "subdir/PROG" |

\
If the modified name does exist then that program will be loaded. Otherwise "PROG" itself will be loaded. \$SPECIAL can be set to spaces to turn off the special [LOADs](LOAD.htm). \$SPECIAL does not affect the [SAVE](SAVE.htm) command.

\$SPECIAL can also be used as a function to return the current value of \$SPECIAL.

Syntax examples:

\$SPECIAL = STR(company\$(1),3)\
\$SPECIAL = "test"\
\$SPECIAL = "mydir/"\
source\$ = \$SPECIAL
