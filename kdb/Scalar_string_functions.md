Scalar string functions supported

String expressions must have a predictable length at prepare time.

| Function | Description |
|----|----|
| ASCII(string_exp) | Returns the ASCII code value of the leftmost character of *string_exp* as an integer. |
| BLOBDATA(*column*,*length*) | Returns length characters from BLOB or CBLOB *column*. |
| CHAR(*code*) | Returns the character that has the ASCII code value specified by *code*. |
| CONCAT(*string_exp1*, *string_exp2*) | Returns a character string that is the result of concatenating *string_exp2* to *string_exp1*. |
| DIFFERENCE(*string_exp1*, *string_exp2*) | Returns an integer value that indicates the difference between the values returned by the SOUNDEX function for *string_exp1* and *string_exp2*. |
| INSERT(*string_exp1*, *start,length*, *string_exp2*) | Returns a character string where *length* characters have been deleted from *string_exp1* beginning at *start* and where *string_exp2* has been inserted into *string_exp,* beginning at *start*. |
| LCASE(*string_exp*) | Converts all upper case characters in *string_exp* to lower case. |
| LEFT(*string_exp*, *count*) | Returns the leftmost *count* of characters of *string_exp* where *count* is a constant expression. |
| LENGTH(*string_exp*) | Returns the number of characters in *string_exp,* excluding trailing blanks. |
| LOCATE(*string_exp1*, *string_exp2*\[, *start*\]) | Returns the starting position of the first occurrence of *string_exp1* within *string_exp2*. The search for the first occurrence of *string_exp1* begins with the first character position in *string_exp2* unless the optional argument, *start*, is specified. If *start* is specified, the search begins with the character position indicated by the value of *start*. The first character position in *string_exp2* is indicated by the value 1. If *string_exp1* is not found within *string_exp2,* the value 0 is returned. |
| LTRIM(*string_exp*) | Returns the characters of *string_exp,* with leading blanks removed. |
| REPEAT(*string_exp*,*count*) | Returns a character string composed of *string_exp* repeated *count* times where *count* is a constant expression. |
| REPLACE(*string_exp1*, *string_exp2*, *string_exp3*) | Replaces all occurrences of *string_exp2* in *string_exp1* with *string_exp3*. |
| RIGHT(*string_exp*, *count*) | Returns the rightmost *count* of characters of *string_exp*. Note that *count* must be a constant expression. |
| RTRIM(*string_exp*) | Returns the characters of *string_exp* with trailing blanks removed. |
| SOUNDEX(*string_exp*) | Returns the standard Soundex four character value for a string. |
| SPACE(*count*) | Returns a character string consisting of *count* spaces where *count* is a constant expression. |
| SUBSTRING(*string_exp*, *start*, *length*) | Returns a character string that is derived from *string_exp* beginning at the character position specified by *start* for *length* characters. Note that *start* and *length* must be constant expressions. |
| UCASE(*string_exp*) | Converts all lower case characters in *string_exp* to upper case. |
