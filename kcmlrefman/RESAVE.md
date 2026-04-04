RESAVE

------------------------------------------------------------------------

General Form:\
\
     RESAVE \[\<\[S\]\[R\]\[!\]\>\] \[#stream,\] filename \[start_line\] \[,end_line\]\
\
Where:\
\
     start_line, end_line      = valid program line numbers within the range 0 \< 32000\
\

------------------------------------------------------------------------

The RESAVE statement saves the program currently in memory over an existing program file. The filename specifies the file to be overwritten. The RESAVE statement is particularly powerful when combined with the [\$PROG]($PROG.htm) function to save the last program loaded onto the disk. This should not be done when programs may have been overlaid as the combined programs will be saved into the one file.

- Specifying a start line number after the filename will resave only program lines after and including the specified line number.
- Specifying a comma and an end line number will only resave the line up to and including the specified line number.
- Specifying both a start and an end line number will resave only the specified lines and the intervening lines.
- The optional \`\<R\>' parameter, if specified causes, the program to be resaved with the text after any [REM](REM.htm) statements removed.

To scramble a program so that it cannot be listed when [LOADed](LOAD.htm), the ! is used in conjunction with the [SELECT PASSWORD](SELECT_PASSWORD.htm) command. See [SELECT PASSWORD](SELECT_PASSWORD.htm).

Syntax examples:

RESAVE "TESTPROG"\
RESAVE \#10,prog\$(3)\
RESAVE \$PROG 400, 9000

See also:

[\$PROG]($PROG.htm), [REMOVE](REMOVE.htm), [SAVE](SAVE.htm), [SELECT PASSWORD](SELECT_PASSWORD.htm)

 
