# SYMNAME(

> Returns the name of the variable or subroutine corresponding to a SYM index.

## Syntax

```
name$ = SYMNAME(index)
```

## Description

Looks up the variable or subroutine name for a symbol index previously obtained with `SYM(`. Primarily used during debugging to display what a SYM index refers to.

## Examples

```kcml
DIM count, n
count = 0
n = SYM(count)
PRINT SYMNAME(n)    : REM  count
```

```kcml
REM Debug: inspect a SYM value
DIM ki_sym
ki_sym = SYM(rec$)
PRINT "SYM refers to: "; SYMNAME(ki_sym)
```

## Notes

- Generally only used for debugging — not needed in production code.
- Returns an empty string if the index is invalid or no longer valid.

## See Also

- `SYM(` — get the index of a variable or subroutine
