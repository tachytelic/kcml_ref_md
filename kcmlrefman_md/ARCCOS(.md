# ARCCOS(

> Returns the arc cosine (inverse cosine) of a numeric expression.

## Syntax

```
ARCCOS( numeric_expression )
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | A value in the range −1 to 1 |

## Description

`ARCCOS(` calculates the arc cosine of its argument. The result is the angle whose cosine equals the argument.

The unit of the result depends on the current trigonometric mode, set with `SELECT`:

| Mode | SELECT statement | Result unit |
|------|-----------------|-------------|
| Radians (default) | `SELECT RADIANS` | Radians |
| Degrees | `SELECT DEGREES` | Degrees |
| Gradians | `SELECT GRADIANS` | Gradians |

Valid wherever a numeric function is legal.

## Examples

### Radians mode (default)

```kcml
: DIM r
: r = ARCCOS(0.5)
: PRINT "ARCCOS(0.5) radians="; r
: $END
```

Output:
```
ARCCOS(0.5) radians= 1.047197551197
```

### Degrees mode

```kcml
: DIM d
: SELECT DEGREES
: d = ARCCOS(0.5)
: PRINT "ARCCOS(0.5) degrees="; d
: SELECT RADIANS
: $END
```

Output:
```
ARCCOS(0.5) degrees= 60
```

### In an expression

```kcml
temp = ARCCOS(.723)
numeric = 17 + ARCCOS(ABS(value))
```

## Notes

- Input must be in the range −1 to 1; values outside this range will produce a runtime error.
- Remember to `SELECT RADIANS` to restore the default mode after using `SELECT DEGREES`.

## See Also

- `COS(` — cosine
- `ARCSIN(` — arc sine
- `ARCTAN(` — arc tangent
- `SELECT` — set trigonometric mode (DEGREES / RADIANS / GRADIANS)
