# MAT IDN (array = IDN)

> Creates an identity matrix: diagonal elements = 1, all others = 0.

## Syntax

```
[MAT] numeric_array = IDN [(dim1 [, dim2])]
```

The array must be square (dim1 == dim2), otherwise an error occurs.

## Description

Sets the identity matrix pattern in the receiver array. Optionally redimensions.

## Example

```kcml
DIM matrix(3,3)
matrix() = IDN
REM Result:
REM 1 0 0
REM 0 1 0
REM 0 0 1
```

## See Also

- `MAT CON` — all ones
- `MAT ZER` — all zeros
- `MAT INV` — matrix inverse
