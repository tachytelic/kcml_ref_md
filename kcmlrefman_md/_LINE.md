# #LINE

> Returns the line number of the currently executing statement.

## Syntax

```
#LINE
```

## Description

Returns the line number of the currently executing KCML statement. Useful for error reporting and debugging.

Special cases:
- **After STOP, TRAP, or an error**: returns the line number of the *next* statement that would have been executed.
- **Program not running or fully completed**: returns `0`.

## Examples

```kcml
DIM ln
ln = #LINE
PRINT "Executing at line "; ln
```

```kcml
REM Report current position in error handler
ON ERROR DO
  PRINT "Error at line "; #LINE; " statement "; #STAT
END DO
```

```kcml
REM Defensive check — confirm program has run
IF #LINE == 0 THEN PRINT "No active program"
```

## Notes

- `#LINE` reflects the line number at the time it is evaluated — in a subroutine, it returns the line in the subroutine, not the calling line.
- Use `#STAT` to get the statement number *within* the current line.
- In `-p` script mode, all statements share line 0 (no line numbers exist); `#LINE` will return `0`.

## See Also

- `#STAT` — statement number within the current line
- `LIST RETURN` — list the return address stack
