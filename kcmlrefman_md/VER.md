# VER(

> Verifies that an alpha string conforms to a format specification. Returns the number of matching characters.

## Syntax

```
VER(alpha_expr, format$)
```

## Description

Checks `alpha_expr` against `format$` character by character. Returns the count of consecutive characters (from the left) that satisfy the format. Stops at the first non-matching character.

Returns the full length of `alpha_expr` if all characters match.

### Format characters

| Char | Matches |
|------|---------|
| `A` | Alphabetic only (A–Z, a–z) |
| `H` | Hexadecimal digit (A–F, a–f, 0–9) |
| `N` | Alphanumeric (A–Z, a–z, 0–9) |
| `P` | Packed decimal |
| `X` | Any character |
| `+` | Sign character (+, -, or blank) |
| `#` | Numeric digit (0–9) |
| other | Literal — only that exact character matches |

For UTF-8/Unicode strings, format characters `A`, `H`, `N`, `P`, `+`, `#` still use ASCII definitions.

## Examples

```kcml
DIM s$10, n
s$ = "12345ABC"
n = VER(s$, "######")     : REM  5  (5 digits match, stops at A)
PRINT n
```

```kcml
REM Validate a date string YYYYMMDD
DIM date$8
date$ = "20260407"
IF VER(date$, "########") == 8 THEN PRINT "Valid date"
```

```kcml
REM Verify hexadecimal
IF VER(hex_input$, "HHHHHHHH") == 8 THEN PRINT "Valid 8-char hex"
```

```kcml
ftmp = VER(form$, "XXXXXX")    : REM  always 6 (X matches anything)
IF VER(temp$, test$) <> 6 THEN PRINT "Mismatch"
```

## Notes

- Useful for validating user input before conversion with `VAL(` or `INT(`.
- `VER(s$, "XXXXXXXX")` always returns the minimum of `LEN(s$)` and 8.
- Complement with `NUM(` for counting leading digits.

## See Also

- `NUM(` — count leading numeric characters
- `LEN(` — string length
- `VAL(` — binary string to number
