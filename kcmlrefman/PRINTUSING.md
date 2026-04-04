PRINTUSING

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/printusing.gif" data-align="BOTTOM" data-border="0" alt="printusing.gif" />\
\
Where:\
<img src="bitmaps/printusing1.gif" data-align="BOTTOM" data-border="0" alt="printusing1.gif" />\
<img src="bitmaps/printusing2.gif" data-align="BOTTOM" data-border="0" alt="printusing2.gif" />\
\

------------------------------------------------------------------------

The statement is used to print data in the specified format on the currently selected output device. If a stream number is specified then the ouput is written to the file currently open on the that stream.

The image specification defines the format of the output on the print line. The image specification may be specified by an alpha variable, by referencing the line number of an [% (Image)](image.htm), or [\$IMAGE]($IMAGE.htm) statement, or by specifying a literal string, for example:

Using a variable:

image\$ = "####.###"\
PRINTUSING image\$, price

Using an [% (Image)](image.htm) statement:

00100 % \####.###\
00110 PRINTUSING 100, price

Using the [\$IMAGE]($IMAGE.htm) statement (required for multi-language support):

00100 \$IMAGE \<\<"£####.###", "####.###FF"\>\>\
00110 PRINTUSING 100, price

Using a literal string:

PRINTUSING "####.###", price

The image specification can contain one or more \# characters to determine the location of a formatted variable. The following symbols may be included in the format specification: dollar sign \`\$', plus signs \`+, ++', minus signs \`-,--', and up arrows \`^'. The integer portion of a numeric format may include commas \`,' before the decimal point \`.'. An image statement may also include other printable characters before and after the format specifications. If a colon is used within an image statement, it will be interpreted as part of the image and not a statement separator.

Numeric print elements

Numeric data can be formatted in either, integer format \`###', fixed point format \`###.###', or exponential format \`##.#^^^^'. The image controls the formatted output of numeric values as follows:

1.  When using the integer format, the integer portion of the value is entered into the print line, and the decimal portion is truncated if specified. If the value is smaller than the image, the value will is padded with leading spaces. If the value is larger than the image, the image is printed in place of the value.
2.  When using the fixed point format, both the integer and the decimal part of the value are entered into the print line. If the integer part of the value is smaller than the image, the value is padded with leading spaces. If the value is larger than the image, the image is printed in place of the value. The decimal portion of the value is truncated or padded with leading zeros to fit the image.
3.  When using the exponential format the exponent is entered into the print line in the form \`E+ee' where \`ee' are the exponential digits. If the value is larger than the image, the image is printed in place of the value.
4.  If the image starts or ends with a plus sign, if the value is positive the sign is edited into the start or end of the print line previous to the first significant digit or after the last. If the value is negative then a minus sign is edited into the start or end of the print line previous to the first significant digit or after the last.
5.  If the image starts or ends with a minus sign, or if the value is negative the sign is edited into start or end of the print line previous to the first significant digit or after the last. If the value is positive then a blank is edited into the start or end of the print line previous to the first significant digit or after the last.
6.  If the image ends with two plus \`++' or minus \`--' signs a \`CR' (Credit) or \`DR' (Debit) will be appended to the end of the output for any negative values. Positive values end with two spaces.
7.  If the image contains a dollar sign \`\$', the dollar sign will be edited into the print line immediately before the first significant digit, and after the sign of the value.
8.  If the image contains commas or a decimal point, the character will be entered into to the print line.

Example:

price = 11123.46: quantity = 47\
PRINTUSING 120, price, quantity\
% -\$###,###.## \###\
 \
     \$11,123.46      47

Alphanumeric print elements

Each image character is replaced by a character from the alpha value. The alpha character string is left justified in the format field. If the alpha string is larger than the image then the string is right truncated. If it is smaller it will be extended with trailing spaces.

Example:

price = 11123.46\
quantity = 47\
code\$ = "ABCDEF"\
PRINTUSING 120, price, quantity, code\$\
% -\$###,###.## \###      \######\
 \
     \$11,123.46      47 ABCDEF

Suppression of Carriage Returns

The carriage return character (HEX(0D)) is usually issued at the end of a print line when all print elements are satisfied or all image specifications have been used. The semi-colon can be used to replace the comma at the point where a carriage return would normally be issued, to separate each print element to suppress the printing of a carriage return. When execution of the PRINTUSING statement is complete, PRINTUSING usually generates a carriage return. This can also be suppressed by appending a semi-colon after the last print element.

Alternative currency support

The [\$CONVERT]($CONVERT.htm) function is used to specify two currency names and a conversion rate to convert between them. The specified rate can then be used with [PRINTUSING](PRINTUSING.htm) to allow reports to dynamically switch the value of currency fields. It is also used by multi-currency enabled forms to automatically convert form fields between two currencies

Currency fields are defined in [PRINTUSING](PRINTUSING.htm) images by the use of the dollar (\$) sign instead of the hash (#) symbol. However, to enable this feature you must set the HEX(10) bit of [\$OPTIONS RUN]($OPTIONS_RUN.htm) and change the default leading currency symbol specified in byte 4 of [\$OPTIONS]($OPTIONS.htm#BYTE4) to a hash symbol, e.g. STR(\$OPTIONS,4 ,1) = "#". For example:

STR(\$OPTIONS, 4, 1) = "#"\
STR(\$OPTIONS RUIN, 47, 1) = OR HEX(10)\
\$CONVERT = "GBP, EUR, 1.23"\
PRINTUSING "-\$\$\$\$\$.\$\$ -#####.##", 5, 5

would give the following output:

 4.07 5.00

See [\$CONVERT]($CONVERT.htm) for more information.

Syntax examples:

PRINTUSING "-######", temp\
PRINTUSING 100, test\$(5), price(4), qt\
PRINTUSING images\$, FLD(temp\$.name\$), qt\
PRINTUSING \#45, image\$, info\
PRINTUSING \#10, 100, test1, name\$

See also:

[\$CONVERT]($CONVERT.htm), [% (Image)](image.htm), [\$IMAGE]($IMAGE.htm)

 
