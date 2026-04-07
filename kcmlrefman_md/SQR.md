# SQR(

> Returns the square root of a numeric expression.

## Syntax

```
SQR(numeric_expr)
```

## Description

Returns the square root of `numeric_expr`. The argument must be non-negative (unless `SELECT ERROR > 66` is set, which returns `SQR(ABS(x))` for negative inputs).

## Examples

```kcml
PRINT SQR(4)       : REM   2.0
PRINT SQR(2)       : REM   1.41421356...
PRINT SQR(100)     : REM  10.0
```

```kcml
result(count) = SQR(test(count))
IF SQR(sample) < 100 THEN PRINT "Small"
temp1, temp2 = 100 + SQR(temp)
```

## Notes

- Passing a negative argument raises error 66 (square root of negative value).
- `SELECT ERROR > 66` suppresses this error and returns `SQR(ABS(x))` instead.

## See Also

- `SELECT ERROR` — suppress computational error 66
- `ABS(` — absolute value
