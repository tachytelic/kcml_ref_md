# RESTORE

> Resets the DATA pointer so READ statements can re-read DATA values.

## Syntax

```
RESTORE
RESTORE line_number
RESTORE LINE line_number [, n]
RESTORE n
```

## Description

Resets the pointer used by `READ` to read from `DATA` statements.

| Form | Effect |
|------|--------|
| `RESTORE` | Reset to first value of first DATA statement |
| `RESTORE line` | Reset to first value of DATA at `line` |
| `RESTORE LINE line` | Same as above |
| `RESTORE LINE line, n` | Set pointer to nth value of DATA at `line` |
| `RESTORE n` | Set pointer to nth value in the entire program (1-based) |

`RUN` and `LOAD` also reset the data pointer to the first DATA value.

## Examples

```kcml
FOR pass = 1 TO 3
  RESTORE
  READ x, y
  PRINT x + y
NEXT pass
DATA 10, 20
REM  Prints 30 three times
```

```kcml
REM Jump to a specific DATA line
RESTORE 5000
READ item$
DATA 5000 "APPLE", "BANANA", "CHERRY"
```

```kcml
REM Jump to 3rd value in program's DATA
RESTORE 3
READ val
DATA 100, 200, 300, 400
REM  val = 300
```

## Notes

- `RESTORE LINE line, n` counts values within the named DATA statement from 1.
- After `RESTORE n` (no LINE), `n` counts across all DATA values in the program.
- Using `RESTORE` without parameters always goes back to the very first DATA value, regardless of which DATA statements exist.

## See Also

- `READ` — read values from DATA
- `DATA` — define constant data
