# CONTINUE NEXT (command)

> Resumes a stopped program and halts it again immediately before the `NEXT` statement at the end of the current `FOR` loop's final iteration.

## Syntax

```
CONTINUE NEXT
```

## Description

A Workbench debugging command. Restarts a halted program and automatically stops it just before the `NEXT` that would complete the current `FOR ... NEXT` loop. Useful for inspecting the final state of a loop.

Can be executed as a single keystroke or from the toolbar in the KCML Workbench.

## See Also

- `CONTINUE` (command) — resume without a breakpoint
- `CONTINUE LOAD` — stop before next LOAD
- `CONTINUE LOOP` — stop before next WEND/UNTIL
- `CONTINUE RETURN` — stop after next RETURN
- `STOP`, `TRAP` — statements that halt execution
