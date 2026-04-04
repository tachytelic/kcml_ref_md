MAT <span style="font-size: 16pt ; ">subtraction</span>

------------------------------------------------------------------------

General Forms:\
\
1.      MAT numeric_receiver_array = numeric_array2 - numeric_array3\
\
2.      numeric_receiver_array = numeric_array2 - numeric_array3\
\

------------------------------------------------------------------------

The MAT subtraction statement subtracts the contents of two numeric arrays of the same dimensions. The sum is then stored into the numeric receiver array. The dimensions of the receiver array are automatically adjusted to agree with the dimensions of the arrays on the right hand side.

Example:

DIM array1(5),array2(5),array3(5)\
FOR count = 1 TO 5\
     array2(count) = count\
     array3(count) = 10 - count\
NEXT count\
array1() = array2() - array3()\
MAT PRINT array1()\
\
-8\
-6\
-4\
-2\
 0

Syntax examples:

MAT z1 = y1-x1\
first() = second() - third()

 
