# SIN(

> Calculates the sine of a numeric expression.

## Syntax

```
SIN(numeric_expr)
```

## Description

Returns the sine of the angle. The unit (radians, degrees, gradians) is set by `SELECT R/D/G`. Default is radians.

## Examples

```kcml
PRINT SIN(0)              : REM   0
PRINT SIN(1.5707963)      : REM   1.0  (π/2 radians = 90°)

SELECT DEGREES
PRINT SIN(90)             : REM   1.0
PRINT SIN(30)             : REM   0.5
PRINT SIN(120)            : REM   0.8660254037844
```

## See Also

- `COS(` — cosine
- `TAN(` — tangent
- `ATN(` — arctangent
- `SELECT D/R/G` — set angle unit
