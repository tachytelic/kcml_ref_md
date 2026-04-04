\$NICE(

------------------------------------------------------------------------

General Form:\
\
     numeric_receiver = \$NICE(numeric_expression)\
\

------------------------------------------------------------------------

The \$NICE( function allows programs to reduce their scheduling priority, by increasing the Unix nice factor. The normal value is 20 but it can be increased to 40 (corresponding to the lowest priority). Only the superuser can decrease the nice factor. Child processes inherit the nice factor of their parent.

If the \$NICE( function fails, the receiver variable will be set to -1. Specifying a nice factor of zero causes the \$NICE( function to return the current value in the receiver variable.

Compatibility notes:

This function is ignored by Windows versions of KCML.

Syntax examples:

old_nice = \$NICE(5)\
PRINT \$NICE(0)

 
