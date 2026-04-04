POS(

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/pos.gif" data-align="BOTTOM" data-border="0" alt="pos.gif" />\
2.      POS(field_variable)\
\
Where:\
\
     hh           = two hexadecimal digits (0-9, A-F)\
\

------------------------------------------------------------------------

The first form of the POS( function returns the position of the first occurrence of a character in an alpha variable, string or string function that satisfies the specified relationship. The POS( function is valid wherever a numeric expression is legal.

The character used for comparison follows the relational operator. If more than one character is supplied then only the first character of the string is used for comparison.

The position of the first character that satisfies the relation, is returned as a numeric value. If the relation is not satisfied then POS( returns zero.

If a minus sign precedes the alpha variable, literal, or string function being searched, POS( returns the position of the last character satisfying the relation.

The second form is used to return the start position of the specified field, e.g:

StartPos = POS(.Name\$)

The [LEN(](LEN(.htm) function can be used to return to size of the field.

Example:

DIM test\$26\
test\$ = "abcdefghijklmnopqrstuvwxyz"\
Test = POS(test\$ = "o")

Syntax examples:

period = POS(record\$ = ".")\
IF (POS(file\$() = "#") == 0)\
big = POS(-after\$ \<\> STR(tst\$,status,1))\
tmp = pos(.name\$)

See also:

[FLD(](FLD(.htm)
