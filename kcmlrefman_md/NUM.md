# NUM(

> Counts the number of leading numeric ASCII characters in an alpha variable.

## Syntax

```
NUM(alpha_var)
NUM(alpha_var, start)
NUM(alpha_var, start, length)
```

## Description

Returns the count of consecutive numeric digit characters (`0`–`9`) beginning at the specified position in `alpha_var`. Scanning stops at the first non-digit character.

If `start` is omitted scanning begins at position 1. If `length` is supplied scanning is limited to that many characters.

Primarily used to validate that a field contains a number before converting it with `VAL(`.

## Examples

```kcml
DIM s$20
s$ = "12345ABC"
PRINT NUM(s$)          : REM  5  (five digits before A)
```

```kcml
s$ = "ABC123"
PRINT NUM(s$)          : REM  0  (no leading digits)
PRINT NUM(s$, 4)       : REM  3  (digits starting at position 4)
```

```kcml
REM Validate before converting
DIM input$10, value
input$ = "42"
IF NUM(input$) == LEN(input$) THEN value = VAL(input$)
```

## Notes

- Returns 0 if the first character (at `start`) is not a digit.
- Does **not** count signs (`+`/`-`) or decimal points — only `0`–`9`.
- Complement with `LEN(` to check whether the entire string is numeric.

## See Also

- `VAL(` — convert string to numeric
- `LEN(` — string length
- `POS(` — position of a character satisfying a relation
