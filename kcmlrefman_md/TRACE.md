# TRACE

> Enables execution tracing for debugging — logs branches, subroutine calls, and loop activity.

## Syntax

```
TRACE
TRACE ON
TRACE OFF
TRACE start_line, end_line
```

## Description

Turns on execution tracing. Trace output logs:
- GOTO / GOSUB branches and RETURN statements
- FOR…NEXT, WHILE…WEND, REPEAT…UNTIL
- SELECT CASE statements
- Trailing statements on TRAP statements
- Subroutine names, argument values, and nesting indentation

Each logged event includes the line number, statement number, and program name.

By default, trace output goes to the Workbench trace window. Outside the Workbench it goes to `/005` (terminal), which can disrupt screen output. Use `SELECT TRACE "filename"` to redirect to a file.

`TRACE start_line, end_line` — limits tracing to the specified line range. Outside this range, no tracing occurs and Ctrl+BREAK is deferred until inside the range.

`TRACE OFF` or `CLEAR` turns off tracing.

## Examples

```kcml
TRACE ON                         : REM  enable tracing from here
'ProcessOrder(order_no)
TRACE OFF                        : REM  disable tracing

TRACE 1000, 5000                 : REM  trace only lines 1000-5000
```

```kcml
REM Redirect trace output before running
SELECT TRACE "/tmp/trace.log"
TRACE
RUN
```

## Notes

- Remove or disable TRACE statements in production code.
- Trace output to `/005` in non-Workbench mode will corrupt the screen — always use `SELECT TRACE` in scripts.

## See Also

- `SELECT TRACE` — redirect trace output
- `STOP` — halt and enter debugger
- `TRAP` — conditional breakpoints on variables or lines
