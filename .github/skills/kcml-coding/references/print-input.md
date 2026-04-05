# KCML Input/Output Reference

Complete reference for screen and console I/O in KCML.

> **Note:** This covers terminal/console I/O. For file I/O, see [file-io.md](file-io.md).

## PRINT Statement

### Basic Syntax

```kcml
PRINT expression [, expression] ...
PRINT expression [; expression] ...
```

### Simple Output

```kcml
PRINT "Hello, World!"
: PRINT 42
: PRINT name$
: PRINT "Value: "; total
```

### Output Separators

| Separator | Effect |
|-----------|--------|
| `;` | No space between items |
| `,` | Tab to next 16-character column |
| (none at end) | Newline after output |
| `;` at end | No newline (continue on same line) |
| `,` at end | Tab, no newline |

### Examples

```kcml
REM Semicolon - no space
: PRINT "A";"B";"C"        : REM Output: ABC

REM Comma - tabbed columns
: PRINT "A","B","C"        : REM Output: A               B               C

REM Suppress newline
: PRINT "Line 1 ";
: PRINT "continues here"   : REM Output: Line 1 continues here
```

### Numeric Output Format

Numbers print with:
- Leading space (or `-` for negative)
- Trailing space
- No leading zeros

```kcml
PRINT 42        : REM " 42 "
: PRINT -3.14   : REM "-3.14 "
: PRINT 0.5     : REM " .5 "
```

Large/small numbers use scientific notation:
```kcml
PRINT 9873244 * 9234439    : REM " 9.117386945012E+13 "
```

### Quotes in Strings

Double the quotes to include them:

```kcml
PRINT "He said ""Hello"""  : REM He said "Hello"
```

### PRINT TO - Output to String Buffer

Build output in a string variable:

```kcml
DIM buffer$100
: buffer$ = BIN(0,2)       : REM Initialize count bytes
: PRINT TO buffer$; "Hello"
: PRINT TO buffer$; " World"
: REM buffer$ contains count + "Hello World"
```

### PRINT #stream - Output to File

```kcml
OPEN #1, "output.txt", "w"
: PRINT #1, "Line 1"
: PRINT #1, "Line 2"
: CLOSE #1
```

## PRINTUSING - Formatted Output

Format numbers and strings with picture strings.

### Syntax

```kcml
PRINTUSING format$, value1, value2, ...
PRINTUSING line_number, value1, value2, ...
```

### Numeric Format Characters

| Char | Meaning |
|------|---------|
| `#` | Digit placeholder |
| `.` | Decimal point |
| `,` | Thousands separator |
| `$` | Currency symbol (floats left) |
| `+` | Show sign (+ or -) |
| `-` | Show sign (- only, space for +) |
| `++` | CR for negative |
| `--` | DR for negative |
| `^^^^` | Scientific notation |

### String Format Character

| Char | Meaning |
|------|---------|
| `\` | String placeholder (each `\` = 1 char) |

### Examples

```kcml
DIM price = 1234.56, qty = 42

: PRINTUSING "####.##", price        : REM "1234.56"
: PRINTUSING "$#,###.##", price      : REM "$1,234.56"
: PRINTUSING "-#####.##", -price     : REM "-1234.56"
: PRINTUSING "+#####.##", price      : REM "+1234.56"
: PRINTUSING "#####.##--", -price    : REM "1234.56DR"

: PRINTUSING "###", qty              : REM " 42"
: PRINTUSING "\\\\\\\\\\\\", name$   : REM Left-justified in 6 chars
```

### Using % Image Statement

```kcml
100 % $#,###.## Qty: ###
: PRINTUSING 100, price, qty
```

### Using $IMAGE Statement

```kcml
$IMAGE <<"-$###,###.##">>
: PRINTUSING $IMAGE, total
```

## INPUT Statement (Basic)

Simple input - considered obsolete, use LINPUT instead:

```kcml
INPUT "Enter name: ", name$
: INPUT value
```

## LINPUT Statement

Enhanced line input with editing:

### Syntax

```kcml
LINPUT [prompt$[,]] [-] variable$ [, [mask], [cursor_pos]]
```

### Options

| Option | Effect |
|--------|--------|
| `-` before var | Underline the input field |
| `?` before var | Start in text entry mode |
| `,cursor_pos` | Initial cursor position (1-based) |

### Examples

```kcml
DIM name$30
: name$ = ""
: LINPUT "Enter name: "-name$

REM With initial value and cursor position
: name$ = "John Doe"
: LINPUT "Edit name: "-name$,,5    : REM Cursor at position 5
```

### Edit Mode Keys

In edit mode (default), function keys control cursor:
- Arrow keys move cursor
- Insert/Delete for editing
- EDIT key toggles to text entry mode

## LINPUT+ Statement (Enhanced)

More functional input with field attributes:

```kcml
LINPUT+ options, variable$, ...
```

See KCML reference for full LINPUT+ documentation.

## KEYIN Statement

Read single character from keyboard:

### Syntax

```kcml
KEYIN char$
KEYIN char$, line_char, line_fkey
```

### Forms

```kcml
REM Wait for any character
: KEYIN key$

REM Wait with function key handling
: KEYIN key$,, function_key_line

REM Polling (non-blocking)
: KEYIN key$, char_line, fkey_line
```

### Example - Wait for Keypress

```kcml
DIM key$1
: PRINT "Press any key..."
: KEYIN key$
: PRINT "You pressed: "; key$
```

### Example - Simple Menu

```kcml
DIM choice$1
: PRINT "1. Option One"
: PRINT "2. Option Two"
: PRINT "Q. Quit"
: PRINT "Choice: ";
: KEYIN choice$
: IF (choice$ == "1") THEN GOSUB 'option_one
: IF (choice$ == "2") THEN GOSUB 'option_two
: IF ($UPPER(choice$) == "Q") THEN $END
```

### Mouse Events (Windows/KClient)

| Code | Event |
|------|-------|
| 0xF1 | Left mouse down |
| 0xF2 | Left mouse up |
| 0xF3 | Left double-click |
| 0xF4 | Right mouse down |
| 0xF5 | Right mouse up |
| 0xF6 | Right double-click |
| 0xF7 | Mouse drag |

## Screen Positioning

### PRINT AT( - Position Output

```kcml
PRINT AT(row, col); "text"
```

### Example

```kcml
PRINT AT(1, 1); "Top left"
: PRINT AT(12, 40); "Center"
: PRINT AT(24, 1); "Bottom left"
```

### PRINT TAB( - Horizontal Tab

```kcml
PRINT "Name"; TAB(20); "Value"
```

### PRINT BOX( - Draw Boxes

```kcml
PRINT BOX(row, col, height, width)
```

## Screen Control

### Clear Screen

```kcml
PRINT HEX(0C)     : REM Form feed - clear screen
```

### Text Attributes (via HEX codes)

| Code | Effect |
|------|--------|
| `HEX(0E)` | Bold on |
| `HEX(0F)` | Attributes off |
| `HEX(12)` | Reverse video on |

```kcml
PRINT HEX(0E); "Bold text"; HEX(0F); " Normal text"
```

## Special Output Characters

| Code | Effect |
|------|--------|
| `HEX(07)` | Bell/beep |
| `HEX(09)` | Tab |
| `HEX(0A)` | Line feed |
| `HEX(0C)` | Form feed (clear) |
| `HEX(0D)` | Carriage return |

## SELECT Statements for I/O

### SELECT INPUT - Redirect Input

```kcml
REM Read from command output
: SELECT INPUT "date ^"
: LINPUT date$
: SELECT INPUT /001     : REM Back to keyboard
```

### SELECT PRINT - Redirect Output

```kcml
SELECT PRINT device$    : REM Redirect print output
: SELECT PRINT /001     : REM Back to terminal
```

## Complete Example: Menu System

```kcml
DIM choice$1, name$30, quit = FALSE

: WHILE (NOT quit)
:   PRINT HEX(0C)        : REM Clear screen
:   PRINT AT(1, 30); "MAIN MENU"
:   PRINT AT(3, 25); "1. Enter Name"
:   PRINT AT(4, 25); "2. Display Name"
:   PRINT AT(5, 25); "Q. Quit"
:   PRINT AT(7, 25); "Choice: ";
:   KEYIN choice$
:   
:   SELECT CASE $UPPER(choice$)
:   CASE "1"
:     PRINT AT(10, 20); "Enter name: ";
:     LINPUT -name$
:   CASE "2"
:     PRINT AT(10, 20); "Name is: "; name$
:     PRINT AT(12, 20); "Press any key..."
:     KEYIN choice$
:   CASE "Q"
:     quit = TRUE
:   END SELECT
: WEND

: PRINT HEX(0C)
: PRINT "Goodbye!"
: $END
```

## Complete Example: Simple Report

```kcml
DIM items$(5), prices(5), i

: items$(1) = "Widget" : prices(1) = 19.99
: items$(2) = "Gadget" : prices(2) = 29.99
: items$(3) = "Gizmo"  : prices(3) = 39.99

: PRINT "Item Report"
: PRINT "==========="
: PRINT
: PRINTUSING "\\\\\\\\\\\\\\\\\\  $###.##", "ITEM", 0
: PRINT "-------------------"

: FOR i = 1 TO 3
:   PRINTUSING "\\\\\\\\\\\\\\\\\\  $###.##", items$(i), prices(i)
: NEXT i

: $END
```

## Best Practices

1. **Use LINPUT over INPUT** - More features and editing
2. **Initialize string variables** - Before using with LINPUT
3. **Use AT( for positioning** - For formatted screens
4. **Use PRINTUSING for numbers** - For consistent formatting
5. **Clear screen appropriately** - Use HEX(0C) when needed
6. **Handle function keys** - For professional applications

## See Also

- [file-io.md](file-io.md) - File input/output
- [string-functions.md](string-functions.md) - String formatting
- [numeric-functions.md](numeric-functions.md) - CONVERT for number formatting
- [control-flow.md](control-flow.md) - Loops for menu systems
