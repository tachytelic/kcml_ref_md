NUM(

------------------------------------------------------------------------

General Form:\
\
     NUM(alpha_variable)\
\

------------------------------------------------------------------------

The NUM( function is used to determine the number of sequential ASCII characters in the specified alpha variable that form an acceptable number.

The characters considered to be numeric by the NUM( function are as follows:

     leading, trailing and embedded blanks\
     digits 0 to 9\
     decimal point (.)\
     minus, or plus sign\
     letters e or E (Exponential)

Syntax example:

new = NUM(FLD(file\$.number\$))

 
