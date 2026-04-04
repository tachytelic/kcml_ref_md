Debugging programs from the console

Introduction

For terminals that do not support the full KCML Workbench a simple line editor and immediate mode debugger is available.

Once a program has been executed, any run time errors will halt program execution and display the program line with the appropriate error message. The reason for the error is reported with a code and an explanation. Recoverable errors may be trapped with [ERROR](ERROR.htm) and [ON ERROR](ON_ERROR.htm) statements, or program execution may be transferred to another line and continued with the [GOTO](GOTO.htm) and [CONTINUE](CONTINUE_command.htm) commands, or can be instructed to continue with the next statement with the [CONTINUE](CONTINUE_command.htm) command. Refer to chapter 21 for a complete list of possible error codes and recovery methods.

Halting program execution

The STOP statement

Program execution can be temporarily halted by pressing the [HALT](TextTermHalt.htm) key, by setting a [TRAP](TRAP.htm) on a specified line and statement number, subroutine label or variable name, or when a [STOP](STOP.htm) statement is executed, all of which interrupt program flow and return to immediate mode.

The [STOP](STOP.htm) statement can be inserted anywhere within the program, but is best used at places within the program code that should never be executed unless there is a serious bug in the program. For example:

. .\
ON count GOTO 1000,2000,3000\
STOP "Invalid option"

would display the stop message if the variable *count* was \<1 or \>3.

The RUN STOPrun command can be used to resolve the program and [STOP](STOP.htm) before any program lines are executed. This can be useful in checking for resolve time errors such as mismatched [DO](DO.htm) groups.

The PANIC statement

As an alternative to the [STOP](STOP.htm) statement the [PANIC](PANIC.htm) statement may be used to create an ASCII file in the current directory containing a snapshot of the current program state. The user will then be returned back to the native operating system prompt terminating **KCML**. The panic file contains program state information including the screen contents, login name (UNIX versions only), terminal number, and the output from the [LIST RETURN](LIST_RETURN.htm), [LIST DIM](LIST_DIM.htm) and [LIST DT](LIST_DT.htm) commands. The file is created in the current working directory, unless the [*PANICDIR* environment variable](EnvVars.htm) is set. When the [PANIC](PANIC.htm) statement is executed the message:

Unexpected program condition on line *lllll* of program *prg\*
Dumping program state to file panic*pppp*\
RETURN to resume

Where *llll* is the program line containing the [PANIC](PANIC.htm) statement, *prg* is the name of the program containing the [PANIC](PANIC.htm) statement, and *pppp* is the UNIX process id number of the currently running **KCML** task. On DOS versions the file is named PAN*lllll*. Where *lllll* is a unique number taken from the current date and time.

The [STOP PANIC ON](PANIC.htm) statement can be used to instruct **KCML** to consider all subsequent [STOP](STOP.htm) statements as [PANIC](PANIC.htm) statements, this avoids having to change existing code containing [STOP](STOP.htm) statements to include [PANIC](PANIC.htm) statements. The STOP PANIC OFFstoppanic statement restore to the original meaning of [STOP](STOP.htm).

The TRAP command

The [TRAP](TRAP.htm) command allows a trap to be set on a specific line number and optionally a specific statement number within the line, or a specific variable or subroutine name. Just before executing a trapped line and statement, variable or subroutine, **KCML** will stop and display the line. E.g.

TRAP 100,5\
TRAP name\$\
TRAP 'get_next_record

would set a trap on line 100 statement 5, on the variable *name\$* and on the subroutine *'get_next_record*.

[TRAP](TRAP.htm) are preserved over a subsequent program [LOAD](LOAD.htm). TRAP’strap are only set for foreground lines, and subroutines unless the reserved word [TRAP](TRAP.htm) is preceded with the \`@' sign, for example:

@TRAP 100,5\
@TRAP 'get_next_record

would set TRAP’s on the same line and subroutine as before but would only halt execution if executed in any global partition. Setting a trap on a variable will stop whenever the variable is executed even if executed in the currently selected global partition.

There is no limit to the number of TRAPs that can be active at any one time. A list of currently active [TRAP](TRAP.htm) can be obtained with the [LIST TRAP](LIST_TRAP.htm) command, for example:

LIST TRAP LINE STAT ---- ---- 100 5 @ 100 5 SUBROUTINE ---------- 'GET_NEXT_RECORD @ 'GET_NEXT_RECORD VARIABLE -------- NAME\$

TRAPs are removed by reissuing the original [TRAP](TRAP.htm) statement, thus toggling the trap off, for example:

TRAP 100,5

would turn off the trap set in the previous example. All foreground [TRAP](TRAP.htm) can be removed with the [TRAP OFF](TRAP.htm) command, all global trap can be removed with the @[TRAP OFF](TRAP.htm), or all TRAPs, both foreground and global, can be removed with the [TRAP ALL OFF](TRAP.htm) command.

The [TRAP](TRAP.htm) command also has a watch point facility allowing optional trailing statements which are executed when a [TRAP](TRAP.htm) is reached. For example:

TRAP name\$ : IF name\$="Steve" THEN STOP

would only stop program execution if the variable *name\$* was equal to \`Steve'. Any number of statements may be used after the [TRAP](TRAP.htm) command. [GOTO](GOTO.htm) and [GOSUB](GOSUB.htm) statements can also be used although care should be taken to ensure that program flow is returned to the [TRAP](TRAP.htm) statement, this may be difficult if [GOTO](GOTO.htm) is used, see table below for some examples of valid [TRAP](TRAP.htm) commands.

|  |  |
|----|----|
| TRAP 1000 | Halt the program before the foreground line 1000 is executed. If the [TRAP](TRAP.htm) is already set then remove it. |
| TRAP 'newsub | Halt the program before the subroutine *'newsub* is executed. If the [TRAP](TRAP.htm) is already set then remove it. |
| @TRAP 9000,4 | Halt the program before the global partition line 9000 statement 4 is executed. If the [TRAP](TRAP.htm) is already set then remove it. |
| TRAP tp\$: IF tp\$="A" THEN GOSUB 9000:count++ | If the variable *tp\$* is executed and it is currently equal to "A" then branch to line 9000. Upon returning or if *tp\$* not equal to "A", increment the variable *count* by 1. If the [TRAP](TRAP.htm) is already set then remove it. |
| TRAP OFF | Remove all foreground [TRAP](TRAP.htm). |
| @TRAP OFF | Remove all global [TRAP](TRAP.htm). |
| TRAP ALL OFF | Remove all foreground and global [TRAP](TRAP.htm). |

Examples of [TRAP](TRAP.htm) commands

See also:

[STOP](STOP.htm), [TRAP](TRAP.htm), [PANIC](PANIC.htm), [CONTINUE](CONTINUE_command.htm), [RUN](RUN.htm)

Analysing the program and variable status

Once in immediate mode, variables may be examined with the [PRINT](PRINT.htm) or [LIST DIM](LIST_DIM.htm) commands, the program itself may be listed with the [LIST](LIST.htm) command, or any of the other [LIST](LIST.htm) commands may be used to obtain information about the current contents and state of the program and memory. The [\$PROG]($PROG.htm), [\#LINE](_LINE.htm), and [\#STAT](_STAT.htm) functions may be used to find the name of the last program loaded, the number of the line currently being executed and the statement number within the line being executed, respectively. The following summarises the [LIST](LIST.htm) statements useful for debugging programs

|  |  |
|----|----|
| [LIST](LIST.htm) | Displays the program text currently held in memory in line sequence. Ranges of lines may be displayed by specifying lines numbers after the command. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST CALL](LIST_CALL.htm) | Displays all references to given [CALL](CALL.htm)s in a program. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST DIM](LIST_DIM.htm) | Displays both common and non-common variables and their contents in the order in which they were declared, except that all common variables precede the non-common variables. |
| [LIST DT](LIST_DT.htm) | Displays the current contents of the device and device equivalence tables. |
| [LIST E](LIST_E.htm) | Displays all local **KCML** environment variables set by the [ENV(](ENV(.htm) function. |
| [LIST FROM'](LIST_FROMquote.htm) | Lists from the first line of the requested subroutine. |
| [LIST RETURN](LIST_RETURN.htm) | Lists information about the currently executing program. Information includes the currently executing line and statement number, the last programs loaded, and the name of the currently selected global partition, if any, and the contents of the return stack. If executed within a subroutine containing local variables then the variable names and contents of any non unique local variables are also shown. |
| [LIST LOCAL](LIST_LOCAL.htm) | Lists either a specified local variable or all currently defined local variables. |
| [LIST SPACE](LIST_SPACE.htm) | Displays a summary of where memory has been allocated. |
| [LIST T](LIST_T.htm) | Searches for instances of the specified text in the program currently being held in memory. If the ‘@’ sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST P](LIST_P.htm) | [LIST P](LIST_P.htm) performs the same function as [LIST T](LIST_T.htm) except that some pattern matching characters similar to those used by UNIX editors can be used. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST TRAP](LIST_TRAP.htm) | Lists all currently active [TRAP](TRAP.htm) statements. |
| [LIST U](LIST_U.htm) | Lists all of the available C user written routines and a summary of their expected arguments. |
| [LIST V](LIST_V.htm) | Lists instances of a variable in a program. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST \#](LISThash.htm) | Lists all references to the specified line within the program currently in memory. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST '](LISTquote.htm) | Lists all references to the specified defined subroutine in a program. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |
| [LIST !](LISTexclam.htm) | Lists the line numbers of lines containing syntax errors. |
| [LIST ?](LISTquestion.htm) | Lists all variables which appear only once in the current program. If the \`@' sign precedes the reserved word LIST then the LISTing is taken from the currently selected global partition. |

Continuing a halted program

As long as no program lines are created or modified, the execution of a program can be continued with one of the [CONTINUE](CONTINUE_command.htm), [CONTINUE LOAD](CONTINUE_LOAD.htm), [CONTINUE LOOP](CONTINUE_LOOP.htm), [CONTINUE NEXT](CONTINUE_NEXT.htm) or [CONTINUE RETURN](CONTINUE_RETURN.htm) commands or each subsequent statement may be stepped one at a time by pressing, if enabled, the HALT/STEPhalt key.

The [CONTINUE](CONTINUE_command.htm) command will resume execution of the program. To [CONTINUE](CONTINUE_command.htm) the program at a different line number the [GOTO](GOTO.htm) statement may be used. Jumping in and out of loops and subroutines is allowed but will eventually generate an error as the next [RETURN](RETURN.htm), NEXT, WEND or UNTIL statement may not be in the return stack.

[CONTINUE LOAD](CONTINUE_LOAD.htm) will restart the program and stop immediately before the next [LOAD](LOAD.htm) statement.

[CONTINUE LOOP](CONTINUE_LOOP.htm) will restart the program and stop immediately before the last iteration which would complete the current [WHILE ... WEND](WHILE.htm) or [REPEAT ... UNTIL](REPEAT.htm) loop.

[CONTINUE NEXT](CONTINUE_NEXT.htm) will restart the program and stop immediately before the last iteration which would complete the current FOR .. NEXT loop.

[CONTINUE RETURN](CONTINUE_RETURN.htm) will restart the program and stop it again immediately after the next [RETURN](RETURN.htm) statement associated with the most recent [GOSUB](GOSUB.htm) or [GOSUB'](GOSUBquote.htm) statement.

The [RUN](RUN.htm) command followed by a line number will resolve the program, and begin execution at the specified line; non-common variables are not cleared from memory and all variables retain their current values.

Tracing program flow

The [TRACE](TRACE.htm) statement produces a trace of program operations. Trace mode may be turned on when the [TRACE](TRACE.htm) statement is either executed from within a program or Immediate mode. Trace mode is turned off with the [TRACE OFF](TRACE.htm) command.

By specifying two line numbers [TRACE](TRACE.htm) output will appear only when the program is executing between the two specified line numbers. While executing outside this range no tracing occurs. While this form of [TRACE](TRACE.htm) is active, the [HALT](TextTermHalt.htm) key will not stop execution until the program is executing a line outside the specified range. Thus programs can be stepped through but standard subroutines in an overlay may be skipped.

Trace reports on [GOTO](GOTO.htm), [GOSUB](GOSUB.htm) and [GOSUB'](GOSUBquote.htm) branches, [RETURN](RETURN.htm) statements, NEXT statements, WHILE ... WENDwhile and REPEAT ... UNTILrepeat loops, [SELECT CASE](SELECT_CASE.htm) statements, and [TRAP](TRAP.htm) executed code.

The [SELECT TRACE](SELECT_TRACE.htm) statement allows the output from the [TRACE](TRACE.htm) command to be written to a native operating system file or device, e.g.

TRACE 1000,5000 SELECT TRACE "/tmp/TRACEFILE"

would copy the output from the [TRACE](TRACE.htm) command into the file \`/tmp/TRACEFILE'. This allows the program to be [TRACE](TRACE.htm)d, without effecting the screen display.
