UNEXT8(

General Form:

UNEXT8(strexpr, numexpr)

Where:

|  |  |
|----|----|
| strexpr | = an alphanumeric expression corresponding to a UTF-8 encoded string |
| numexpr | = a byte index into the string corresponding to the first byte of the current character. Counted from 1. |

------------------------------------------------------------------------

The UNEXT8( numeric function is used to return the byte index of the first byte of the next character in a string expression which is presumed to represent a UTF-8 encoded [Unicode](TutorialUnicode.htm) string. In UTF-8 chracters are encoded as one, two or three byte sequences. The current position in the string is passed as the second argument and corresponds to the byte index of the first byte of the character counted from 1. The result is returned as a numeric value counted from 1. The UNEXT8( function is valid wherever a numeric function is legal.

The function will return 0 if called for the last character in the string. It will return -1 if the current index is not in the string, that is it is less than 1 or more than the number of bytes in the string.

The string must be properly encoded UTF-8 and if applied to incorrect encoding or called with a byte index corresponding to the second or third byte of a multibyte sequence then the result is not defined. Remember that HEX(FE) and HEX(FF) characters cannot occur in a UTF-8 string.

Example:

DIM a\$="\$€£"\
IF (a\$ \<\> HEX(24E282ACC2A3)) THEN PANIC\
IF (UNEXT8(a\$,2)) \<\> 5 THEN PANIC\

See also:

[UPREV8(](UPREV8(.htm)\
[ULEN8(](ULEN8(.htm)\
