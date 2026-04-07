# CONTINUE LOAD (command)

> Resumes a stopped program and halts it again immediately before the first statement executed after the next `LOAD`.

## Syntax

```
CONTINUE LOAD
```

## Description

A Workbench debugging command. Restarts a halted program and automatically stops it again at the first statement that runs after a new program is loaded via `LOAD`. Useful for stepping into loaded modules.

Can be executed as a single keystroke or from the toolbar in the KCML Workbench.

## See Also

- `CONTINUE` (command) — resume without a breakpoint
- `CONTINUE LOOP` — stop before next WEND/UNTIL
- `CONTINUE NEXT` — stop before next NEXT
- `CONTINUE RETURN` — stop after next RETURN
- `STOP`, `TRAP` — statements that halt execution
