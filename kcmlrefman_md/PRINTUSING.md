# PRINTUSING

> Prints values using a format image — controls numeric formatting, currency symbols, sign display, and column widths.

## Syntax

```
PRINTUSING image, expr [, expr ...]
PRINTUSING #stream, image, expr [, expr ...]
PRINTUSING image, expr [, expr ...];     (suppress trailing CR)
```

Where `image` is:
- A literal string: `"####.##"`
- An alpha variable containing the image
- A line number referencing an `%` (image) or `$IMAGE` statement

## Image characters

| Char | Meaning |
|------|---------|
| `#` | One digit position |
| `.` | Decimal point |
| `,` | Thousands separator (before `.`) |
| `$` | Float dollar sign (before first significant digit) |
| `+` at start/end | Always show sign (`+` positive, `-` negative) |
| `-` at start/end | Show `-` for negative, blank for positive |
| `++` / `--` at end | Append `CR`/`DR` for negative values |
| `^` (four) | Exponential format (`##.####^^^^`) |
| alpha `#` chars | Fixed-width left-justified string field |

## Examples

```kcml
DIM price
price = 11123.46
PRINTUSING "   $###,###.##", price
REM      $11,123.46
```

```kcml
DIM qty
qty = -47
PRINTUSING "###--", qty
REM     47DR
```

```kcml
REM Using % image statement
00100 % -$###,###.##       ###
00110 PRINTUSING 100, price, qty
```

```kcml
REM Multi-language with $IMAGE
00100 $IMAGE <<"£####.###", "####.###FF">>
00110 PRINTUSING 100, price
```

```kcml
REM Image in a variable
DIM img$20
img$ = "####.###"
PRINTUSING img$, price
```

```kcml
REM Alphanumeric field in image
DIM code$10
code$ = "ABCDEF"
PRINTUSING "######", code$    : REM  ABCDEF (left-justified, 6 wide)
```

```kcml
REM Suppress carriage return
PRINTUSING "####.##", price;
PRINT " each"
```

## Notes

- If the value overflows the image (too many digits), the image characters are printed as-is (e.g. `######.##`).
- Decimal portion is truncated (not rounded) to fit the image.
- The `,` in an image is a thousands separator, **not** the statement separator — colons in `%` images are treated as image characters, not statement separators.
- For output to a buffer, see `PRINTUSING TO`.

## See Also

- `PRINTUSING TO` — format into a string buffer
- `PRINT` — unformatted output
- `$IMAGE` — multi-language image statement
