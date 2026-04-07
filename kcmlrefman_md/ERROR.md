# ERROR

> Traps a recoverable runtime error from the immediately preceding statement and executes an alternative block.

## Syntax

```
statement : ERROR DO
    ...
END DO
```

Or inline (single-statement error handler):
```
statement : ERROR statement
```

## Description

`ERROR` is placed **immediately after** the statement it protects (on the same logical line, after a `:`). When that statement fails with a recoverable error, `ERROR` suppresses the normal error response and executes the body of the `DO` group (or the single statement).

If **no error** occurred, execution continues with the statement **after** the `DO` group (skipping the error handler body).

`ERROR` can only handle **recoverable** errors (typically error codes 48 and 65–99). Fatal errors cannot be trapped. Whether an error is recoverable or fatal can be found in `berror.d`.

Errors suppressed with `SELECT ERROR` are **not** detectable by `ERROR`.

### Modern alternative

For new code, use the structured `TRY ... CATCH ... END TRY` mechanism (KCML 6.20+) instead. `ERROR` is not allowed at `$COMPLIANCE` level 3 or above.

## Example

### File open with error trap

```kcml
LOAD program$ : ERROR DO
    action = junk
    'DisplayError()
END DO
```

### Inline single-statement handler

```kcml
CONVERT str$ TO num : ERROR PRINT "Bad number: "; str$
```

## Notes

- `ERROR` must immediately follow the statement being protected (no intervening statements).
- The error body is only executed if an error occurred in the preceding statement.
- `ERR` inside the error handler contains the error code.
- Multiple `ERROR DO` blocks can appear in a program; each protects only its immediately preceding statement.
- Prefer `TRY/CATCH` for new code — it is cleaner and works at higher `$COMPLIANCE` levels.

## See Also

- `TRY` / `CATCH` / `END TRY` — structured error handling (KCML 6.20+, preferred)
- `ON ERROR` — set a global error handler
- `ERR` — error code of the last error
- `ERR$(` — descriptive text for an error code
- `SELECT ERROR` — suppress specific errors globally
- `DO` / `END DO` — statement grouping
