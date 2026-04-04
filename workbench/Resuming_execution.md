## Resuming execution

A program halted in the debugger can be resumed by pressing C for CONTINUE. To move through the program a line at a time see [Stepping](stepping.htm).

If halted inside a subroutine, pressing **R** will resume execution and halt again when the [RETURN](mk:@MSITStore:kcmlrefman.chm::/RETURN.htm) is executed. This is exactly the same as the [CONTINUE RETURN](mk:@MSITStore:kcmlrefman.chm::/CONTINUE_RETURN.htm) command. Similarly **N** does a [CONTINUE NEXT](mk:@MSITStore:kcmlrefman.chm::/CONTINUE_NEXT.htm)), **O** does a [CONTINUE LOOP](mk:@MSITStore:kcmlrefman.chm::/CONTINUE_LOOP.htm) and **L** does a [CONTINUE LOAD](mk:@MSITStore:kcmlrefman.chm::/CONTINUE_LOAD.htm).

If you believe that the program will reach a particular line but you don't want to step through each line on the way, then put the cursor on the target statement and press **G** for GOTO. This sets a temporary [trap](Setting_traps.htm) at this line and resumes execution.

To restart execution from a different point in the program move the cursor to the target statement and press **S** to SET it to be the new current line.
