# MAT INV (array = INV)

> Computes the inverse of a square numeric matrix using the Gauss-Jordan method.

## Syntax

```
[MAT] receiver = INV(array) [det [, ndet]]
```

| Element | Description |
|---------|-------------|
| `array` | Source square matrix |
| `det` | Optional numeric receiver — set to the determinant |
| `ndet` | Optional numeric receiver — set to the normalised determinant |

## Description

Assigns the inverse of `array` to `receiver`. The same array can appear on both sides. The receiver is automatically resized to match the source.

The matrix must be:
- Square (dim1 == dim2)
- Non-singular (determinant ≠ 0)

Uses Gauss-Jordan elimination with maximum pivoting.

## Examples

```kcml
MAT abc = INV(xyz), det, ndet
abc() = INV(xyz()), dt1, dt2
```

## See Also

- `MAT IDN` — identity matrix
- `MAT TRN` — transpose
- `MAT_multiplication` — matrix multiplication
