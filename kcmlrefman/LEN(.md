LEN(

General Form:\
<img src="bitmaps/len.gif" data-align="BOTTOM" data-border="0" alt="len.gif" />

\

------------------------------------------------------------------------

The LEN( numeric function is used to determine the length in bytes of an alphanumeric argument. The result is returned as a numeric value. The LEN( function is valid wherever a numeric function is legal.

Trailing spaces are not considered to be part of an alpha variable. If a variable only contains spaces, then the value returned will be 1. This function does not examine the encoding of a string and returns the number of bytes rather than characters. To get the number of characters for a UTF-8 encoded [Unicode](TutorialUnicode.htm) string use the [ULEN8(](ULEN8(.htm) function.

The LEN( function can also be used in conjunction with the [STR(](STR(.htm) function to get the defined length of a string e.g.

DIM a\$32\
IF (LEN(STR(a\$))) \<\> 32 THEN PANIC

The LEN( numeric function can also determine the length of the substring defined by a [field variable](TutorialFields.htm). For example:

.fred\$ = (1,16)\
.value = (17,"-###.##)\
First = LEN(.fred\$)\
Second = LEN(.value)

The [POS(](POS(.htm) function may be used to return the starting position of a field variable and the [PACK(](PACKfn.htm) function can return the packing specifier.

Syntax examples:

Red = 100 + LEN(Actual\$)\
Green = LEN(.Field_Name\$)
