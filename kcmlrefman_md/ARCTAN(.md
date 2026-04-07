# ARCTAN(

> Returns the arc tangent (inverse tangent) of a numeric expression.

## Syntax

```
ARCTAN( numeric_expression )
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | Any numeric expression |

## Description

`ARCTAN(` calculates the arc tangent of its argument. Unlike `ARCCOS(` and `ARCSIN(`, there is no domain restriction — any numeric value is valid.

The unit of the result depends on the current trigonometric mode, set with `SELECT`:

| Mode | SELECT statement | Result unit |
|------|-----------------|-------------|
| Radians (default) | `SELECT RADIANS` | Radians |
| Degrees | `SELECT DEGREES` | Degrees |
| Gradians | `SELECT GRADIANS` | Gradians |

Valid wherever a numeric function is legal.

## Examples

### Degrees mode

```kcml
: DIM d
: SELECT DEGREES
: d = ARCTAN(1)
: PRINT "ARCTAN(1) degrees="; d
: SELECT RADIANS
: $END
```

Output:
```
ARCTAN(1) degrees= 45
```

(ARCTAN(1) = 45° because tan(45°) = 1)

### In an expression

```kcml
Test = ARCTAN(.723)
numeric = 17 + ARCTAN(ABS(value))
```

## See Also

- `TAN(` — tangent
- `ARCCOS(` — arc cosine
- `ARCSIN(` — arc sine
- `SELECT` — set trigonometric mode
