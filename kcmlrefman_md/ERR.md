# ERR

> Returns the error code of the most recent runtime error.

## Syntax

```
ERR
```

Returns a numeric value. Valid wherever a numeric expression is legal.

## Description

`ERR` holds the error code from the most recent recoverable runtime error. After `ERR` is referenced, it is **reset to zero** — so subsequent references return 0.

Typical use: copy `ERR` into a local variable immediately after an error-handling block.

Error codes:
- Two-digit codes (65–99): standard KCML recoverable runtime errors
- Codes 1000–9999: user-defined errors raised with `THROW ERR`

## Examples

### In TRY/CATCH

```kcml
TRY
    'OpenSomeFile()
CATCH
    errcode = ERR
    IF (errcode == 82 OR errcode == 83)
        PRINT "File not found or already exists"
    END IF
END TRY
```

### In ERROR DO block

```kcml
: OPEN #1, "myfile.txt", INPUT
: ERROR DO
:   errcode = ERR
:   PRINT "Open failed, ERR="; errcode
: END DO
: $END
```

### Simple inline check

```kcml
result = ERR
IF (result == 82) THEN PRINT "File not found"
```

## Notes

- `ERR` is cleared to 0 after each read. Copy it to a variable before using it multiple times.
- `ERR$(ERR)` returns the descriptive text for the current error code.
- `$ERR` (from KCML 6.0+) returns the last error message text — equivalent to `ERR$(ERR)`.

## See Also

- `ERR$(` — return descriptive text for an error code
- `$ERR` — last error message text
- `$OSERR` — last OS-level error
- `ERROR` — old-style per-statement error trap
- `TRY` / `CATCH` / `THROW` — structured error handling (KCML 6.20+)
- `ON ERROR` — set a global error handler
