\#STAT <span style="font-size: 16pt ; ">function</span>

------------------------------------------------------------------------

General Form:\
\
     \#STAT\
\

------------------------------------------------------------------------

The \#STAT function is used to return the statement number within the line of the currently executing statement, including a statement that has previously encountered a system error. In immediate mode, just after a [STOP](STOP.htm) or [TRAP](TRAP.htm) has occurred, \#STAT is that of the next statement that would have been executed.

See also:

[\#LINE](_LINE.htm), [LIST RETURN](LIST_RETURN.htm)
