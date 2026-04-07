# ON ERROR

> Legacy error capture — stores error information in variables instead of raising an exception.

## Syntax

```
ON ERROR var1, var2 GOTO line
ON ERROR GOTO line
ON ERROR GOTO 0
```

## Description

Installs a runtime error handler. When a KCML runtime error occurs:

1. `var1` receives the error code (numeric).
2. `var2` receives the error string / message.
3. Execution jumps to `line`.

`ON ERROR GOTO 0` cancels the current error handler, restoring the default behaviour (panic/abort on error).

`ON ERROR GOTO line` without variables still traps the error but does not capture the code or message.

### Error variables

After a trapped error the error code and message can also be read via `$ERR` (numeric) and `$ERRTEXT$` (string) system variables.

## Examples

```kcml
DIM errcode, errmsg$80
ON ERROR errcode, errmsg$ GOTO 9000
OPEN #1, "/nonexistent/file", "r"
CLOSE #1
$END

9000 PRINT "Error"; errcode; "–"; TRIM(errmsg$)
     ON ERROR GOTO 0
     $END
```

```kcml
REM Suppress errors for optional file open
DIM ok
ok = 1
ON ERROR ok GOTO skip_err
OPEN #5, "optional.dat", "r"
GOTO skip_err
skip_err:
ON ERROR GOTO 0
IF ok <> 1 THEN PRINT "File not found — skipping"
```

## Notes

- **Superseded** by `TRY / CATCH / END TRY` in modern KCML — prefer TRY/CATCH in new code.
- `ON ERROR GOTO 0` **must** be called inside the error handler before leaving it; otherwise any subsequent error is silently ignored.
- The handler is active per-program; it is not inherited by subroutines called from within a handler.
- `$ERR` and `$ERRTEXT$` hold the most recent error regardless of whether an ON ERROR handler is active.

## See Also

- `TRY / CATCH` — structured exception handling (preferred)
- `$ERR` — current error code
- `PANIC` — force a panic dump
