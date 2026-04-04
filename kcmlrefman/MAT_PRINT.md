MAT PRINT

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/matprint.gif" data-align="BOTTOM" data-border="0" alt="matprint.gif" /> \
<img src="bitmaps/matprint1.gif" data-align="BOTTOM" data-border="0" alt="matprint1.gif" />\
\
Where:\
\
     array_name           = an alpha or numeric array variable\
\

------------------------------------------------------------------------

The MAT PRINT statement is used to display the contents of the specified alpha or numeric array variables. Each array variable is displayed in a row-by-row format.

If the TO clause is specified with the second form, the output is added to a string buffer at a position determined by the binary value of a count held in the first two bytes of the alpha receiver variable. After the print operation the count is updated by the number of characters added to the buffer. If the count is zero then the first character will be inserted at byte three of the string. The first two bytes of the receiver variable should therefore be initialised to HEX(00) before the [PRINT TO](PRINT.htm) statement is executed.

Example:

DIM test(2,2), test\$(2)5\
test() = CON\
test\$(1) = "adcdefghij"\
test\$(2) = "fghij"\
PRINT test(),test\$()\
\
 1           1\
 1           1\
 abcdefghij

Syntax examples:

PRINT array(), "FRED"\
MAT PRINT B;C;\
PRINT TO test\$, new()

See also:

[PRINT](PRINT.htm)

 
