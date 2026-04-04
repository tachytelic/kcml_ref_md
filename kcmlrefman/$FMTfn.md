\$FMT(

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = \$FMT(format\$, num_expr1 \[,num_expr2\] ...)\
\

------------------------------------------------------------------------

This function is used to convert values into formatted output directly into the receiver variable. The specified format determines how the values are placed into the receiver variable. For more information about the avilable formats refer to the [PRINTUSING](PRINTUSING.htm) statement.

Note that only one \$FMT( function can be used per statement otherwise the second will overwrite the first.

Examples:

.Edit1.Text\$ = \$FMT("-###.##", value)\
Buffer\$ = \$FMT(" -######.### ", Value1, Value2, Value3)

See Also:

[PRINTUSING](PRINTUSING.htm)
