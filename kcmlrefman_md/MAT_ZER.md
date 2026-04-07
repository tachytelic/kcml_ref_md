# MAT ZER (array = ZER)

> Sets all elements of a numeric array to zero.

## Syntax

```
[MAT] numeric_array = ZER [(dim1 [, dim2])]
```

The `MAT` keyword is optional and deprecated — the bare form is preferred.

## Description

Sets every element of the numeric array to zero. Optionally redimensions the array at the same time.

## Examples

```kcml
: DIM a(3)
: a() = ZER
: PRINT "a(1)="; a(1)    REM 0
: $END
```

Output: `a(1)= 0`

With redimension:
```kcml
a() = ZER(5)           REM resize to 5 and zero-fill
first() = ZER(second, third)   REM 2D redimension
```

## Notes

- To free allocated space before redimensioning: `a() = ZER(0)` then `a() = ZER(new_size)`.
- Equivalent to looping `FOR i = 1 TO DIM(a(),1) : a(i) = 0 : NEXT i` but faster.

## See Also

- `MAT CON` — set all elements to 1
- `MAT REDIM` — resize an array
- `DIM` — declare an array
