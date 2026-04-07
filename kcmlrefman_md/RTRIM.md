# RTRIM(

> Removes trailing spaces (or a specified character) from the right side of a string.

## Syntax

```
result$ = RTRIM(alpha_expr [, char$])
```

## Description

Returns `alpha_expr` with trailing spaces removed. If `char$` is supplied, that character is trimmed instead of spaces.

## Examples

```kcml
DIM s$20, r$20
s$ = "Hello     "
r$ = RTRIM(s$)
PRINT "["; r$; "]"   : REM  [Hello]
```

```kcml
REM Trim a specific character
DIM buf$20
buf$ = "dataCCCC"
PRINT RTRIM(buf$, "C")   : REM  data
```

```kcml
REM Common pattern: trim before writing to file
size = WRITE #1, RTRIM(Buffer$)
```

```kcml
REM Trim binary padding
DIM rec$10
rec$ = "test" & HEX(FFFFFFFFFFFF)
rec$ = RTRIM(rec$, HEX(FF))
PRINT rec$    : REM  test
```

## Notes

- Returns the string with trailing occurrences of `char$` removed (default: space `HEX(20)`).
- Does not modify the original variable — returns a new string.
- `LTRIM(` removes leading characters; `TRIM(` removes both ends.

## See Also

- `LTRIM(` — remove leading characters
- `TRIM(` — remove both leading and trailing spaces
- `LEN(` — content length (excludes trailing spaces naturally)
