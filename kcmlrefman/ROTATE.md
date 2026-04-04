ROTATE

------------------------------------------------------------------------

General Form:\
\
     ROTATE \[C\] (alpha_variable, numeric_expression)\
\
Where:\
\
     -8 \< numeric_expression \< 8\
\

------------------------------------------------------------------------

The ROTATE statement is used to rotate the bits of each byte in the alpha variable. All bytes of the alpha variable are operated on including trailing spaces.

The numeric expression specifies the number of bits to rotate. A positive expression signifies that the bits are to be rotated to the left. A negative expression signifies that the bits are to be rotated to the right.

If the optional C parameter is used, the entire value of the alpha variable is rotated by the specified number of bits.

Syntax examples:

ROTATE(test\$,4)\
ROTATE(test\$(9),bits)\
ROTATEC(bytes\$, -2)

 
