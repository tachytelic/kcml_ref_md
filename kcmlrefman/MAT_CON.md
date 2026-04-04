MAT CON

------------------------------------------------------------------------

General Forms:\
\
1.      MAT numeric_receiver_array = CON \[(dim1 \[,dim2\])\]\
\
2.      numeric_receiver_array = CON \[(dim1 \[,dim2\])\]\
\

------------------------------------------------------------------------

The MAT CON statement is used to set all elements of the numeric receiver array to one. The array may be explicity redimensioned by specifying the new dimensions, within parentheses, after the CON keyword, e.g.

MAT B = CON(15,15)

Example:

DIM test(2,2)\
test() = CON\
MATPRINT test()

1      1\
1      1

Syntax examples:

MAT a1 = CON(90,9)\
MAT test = CON\
last()= CON\
first() = CON(second,third)

 
