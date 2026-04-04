Program resolution and execution

Program execution can be started in a number of ways. Either by pressing the F11 execute key in the **KCML Workbench** or by entering the [RUN](RUN.htm) or [LOAD RUN](LOAD_RUN.htm) commands at the immediate mode prompt in the Workbench console window, or if a **KCML** program name immediately follows the **KCML** utility when it is called from the native operating system. Before program execution can begin the program is resolved. The resolution process performs the following functions:

- The program is sequentially scanned for syntax errors. All line number and variable references, [FOR](FOR.htm) ... NEXT, [REPEAT](REPEAT.htm) ... UNTIL, [WHILE](WHILE.htm) ... WEND loops, [SELECT CASE](SELECT_CASE.htm) statements and DOdo groups are verified.
- [DIM](DIM.htm) and [COM](COM.htm) statements are executed and space is reserved for all variables that have not already been defined. Numeric variables are initialised to zero, and alpha variables are set to blanks.
- The data pointer used by the [READ](READ.htm) statement is set to the first value of the first [DATA](DATA.htm) statement in the program.

Once the resolution process is complete and no errors have occurred, **KCML** then begins to execute the program code. If an error occurs during the resolution process an error is displayed and the resolution process is halted.

Resolution without execution can be forced by pressing the SHIFT-F9 in the **KCML Workbench** or by entering the [RUN STOP](RUN.htm) command at the immediate mode prompt.

Once the program has been successfully resolved execution will begin at the first statement and will continue until either one of the following statements is executed:

- STOP
- \$END
- END
- PANIC

or until the program executes the last line of the program, an unfielded error occurs or a [TRAP](TRAP.htm) event occurs.

Execution can be interrupted with the [HALT](TextTermHalt.htm) or [RESET](TextTermHalt.htm) keys if they have been enabled. The [HALT](TextTermHalt.htm) key causes **KCML** to save the current program state and switch to the Workbench debugger window if available. If the terminal does not support the Workbench then the immediate mode prompt is displayed. Provided that the program is not altered by editing, adding or deleting program lines, the program can be restarted where it left off with the [CONTINUE](CONTINUE.htm) command. This can be done by pressing the 'C' key in the Workbench or alternatively the CONTINUE command can be entered directly at the immediate mode prompt. Execution can be restarted at any other line using 'S' command followed by the 'C' command. In immediate mode this can be done with the [GOTO](GOTO.htm) and [CONTINUE](CONTINUE.htm) commands. Each time the SPACEBAR is pressed **KCML** will single step through the program a line at a time.

If program lines are changed or if new lines are added to the program then the program must be re-resolved before it can be restarted.
