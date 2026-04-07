# RETURN CLEAR

> Clears the most recent subroutine return stack entry without returning to the caller.

## Syntax

```
RETURN CLEAR
RETURN CLEAR ALL
```

## Description

`RETURN CLEAR` discards the most recent `GOSUB` / `GOSUB'` stack entry (and any associated `FOR … NEXT` information). Execution continues with the statement immediately after `RETURN CLEAR` — it does **not** jump back to the caller.

`RETURN CLEAR ALL` clears all subroutine, local variable, and `FOR … NEXT` information from the entire return stack.

### KCML 5+ restriction

In KCML 4.0, `RETURN CLEAR` was sometimes used to exit a function called inside an arithmetic expression (e.g. `a = 2 + 'sub()`). This left data on KCML's internal arithmetic stack and would eventually cause a stack overflow in a loop. KCML 5.0+ detects this and raises a **P41.6** error.

To restore the old (unsafe) KCML 4 behaviour: set the `COMPAT40` environment variable, or set byte 38 of `$OPTIONS RUN`.

## Examples

```kcml
REM Abandon a subroutine cleanly
GOSUB 1000
PRINT "After subroutine"
$END

1000 IF some_condition THEN RETURN CLEAR
     REM  ... normal subroutine body ...
     RETURN
```

```kcml
REM Clear all nested returns (emergency exit pattern)
RETURN CLEAR ALL
$END
```

## Notes

- Use `RETURN CLEAR` sparingly — it breaks the structured call/return model.
- Prefer `BREAK` for exiting loops, and `RETURN` or `TRY/CATCH` for error handling.
- `RETURN CLEAR ALL` is useful in error recovery when the call stack depth is unknown.

## See Also

- `RETURN` — normal subroutine return
- `GOSUB` — call a subroutine
- `TRY / CATCH` — structured error handling
