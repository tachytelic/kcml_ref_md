# PRINT

> Outputs values to the current print device, a file stream, or a string buffer.

## Syntax

```
PRINT [print_item [separator print_item] ...]
PRINT #stream, print_item ...
PRINT TO buffer$; print_item ...
```

Where separators are:
- `;` — append directly (no extra space)
- `,` — tab to next column (tab stops every 16 characters)

## Description

`PRINT` sends output to the current PRINT device (set via `SELECT PRINT`). In immediate mode it goes to the console. In script mode (`kcml -p`) it goes to stdout.

### Separators

| Separator | Effect |
|-----------|--------|
| `;` | No separator — items are adjacent |
| `,` | Tab to next multiple of 16 |
| Trailing `;` | Suppress carriage return — next PRINT continues on same line |
| Trailing `,` | Same, but with tab |
| Neither | Carriage return appended automatically |

### Printing numerics

Numeric values always print with a leading space (or `-` for negatives) and a trailing space. No leading/trailing zeros. Very large or small values use scientific notation (`1.23456789012E+13`).

### Printing strings

Literal strings print exactly as written including trailing spaces. Variables print their content including space padding.

### PRINT TO buffer$

Appends output into a string variable. The first two bytes hold a binary count of bytes written — initialise to `HEX(00)` before first use.

### PRINT #stream

Redirects output to an open file stream. `AT(`, `BOX(`, and `TAB(` are ignored when printing to files.

### Embedded quotes

Enter `""` (double-double-quote) inside a string literal to produce a single `"` in the output.

## Examples

### Example 1 — Semicolon vs comma separators
```kcml
01000 REM Separator comparison
: PRINT "Semicolon: " ; "A" ; "B" ; "C"
: PRINT "Comma: " , "A" , "B" , "C"
: $END
```
**Output:**
```
Semicolon: ABC
Comma:          A               B               C
```

### Example 2 — Numeric output formatting
```kcml
01000 REM Numeric PRINT behaviour
: PRINT 100 * 40 / 2
: PRINT -99
: PRINT 9873244 * 9234439
: $END
```
**Output:**
```
 2000 
-99 
 9.117386945012E+13 
```

### Example 3 — Trailing semicolon for same-line continuation
```kcml
01000 REM Print numbers on one line using trailing semicolons
: DIM x
: FOR x = 1 TO 5
:   PRINT x ;
: NEXT x
: PRINT ""
: $END
```
**Output:**
```
 1  2  3  4  5
```

### Example 4 — Embedded quotes and substrings
```kcml
01000 REM Printing substrings and embedded quotes
: DIM apple$10
: apple$ = "ABCDEFGHIJ"
: PRINT apple$
: PRINT STR(apple$,5,5)
: PRINT "She said ""hello"" to him"
: $END
```
**Output:**
```
ABCDEFGHIJ
EFGHI
She said "hello" to him
```

## Notes

- Use `PRINT USING` for formatted numeric output (currency, decimal places, etc.) — see [PRINTUSING](PRINTUSING.md).
- `PRINT AT(row, col)` positions the cursor for screen output — see [PRINT AT](PRINT_AT.md).
- When writing to files (`PRINT #stream`), `AT(`, `BOX(`, `TAB(` are silently ignored.
- `PRINT TO buffer$` requires the first two bytes initialised to `HEX(0000)` before the first write. The count in those bytes is updated automatically after each write.
- A carriage return (`HEX(0D)`) is appended automatically unless the statement ends with `;` or `,`.

## See also

[PRINTUSING](PRINTUSING.md), [SELECT PRINT](SELECT_PRINT.md), [MAT PRINT](MAT_PRINT.md)
