# THROW ERR

> Forces a runtime error, typically to re-raise an error within TRY/CATCH blocks.

## Syntax

```
THROW ERR integer_expr
THROW ERR                  (rethrow current error, only inside CATCH)
```

## Description

Raises the specified error number as a runtime error. The error can be caught by an enclosing `TRY/CATCH` block.

Valid error numbers:
- **1–99**: KCML system errors.
- **1000–9999**: User-defined errors. Use the constant `_KCML_USER_ERROR`.

`THROW ERR` without an argument (inside a `CATCH` block) re-raises the current error, including any minor error code information — used to pass errors to an outer handler.

If there is no enclosing `TRY/CATCH` handler, the thrown error becomes a runtime error (PANIC or Workbench entry).

All errors thrown with `THROW ERR` are considered **recoverable** and can be caught.

**Requires `$COMPLIANCE` level 2 or above** (KCML 6.20+).

## Examples

```kcml
REM Re-throw to outer handler
TRY
  REM ... inner code ...
CATCH
  DIM errcode
  errcode = ERR
  IF errcode == 82 THEN DO
    REM handle here
  ELSE
    THROW ERR errcode    : REM  pass to outer TRY
  END DO
END TRY
```

```kcml
REM User-defined error
THROW ERR _KCML_USER_ERROR
```

```kcml
REM Rethrow current error
TRY
  REM ...
CATCH
  PRINT "Logged error: "; ERR
  THROW ERR              : REM  rethrow with original minor code
END TRY
```

## Notes

- Introduced in KCML 6.20 as part of the `TRY/CATCH` facility.
- Use `ON ERROR` for KCML versions before 6.20.

## See Also

- `TRY / CATCH` — structured exception handling
- `ON ERROR` — legacy error capture
- `ERR` — current error number
- `_KCML_USER_ERROR` — constant for user errors (1000+)
