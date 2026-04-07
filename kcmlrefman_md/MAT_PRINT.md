# MAT PRINT (PRINT array)

> Prints the contents of an array in row-by-row format.

## Syntax

```
PRINT array() [, array() ...]
MAT PRINT array() [; array() ...]
PRINT TO buffer$, array()
```

The `MAT PRINT` form is deprecated; use `PRINT array()` instead.

## Description

Displays each element of the array on a new line, row by row. For 2D arrays, each row is displayed left to right.

### PRINT TO form

Appends formatted output to a string buffer. The first two bytes of `buffer$` hold a binary count of bytes written (initialise to `HEX(00)` before the first call). The first character is inserted at byte 3.

## Example

```kcml
DIM test(2,2)
test() = CON
PRINT test()
REM Output:
REM  1  1
REM  1  1
```

## Notes

- `MAT PRINT` is deprecated; KCML automatically rewrites it to `PRINT array()`.
- Numeric arrays print in KCML's standard numeric format.

## See Also

- `PRINT` — general print statement
- `MAT_assignment` — copy array
