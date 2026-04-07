# #STAT

> Returns the statement number within the current line of the executing statement.

## Syntax

```
#STAT
```

## Description

Returns the statement number (position within the line) of the currently executing KCML statement. KCML allows multiple statements on one line separated by `:`, and `#STAT` identifies which one is active.

- **After STOP or TRAP**: returns the statement number of the *next* statement that would have been executed.
- Useful alongside `#LINE` for precise error location.

## Examples

```kcml
DIM ln, st
ln = #LINE
st = #STAT
PRINT "Line "; ln; " statement "; st
```

```kcml
REM Error handler with full location info
ON ERROR DO
  PRINT "Error at line "; #LINE; " stmt "; #STAT
END DO
```

## Notes

- Statement numbers within a line start at 1.
- In `-p` script mode (no line numbers), `#LINE` is always 0 but `#STAT` still increments across statements.

## See Also

- `#LINE` — current line number
- `LIST RETURN` — list the return address stack
