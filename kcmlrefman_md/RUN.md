# RUN

> Starts execution of the program currently in memory.

## Syntax

```
RUN
RUN line_number
RUN line_number, statement_number
RUN STOP
```

## Description

`RUN` resolves and executes the in-memory program. Resolution:
1. Scans for syntax errors; verifies line numbers, variables, `WHILE/WEND`, `REPEAT/UNTIL`, and `IF/END IF` pairs.
2. Closes any auto-allocated open streams and KISAM handles.
3. Allocates space for undeclared variables (numerics → 0, strings → spaces).
4. Sets the `READ`/`DATA` pointer to the first `DATA` value.

| Form | Effect |
|------|--------|
| `RUN` | Clears all non-COM variables, resolves, and runs from first line |
| `RUN line` | Resolves without clearing variables; runs from `line` |
| `RUN line, stmt` | Resolves without clearing; starts at statement `stmt` of `line` |
| `RUN STOP` | Resolves but stops before executing (check for resolve errors) |

`RUN` can also be used as a statement inside a program to restart it (equivalent to pressing HALT and entering RUN in immediate mode).

## Examples

```kcml
RUN                   : REM  start from beginning, clear variables
RUN 1200              : REM  start from line 1200 (variables preserved)
RUN 9000, 7           : REM  start at 7th statement of line 9000
RUN STOP              : REM  resolve only — don't execute
```

```kcml
REM Use in a program to force restart
1900 RUN
```

## Notes

- `RUN` without a line number clears **all non-COM variables** — COM variables survive.
- `RUN line` preserves variable values (useful for re-running after a breakpoint).
- Cannot jump into the middle of a `FOR … NEXT` loop or subroutine with `RUN line`.
- To execute a different program entirely, use `LOAD RUN`.

## See Also

- `LOAD RUN` — load and run a program
- `CONTINUE` — resume a halted program
- `LOAD` — load a program without running
