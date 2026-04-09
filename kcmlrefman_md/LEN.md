# LEN(

> Returns the content length of a string (excluding trailing spaces), or the declared size of a string.

## Syntax

```
numeric = LEN(alpha_expression)
numeric = LEN(STR(alpha_variable))   REM declared size
numeric = LEN(.field_variable)       REM field length
```

## Description

`LEN(` returns the number of bytes in the alpha expression **not counting trailing spaces**. This is the content length, not the declared allocation.

**Important edge case:** If a string contains only spaces, `LEN(` returns **1**, not 0.

To get the **declared allocation size** of a string variable rather than its content length, wrap it in `STR(`:
```kcml
DIM s$32
PRINT LEN(s$)        REM content length (probably 1 - all spaces)
PRINT LEN(STR(s$))   REM declared size = 32
```

`LEN(` counts **bytes**, not characters. For UTF-8 encoded Unicode strings use `ULEN8(` instead.

`LEN(` also works on field variables to return the byte size of that field.

## Examples

### Example 1 — Content length vs declared size
```kcml
01000 REM LEN returns content length, LEN(STR()) returns declared size
: DIM s$20
: s$ = "Hello World"
: PRINT "LEN of content: " ; LEN(s$)
: PRINT "LEN of declared size: " ; LEN(STR(s$))
: $END
```
**Output:**
```
LEN of content:  11 
LEN of declared size:  20 
```

### Example 2 — Edge case: all-spaces string returns 1
```kcml
01000 REM Blank string returns 1, not 0
: DIM blank$10, one_char$5
: one_char$ = "A"
: PRINT "LEN of all-spaces: " ; LEN(blank$)
: PRINT "LEN of 'A': " ; LEN(one_char$)
: $END
```
**Output:**
```
LEN of all-spaces:  1 
LEN of 'A':  1 
```

### Example 3 — Use LEN for input validation and truncation guard
```kcml
01000 REM Check if string has content before processing
: DIM name$30
: name$ = "Smith"
: IF LEN(name$) > 1 THEN PRINT "Name: " ; RTRIM(name$)
: IF LEN(name$) <= 1 THEN PRINT "Name is blank"
: REM Use LEN to extract only the content portion
: DIM content$20
: content$ = STR(name$, 1, LEN(name$))
: PRINT "Content only: [" ; RTRIM(content$) ; "]"
: $END
```
**Output:**
```
Name: Smith
Content only: [Smith]
```

## Notes

- `LEN(` returning `1` for a blank string is a well-known KCML quirk — test for blank with `RTRIM(s$) == ""` or `LEN(s$) <= 1` if the string could contain a single space.
- `LEN(STR(var$))` is the idiomatic way to get the declared size of any string variable — useful for assertions and buffer management.
- For a field variable: `LEN(.myfield$)` returns the byte width of the field as defined in `DEFRECORD`.
- `POS(` is used to get the starting position of a field variable; `PACK(` returns the packing specifier.

## See also

[STR(](STR.md), [RTRIM(](RTRIM.md), [POS(](POS.md), [ULEN8(](ULEN8.md)
