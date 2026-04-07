# PRINT

> Outputs values to the current print device, a file stream, or a string buffer.

## Syntax

```
PRINT [expr [, | ; expr] ...]
PRINT #stream, [expr [, | ; expr] ...]
PRINT TO buffer$, [expr [, | ; expr] ...]
```

## Description

`PRINT` sends output to the currently selected print device (set via `SELECT PRINT`). In script mode (`-p`) this is stdout.

### Separators

| Separator | Effect |
|-----------|--------|
| `,` (comma) | Tab to next 16-character column boundary |
| `;` (semicolon) | Append immediately with no gap |
| (end of statement) | Appends carriage return (`HEX(0D)`) |
| Trailing `,` or `;` | Suppresses the CR; next PRINT continues on same line |

### Printing to a stream

`PRINT #stream, ...` writes to a file opened with `OPEN #stream`. `AT(`, `BOX(`, and `TAB(` are ignored when printing to a file.

### Printing to a buffer

`PRINT TO buffer$, ...` appends output into an alpha variable. The first two bytes of `buffer$` hold a binary count of bytes stored so far. Initialize with `buffer$ = BIN(0, 2)` (or `HEX(0000)` in first two bytes). If the buffer is full, output is truncated and the count is clamped to the buffer length.

## Numeric output format

- Positive numbers: leading space, value, trailing space.
- Negative numbers: leading `-`, value, trailing space.
- Large/small values: scientific notation (`1.234567890123E+15`).
- No leading or trailing zeros.

## Examples

```kcml
PRINT "Hello, World!"       : REM  Hello, World!
PRINT 42                    : REM   42
PRINT 100 * 40 / 2          : REM   2000
PRINT "A","B","C"           : REM  A               B               C
PRINT "A";"B";"C"           : REM  ABC
```

```kcml
REM Suppress trailing CR with semicolon
PRINT "Enter name: ";
REM  (next PRINT continues on same line)
```

```kcml
REM Print to file
OPEN #1, "/tmp/out.txt", "w"
PRINT #1, "Line 1"
PRINT #1, "Line 2"
CLOSE #1
```

```kcml
REM Print to buffer
DIM buf$200
buf$ = HEX(0000)             : REM init count to 0
PRINT TO buf$; "Hello"
PRINT TO buf$; " World"
PRINT HEXOF(-buf$)           : REM shows count + content
```

```kcml
REM Embedded quotes using double-double-quote
PRINT "She said ""hello"" to me"
REM  She said "hello" to me
```

## Notes

- Use `HEX(22)` for quotes in string variables (`HEX(22)` = `"`); the double-quote technique above works only in literal strings in source code.
- `AT(`, `BOX(`, `TAB(` are PRINT functions for screen positioning — see their own pages.
- `PRINT AT(row, col)` combines output and cursor positioning in one statement.

## See Also

- `PRINT AT(` — print at screen position
- `PRINT TAB(` — tabbed output
- `PRINTUSING` — formatted numeric output
- `SELECT PRINT` — change the print device
- `OPEN #` — open a file stream
