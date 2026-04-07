# ON … SELECT

> Conditional SELECT — executes a SELECT block only when a variable matches.

## Syntax

```
ON var SELECT
  = value1 : statements
  = value2 : statements
  ...
END SELECT
```

## Description

`ON var SELECT` is a variant of `SELECT` that only evaluates when `var` is non-zero (for numerics) or non-blank (for strings). If `var` is zero / empty the entire block is skipped.

Inside the block the syntax is identical to a standard `SELECT` statement: each arm starts with a relational comparison, and the first matching arm executes.

## Examples

```kcml
DIM status, msg$30
status = 2

ON status SELECT
  = 1 : msg$ = "Active"
  = 2 : msg$ = "Suspended"
  = 3 : msg$ = "Closed"
  ELSE : msg$ = "Unknown"
END SELECT

PRINT msg$
```

Output:
```
Suspended
```

```kcml
REM When status=0 the block is skipped entirely
status = 0
msg$ = "Unchanged"
ON status SELECT
  = 1 : msg$ = "Active"
END SELECT
PRINT msg$   : REM  Unchanged
```

## Notes

- Equivalent to `IF var <> 0 THEN SELECT var … END SELECT` but more concise.
- Use plain `SELECT` when the variable will never be zero/blank.
- `ELSE` arm inside the block catches all unmatched cases (only reached when `var` is non-zero).

## See Also

- `SELECT` — standard multi-way conditional
- `ON … GOSUB` — computed branch by index
- `IF/END IF` — structured conditional
