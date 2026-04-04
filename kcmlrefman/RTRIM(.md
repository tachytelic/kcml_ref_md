RTRIM(

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = RTRIM(alpha_expression \[, char\$\])\
\
Where:\
\
     char\$           = an alpha expression specifying the character to be trimmed.\
\

------------------------------------------------------------------------

This function is used to trim off trailing blanks from the right hand side of the string alpha expression. The optional char\$ can specify an alternative character to trim.

Syntax Examples:

FLD(Record\$.Result\$) = RTRIM(Buffer\$)\
Size = WRITE \#1, RTRIM(Buffer\$, HEX(FF))
