LTRIM(

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = LTRIM(alpha_expression \[, char\$\])\
\
Where:\
\
     char\$           = an alpha expression specifying the character toi be trimmed.\
\

------------------------------------------------------------------------

This function is used to trim off leading blanks from the left hand side of the string alpha expression. The optional char\$ can specify an alternative character to trim.

Syntax Examples:

FLD(Record\$.Result\$) = LTRIM(Buffer\$)\
Size = WRITE \#1, LTRIM(Buffer\$, HEX(FF))

 
