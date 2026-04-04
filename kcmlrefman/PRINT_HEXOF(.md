PRINT HEXOF(

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/printhexof.gif" data-align="BOTTOM" data-border="0" alt="printhexof.gif" />\
\

------------------------------------------------------------------------

The HEXOF( function prints the value of the alpha variable, literal string or string function in hexadecimal format. Trailing spaces (HEX(20)) are also printed. The HEXOF( function can only be used in conjunction with the [PRINT](PRINT.htm) statement. Multiple [PRINT](PRINT.htm) functions ([AT(](PRINT_AT(.htm), [BOX(](PRINT_BOX(.htm), [HEXOF(](PRINT_HEXOF(.htm), [TAB(](PRINT_TAB(.htm) ) can be incorporated any where in the [PRINT](PRINT.htm) statement, separated with semi-colons.

Inserting a minus sign before the alpha variable, literal string, or string function, causes the HEXOF( function to insert spaces between each pair of bytes.

Example:

DIM test\$8\
test\$ = "ABCDEFG "\
PRINT HEXOF(-test\$)\
 4142 4344 4546 4720

Inserting a plus sign before the alpha variable, literal string or string function, causes the HEXOF function to print the ASCII equivalence on the right-hand side of the output. In this format 16 characters are printed on each line.

Example:

DIM test\$8\
test\$ = "ABCDEFG "\
PRINT HEXOF(+test\$)\
 4142 4344 4546 4720                \*ABCDEFG \*

See also:

[PRINT](PRINT.htm), [PRINT AT(](PRINT_AT(.htm), [PRINT BOX(](PRINT_BOX(.htm), [PRINT TAB(](PRINT_TAB(.htm)

 
