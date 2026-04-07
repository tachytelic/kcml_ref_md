# SGN(

> Returns the sign of a numeric expression: -1, 0, or 1.

## Syntax

```
SGN(numeric_expr)
```

## Description

Returns:
- `-1` if `numeric_expr < 0`
- `0` if `numeric_expr = 0`
- `1` if `numeric_expr > 0`

## Examples

```kcml
PRINT SGN(-42)    : REM  -1
PRINT SGN(0)      : REM   0
PRINT SGN(100)    : REM   1
```

```kcml
REM Use to normalise direction
abc = SGN(result)
Second = test * SGN(totals(count) * 10)
```

## See Also

- `ABS(` — absolute value
- `INT(` — floor integer
