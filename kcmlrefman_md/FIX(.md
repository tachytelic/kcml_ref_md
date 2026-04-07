# FIX(

> Returns the integer portion of a numeric expression, truncating towards zero.

## Syntax

```
FIX( numeric_expression )
```

Returns a numeric integer value. Valid wherever a numeric function is legal.

## Description

`FIX(` truncates a number to its integer part, always towards zero:
- Positive values: rounds down (same as `INT(`)
- Negative values: rounds up (unlike `INT(` which always rounds down)

This is the "truncate toward zero" (C-style integer truncation) behavior.

## Examples

```kcml
: DIM y
: y = FIX(3.7)
: PRINT "FIX(3.7)="; y
: y = FIX(-3.7)
: PRINT "FIX(-3.7)="; y
: $END
```

Output:
```
FIX(3.7)= 3
FIX(-3.7)=-3
```

### Comparison with INT(

| Expression | `FIX(` | `INT(` |
|------------|--------|--------|
| `3.7` | 3 | 3 |
| `-3.7` | -3 | -4 |
| `3.0` | 3 | 3 |
| `-3.0` | -3 | -3 |

In expressions:
```kcml
Test = FIX(190.723 * 2)
Total = 17 + FIX(ABS(temp))
```

## Notes

- Use `FIX(` when you want C-style truncation (toward zero).
- Use `INT(` when you want floor (always toward negative infinity).
- For rounding to nearest integer, use `INT(x + 0.5)`.

## See Also

- `INT(` — floor function (truncates toward negative infinity)
- `ABS(` — absolute value
- `SGN(` — sign of a number (-1, 0, 1)
