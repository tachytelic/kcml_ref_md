MAT IDN

------------------------------------------------------------------------

General Forms:\
\
1.      MAT numeric_receiver_array = IDN \[(dim1 \[,dim2\])\]\
\
2.      numeric_receiver_array = IDN \[(dim1 \[,dim2\])\]\
\

------------------------------------------------------------------------

The MAT identity statement sets the diagonal elements of the numeric receiver array to one and the non-diagonal elements to zero. An error will result if the receiver array is not a square matrix. The array may be explicity redimensioned by specifying the new dimensions, within parentheses, after the IDN keyword, e.g.

MAT B = IDN(15,15)

Example:

DIM matrix(3,3)\
MAT matrix = IDN\
PRINT matrix()

1      0      0\
0      1      0\
0      0      1

Syntax examples:

MAT fred = IDN\
fred() = IDN\
MAT alpha = IDN(9,9)\
beta()=IDN(first,second)

 
