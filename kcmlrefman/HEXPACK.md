HEXPACK

------------------------------------------------------------------------

General Form:\
\
     HEXPACK alpha_variable1 FROM alpha_variable2\
\

------------------------------------------------------------------------

The HEXPACK statement is used to convert an ASCII character string of hexadecimal digits into their binary equivalent. Each pair of ASCII characters in alpha variable2 is converted into a single character and is stored into alpha_variable1. The characters in the alpha variable2 must be valid hexadecimal digits within the range 0-9 and A-F. Any trailing spaces in alpha_variable2 are ignored.

Alpha_variable1 should in theory be half the size of alpha_variable2 as each pair of digits is converted into a single character. If alpha_variable1 is too short to contain the entire converted value, then an error will result. If alpha_variable1 is longer than the converted value, then the remaining bytes are left unchanged.

Syntax examples:

HEXPACK junk1\$ FROM junk2\$\
HEXPACK point\$() FROM table\$()\
HEXPACK STR(pot\$,1,4) FROM STR(pan\$,10,8)

See also:

[HEXUNPACK](HEXUNPACK.htm)

 
