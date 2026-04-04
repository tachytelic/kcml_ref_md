LIST TRAP

------------------------------------------------------------------------

General Form:\
\
     LIST \[title\] TRAP \[\*\]\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST TRAP statement lists all the [TRAPs](TRAP.htm) currently active showing the line and statement numbers.

When using the KCML Workbench, TRAPped lines are flagged in the left hand margin.

If an asterisk follows the word TRAP then the line number and statement where the TRAP is set will be LISTed in full. Leading colons (:) are inserted to show the exact position of the [TRAP](TRAP.htm) within the line, any watchpoints set by [TRAP](TRAP.htm) are also listed, for example:

LIST TRAP \*\
 LINE STAT\
 ---- ----\
 00010 FOR count=1 TO length\
 09000 :::STR(beta\$,2,3)=code\$\
 09000 ::::FOR y=2 TO 20 STEP 2\
\
 SUBROUTINE\
 ----------\
 'GET\
 00030 :::DEFFN'open_file(fd, name\$, p) - executes\
    : PRINT HEXOF(+test\$)\
\
 VARIABLE\
 --------\
 BA\$

without the asterisk the output would be as follows:

:LIST TRAP\
 LINE STAT\
 ---- ----\
 1000 3\
 2010 5\
 2090 1\
\
 SUBROUTINE\
----------\
 'GET - executes\
    : PRINT HEXOF(+test\$)\
 \
 VARIABLE\
 --------\
 BA\$

Note that adding the asterisk to LIST TRAP will only have effect if the program is resolved.

See also:

[TRAP](TRAP.htm)

 
