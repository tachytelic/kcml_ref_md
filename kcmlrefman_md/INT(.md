# INT(

> Returns the largest integer less than or equal to a numeric expression (floor function).

## Syntax

```
INT( numeric_expression )
```

Returns a numeric integer. Valid wherever a numeric function is legal.

## Description

`INT(` returns the floor of a number — the greatest integer that is less than or equal to the argument.

- **Positive numbers**: truncates toward zero (same as `FIX(`)
- **Negative numbers**: rounds away from zero (unlike `FIX(` which truncates toward zero)

## Examples

```kcml
: DIM x
: x = INT(3.7)
: PRINT "INT(3.7)="; x
: x = INT(-3.7)
: PRINT "INT(-3.7)="; x
: $END
```

Output:
```
INT(3.7)= 3
INT(-3.7)=-4
```

### Comparison with FIX(

| Expression | `INT(` | `FIX(` |
|------------|--------|--------|
| `3.7` | 3 | 3 |
| `-3.7` | **-4** | -3 |
| `3.0` | 3 | 3 |
| `-3.0` | -3 | -3 |

### Common uses

```kcml
REM Scale a random number to a range:
Random = INT(RND(1) * 10000)

REM Integer arithmetic:
Texting = 100 + INT(12 * Variable)

REM Round to nearest integer:
Rounded = INT(x + 0.5)
```

## Notes

- `INT(` always rounds down (toward negative infinity). Use `FIX(` for C-style truncation toward zero.
- To round to nearest: `INT(x + 0.5)`.
- For rounding to N decimal places: `INT(x * 10^N + 0.5) / 10^N`.

## See Also

- `FIX(` — truncate toward zero (C-style)
- `ABS(` — absolute value
- `RND(` — random number
