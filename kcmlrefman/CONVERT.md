CONVERT

------------------------------------------------------------------------

\
General Forms :\
\
1.      CONVERT alpha_variable TO numeric_receiver\
\
2.      CONVERT numeric_expression TO alpha_receiver, (picture)\
\
Where:\
     <img src="bitmaps/convert.gif" data-align="BOTTOM" data-border="0" alt="convert.gif" />\
\

------------------------------------------------------------------------

The CONVERT statement is used to convert an alpha variable to a numeric receiver or a numeric value to an alpha receiver string.

Alpha variable to numeric receiver

This first form of the CONVERT statement converts the contents of an alpha variable to a numeric receiver. The contents of the alpha variable must be a valid ASCII representation of a number, otherwise a recoverable error will occur.

Example:

CONVERT total\$ TO new_total

Numeric expression to Alpha receiver

The second form of the CONVERT statement converts a numeric expression into an alpha receiver in the format specified by the picture.

The picture specifies exactly how the numeric value is to be converted. Each character in the picture corresponds to a character in the resulting alpha receiver. The picture is made of digit selector characters \`#' to signify a single digit, optional plus signs \`+, ++', minus signs \`-, --', decimal points \`.', and exponent signs \`^' are used to specify sign, decimal point position, and exponential format. The picture can be put into two separate classifications, fixed point \`###.##' and exponential \`#.##^^^^'. The picture formats the numeric values based on the following rules:

- If the picture starts or ends with a minus \`-' sign, CONVERT will only generate a sign for negative values, a blank is inserted for positive values.
- If the picture starts or ends with a \`+' sign, the real sign of the value is generated.
- If no sign is specified then the absolute value of the expression is converted and no sign is added into the character string.
- If the picture ends with two plus signs \`++' or two minus signs \`--', then the characters \`CR' (Credit) or \`DB' (Debit), respectively, will be appended to the end of the alpha receiver for negative values only. For positive values two spaces will be appended.
- If the picture contains a decimal point \`.', a comma \`,' or a dollar sign \`\$', the characters will then be converted into the corresponding positions in the alpha receiver.
- If the picture is exponential, i.e. when four exponent signs are used (^^^^), then the numeric value is converted into the alpha receiver in exponential format. The format is expressed as \`E+nn' where nn is the exponent.

Example:

field = 13579.2468\
CONVERT field TO total1\$,(#####.#####)\
.Edit1.text\$ = total1\$

Syntax examples:

CONVERT 159.9 TO tmp\$,(###.##)\
CONVERT tap\$ TO new_number\
CONVERT STR(actual\$,4,6) TO new_number\
CONVERT old TO balance\$,(\$###,###.###--)\
CONVERT old TO FLD(record\$.entry\$),(picture1\$)

 
