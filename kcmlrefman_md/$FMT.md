# $FMT(

> Formats a numeric or alpha value into a string using a PRINTUSING-style image.

## Syntax

```
alpha_receiver = $FMT(format$, expression [, expression2 ...])
```

## Description

`$FMT(` formats one or more values into a string using the same image format specifiers as `PRINTUSING`. It is a convenient alternative to `PRINTUSING TO` when you need the result as a string variable rather than printed output.

`format$` is a PRINTUSING image string. For numeric values, the key specifier is `#` — each `#` represents one digit position. Additional format characters:

| Character | Meaning |
|-----------|---------|
| `#` | Digit position (right-justified, space-padded) |
| `.` | Decimal point |
| `,` | Thousands separator (in integer part) |
| `-` | Leading sign (blank for positive, `-` for negative) |
| `+` | Leading sign (`+` for positive, `-` for negative) |
| `$` | Floating currency symbol (appears before first digit) |
| `^^^^` | Exponential format (4 carets = `E+ee`) |

For alpha values, each `#` in the format is replaced by one character from the string (left-justified, space-padded to fill).

> **Important:** `$FMT(` uses a static internal buffer. Only call it **once per statement** — calling it twice in the same statement causes the second call to overwrite the buffer before the first is consumed, giving incorrect results.

## Examples

### Example 1 — Numeric formatting
```kcml
01000 REM Format prices with $FMT(
: DIM r$20
: r$ = $FMT("-####.##", 1234.567)
: PRINT "Price: ["; RTRIM(r$); "]"
: r$ = $FMT("-####.##", -99.5)
: PRINT "Negative: ["; RTRIM(r$); "]"
: r$ = $FMT("-####.##", 0.09)
: PRINT "Small: ["; RTRIM(r$); "]"
: $END
```
**Output:**
```
Price: [ 1234.56]
Negative: [  -99.50]
Small: [    0.09]
```

### Example 2 — Sign, currency and alignment
```kcml
01000 REM Formatting with sign and currency symbol
: DIM r$20
: r$ = $FMT("+####.##", 3.14)
: PRINT "With sign: ["; RTRIM(r$); "]"
: r$ = $FMT("-$###,###.##", 11123.46)
: PRINT "Currency: ["; RTRIM(r$); "]"
: r$ = $FMT("####", 42)
: PRINT "Integer: ["; RTRIM(r$); "]"
: $END
```
**Output:**
```
With sign: [   +3.14]
Currency: [ $11,123.46]
Integer: [  42]
```

### Example 3 — Percentage and overflow
```kcml
01000 REM Percent format; overflow shows image
: DIM r$20
: r$ = $FMT("##.## %", 78.5)
: PRINT "Pct: ["; RTRIM(r$); "]"
: REM If value exceeds image width, image is printed as-is
: r$ = $FMT("##", 9999)
: PRINT "Overflow: ["; RTRIM(r$); "]"
: $END
```
**Output:**
```
Pct: [78.50 %]
Overflow: [##]
```
> When the value is too large for the format, KCML prints the `#` characters literally as a visual overflow indicator.

## Notes

- Use only once per statement — calling `$FMT(` twice in the same expression overwrites the result buffer.
- `0` in the format string is a literal zero character, not a digit position — use `#` for digits.
- If the value exceeds the image width, the `#` characters are printed as-is (a clear overflow signal).
- The format image is identical to `PRINTUSING` image syntax; see `PRINTUSING` for full reference.
- Added in KCML 5.x.

## See also

[PRINTUSING](PRINTUSING.md), [PRINTUSING_TO](PRINTUSING_TO.md)
