# CONTINUE RETURN (command)

> Resumes a stopped program and halts it again immediately after the next `RETURN` from the most recent `GOSUB`.

## Syntax

```
CONTINUE RETURN
```

## Description

A Workbench debugging command. Restarts a halted program and automatically stops it immediately after the `RETURN` statement that completes the current `GOSUB` call. Useful for stepping out of a subroutine and inspecting the state on return.

Can be executed as a single keystroke or from the toolbar in the KCML Workbench.

## See Also

- `CONTINUE` (command) — resume without a breakpoint
- `CONTINUE LOAD` — stop before next LOAD
- `CONTINUE LOOP` — stop before next WEND/UNTIL
- `CONTINUE NEXT` — stop before next NEXT
- `STOP`, `TRAP` — statements that halt execution
- `GOSUB`, `RETURN` — subroutine call/return
