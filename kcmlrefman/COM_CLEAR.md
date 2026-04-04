COM CLEAR

------------------------------------------------------------------------

General Form:\
\
     COM CLEAR \[ variable_name \]\
\
Where:\
\
     variable_name      =      an alpha or numeric variable\
\

------------------------------------------------------------------------

The COM CLEAR statement is used to define all or some of the previously defined common variables to non-common variables. The dimensions and contents of the variables are left unchanged.

If no variable names are specified then all currently defined common variables are re-defined as non-common variables. If a common variable name is specified then that variable and all of the common variables defined after it in the current program are changed to non-common variables. Only variables that have previously been defined with a [COM](COM.htm) or [DIM](DIM.htm) statement may be cleared.

If a non-common variable name is specified, then all non-common variables defined prior to the specified variable become common variables.

Examples:

COM CLEAR: LOAD "PRG-1"

This would re-define all previously defined common variables to non-common variables. The effect of this is that when the program \`PRG-1' is loaded all previously defined variables, whether they were common or non-common are lost.

COM one, two, three, four(100), five(10)\
six, seven = value_1\
     .           .\
COM CLEAR three

This would re-define three, four, five as non-common; one and two would remain common. If on line 9000 the variable three was replaced with the variable seven then six and seven would be re-defined as common, value_1 would remain non-common, and all the variables on line 750 would remain common.

See also:

[COM](COM.htm), [DIM](DIM.htm)

 
