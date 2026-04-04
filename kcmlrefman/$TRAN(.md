\$TRAN( character translation

------------------------------------------------------------------------

General Forms:

1.  \$TRAN(alpha_variable, translation_table \[, HEX(hh) \] ) \[R\]\
    \
2.  \$TRAN(alpha_variable, translation_table) \[, HEX(hh) \] \[R\]

Where:\
<img src="bitmaps/trand1.gif" data-align="BOTTOM" data-border="0" alt="trand1.gif" />\

hh = two hex digits 0-9 or A-F.

------------------------------------------------------------------------

This form of the \$TRAN statement is used to perform a character by character translation on all the characters in an alpha_variable. \$TRAN is particularly useful for ASCII to EBCDIC conversions.

If the optional hex digits are specified, \$TRAN logically [ANDs](AND.htm) each character of the alpha variable with the specified hex pair before the translation takes place.

If the 'R' parameter is specified, the translation table, specified by the second alpha variable or literal string, should consist of pairs of characters, the first character represents the 'to' character and the second represents the 'from' character. Therefore if 'AZ' was specified as the translation table, all occurrences of 'Z' in the alpha variable would be changed to 'A'.

If the 'R' parameter is omitted, the binary value of each character plus 1 is used to determine a position in the translation table. The character in the alpha variable is then replaced with the corresponding character in translation table. If the binary value of a character is greater than the size of the translation table, the character in the alpha variable remains unchanged.

Syntax examples:

\$TRAN(test\$(4),"011223344556677889")R\
\$TRAN(conversion\$,HEX(0D0A 0F0D),HEX(1B))\
\$TRAN(FLD(record\$.flags\$),table\$)R
