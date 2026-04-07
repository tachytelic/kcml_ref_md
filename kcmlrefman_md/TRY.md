# TRY / CATCH / END TRY

> Structured exception handling — catches runtime errors in a block of code.

## Syntax

```
TRY
  statements
[CATCH ERR error_code [, error_code ...]]
  statements
[CATCH]
  statements
END TRY
```

## Description

`TRY` / `CATCH` provides structured error handling (KCML 6.20+, `$COMPLIANCE` level 1+).

- Code between `TRY` and the first `CATCH` is protected.
- `CATCH ERR n` handles specific error codes (1–99 for KCML errors, 1000–9999 for user errors).
- `CATCH` (no ERR) is the catch-all; must be last.
- At least one `CATCH` or `CATCH ERR` clause is required.
- Multiple `CATCH ERR` clauses are allowed; only one bare `CATCH`.

`TRY` blocks nest — an unhandled error propagates to the nearest outer `TRY/CATCH`.

`THROW ERR` re-raises an error to an outer handler.

`$COMPLIANCE` level 3+ deprecates `ON ERROR` and `ERROR DO` in favour of `TRY/CATCH`.

## Examples

```kcml
TRY
  OPEN #1, "/tmp/data.dat", "r"
  LINPUT #1, line$
  CLOSE #1
CATCH ERR 80
  PRINT "File not found"
CATCH
  PRINT "Unexpected error: "; ERR
END TRY
```

```kcml
REM Nested TRY blocks
DEFSUB 'DoSums(a, b)
  LOCAL DIM r
  TRY
    r = 'divide(a, b)
  CATCH
    'log_error(ERR)
    r = 0
  END TRY
  RETURN r
END SUB

DEFSUB 'divide(quotient, divisor)
  LOCAL DIM dividend
  TRY
    dividend = quotient / divisor
  CATCH ERR 62
    REM division by zero → infinity
    dividend = 9E99
  CATCH ERR 63
    REM zero / zero = 0
    dividend = 0
  END TRY
  RETURN dividend
END SUB
```

```kcml
REM Re-throw to outer handler
TRY
  REM ...
CATCH
  IF ERR == 82 THEN DO
    REM handle here
  ELSE
    THROW ERR         : REM  rethrow current error
  END DO
END TRY
```

## Notes

- Error codes in `CATCH ERR` expressions are evaluated at **resolve time** (like `DIM` expressions).
- `_KCML_USER_ERROR` is the constant for user-defined error numbers (1000+).
- In the Workbench, runtime errors in `TRY` blocks still stop execution at the error point; `CONTINUE` then enters the `CATCH` block.
- `TRY/CATCH` introduced in KCML 6.20. Use `ON ERROR` for older versions.

## See Also

- `THROW ERR` — raise or re-raise an error
- `ON ERROR` — legacy error handling
- `ERR` — current error number
- `SELECT ERROR` — suppress computational errors
