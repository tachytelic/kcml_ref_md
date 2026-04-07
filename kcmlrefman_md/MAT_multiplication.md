# MAT multiplication (array * array or scalar * array)

> Multiplies two numeric arrays (matrix multiplication) or a scalar by an array.

## Syntax

```
receiver() = array1() * array2()         REM matrix multiplication
receiver() = (scalar_expr) * array()     REM scalar multiplication
```

The scalar expression must be in parentheses.

## Description

**Scalar multiplication**: multiplies every element by the scalar. Array dimensions must match between source and receiver.

**Matrix multiplication**: standard matrix product. Dimensions must be compatible:
- Columns of `array1` must equal rows of `array2`
- `receiver` rows = `array1` rows; `receiver` columns = `array2` columns

## Examples

```kcml
: DIM a(2), b(2)
: b(1)=5 : b(2)=10
: a() = (100) * b()
: PRINT "a(1)="; a(1)    REM 500
: $END
```

Output: `a(1)= 500`

```kcml
REM Matrix product
DIM result(2,2), m1(2,3), m2(3,2)
result() = m1() * m2()
```

## See Also

- `MAT_addition` — element-by-element addition
- `MAT INV` — matrix inverse
- `MAT TRN` — transpose
