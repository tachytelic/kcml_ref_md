PACK

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/pack.gif" data-align="BOTTOM" data-border="0" alt="pack.gif" />\
\
Where:\
<img src="bitmaps/pack1.gif" data-align="BOTTOM" data-border="0" alt="pack1.gif" />\
\

------------------------------------------------------------------------

The PACK statement is used to store a list of numeric values in an alphanumeric variable in packed decimal format using the format specified by the image.

The image consists of \`#' characters to signify a single digit, and optionally, plus signs, minus signs, decimal points, and up arrows may be used to specify sign, decimal point position, and exponential format. Embedded commas are ignored. The image can either be fixed point \`###.##' or exponential \`#.###^^^^'. Values are packed as follows:

The PACK statement packs two numeric digits per byte, each digit relates to one \`#' character in the image.

Data is left justified within the alpha variable.

If leading or trailing plus or minus signs are specified, PACK will place them in the high-order half-byte, followed by the packed number. If specified, the exponent occupies the low order half-bytes. The sign of the number or exponent is represented by a single hex digit. This may contain the following values:

0      if both the number and the exponent are positive\
1      if the number is negative and the exponent is positive\
8      if the number is positive and the exponent is negative\
9      if both the number and exponent are negative

The decimal point is not stored during PACK operations, but must be specified when the variable is [UNPACKed](UNPACK.htm).

Fixed point values are truncated or extended with zeros to match the image specification if required.

The packed value always requires a whole number of bytes, even if the image specifies that a fraction is to be used. The table below gives a few examples of the number of bytes used by certain images.

Examples of bytes used by PACK for certain images.

| **PACK image** | **Bytes** |
|----------------|-----------|
| \#             | 1         |
| \###           | 2         |
| \##.##         | 2         |
| -####.##       | 4         |
| \##.##^^^^     | 3         |

\
Syntax examples:

PACK(###.###) file\$ FROM total\
PACK(+###.####) FLD(record\$.cost\$) FROM cost/2\
PACK(form\$) file\$ FROM price()
