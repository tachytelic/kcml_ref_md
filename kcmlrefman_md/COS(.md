# COS(

> Returns the cosine of a numeric expression.

## Syntax

```
COS( numeric_expression )
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | An angle value |

## Description

`COS(` calculates the cosine of its argument. The unit of the argument depends on the current trigonometric mode:

| Mode | SELECT statement | Argument unit |
|------|-----------------|---------------|
| Radians (default) | `SELECT RADIANS` | Radians |
| Degrees | `SELECT DEGREES` | Degrees |
| Gradians | `SELECT GRADIANS` | Gradians |

Valid wherever a numeric function is legal.

## Examples

### Degrees mode

```kcml
: DIM d
: SELECT DEGREES
: d = COS(60)
: PRINT "COS(60deg)="; d
: d = COS(0)
: PRINT "COS(0deg)="; d
: SELECT RADIANS
: $END
```

Output:
```
COS(60deg)= 0.5
COS(0deg)= 1
```

### Radians mode

```kcml
: DIM r
: r = COS(0)
: PRINT "COS(0rad)="; r
: $END
```

Output: `COS(0rad)= 1`

### In expressions

```kcml
test = COS(.723)
numeric = 17 + COS(ABS(temporary))
```

## See Also

- `ARCCOS(` — inverse cosine
- `SIN(` — sine
- `ARCSIN(` — inverse sine
- `TAN(` — tangent
- `SELECT` — set trigonometric mode
