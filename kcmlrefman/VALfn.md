VAL(

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/val.gif" data-align="BOTTOM" data-border="0" alt="val.gif" />\
\
Where:

digit = a numeric expression

------------------------------------------------------------------------

The VAL( numeric function is used to return a numeric value from a binary value contained in an alphanumeric argument. The second argument specifies the the number of bytes to be converted. This argument must calculate to a number ranging from -6 to +6, otherwise an error will result. Only the integer portion of this argument is used. If this digit is negative then the binary value is considered to be signed in the two's complement convention. The VAL( function is valid wherever a numeric function is legal. The VAL( function is the inverse of the [BIN(](BIN(.htm) function.

Though 6 byte strings are allowed you should be aware that the maximum number that this implies, 0xFFFFFFFFFFFF or 281474976710655, has 15 digits and exceeds the 13 digit maximum precision of KCML numbers. To avoid problems with precision you should restrict yourself to either 5 bytes or use 6 bytes only if you are sure the decimal number will not exceed approx 1.0E13 or 0x08FFFFFFFFFF say.

Syntax examples:

test = VAL(alpha\$(1))\
test1 = VAL("ABC",3)\
test1 = VAL(array\$(2),-3)\
IF (VAL(temp\$,6) \> test(count))

See also:

[BIN(](BIN(.htm)
