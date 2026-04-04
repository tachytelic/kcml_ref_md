HEX(

------------------------------------------------------------------------

General Form:\
\
     HEX( hh \[hh ...\] )\
\
Where:\
\
     h      = hexadecimal digit within the range 0-9 or A-F\
\

------------------------------------------------------------------------

The HEX( literal permits the use of 8-bit (1-byte) characters in KCML programs. Each character in the string is represented by two hexadecimal digits. An error will occur if an odd number of hex digits is used. The HEX( literal is valid wherever an alphanumeric literal string is legal.

The HEX( literal is generally used to incorporate characters that are not available from the keyboard. For example:

PRINT HEX(0307)

would first clear the screen (HEX(03)) and home the cursor, then it would make the terminal bell sound (HEX(07)). Any character can be represented by a pair of hex digits.

Syntax examples:

output\$ = HEX(020402000F) & string\$\
PRINT HEX(0106);title\$\
IF (saw\$(count) = HEX(0A))

 
