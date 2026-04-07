# MAT subtraction (array - array)

> Subtracts two numeric arrays element-by-element into a receiver array.

## Syntax

```
receiver() = array2() - array3()
```

Both source arrays must have the same dimensions.

## Example

```kcml
DIM a(3), b(3), c(3)
a() = CON                    REM a = [1, 1, 1]
b(1)=3 : b(2)=3 : b(3)=3
c() = b() - a()              REM c = [2, 2, 2]
```

## See Also

- `MAT_addition` — add arrays
- `MAT_multiplication` — multiply arrays
