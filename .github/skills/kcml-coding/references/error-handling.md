# KCML Error Handling Reference

Complete reference for error handling in KCML programs.

## Modern Error Handling: TRY/CATCH

The recommended way to handle errors in KCML 6.20+ is with TRY/CATCH blocks.

### Basic Syntax

```kcml
TRY
:   REM Code that might fail
:   risky_operation()
: CATCH ERR error_code
:   REM Handle specific error
: CATCH
:   REM Handle any other error
: END TRY
```

### Complete Example

```kcml
DEFSUB 'safe_divide(a, b)
:   LOCAL DIM result
:   TRY
:     result = a / b
:   CATCH ERR 62
:     REM Division by zero - return infinity
:     result = 9E99
:   CATCH ERR 63
:     REM Zero divided by zero
:     result = 0
:   END TRY
:   RETURN result
: END SUB
```

```kcml
DIM answer
: TRY
:    answer = 10 / 0
: CATCH ERR 62
:    PRINT "Division by zero caught"
:    answer = 0
: END TRY
: PRINT answer
: $END
```
<!-- UNTESTED -->

```kcml
DIM ec
: TRY
:    OPEN #1, "nonexistent.txt", "r"
: CATCH
:    ec = ERR
:    PRINT "Error "; ec; ": "; ERR$(ec)
: END TRY
: $END
```
<!-- UNTESTED -->

### Catching Multiple Error Codes

```kcml
TRY
:   OPEN #1, filename$, "r"
: CATCH ERR 82, 83
:   REM 82 = file not found, 83 = permission denied
:   PRINT "Cannot open file"
: CATCH
:   REM Any other error
:   PRINT "Unexpected error: "; ERR
: END TRY
```

```kcml
DIM filename$50, ok
: filename$ = "data.txt"
: ok = 0
: TRY
:    OPEN #1, filename$, "r"
:    ok = 1
: CATCH ERR 82, 83
:    PRINT "File not accessible: "; filename$
: CATCH
:    PRINT "Unexpected open error: "; ERR
: END TRY
: IF ok THEN CLOSE #1
: $END
```
<!-- UNTESTED -->

### Nested TRY Blocks

```kcml
TRY
:   TRY
:     REM Inner operation
:     result = 'risky_calc(value)
:   CATCH ERR 62
:     REM Handle locally
:     result = 0
:   END TRY
:   REM Continue with result
: CATCH
:   REM Handle errors from outer block
:   PRINT "Outer error: "; ERR
: END TRY
```

## THROW ERR - Raising Errors

Use THROW to signal an error condition:

```kcml
THROW ERR error_code
```

### Throwing User-Defined Errors

User error codes range from 1000-9999:

```kcml
REM Define constants for your errors
: DIM _ERR_INVALID_INPUT = 1001
: DIM _ERR_OUT_OF_RANGE = 1002

: DEFSUB 'validate(value)
:   IF (value < 0) THEN DO
:     THROW ERR _ERR_INVALID_INPUT
:   ENDDO
:   IF (value > 1000) THEN DO
:     THROW ERR _ERR_OUT_OF_RANGE
:   ENDDO
: END SUB
```

### Rethrowing Errors

To pass an error to an outer handler:

```kcml
TRY
:   'process_data()
: CATCH
:   errcode = ERR
:   IF (errcode == 82) THEN DO
:     REM Handle file not found locally
:     PRINT "File missing"
:   ELSE DO
:     REM Pass other errors to outer handler
:     THROW ERR errcode
:   ENDDO
: END TRY
```

### Rethrow Current Error

Without arguments, THROW rethrows the current error:

```kcml
TRY
:   risky_operation()
: CATCH
:   'log_error(ERR)
:   THROW ERR  : REM Rethrow to outer handler
: END TRY
```

## ERR Function - Get Error Code

The ERR function returns the most recent error code:

```kcml
errcode = ERR
```

**Important:** ERR is cleared after being read, so copy it immediately:

```kcml
TRY
:   operation()
: CATCH
:   errcode = ERR  : REM Save it first!
:   IF (errcode == 82 OR errcode == 83) THEN DO
:     REM Use the saved value
:   ENDDO
: END TRY
```

## ERR$( Function - Error Message

Get the error message for an error code:

```kcml
message$ = ERR$(errcode)
PRINT "Error: "; ERR$(82)  : REM "file not found"
```

## Common KCML Error Codes

### File Errors

| Code | Description |
|------|-------------|
| 80 (D80) | File not open |
| 82 (P82) | File not found |
| 83 (P83) | Permission denied |
| 96 (I96) | File has read access only |

### Computational Errors

| Code | Description |
|------|-------------|
| 60 (C60) | Numeric overflow |
| 62 (C62) | Division by zero |
| 63 (C63) | Zero divided by zero |
| 64 (C64) | Negative square root |
| 65 (C65) | Log of zero or negative |

### Data Errors

| Code | Description |
|------|-------------|
| 24 (S24) | Illegal expression or missing variable |
| 34 (P34) | Invalid parameter |
| 37 (P37) | Subscript out of range |
| 41 (P41) | Return without gosub |
| 48 (P48) | Data type mismatch |

### User-Defined Errors

| Range | Description |
|-------|-------------|
| 1000-9999 | User-defined error codes |

## Legacy Error Handling (Deprecated)

### ERROR DO Statement

The ERROR statement catches errors on the immediately preceding statement:

```kcml
LOAD program$: ERROR DO
:   PRINT "Load failed"
:   'handle_error()
: ENDDO
```

**Note:** ERROR DO is deprecated in $COMPLIANCE level 3+. Use TRY/CATCH instead.

### ON ERROR Statement

Global error handler (deprecated):

```kcml
ON ERROR error$, line$ GOTO 10000
REM ... program code ...
10000 REM Error handler
: PRINT "Error "; error$; " at line "; line$
```

**Note:** ON ERROR is deprecated. Use TRY/CATCH for modern code.

## Error Recovery Patterns

### Retry with Backoff

```kcml
DIM retries = 3
: success = FALSE
: WHILE (retries > 0 AND NOT success)
:   TRY
:     'connect_to_server()
:     success = TRUE
:   CATCH
:     retries = retries - 1
:     IF (retries > 0) THEN DO
:       PRINT "Retrying..."
:       $BREAK 100  : REM Wait 2 seconds
:     ENDDO
:   END TRY
: WEND
: IF (NOT success) THEN PRINT "Failed after retries"
```

### Cleanup with Error Handling

```kcml
DIM file_open = FALSE
: TRY
:   OPEN #1, "data.txt", "r"
:   file_open = TRUE
:   'process_file()
: CATCH
:   PRINT "Error: "; ERR$(ERR)
: END TRY
: IF (file_open) THEN CLOSE #1  : REM Always cleanup
```

### Error Logging

```kcml
DEFSUB 'log_error(errcode)
:   LOCAL DIM msg$200, timestamp$20
:   timestamp$ = $TODAY & " " & $TIME
:   msg$ = timestamp$ & " Error " & STR$(errcode) & ": " & ERR$(errcode)
:   OPEN #9, "error.log", "a"
:   ret = WRITE #9, msg$ & HEX(0A)
:   CLOSE #9
: END SUB
```

## Error-Safe Subroutine Pattern

```kcml
DEFSUB 'safe_operation(input, BYREF result, BYREF error_code)
:   error_code = 0
:   TRY
:     REM Perform operation
:     result = 'calculate(input)
:   CATCH
:     error_code = ERR
:     result = 0
:   END TRY
: END SUB

REM Usage:
: DIM res, err
: 'safe_operation(value, BYREF res, BYREF err)
: IF (err <> 0) THEN DO
:   PRINT "Operation failed: "; ERR$(err)
: ELSE DO
:   PRINT "Result: "; res
: ENDDO
```

## $COMPLIANCE Levels

Error handling behavior varies by compliance level:

| Level | Behavior |
|-------|----------|
| 0 | All error handling allowed |
| 1 | TRY/CATCH recommended |
| 2 | THROW ERR available |
| 3+ | ERROR DO and ON ERROR disallowed |

Set compliance level:

```kcml
$COMPLIANCE 2
```

## Best Practices

1. **Use TRY/CATCH** - Modern, structured error handling
2. **Save ERR immediately** - It's cleared after reading
3. **Be specific** - Catch specific error codes when possible
4. **Always have a default CATCH** - Prevent unhandled errors
5. **Don't ignore errors** - At minimum, log them
6. **Clean up resources** - Close files, free memory even after errors
7. **Use meaningful error codes** - Define constants for user errors

## See Also

- [file-io.md](file-io.md) - File operation errors
- [subroutines.md](subroutines.md) - Error handling in subroutines
- [control-flow.md](control-flow.md) - IF/ELSE for error checks
