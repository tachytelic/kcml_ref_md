MAT <span style="font-size: 16pt ; ">multiplication</span>

------------------------------------------------------------------------

General Forms:\
<img src="bitmaps/matmultiply.gif" data-align="BOTTOM" data-border="0" alt="matmultiply.gif" />\
<img src="bitmaps/matmultiply1.gif" data-align="BOTTOM" data-border="0" alt="matmultiply1.gif" />\
\

------------------------------------------------------------------------

The MAT multiplication statement multiplies the contents of numeric_array2 with either numeric_array1 or any scalar numeric expression. The result is stored into the receiver variable. If a scalar numeric expression is used it must be enclosed in parentheses. Matrices must have compatible dimensions, that is for scalar multiplication the dimensions of the receiver array must match those of numeric_array2. For matrix multiplications the number of rows in numeric_array2 must agree with the number of columns in numeric_array1, the number of rows in the receiver array must be the same as the number of rows in numeric_array1 and the number of columns in the receiver should be the same as the number of columns in numeric_array2.

Example:

DIM array1(2),array3(2)\
array3(1) = 5\
array3(2) = 10\
array1() = (100) \* array3()\
PRINT array1()\
\
 500\
 1000

Syntax examples:

MAT one = two \* three\
new() = first() \* second()\
new() = (old(there)) \* first()
