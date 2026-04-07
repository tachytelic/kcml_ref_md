# MAT TRN (array = TRN)

> Assigns the transpose of a numeric matrix to a receiver array.

## Syntax

```
[MAT] receiver = TRN(array)
```

## Description

Transposes `array` into `receiver`: element `(i,j)` of the source becomes element `(j,i)` of the receiver. The first dimension of `receiver` must match the second dimension of `array`, and vice versa.

## Example

```kcml
DIM array1(3,3), array2(3,3)
REM fill array2 with: 2,5,7, 2,1,9, 7,3,4
array1() = TRN(array2())
REM Result:
REM 2 2 7
REM 5 1 3
REM 7 9 4
```

## See Also

- `MAT INV` — matrix inverse
- `MAT_multiplication` — matrix multiplication
