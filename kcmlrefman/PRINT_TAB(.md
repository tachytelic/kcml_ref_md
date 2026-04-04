PRINT TAB(

------------------------------------------------------------------------

General Form:\

1.  PRINT TAB(numeric_expression)
2.  PRINT TAB(strexpr, numeric_expression)

------------------------------------------------------------------------

The PRINT TAB() function is used to position the cursor to the specified column position. The TAB( function can only be used in conjunction with the [PRINT](PRINT.htm) statement. This statement is only relevant when developing text based applications. Multiple [PRINT](PRINT.htm) functions ([AT(](PRINT_AT(.htm), [BOX(](PRINT_BOX(.htm), [HEXOF(](PRINT_HEXOF(.htm), [TAB(](PRINT_TAB(.htm) ) can be incorporated anywhere in the [PRINT](PRINT.htm) statement, separated with semi-colons or commas.

Using the TAB( function on the screen, will overwrite with spaces all intervening characters on the line. If the specified column has already been passed, the TAB( function is ignored. Specifying a column number greater than the currently selected line width, causes the cursor to be positioned at the first position on the next line.

The second form is used to specify a fixed width for the given string expression which is to be printed at the current tab position. The second arguement to the function is the width of the field. If this is less than the actual length of the string expression then the expression will be clipped to that width whereas if it is greater then the field will be passed with spaces to move the tab position to the next position after the field. This function is most useful in connection with [multilanguage applications](TutorialLangs.htm) where the length of the string may differe markedly between languages.

Example:

FOR count = 1 to 5\
     PRINT TAB(4\*count); count;\
NEXT count\
\
    1 2 3 4 5

Syntax examples:

PRINT TAB(7);heading\$(1); TAB(20);heading\$(2)\
PRINT TAB(count \* 4);temp\$(count)\
PRINT act\$(1); TAB(count);"Title = ";title\$

See also:

[PRINT](PRINT.htm), [PRINT AT(](PRINT_AT(.htm), [PRINT BOX(](PRINT_BOX(.htm), [PRINT HEXOF(](PRINT_HEXOF(.htm)
