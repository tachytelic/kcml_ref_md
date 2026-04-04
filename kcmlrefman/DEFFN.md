DEFFN <span style="font-size: 16pt ; ">define function</span>

------------------------------------------------------------------------

General Form:\
\
     DEFFNdesc(numeric_scalar_var) = expression\
\
Where:\
     desc           = an alphanumeric description or a single numeric digit\
                    that identifies the function.\
\

------------------------------------------------------------------------

The DEFFN (define function) statement is used to define a function from within a program, which can later be called with the [FN](FN.htm) function from within a numeric expression.

Each function is identified with either a single numeric digit (0-9) or a combination of alphanumeric characters. As with normal variable names, if the function name consists of several alphanumeric characters, then the first character must be an alpha character. Each function must include a single numeric expression which is performed when the [FN](FN.htm) function is called. The numeric scalar variable is used only to pass a value from the [FN](FN.htm) function into the numeric expression. The contents of the scalar variable are not altered by the DEFFN function.

The DEFFN function can appear anywhere in the program without affecting the program flow. If more than one definition appears for the same function name, the definition which appears first in the program will be used.

The currently selected global partition, if any, is always searched before the foreground partition unless the environment variable KEEPSHARED is set, then the foreground partition is searched before the global.

Syntax Example:

DEFFN area(radius) = \#PI \* radius ^ 2

See also:

[FN](FN.htm)

 
