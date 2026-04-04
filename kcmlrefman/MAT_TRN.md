MAT TRN

------------------------------------------------------------------------

General Forms:\
\
1.      MAT numeric_receiver_array = TRN(numeric_array)\
\
2.      numeric_receiver_array = TRN(numeric_array)\
\

------------------------------------------------------------------------

The MAT transposition statement is used to place the transpose of the second numeric array into the receiver array.

The transposition operation takes place element by element. For example, the contents of element(4,5) in the second numeric array will be placed into element (5,4) in the receiver array.

The dimensions of the two arrays must agree, the first dimension of the receiver array should be the same as the second dimension of the second numeric array and visa versa.     

Example:

DIM array1(3,3),array2(3,3)\
MAT INPUT array2()\
array1() = TRN(array2())\
MAT PRINT array1()\
\
 ? 2, 5, 7, 2, 1, 9, 7, 3, 4\
 2      2      7\
 5      1      3\
 7      9      4

Syntax examples:

MAT temp() = TRN(next_array())\
first() = TRN(second())

 
