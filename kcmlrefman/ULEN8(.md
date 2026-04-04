ULEN8(

General Form:

ULEN8(strexpr)

------------------------------------------------------------------------

The ULEN8( numeric function is used to determine the length in characters of a string expression which is presumed to represent a UTF-8 encoded [Unicode](TutorialUnicode.htm) string. The result is returned as a numeric value. The ULEN8( function is valid wherever a numeric function is legal.

Trailing spaces are not considered to be part of the string unless enclosed in a [STR(](STR(.htm) expression. If a variable only contains spaces then the value returned will be 0. This is different to the [LEN(](LEN(.htm) function which would have returned 1.

The string must be properly encoded UTF-8 and the result when applied to incorrect encoding is not defined. Remember that HEX(FE) and HEX(FF) characters cannot occur in a UTF-8 string.

Example:

DIM a\$="\$€£"\
IF (a\$ \<\> HEX(24E282ACC2A3)) THEN PANIC\
IF (ULEN8(a\$)) \<\> 3 THEN PANIC\
