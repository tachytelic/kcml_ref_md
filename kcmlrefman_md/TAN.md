# TAN(

> Calculates the tangent of a numeric expression.

## Syntax

```
TAN(numeric_expr)
```

## Description

Returns the tangent of the angle. The unit (radians, degrees, gradians) is set by `SELECT R/D/G`. Default is radians.

## Examples

```kcml
PRINT TAN(0.785398)     : REM  ≈ 1.0  (π/4 radians = 45°)
```

```kcml
SELECT DEGREES
PRINT TAN(45)           : REM   1.0
PRINT TAN(0)            : REM   0.0
```

```kcml
Test = TAN(0.723)
Value = 17 + TAN(ABS(temp))
```

## Notes

- `TAN(π/2)` (90°) is undefined — returns a very large number.
- Use `ATN(` for the inverse.

## See Also

- `SIN(` / `COS(` — other trigonometric functions
- `ATN(` — arctangent (inverse tangent)
- `SELECT D/R/G` — set angle unit
