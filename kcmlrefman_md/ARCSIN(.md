# ARCSIN(

> Returns the arc sine (inverse sine) of a numeric expression.

## Syntax

```
ARCSIN( numeric_expression )
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | A value in the range −1 to 1 |

## Description

`ARCSIN(` calculates the arc sine of its argument. The result is the angle whose sine equals the argument.

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
: d = ARCSIN(0.5)
: PRINT "ARCSIN(0.5) degrees="; d
: SELECT RADIANS
: $END
```

Output:
```
ARCSIN(0.5) degrees= 30
```

### In an expression

```kcml
Test = ARCSIN(.723)
numeric = 17 + ARCSIN(ABS(value))
```

## Notes

- Input must be in the range −1 to 1.
- Default mode is radians; use `SELECT DEGREES` to get degree results.

## See Also

- `SIN(` — sine
- `ARCCOS(` — arc cosine
- `ARCTAN(` — arc tangent
- `SELECT` — set trigonometric mode
