CONTINUE

------------------------------------------------------------------------

General Form:\
\
     CONTINUE\
\

------------------------------------------------------------------------

The CONTINUE statement is used to skip the remainder of a [FOR ... NEXT](FOR.htm) , [WHILE ... WEND](WHILE.htm) , or [REPEAT ... UNTIL](REPEAT.htm) loop and resume execution at the start of the next iteration re-evaluating the condition. The CONTINUE must actually fall within the body of the loop and cannot be inside a subroutine called from within the loop. The pairing of CONTINUE with the [FOR](FOR.htm), [WHILE](WHILE.htm) or [REPEAT](REPEAT.htm) statements is checked at resolve time.

The CONTINUE statement, if entered within an immediate mode [FOR](FOR.htm), [WHILE](WHILE.htm) or [REPEAT](REPEAT.htm) loop will be treated as the CONTINUE command and will attempt to resume execution of the program currently in memory.

Example:

WHILE in_loop\<10 DO\
     IF ++in_loop = 5 THEN CONTINUE\
     'Update()\
WEND

See also:

[BREAK](BREAK.htm), [REPEAT ... UNTIL](REPEAT.htm) [STOP](STOP.htm),[TRAP](TRAP.htm), [WHILE ...WEND](WHILE.htm), [FOR ... TO, NEXT](FOR.htm), [CONTINUE](CONTINUE_command.htm)
