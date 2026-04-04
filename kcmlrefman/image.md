% (Image)

------------------------------------------------------------------------

General Form:\
\
     % \[character_string\] \[format_specification\]\
\
Where:\
\
     character_string           = a string of alphanumeric characters\
<img src="bitmaps/image.gif" data-align="BOTTOM" data-border="0" alt="image.gif" />\
\

------------------------------------------------------------------------

The Image \`%' statement provides a method for formatting the output of a [PRINTUSING](PRINTUSING.htm) statement. The percent sign \`%', which appears as the first character on the line, identifies the Image statement. If multi-language support is required then the [\$IMAGE]($IMAGE.htm) statement should be used.

The format specification contains one or more \`#' characters to determine the location of a formatted variable. The following symbols may be included in the format specification: dollar sign \`\$', plus signs \`+, ++', minus signs \`-,--', and up arrows \`^'. The integer portion of a numeric format may include commas \`,' before the decimal point \`.'. An Image statement may also include other printable characters before and after the format specifications. If a colon is used within an image statement, it will be interpreted as part of the image and not a statement separator.

The \`\$' sign can be replaced with other currency symbols by setting byte 4 of [\$OPTIONS]($OPTIONS.htm#BYTE4) for a single character symbol or by setting the environment variable CURCHAR if the symbol requires several bytes. Similarly the symbol used for the decimal point can be changed from a period to another character by setting byte 6 of [\$OPTIONS]($OPTIONS.htm#BYTE6) or by setting the environment variable DOTCHAR. The comma character that separates groups of digits can be respecified in byte 5 of [\$OPTIONS]($OPTIONS.htm#BYTE5) or with the environment variable SEPCHAR. Changing the currency, decimal or separator characters only effects the output of the [PRINTUSING](PRINTUSING.htm) statement. The characters used for these functions in the image must still be \`\$', period and comma.

Syntax examples:

% \####.##      \####.##      \##.##      \#\
% Type \### Grand Total \$######.##\
% \###-- \###,###,##++

See also:

[\$IMAGE]($IMAGE.htm), [PRINTUSING](PRINTUSING.htm), [\$OPTIONS]($OPTIONS.htm)
