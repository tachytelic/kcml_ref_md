# MAT addition (array + array)

> Adds two numeric arrays element-by-element into a receiver array.

## Syntax

```
receiver() = array2() + array3()
```

Both source arrays must have the same dimensions. The receiver is automatically resized to match.

## Example

```kcml
: DIM a(3), b(3), c(3)
: b() = CON           REM b = [1, 1, 1]
: a() = ZER           REM a = [0, 0, 0]
: c() = b() + a()
: PRINT "c(1)="; c(1)  REM 1
: $END
```

Output: `c(1)= 1`

## See Also

- `MAT_subtraction` — subtract arrays
- `MAT_multiplication` — multiply arrays / scalar multiply
