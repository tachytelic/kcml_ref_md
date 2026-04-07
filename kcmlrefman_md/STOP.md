# STOP

> Halts program execution and returns to the KCML editor/debugger.

## Syntax

```
STOP
STOP "message"
STOP #
```

## Description

`STOP` halts execution and enters the Workbench debugger. Used for breakpoints during development.

After stopping:
- Step-through and step-over keys advance execution.
- `CONTINUE` resumes at the statement after `STOP`.

`STOP PANIC ON` makes all subsequent `STOP` statements behave like `PANIC` (write a dump and terminate).

## Examples

```kcml
REM Debug breakpoint
DIM x
x = calculate()
STOP "Check x here"
PRINT x
```

## Notes

- Remove `STOP` statements before deploying to production.
- `STOP PANIC ON` / `STOP PANIC OFF` — see `STOP_PANIC`.
- When `NOPROG` environment variable is set and `STOP PANIC` is active, entering immediate mode causes a PANIC.

## See Also

- `CONTINUE` — resume after STOP
- `STOP PANIC` — treat STOP as PANIC
- `PANIC` — force a dump and terminate
- `TRACE` — execution tracing
