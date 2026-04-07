# TRUE / FALSE

> Numeric constants: TRUE = 1, FALSE = 0.

## Description

`TRUE` and `FALSE` are built-in numeric constants. Any numeric variable can hold a true/false value:

```kcml
flag = TRUE     : REM  flag = 1
flag = FALSE    : REM  flag = 0
```

Used for readable conditionals and infinite loops:

```kcml
IF flag == TRUE THEN PRINT "Yes"
WHILE TRUE DO
  REM  ...
WEND
```

`BOOL(x)` converts any numeric to `TRUE` (if non-zero) or `FALSE` (if zero).

## Examples

```kcml
DIM found
found = FALSE
FOR i = 1 TO 10
  IF arr(i) == target THEN found = TRUE : BREAK
NEXT i
IF found == TRUE THEN PRINT "Found at "; i
```

```kcml
REM Infinite loop with BREAK
WHILE TRUE DO
  LINPUT "Command: ", cmd$
  IF TRIM(cmd$) == "QUIT" THEN BREAK
  'Process(cmd$)
WEND
```

## Notes

- `TRUE = 1`, `FALSE = 0` — numerically.
- `BOOL(x)` returns TRUE if `x <> 0`, FALSE if `x = 0`.
- Comparison operators return TRUE (1) or FALSE (0).

## See Also

- `FALSE` — same page (FALSE = 0)
- `BOOL(` — convert numeric to TRUE/FALSE
- `WHILE` — loop with condition
