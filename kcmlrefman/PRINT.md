PRINT

------------------------------------------------------------------------

General Form:\
     <img src="bitmaps/print.gif" data-align="BOTTOM" data-border="0" alt="print.gif" />\
\
Where:\
<img src="bitmaps/print1.gif" data-align="BOTTOM" data-border="0" alt="print1.gif" />\
\

------------------------------------------------------------------------

The PRINT statement is used to print the values of the specified print information onto the current PRINT device defined in the device table or into a string buffer. This statement is only relevant when developing text based applications. The PRINT statement can contain both alpha and numeric information as well as the PRINT functions, [AT(](PRINT_AT(.htm), [BOX(](PRINT_BOX(.htm), [HEXOF(](PRINT_HEXOF(.htm) and [TAB(](PRINT_TAB(.htm).

In program mode PRINT output is sent to the device currently set for PRINT operations in the device table. In immediate mode, the output goes to the current console output device. If while printing the contents of a variable the output contains more lines than can be displayed on the screen, the message \`Press RETURN for more' is displayed.

With PRINT TO the output is added to a string buffer at a position determined by the binary value of a count held in the first two bytes of the string. After the print operation the count is updated by the number of characters added to the buffer. If the count is zero then the first character will be inserted at byte 3 of the string. The first two bytes of the variable should therefore be initialised to HEX(00) before the PRINT TO statement is executed.

If the print information is to be redirected to a file the optional \#stream may be specified. A file must have previously been opened on the specified stream. When printing to files in this way AT(, BOX( and TAB( functions are ignored.

If the total number of characters to be stored in the alpha variable exceeds the length of the alpha variable, output is truncated, and the count is set to the length of the alpha variable.

Comma and semi-colon characters are used to delimit print information. A comma forces a tab between the start of each piece of information, where tab stops are every 16 characters. A semi-colon appends the information directly after the previous information. Ending a PRINT statement with a comma or a semi-colon will effect the way the next PRINT statement starts printing.

Example:

PRINT "A","B","C"\
\
 A B C

PRINT "A";"B";"C",\
PRINT "D"\
\
 ABC D

buffer\$ = BIN(0,2)\
PRINT TO buffer\$;"A"\
PRINT HEXOF(-buffer\$)\
\
0002 410D 2020 2020 2020 2020 2020 2020

Printing Alphanumeric information

Alphanumeric information can be printed as either a literal string, alpha variable, or a string function, e.g. [STR(](STR(.htm). Literal strings are printed exactly as they appear in the quotation marks, including trailing spaces.

Example:

DIM apple\$10\
apple\$ = "ABCDEFGHIJ"\
PRINT "HELLO"\
PRINT apple\$\
PRINT STR(apple\$,5,5)\
\
HELLO\
ABCDEFGHIJ\
EFGHI

Note that KCML also allows quotes to be entered within literal strings by entering the quotes twice, e.g.

PRINT "Double quotes "" may be displayed"

would print the following

Double quotes " may be displayed

Printing Numeric Information

Numeric information can be printed either as numeric expressions, numeric variables or constants. If a numeric expression is specified anywhere in the PRINT statement, PRINT will evaluate the expression and print the result.

Example:

PRINT 100 \* 40 / 2\
 2000

A numeric value will always be printed with a leading minus sign if the value is negative, a leading space and a trailing space. Leading and trailing zeros are not displayed.

Any numeric value less than 0.1 which cannot be represented in exponential format with 17 characters or less is printed in Scientific Notational Format. A value printed in this format always occupies 18 character positions. The first character position contains a minus sign for a negative number and a blank for a positive number. The character positions contain a leading minus sign or blank, one integer digit, a decimal point, 10 decimal digits, the letter E, the sign of the exponent, a 2 digit exponent, and a trailing space.

Example:

PRINT 9873244 \* 9234439\
 9.117386945012E+13\
PRINT -987654321 \* 123456789\
 -1.219326311126E+17

<span id="NewLineChar"></span>

Carriage return generation

A carriage return (HEX(0D)) is automatically appended to the end of each PRINT statement unless a trailing comma or semi-colon is used. A carriage return can also be forced during the operation of a PRINT statement by incorporating a HEX(0D) character within the output information. If a line longer than the width of the output device is printed will cause the information to wrap round onto the next line, giving the same effect as printing a HEX(0D) character.

<span id="DevType"></span>

Using different device types with PRINT statements

The device type is represented by the first character of the output device address, the following device types are available:

| DevType | Purpose               |
|---------|-----------------------|
| 0       | Maps CR to CR/LF      |
| 1       | Send LF instead of CR |
| 2       | Sends CR only         |
| 4       | No LF or CR           |
| 7       | Same as 2             |

Example:

SELECT PRINT /004\
FOR count = 1 TO 3\
    PRINT " This is a test print "\
NEXT count\
SELECT PRINT /005

In the above example the local printer device is selected on the first line, using the /004 device will print a linefeed character (HEX(0A)) after each line of text is printed.

Syntax examples:

PRINT "count = ", count\
PRINT LOG(act) \* 100\
PRINT lists\$;" test string ", array(count)\
PRINT text\$(), files()

See also:

[PRINT AT(](PRINT_AT(.htm), [PRINT BOX(](PRINT_BOX(.htm), [PRINT HEXOF(](PRINT_HEXOF(.htm), [PRINT TAB(](PRINT_TAB(.htm), [MAT PRINT](MAT_PRINT.htm)
