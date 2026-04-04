ALL(

------------------------------------------------------------------------

General Form:\
     **<span style="font-size: 20pt ; "><img src="bitmaps/all.gif" data-align="BOTTOM" data-border="0" alt="all.gif" /></span>\**
Where:\
\
     hex_pair      = two hexadecimal digits (0-9 or A-F)\
\
     length           = a numeric expression\

------------------------------------------------------------------------

The ALL( function defines a string of characters in which each character is equal to the character specified in the function. If more than one character is specified, then only the first character is used by the ALL( function. The ALL( function is valid only in [PRINT](PRINT.htm) statements, and in the alphanumeric portion of an alphanumeric assignment statement.

The ALL( function can be used to initialise alpha variables and arrays. ALL( can be also be used in logical operations for changing certain bits in every character of an alpha variable or array.

For example, the following statements would both initialise the entire contents *library\$()* to spaces:

library\$() = ALL(HEX(20))\
library\$() = ALL(" ")

Syntax examples:

type\$ = AND ALL(HEX(7F))\
line\$ = ALL("-",100)\
flags\$ = ALL(character\$)\
STR(sample\$,15,20) = OR ALL(F0,2)

 
