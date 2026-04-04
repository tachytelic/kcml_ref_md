RND(

------------------------------------------------------------------------

General Form:\
\
     RND(numeric_expression)\
\

------------------------------------------------------------------------

The RND( function generates a random number between 0 and 1. The RND( function is valid wherever a numeric expression is valid.

If the numeric expression is zero, the RND( function returns the first value in the random number list. A non-zero number returns the next number in the list.

Using zero as the numeric expression at the beginning of a program ensures that the same sequence of random numbers are generated each time the program is executed.

Syntax examples:

IF (RND(0) \<\> old)\
temp = INT(RND(1) \* 1000)

 
