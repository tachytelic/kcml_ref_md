PRINT \#

------------------------------------------------------------------------

General form:\
\
     PRINT \#stream \[, variable\] ...\
\
Where:\
\
     stream           = a valid stream number \< 255\
\

------------------------------------------------------------------------

The PRINT \# statement directs normal [PRINT](PRINT.htm) output to the specified data stream. The stream must have a file [OPEN](OPENhash.htm)ed otherwise an error will occur. Stream zero is considered to be the screen, and will allow normal [PRINT](PRINT.htm) operations to be performed. Other streams will ignore PRINT operations such as AT(, BOX(, and TAB(.

Under Unix the end of line character HEX(0D) will automatically be translated to a line feed character (HEX(0A)). Under DOS/Windows the end of line character will automatically be translated to a HEX(0D0A).
