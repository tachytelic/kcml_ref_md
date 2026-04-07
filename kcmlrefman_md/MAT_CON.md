# MAT CON (array = CON)

> Sets all elements of a numeric array to one.

## Syntax

```
[MAT] numeric_array = CON [(dim1 [, dim2])]
```

The `MAT` keyword is optional and deprecated.

## Description

Sets every element of the numeric array to 1. Optionally redimensions the array.

## Examples

```kcml
: DIM b(3)
: b() = CON
: PRINT "b(1)="; b(1)    REM 1
: $END
```

With redimension:
```kcml
b() = CON(15, 15)
```

## See Also

- `MAT ZER` — set all elements to zero
- `MAT IDN` — identity matrix (diagonal = 1, rest = 0)
- `MAT REDIM` — resize an array
