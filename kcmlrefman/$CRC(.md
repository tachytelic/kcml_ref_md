\$CRC(

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = \$CRC(alpha_expression \[,alpha_expression2\])\
\

------------------------------------------------------------------------

This functions is used to calculate a 32 bit Cyclic Redundancy Check (CRC) for a string. Cyclic Redundancy Check (or CRC) functions are widely used for packet checksums in communications.

This function can only be used on the right hand side of an assignment statement and cannot be combined with other string operators such as ["&"](concat.htm), [AND](AND.htm), [OR](OR.htm), etc. Each byte of alpha_expression1 is examined in turn and combined into a running CRC value, which will then be copied into the alpha_receiver. The alpha_receiver must be at least four bytes long. Note that all bytes of alpha_expression1, including trailing blanks, are incorporated into the CRC. The start value is taken from the optional second alpha expression, which must be at least four bytes long. If not present then the conventional value of HEX(FFFFFFFF) will be used.

Syntax examples:

Check\$ = \$CRC(Main\$)\
Buffer\$ = \$CRC(MainBuffer\$, StartVal\$)
