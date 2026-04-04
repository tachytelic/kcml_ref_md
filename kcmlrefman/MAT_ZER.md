MAT ZER

------------------------------------------------------------------------

General Forms:\
\
1.      MAT numeric_receiver_array = ZER \[(dim1 \[,dim2\])\]\
\
2.      numeric_receiver_array = ZER \[(dim1 \[,dim2\])\]\
\

------------------------------------------------------------------------

The MAT ZER statement is used to set all elements of the numeric receiver array to zero. The array may be explicity redimensioned by specifying the new dimensions, within parentheses, after the ZER keyword, e.g.

MAT B = ZER(15,15)

Example:

DIM test(2,2)\
test() = ZER\
MATPRINT test()\
\
 0           0\
 0           0

Syntax examples:

MAT a1 = ZER(90,9)\
MAT test = ZER\
last()= ZER\
first() = ZER(second,third)

See also:

[MAT REDIM](MAT_REDIM.htm),

 
