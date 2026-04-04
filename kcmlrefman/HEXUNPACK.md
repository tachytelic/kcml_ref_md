HEXUNPACK

------------------------------------------------------------------------

General Form:\
\
     HEXUNPACK alpha_variable1 TO alpha_variable2\
\

------------------------------------------------------------------------

The HEXUNPACK statement is used to convert the binary value of an alpha variable into an ASCII character string consisting of hexadecimal digits within the range 0-9, A-F. Each half-byte in alpha_variable1 is converted into a full byte in alpha_variable2, therefore alpha_variable2 should double the length of alpha\_ variable1.

If alpha_variable2 is too short to contain the entire converted value, then an error will result. If alpha_variable2 is longer than the converted value, then the remaining bytes are left unchanged.

Example:

DIM pa\$4, pb\$2\
pb\$ = HEX(6FC9)\
HEXUNPACK pb\$ TO pa\$\
PRINT pa\$\
 \
 6FC9

Syntax examples:

HEXUNPACK junk1\$ TO junk2\$\
HEXUNPACK point\$() TO table\$()\
HEXUNPACK STR(pot\$,1,4) TO STR(pan\$,10,8)

See also:

[HEXPACK](HEXPACK.htm)

 
