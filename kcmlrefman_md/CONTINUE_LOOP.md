# CONTINUE LOOP (command)

> Resumes a stopped program and halts it again before the next `WEND` or `UNTIL` that ends the current `WHILE` or `REPEAT` loop.

## Syntax

```
CONTINUE LOOP
```

## Description

A Workbench debugging command. Restarts a halted program and automatically stops it just before the loop-closing statement (`WEND` or `UNTIL`) of the current loop iteration. Useful for inspecting variables at the end of each loop pass.

Can be executed as a single keystroke or from the toolbar in the KCML Workbench.

## See Also

- `CONTINUE` (command) — resume without a breakpoint
- `CONTINUE LOAD` — stop before next LOAD
- `CONTINUE NEXT` — stop before next NEXT
- `CONTINUE RETURN` — stop after next RETURN
- `STOP`, `TRAP` — statements that halt execution
