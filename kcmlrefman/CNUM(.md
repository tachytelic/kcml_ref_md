CNUM(

------------------------------------------------------------------------

General Form:\
\
     CNUM(string_expression)\
\

------------------------------------------------------------------------

The function take the string argument and returns a KCML numeric. It supports integer numbers, floating point numbers, and numbers containing exponentials. Decoding stops with the first non-numeric character so the string does not have to be space filled.

Note: At present this routine will only use the first 32 characters of a string to perform the conversion on.

Syntax examples:

ret = CNUM("1234")\
ret = CNUM("1234.1234")\
ret = CNUM("-1234")\
ret = CNUM("12e2")

See also:

[CONVERT](CONVERT.htm)
