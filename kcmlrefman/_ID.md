\#ID <span style="font-size: 16pt ; ">function</span>

------------------------------------------------------------------------

General Form:\
\
     \#ID\
\

------------------------------------------------------------------------

The \#ID function returns a number ranging from 1-65535 that is specific to each KCML installation. On DOS versions the value returned by the \#ID function is taken from the Network Interface Card address (NIC). On all other versions the value returned by \#ID will be the same as the value returned by the [\#GOLDKEY](_GOLDKEY.htm) function. In all cases \#ID can be changed by setting the KCML_ID environment variable to an appropriate value. \#ID is valid wherever a numeric expression is valid.

Syntax example:

number = \#ID

See also:

[\#GOLDKEY](_GOLDKEY.htm)

 
