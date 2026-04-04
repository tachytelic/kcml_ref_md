LIST L

------------------------------------------------------------------------

General Form:

LIST \[title\] L

Where:

title = alpha_variable or a literal string

------------------------------------------------------------------------

The LIST L statement lists warnings releating to the state of the program currently in memory. Once executed LIST L will first resolve the program and report all lines that contain syntax errors. LIST L will then check for the following:

- That all [FOR ... TO](FOR.htm) statements have a matching NEXT statement and vice versa, although the index variable is not checked.
- That all [REPEAT](REPEAT.htm) statements have a matching UNTIL and vice versa.
- That all [WHILE](WHILE.htm) statements have a matching WEND and vice versa.
- That all [DO](DO.htm) statements have a matching END DO, and vice versa.

Problems reported by lines that start with the word "ERROR" must be fixed as these will stop the program from executing. Problems reported by lines that start with the word "WARNING" should be checked as these may cause errors during program execution.

Example:

LIST L\
WARNING: line 00020 statement 2 possible NEXT BREAK\
ERROR: line 00021 statement 1 P31 Incomplete DO group\
ERROR: line 00020 statement 2 P31 Incomplete loop\
WARNING: line 00010 statement 1 FOR without NEXT

From this example the the following can be ascertained:

- Line 20 statement 2 is a [BREAK](BREAK.htm) statement that is within a [WHILE ... WEND](WHILE.htm) which is within a [FOR ... NEXT](FOR.htm).
- Line 21 contains an [ENDDO](DO.htm) statement that has no matching [DO](DO.htm) statement.
- Line 20 has a [REPEAT](REPEAT.htm) or [WHILE](WHILE.htm) statement without a matching UNTIL or WEND statement.
- Line 10 has a [FOR ... TO](FOR.htm) statement without a matching NEXT statement.

See also:

[BREAK](BREAK.htm), [CONTINUE](CONTINUE.htm)
