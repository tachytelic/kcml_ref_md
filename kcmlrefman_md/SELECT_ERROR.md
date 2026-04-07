# SELECT ERROR

> Suppresses system messages for computational errors and returns default values instead.

## Syntax

```
SELECT ERROR > error_code
SELECT ERROR > error_code, PRINT /device
```

## Description

When a computational error in the range 60–69 occurs after `SELECT ERROR`, the error message is suppressed and a default value is returned instead of halting.

`SELECT ERROR > 60` resets to default (no suppression).

### Error codes and default return values

| Code | Condition | Default value returned |
|------|-----------|----------------------|
| 60 | Underflow | 0 |
| 61 | Overflow | +9.999999999999E99 |
| 62 | Division by zero | +9.999999999999E99 |
| 63 | Zero / or ^ zero | 0 |
| 64 | Zero raised to negative power | +9.999999999999E99 |
| 65 | Negative number raised to non-integer power | ABS(A) ^ B |
| 66 | Square root of negative value | SQR(ABS(A)) |
| 67 | Log of zero | -9.999999999999E99 |
| 68 | Log of negative value | LOG(ABS(A)) |
| 69 | Argument too large | 0 |

`SELECT ERROR > 65` suppresses errors 65 through 69; errors 60–64 still raise messages.

The optional `PRINT /device` sends a notification to the specified device even when the error is suppressed.

## Examples

```kcml
SELECT ERROR > 62         : REM  suppress division by zero and above
DIM x, y
y = 0
x = 100 / y              : REM  returns 9.999999999999E99 instead of error
PRINT x
```

```kcml
SELECT ERROR > 60         : REM  reset — all errors raised normally
```

## Notes

- The SELECT ERROR setting is reset to default on `CLEAR` or `LOAD RUN`.
- Use `TRY/CATCH` or `ON ERROR` for more controlled error handling.

## See Also

- `ON ERROR` — legacy error capture
- `TRY / CATCH` — structured exception handling
- `SELECT` — overview
