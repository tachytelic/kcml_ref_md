READ

------------------------------------------------------------------------

General Form:\
\
     READ variable \[, variable\] ...\
\
Where:\
\
     variable           = alpha, numeric or field variable or array\
\

------------------------------------------------------------------------

The READ statement is used, in conjunction with the [DATA](DATA.htm) statement, to assign alpha numeric or field values to alphanumeric or field variables. The READ statement sequentially searches the program for a [DATA](DATA.htm) statement, the values held in the [DATA](DATA.htm) statement are then sequentially assigned to the variables in the READ statement. The assignment process continues until all variables in the READ statement have been satisfied. The types of variables in the READ variable list must match the types of data in the [DATA](DATA.htm) statement (alpha to alpha, numeric to numeric, field to field).

If the READ statement contains more variables than there is data in the [DATA](DATA.htm) statement, the system searches sequentially through the program for another [DATA](DATA.htm) statement to continue assigning variables. If the READ statement contains fewer variables than there is data in the [DATA](DATA.htm) statement, the next READ statement continues at the first unused value in the [DATA](DATA.htm) statement.

Data values may be re-used by resetting the pointer with the [RESTORE](RESTORE.htm) statement.

Example:

READ abc, def, abc\$, def\$\
PRINT abc, def, abc\$, def\$\
DATA 120.10, 1000, "HELLO!", "GOODBYE!"\
 \
 120.10           1000           HELLO!           GOODBYE!

Syntax examples:

READ act(1), temp(count), test\$(4)\
READ apple\$(), file\$()

See also:

[DATA](DATA.htm), [RESTORE](RESTORE.htm), [MAT READ](MAT_READ.htm)

 
