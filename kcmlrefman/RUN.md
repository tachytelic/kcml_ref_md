RUN

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/run.gif" data-align="BOTTOM" data-border="0" />\
\

------------------------------------------------------------------------

The RUN command is used to initiate execution of the program currently in memory. Note that programs can also be executed by pressing the F11 key within the Workbench.

Before program execution begins the program is **resolved**. The resolution process performs the following functions:

- The program is sequentially scanned for syntax errors. All line numbers and variable references are verified. All [WHILE ... WEND](WHILE.htm) and [REPEAT ... UNTIL](REPEAT.htm) . loops are verified and [IF ... END IF](IFENDIF.htm) pairs are matched. If an error is encountered program execution is terminated and the error message is displayed.
- Any temporary file streams opened with the autoallocate mode of [OPEN#](OPENhash.htm) will be closed and deselected. Similarly any temporary KCML database handles allocated by [KI_ALLOC_HANDLE](mk:@MSITStore:kdb.chm::/tmp/KI_ALLOC_HANDLE.htm) will be closed and freed.
- Space is reserved for all variables that have not already been defined. Numeric variables are initialized to zero, and alpha variables are set to blanks. As of KCML 5.02 this is not strictly true as arrays and strings will have this deferred until they are first used. Such variables have any space currently allocated freed and they are marked as unused pending first reference.
- The data pointer used by the [READ](READ.htm) statement is set to the first value of the first [DATA](DATA.htm) statement in the program.

Once the resolution process is complete and no errors have occurred, the RUN command then begins executing the program code.

- If no line number is specified then all non-common variables are cleared from memory, the resolution process is performed, and finally execution of the program code begins from the first line number in the program.
- If a line number is specified, the program is resolved, and execution begins at the specified line, non-common variables are not cleared from memory and all variables retain their current values. RUN cannot be used to jump into the middle of a [FOR ... NEXT](FOR.htm) loop, or a subroutine. By specifying a statement number, execution can be started from a specific statement on a specific line.

RUN can also be used without any line numbers as a statement in a program to force the program to be restarted as if halt had been pressed and RUN entered in immediate mode.

RUN STOP will resolve a program and stop just before execution. The program can be started with [CONTINUE](CONTINUE_command.htm). This can be useful in checking for resolve time errors such as mismatched [IF ... END IF](IFENDIF.htm) statements.

Syntax examples:

RUN\
RUN 1200\
RUN 9000,7\
RUN STOP\
1900 RUN

See also:

[LOAD RUN](LOAD_RUN.htm)
