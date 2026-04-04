Controlling the screen

The terminal's screen is accessed as device /005 which is predefined as standard output (stdout). It is possible to redirect standard output to another device or file when **KCML** is initially started but it is not possible to redefine /005 within KCML using the \$DEVICEdeviced statement. To print text on the screen under program control the [PRINT](PRINT.htm), [PRINTUSING](PRINTUSING.htm) or \$GIO statements can be used if the [PRINT](SELECT_PRINT.htm) device has been selected to /005. The console output device ([CO](SELECT_CO.htm)) is used for all immediate mode output and is predefined as /005. To define the [PRINT](SELECT_PRINT.htm) device the [SELECT](SELECT.htm) statement is used, for example:

SELECT PRINT /005 PRINT "Hello world" SELECT PRINT /005(80)

In the last example an optional screen width has been specified. The screen width can be set to anything up to 255. If a line exceeds the width a carriage return will automatically be inserted by KCML to wrap the line at that point. A width of zero disables the autowrap detection. The first digit of the device in the [SELECT](SELECT_PRINT.htm) instructs KCML how to handle carriage returns at the end of a line, this digit can be set to any one of the following:

| Code | Purpose                                           |
|------|---------------------------------------------------|
| 0    | Maps CR to CR/LF.                                 |
| 1    | Send LF instead of CR.                            |
| 2    | Sends CR only.                                    |
| 4    | As 0 except that the column count is not updated. |
| 7    | Same as 2.                                        |

Type 4 has the effect of not issuing the automatic carriage return at the end of [PRINT](PRINT.htm) statements or at the end of the line.

Note that the digits 3, 5, 6, and 8-F are reserved for platter and communications operations.

KCML considers the carriage return (CR), i.e. HEX(0D), as a new line character so the screen is normally selected as /005 to make KCML add the linefeed and force the cursor to the next line. If the line width selected exceeds the physical width of the screen then KCML assumes that the terminal will wrap back to column zero on the same line. Normally the programmer will specify the screen width as equal to or less than the actual width so that KCML can insert a carriage return and a corresponding line feed when the width is exceeded.

Carriage returns are added automatically after each [PRINT](PRINT.htm) or [PRINTUSING](PRINTUSING.htm) statement unless a semi-colon is added at the end of the statement.

KCML considers the screen to have at least 24 rows and 80 columns which are numbered from zero with row 0, column 0 in the top left. The physical screen size is specified in the *TERMINFO* database.

A program controls the screen by issuing defined escape sequences using characters less than HEX(10), see the table below

| Code | Description |
|----|----|
| 01 | Homes the cursor to row 0, column 0. |
| 02 | Start of multi-character escape sequence, see below. |
| 03 | Homes the cursor to row 0, column zero and clears the screen. Attributes are unchanged but box graphics are cleared. |
| 05 | Make cursor visible. |
| 06 | Make cursor invisible. |
| 07 | Sound terminal bell. |
| 08 | Non-destructive backspace. |
| 09 | Non-destructive forward space. |
| 0A | Line feed. Move to same column on the next row. If already on the last row then scroll the screen up one line. |
| 0C | Reverse line feed. Move to same column on the previous row. If already on the top row then wrap to last row. |
| 0D | Carriage return. Move to column zero on the same line. KCML will add a line feed for device /005. |
| 0E | Enable current attribute. |
| 0F | Disable current attribute. |

KCML control characters
