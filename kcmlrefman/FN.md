FN

------------------------------------------------------------------------

General Form:\
\
     FN desc (numeric_expression)\
\
Where:\
\
     desc           = an alphanumeric description or a single numeric digit\
                         that identifies the function.\
\

------------------------------------------------------------------------

The FN function is used to invoke functions defined by the [DEFFN](DEFFN.htm) function definition statement. The FN function is valid wherever a numeric function is legal.

FN is used in conjunction with the [DEFFN](DEFFN.htm) statement. If more than one definition appears with the same function name, the definition which appears first in the program will be used.

The FN function can also be used within a [DEFFN](DEFFN.htm) statement, e.g.

DEFFN position(X) = FN 1(X) + 2 \* FN has(X)

Syntax examples:

start1 = FN 1(45 \* act) + FN 2(45)

See also:

[DEFFN](DEFFN.htm)

 
