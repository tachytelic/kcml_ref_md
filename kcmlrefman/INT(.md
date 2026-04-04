INT(

------------------------------------------------------------------------

General Form:\
\
     INT(numeric_expression)\
\

------------------------------------------------------------------------

The INT( function returns the integer portion of a numeric expression. For integer values, the INT( of the value is identical to the original. For non-integer values, INT( will return the greatest integer that is less than the original value. With negative numbers INT( always truncates down whereas [<u><span style="color: #00ff00; ">FIX(</span></u>](FIX(.htm) truncates towards zero.

Syntax examples:

Texting = 100 + INT(12 \* Variable)\
Random = INT(RND(1)\*10000)

 
