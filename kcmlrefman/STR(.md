STR(

------------------------------------------------------------------------

General Form:\
\
     STR(alpha_expression\[,\[start\]\[,length\] \] )\
\
Where:\
\
     start           = a numeric expression specifying the location of a substring within the\
                alpha variable.\
\
     length           = a numeric expression specifying the length of the substring.\
\

------------------------------------------------------------------------

The STR( alphanumeric function is used to define a substring of an alpha expression. STR( allows the entire alpha variable or just a portion of the variable to be examined or modified. The STR( function is valid wherever an alpha variable is legal.

If the start parameter is omitted, a default start position of 1 is assumed.

If the length parameter is omitted, the remainder of the alpha variable is used, including trailing spaces.

If both parameters are omitted, then the entire alpha variable will be used. The expression [LEN(](LEN(.htm)[STR(](STR(.htm)variable\$)) is an easy way to discover the defined length of the string variable\$.

The STR( function may be used on either side of the equals sign in an assignment statement. If STR( is used on the left hand side of the equals sign and the value received is shorter than the specified substring, the substring is padded with trailing spaces.

The [FLD(](FLD(.htm) function can be used instead of STR( to not only improve readability, but in most circumstances [FLD(](FLD(.htm) will execute quicker..

Syntax examples:

STR(area\$,,1) = HEX(02)\
STR(temp\$,2) = ALL(HEX(FF))\
STR(test\$, count, 10) = STR(object\$, count, 10)\
IF (STR(average\$,,1) == HEX(FF))

See also:

[FLD(](FLD(.htm)
