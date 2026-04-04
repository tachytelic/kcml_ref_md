BIN(

------------------------------------------------------------------------

General Form:

alpha_receiver = ... BIN(numeric_expression \[,bytes\]) ...

Where:

bytes = an integer numeric expression between -6 and +6

------------------------------------------------------------------------

The BIN (binary) function is used to convert the integer value of a numeric expression into a binary value. The number of bytes in the binary value is specified by the second argument. If the second argument is omitted, a length of one byte is assumed. The BIN( function can only be used in the alpha expression portion of an alpha numeric assignment statement. BIN( is particularly useful for conversions of numbers that are stored in internal binary format to binary. Only ten BIN( functions may be used per statement.

The second argument of the BIN( function is used to specify the length, type and content of the resultant character string. This argument must calculate to a number ranging from -6 to +6, otherwise an error will occur. Only the integer portion of the argument is used. If the second argument is negative then signed two's complement binary is assumed.

Though 6 byte strings are allowed you should be aware that the maximum number that this implies, 0xFFFFFFFFFFFF or 281474976710655, has 15 digits and exceeds the 13 digit maximum precision of KCML numbers. To avoid problems with precision you should restrict yourself to either 5 bytes or use 6 bytes only if you are sure the decimal number will not exceed approx 1.0E13 or 0x08FFFFFFFFFF say.

Syntax examples:

care\$ = BIN(variable1\*4,3)\
string\$ = BIN(character1,-apple1)

See also:

[VAL(](VALfn.htm)
