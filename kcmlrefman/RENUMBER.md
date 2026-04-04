RENUMBER <span style="font-size: 16pt ; ">command</span>

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/renumber.gif" data-align="BOTTOM" data-border="0" alt="renumber.gif" />\
\
Where:\
\
     start_line, end_line, new_start      = valid program line numbers ranging from 0 \< 32000\
\
     increment                = positive integer\
\

------------------------------------------------------------------------

The RENUMBER command renumbers the program lines of the program currently in memory.

The RENUMBER command can perform the following renumbering operations:

- RENUMBER with no line numbers specified, renumbers all program lines, starting with the number 10 and incrementing in steps of 10.
- RENUMBER followed by a start line number, renumbers the specified line number and all program lines after the specified line number, in steps of 10. Lines before are left unchanged.
- RENUMBER followed by an end line number, renumbers all lines starting from 0 to the specified number in steps of 10. Lines after the end line number are left unchanged.
- RENUMBER followed by a start and an end line number, renumbers the specified line and the intervening lines in steps of 10.
- RENUMBER followed by a new start line number, renumbers the specified lines, if any, with the line numbers starting at the new line number.
- Specifying a STEP value alters the step with which programs are numbered, the default is 10.

After renumbering, the system automatically changes any references to the renumbered lines statements. (E.g. any [GOTO](GOTO.htm), [GOSUB](GOSUB.htm), [RESTORE](RESTORE.htm), etc.)

Examples:

RENUMBER 100-500 TO 1000 STEP 5\
RENUMBER 10000, 12000 TO 25000
