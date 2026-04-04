\$PRINTF(

------------------------------------------------------------------------

General Form:\
\
     alpha_receiver = \$PRINTF(format\$, expr1 \[,expr2\] ...)\
\

------------------------------------------------------------------------

The specified format determines how the strings and values are placed into the receiver variable.

\$PRINTF can be used as a function anywhere a string expression is allowed, including as an argument in a function call. However it uses a small number of internally allocated memory buffers to hold the result string (16 in KCML 6.20) so there is a possibility of reuse of a buffer in deep recursion or in generated code that uses many \$PRINTF expressions on the same statement.

The format

The format string contains two types of characters, ordinary characters, which are copied to the output, and conversion specifications, each of which causes conversion and output of the next sucessive argument to \$PRINTF, except for the special "\$" specifier, which allows you to choose the [position](#posit) of a particular argument number.

Each conversion specification begins with the character "%" and ends with a conversion character. Between the "%" and the conversion character there may be, in order

| Element | Description |
|----|----|
| n\$ | Optional argument specifier. This will convert argument n |
| \- | Left adjustment of the converted argument in its field |
| field width | The minimum field width. Converted argument will be padded with blanks if necessary |
| . | A period to separate the field width from the precision |
| Precision | Maximum number of characters for a string, or the number of digits after the decimal point for numbers |

The conversion characters

| Conversion characters | Argument type | Purpose |
|----|----|----|
| s | String | Inserts argument as a string, trailing spaces are stripped |
| S | String | Inserts argument as a string, traing spaces are not stripped |
| d | Numeric/Integer | Argument will be inserted as a 32-bit decimal integer with no rounding. |
| ld | Numeric/Integer | Argument will be inserted as a large decimal integer with no rounding. |
| x | Integer | Value will be inserted as a hexadecimal (base 16) integer. |
| f | Numeric | Value will be inserted as a floating point number, no exponent. |
| g | Numeric | Value will be inserted as a floating point number with an exponent if necessary. |
| % | None | Literal percent sign |

Escape characters

The \$PRINTF statement also provides escape characters

| Escape Character | Purpose                                 | Character value |
|------------------|-----------------------------------------|-----------------|
| "\a"             | Bell or alarm                           | HEX(07)         |
| "\b"             | Backspace                               | HEX(08)         |
| "\n"             | New line                                | HEX(0D)         |
| "\t"             | Tab                                     | HEX(09)         |
| "\\"             | Literal single quote                    |                 |
| "\\"             | Literal backslash                       |                 |
| "\\"             | Literal question mark                   |                 |
| "\xNN"           | ASCII character in hexadecimal notation | HEX(NN)         |
| "\NNN"           | ASCII character in octal notation       | 0NNN            |

If the escape character is not recognized then the character itself is output. For example "\x" will produce an x in the output.

Formatting numbers and strings

The %x format expects an integer argument, and will output the hexadecimal equivalent. For example, an argument of 10, will return the hex equivalent "a", and an argument of 16 will return "10". It is also possible to specify %X to get the output in capitals, so an argument of 10 to %X will return "A".

Floating point numbers can be converted using either %f or %g. The default behavior for the %f notation is to represent the value to 6 decimal places. The %g format is more flexible as it will only convert as many characters that are necessary to accurately represent the value. The %g format will also use scientific notation, with an exponent, for very large or small floating point numbers.

Both the %f and %g formats allow a floating point number to be displayed to a specified number of digits. This is achieved by using the **.precision** element in the format string.

Examples:

a\$ = \$PRINTF("Distance to the nearest star is %g km", 4.2 \* 2.9979e5 \* 365 \* 24 \* 60 \* 60)\
a\$ = \$PRINTF("Distance to the nearest star is %f km", 4.2 \* 2.9979e5 \* 365 \* 24 \* 60 \* 60)\
a\$ = \$PRINTF("Pi to three decimal places is %.3f", \#PI)\
survey_result\$ = \$PRINTF("Survey showed that %.1f%% preferred %s to %s.", 100\*votes/samplesize, brand_A\$, brand_B\$)\
Buffer\$ = \$PRINTF("%d in hex is %x", value, value)

A format string may also contain a **field width**. This allocates a specified amout of room in the output string. If the converted argument does not fill the field width then the remainder is padded with blanks. By default, a converted argument is right-hand justified, so any padding will precede the converted argument. Left-hand justfication can be achieved by specifying a negative field width. In this case any padding will come after the converted argument. For example:

Buffer\$ = \$PRINTF("%10d boxes of %10s will cost %10d", Value1, strvalue\$, Value3)\
Buffer\$ = \$PRINTF("%-10d boxes of %-10s will cost %-10s", Value1, strvalue\$, Value3)

Note that there is no way of specifying the **maximum** number of characters to use for a numeric argument, only the **minimum** total field width.

Positional Arguments

Normally \$PRINTF will sequentially process one argument after the next. However, a format string can also contain an explicit reference to a specific argument. To convert argument n the format string should contain a n\$ element. For example:

a\$ = \$PRINTF("Price of %1\$d %2\$s is %3\$d", numitems, item\$, total)\
a\$ = \$PRINTF("%3\$d is the total price of %1\$d %2\$s.d", numitems, item\$, total)

One of the most important use of positional arguments is for multi-lingual strings where the ordering is different for each language. Note that the same argument may be referenced more than once. The first examples can be more efficiently written:

a\$ = \$PRINTF("Distance to the nearest star is %1\$g km\nDistance to the nearest star is %1\$f km"", 4.2 \* 2.9979e5 \* 365 \* 24 \* 60 \* 60)\
Buffer\$ = \$PRINTF("%1\$d in hex is %1\$x", value)

See Also:

[\$FMT]($FMTfn.htm)
