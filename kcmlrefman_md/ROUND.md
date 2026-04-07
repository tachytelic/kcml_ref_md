# ROUND(

> Rounds a numeric value to a specified number of decimal places or integer position.

## Syntax

```
ROUND(value, places)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `value` | Numeric expression to round |
| `places` | Positive = decimal places; negative = integer positions left of decimal |

## Description

Rounds `value` to the precision specified by `places`:

- `places > 0` — round to that many decimal places.
- `places = 0` — round to nearest integer.
- `places < 0` — round to the nearest 10^(-places) (e.g. -2 rounds to nearest 100).

## Examples

```kcml
PRINT ROUND(1234.56789, 2)    : REM   1234.57
PRINT ROUND(1234.56789, 0)    : REM   1235
PRINT ROUND(1234.56789, -2)   : REM   1200
PRINT ROUND(1234.56789, -3)   : REM   1000
PRINT ROUND(2.5, 0)           : REM   3  (rounds half up)
PRINT ROUND(-2.5, 0)          : REM  -2 or -3 (platform dependent)
```

Verified output:
```
 1234.57
 1235
 1200
 1000
 3
```

```kcml
REM Financial rounding to 2 decimal places
DIM total, tax
tax = ROUND(total * 0.2, 2)
```

## Notes

- Positive `places` is the common use case for financial/display rounding.
- `ROUND(x, -n)` rounds to `10^n` — e.g. `ROUND(x, -3)` rounds to nearest thousand.
- For truncation (not rounding), use `INT(` for positive numbers.

## See Also

- `INT(` — floor (truncate toward negative infinity)
- `PRINTUSING` — formatted numeric output with automatic rounding
