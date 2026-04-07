# ABS(

> Returns the absolute value of a numeric expression.

## Syntax

```
ABS( numeric_expression )
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | Any numeric expression |

## Description

`ABS(` strips the sign from a number, returning the non-negative magnitude. Valid wherever a numeric function is legal — in assignments, conditions, PRINT, and other numeric contexts.

## Examples

### Basic usage

```kcml
: DIM x, y, z
: x = ABS(-42)
: y = ABS(3.14)
: z = ABS(0)
: PRINT "ABS(-42)="; x
: PRINT "ABS(3.14)="; y
: PRINT "ABS(0)="; z
: $END
```

Output:
```
ABS(-42)= 42
ABS(3.14)= 3.14
ABS(0)= 0
```

### In an expression

```kcml
old_position = ABS(147 * next_position)
IF (ABS(section) <> 24)
```

### Distance calculation

```kcml
: DIM a, b, dist
: a = 10 : b = 7
: dist = ABS(a - b)
: PRINT "Distance="; dist
: $END
```

## See Also

- `SGN(` — returns the sign (-1, 0, or 1) of a number
- `INT(` — truncates to integer
