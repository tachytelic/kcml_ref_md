# SELECT D/R/G (trigonometric mode)

> Sets the angle unit for trigonometric functions: Degrees, Radians, or Gradians.

## Syntax

```
SELECT DEGREES
SELECT RADIANS
SELECT GRADIANS
SELECT D
SELECT R
SELECT G
```

## Description

Controls the unit used by `SIN(`, `COS(`, `TAN(`, `ASIN(`, `ACOS(`, `ATN(`.

| Mode | Unit |
|------|------|
| `RADIANS` (default) | Radians (2π = full circle) |
| `DEGREES` | Degrees (360 = full circle) |
| `GRADIANS` | Gradians / grads (400 = full circle) |

The mode resets to RADIANS after `CLEAR` or `SELECT R`.

## Examples

```kcml
SELECT RADIANS
PRINT SIN(120)        : REM   0.5806111842123

SELECT GRADIANS
PRINT SIN(120)        : REM   0.9510565162952

SELECT DEGREES
PRINT SIN(120)        : REM   0.8660254037844
```

```kcml
REM Common usage: degrees for business calculations
SELECT DEGREES
DIM angle
angle = 45
PRINT SIN(angle)      : REM   0.7071067811865
```

## Notes

- The default is **radians**; always set the mode explicitly if your code uses degrees.
- A `CLEAR` statement resets to radians.

## See Also

- `SIN(` / `COS(` / `TAN(` — trigonometric functions
- `ATN(` — arctangent
- `SELECT` — overview
