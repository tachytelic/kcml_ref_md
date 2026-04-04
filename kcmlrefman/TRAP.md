TRAP <span style="font-size: 16pt ; ">command</span>

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/trap.gif" data-align="BOTTOM" data-border="0" alt="trap.gif" />\
\

------------------------------------------------------------------------

The TRAP command allows a trap to be set on any of the following:

A specific program line and an optional statement number. If the @ sign precedes the reserved word TRAP then the specified line and statement number is trapped before it is next executed within a global partition.

A subroutine defined with either the [DEFFN'](DEFFNquote.htm), [DEFSUB'](DEFSUB.htm) or the [\$DECLARE']($DECLARE.htm) statements. If the @ sign precedes the reserved word TRAP then the specified subroutine is trapped before is is next executed within a global partition.

A variable, including arays, field and global variables.

Just before executing a trapped statement, KCML will stop executing and display the line. Execution can be resumed by entering a [CONTINUE](CONTINUE_command.htm), [CONTINUE LOAD](CONTINUE_LOAD.htm), [CONTINUE LOOP](CONTINUE_LOOP.htm), [CONTINUE NEXT](CONTINUE_NEXT.htm) or [CONTINUE RETURN](CONTINUE_RETURN.htm) statement, or by HALT/STEPing the program.

All forms of trap can also have optional trailing statements which are executed when the trap is reached, for example:

TRAP record\$ IF record\$="TST123" THEN STOP

would only stop the program when the variable record\$ is set to "TST123". All statements except [GOTO](GOTO.htm) can be used after the TRAP statement including [GOSUB](GOSUB.htm) and [DEFFN'](DEFFNquote.htm). Though you must make sure that program control returns to the TRAP command. If a [STOP](STOP.htm) of [PANIC](PANIC.htm) statement is executed within a TRAP command, subsequent step operations in the editor or [CONTINUE](CONTINUE_command.htm) commands will return control to the program and not the TRAP command.

There is no limit to the number of traps that can be active at any one time. Currently active traps can be displayed with the [LIST TRAP](LIST_TRAP.htm) command. Individual traps can be removed by reissuing the original TRAP statement, thus toggling the trap off. All foreground traps are removed with TRAP OFF or unless [CLEAR](CLEAR.htm) is issued. Background traps are removed by executing the @TRAP OFF statement. Alternatively, both background and foreground traps may be removed with the TRAP ALL OFF statement. All traps are preserved across [LOAD](LOAD.htm) statements.

Examples:

|  |  |
|----|----|
| TRAP 100 | Sets a trap on the first statement of line 100 for the foreground program only. |
| @TRAP 1000,5 | Sets a trap on statement 5 of line 1000 in the global partition. |
| TRAP 'merge | Sets a trap at the start of the foreground subroutine 'merge, the subroutine may be defined with either the [DEFFN'](DEFFN.htm), [DEFSUB'](DEFSUB.htm), or the [\$DECLARE']($DECLARE.htm) statement. |
| @TRAP 'new | Sets a trap at the start of the global subroutine 'new. |
| TRAP new_var\$( | Sets a trap before the next time that the variable new_var\$( is referenced. Variabled are trapped in both the foreground and global partitions. |
| TRAP OFF | Remove all foreground traps. |
| @TRAP OFF | Remove all global traps. |
| TRAP ALL OFF | Remove both foreground and global traps. |

TRAP 'open_file IF file\$ = "STOCK" THEN GOSUB 'reorganise: ELSE PRINT file\$

If the variable file\$ is set to STOCK when the subroutine 'open_file is executed then the subroutine 'reorganise will be executed before normal program execution continues, otherwise the variable file\$ is printed.

See also:

[CONTINUE](CONTINUE_command.htm), [CONTINUE LOAD](CONTINUE_LOAD.htm), [CONTINUE LOOP](CONTINUE_LOOP.htm),\
[CONTINUE NEXT](CONTINUE_NEXT.htm), [CONTINUE RETURN](CONTINUE_RETURN.htm), [LIST TRAP](LIST_TRAP.htm)

 
