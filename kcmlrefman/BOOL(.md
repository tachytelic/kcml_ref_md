BOOL(

------------------------------------------------------------------------

General Form:\
\
     BOOL(expression)\
\
\
Where expression = string expression or numeric expression\
\
\

------------------------------------------------------------------------

The BOOL( function may be used to replace a conditional expression.

If the argument is numeric, it converts the numeric expression to a Boolean expression with zero considered to be [FALSE](FALSE.htm) and non-zero considered to be [TRUE](TRUE.htm).

If the argument is a string then the first character is used; with 'Y', 'y', 'T', 't', or '1' reprsenting [TRUE](TRUE.htm); and 'N', 'n', 'F', 'f', and '0' representing [FALSE.](FALSE.htm)

Syntax examples:

flag=BOOL(new1)\
UNTIL BOOL(end_loop)\
flag = BOOL("Y")\
flag = BOOL("1")\
UNTIL BOOL(str\$)

See also:

[COND(](COND(.htm)
