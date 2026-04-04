\#LINE <span style="font-size: 16pt ; ">function</span>

------------------------------------------------------------------------

General Form:\
\
     \#LINE\
\

------------------------------------------------------------------------

The \#LINE function is used to return the line number in the program, that contains the currently executing statement. In immediate mode, just after a [STOP](STOP.htm), a [TRAP](TRAP.htm) or an error, the line number is that of the next statement that would have been executed. If the program has not been run or has been completed, i.e. there are no more statements to be executed, \#LINE will return zero.

See also:

[\#STAT](_STAT.htm), [LIST RETURN](LIST_RETURN.htm)

 
