# % (Image)

> Define a numeric output format template for `PRINTUSING`.

## Syntax

```
% [character_string] format_specification
```

## Description

The `%` statement defines a format template used by `PRINTUSING` to produce formatted numeric output. The `%` must appear as the first character on the line.

The format specification uses `#` characters to mark where formatted numbers will be placed. Other printable characters (including currency symbols, labels, etc.) appear literally in the output.

**Note:** A `:` within an Image statement is treated as part of the image, not as a statement separator.

### Format characters

| Character | Meaning |
|-----------|---------|
| `#` | One numeric digit position |
| `.` | Decimal point |
| `,` | Thousands separator (in integer portion) |
| `$` | Currency symbol (leading, floating, or fixed) |
| `+` | Leading sign (always shown) |
| `++` | Trailing sign |
| `-` | Leading minus (only for negative) |
| `--` | Trailing minus |
| `^` | Exponent notation |

### Localisation

The default characters can be overridden:
- **Currency symbol**: byte 4 of `$OPTIONS` (single-byte) or `CURCHAR` environment variable (multi-byte)
- **Decimal point**: byte 6 of `$OPTIONS` or `DOTCHAR` environment variable
- **Thousands separator**: byte 5 of `$OPTIONS` or `SEPCHAR` environment variable

These only affect `PRINTUSING` output. The Image format itself must still use `$`, `.`, and `,`.

For multi-language support use `$IMAGE` instead of `%`.

## Examples

```kcml
% ####.##
% ##.##
% #
% Type ###  Grand Total $######.##
% ###--      ###,###,##++
```

Used with `PRINTUSING`:

```kcml
10 % ####.##
20 PRINTUSING 10: 1234.5  : REM  prints  1234.50
```

## See Also

- `PRINTUSING` — formatted output using an Image template
- `$IMAGE` — Image statement with multi-language support
- `$OPTIONS` — runtime options (currency, decimal, separator characters)
