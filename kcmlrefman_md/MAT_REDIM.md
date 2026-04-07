# MAT REDIM

> Resizes an array at runtime.

## Syntax

```
MAT REDIM array_name(dim1 [, dim2])[length] [, ...]
```

## Description

Changes the dimensions of an array. The new size may be larger or smaller than the original.

- **Growing**: allocates new memory, copies existing content, frees old allocation. Can be expensive.
- **Shrinking**: only changes the dimension record; memory is not freed and content outside the new bounds remains unchanged.

To actually **free** memory from a shrunken array: redim to zero first, then to the new size.

### Memory management pattern for COM buffers

```kcml
COM buf$0         REM declare with zero size — no allocation
MAT REDIM buf$(1000)   REM allocate when needed
REM ... use buf$ ...
MAT REDIM buf$(0)      REM free memory when done
```

## Examples

```kcml
: DIM a(3)
: MAT REDIM a(5)
: PRINT "DIM="; DIM(a(),1)    REM 5
: $END
```

Output: `DIM= 5`

```kcml
MAT REDIM list$(count)80     REM resize string array
MAT REDIM matrix(rows, cols) REM 2D resize
```

## Notes

- `LOCAL DIM` variables can also be resized with `MAT REDIM`.
- For string scalars, use `REDIM var = expr` (the assignment form) instead.
- Redim to 0 then to new size to free surplus memory: `a() = ZER(0) : a() = ZER(new)`.

## See Also

- `DIM` — initial declaration
- `MAT ZER` — zero-fill (can include redimension)
- `LOCAL DIM` — local variables in subroutines
- `DIM(` — query array dimensions
