# #PI

> Returns the mathematical constant pi (3.14159265359).

## Syntax

```
#PI
```

## Description

Returns the value of pi to 11 decimal places: `3.14159265359`. Valid wherever a numeric expression is legal.

## Examples

```kcml
DIM area, radius
radius = 5
area = #PI * radius ^ 2
PRINT area          : REM  78.5398163397
```

```kcml
DIM circumference, diameter
diameter = 10
circumference = #PI * diameter
PRINT circumference : REM  31.4159265359
```

```kcml
IF temp < #PI THEN PRINT "Below pi"
```

## Notes

- `#PI` is a read-only system constant — it cannot be assigned.
- The value uses KCML's default floating-point precision.

## See Also

- `SIN(` — sine
- `COS(` — cosine
- `TAN(` — tangent
- `SQR(` — square root
