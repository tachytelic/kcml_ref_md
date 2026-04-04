MAT READ

------------------------------------------------------------------------

General Forms:\
\
1.      MAT READ array_name \[(dim1 \[,dim2\])\[length\]\] \[, ...\]\
\
2.      READ array_name \[(dim1 \[,dim2\])\[length\]\] \[, ...\]\
\
Where:\
\
     array_name           = an alpha, numeric or field variable or array.\
\

------------------------------------------------------------------------

The MAT READ statement is used to assign values contained in [DATA](DATA.htm) statements to the specified arrays which may be explicitly redimensioned.

Arrays are assigned on a row-by-row basis, working from left to right within each array. The data is read from the first [DATA](DATA.htm) statement found in the program, unless the [RESTORE](RESTORE.htm) statement specifies a different line data. An error will occur is there is insufficient data to satisfy the specified arrays. An error will also occur if the value to be transferred does not match the variable type required by the arrays.

Example:

DIM array(2,2),string\$(2)7\
READ array(), string\$()\
MAT PRINT array(),string\$()\
DATA 1,2,3,4,"hello","goodbye"\
\
 1           2\
 3           4\
 hello\
 goodbye

Syntax examples:

MAT READ values(), more()\
READ paint\$(), temp()

See also:

[READ](READ.htm)

 
