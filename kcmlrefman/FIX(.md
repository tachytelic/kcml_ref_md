FIX(

------------------------------------------------------------------------

General Form:\
\
     FIX(numeric_expression)\
\

------------------------------------------------------------------------

The FIX( function returns the integer portion of the numeric expression. FIX( always truncates towards zero (while the [INT(](INT(.htm) function always truncates down). FIX( is valid wherever a numeric function is legal.

Syntax examples:

Test = FIX(190.723\*2)\
Total = 17+FIX(ABS(temp))

 
