VER(

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/ver.gif" data-align="BOTTOM" data-border="0" alt="ver.gif" />\
\
Where:\
<img src="bitmaps/ver1.gif" data-align="BOTTOM" data-border="0" alt="ver1.gif" />\
\

------------------------------------------------------------------------

The VER( function is used to verify that an alphanumeric variable or literal string conforms to a specified format. The first variable or literal is verified against the second. The function returns the number of consecutive characters in the alpha variable or literal that match the format specification. Once an illegal character is detected the function terminates. VER( is valid wherever a numeric expression is legal.

The valid character representations in the format specification for the VER( function.

Format Character

Format Specification Characters

A

Alphabetic character only (A-Z, a-z)

H

Hexadecimal character only (A-F, a-f, 0-9)

N

Alphanumeric character only (A-Z, a-z, 0-9)

P

Packed decimal

X

Any character

\+

Sign character (+, -, or blank)

\#

Numeric only (0-9)

other

Only the specified character

Note: When used with a UTF-8 and UNICODE characters the format specification characters A, H, N, P, +, \# will still use the ASCII characters for determining valid characters.

\
Syntax examples:

ftmp = VER(form\$, "XXXXXX")\
IF (VER(temp\$,test\$) \<\> 6 )
