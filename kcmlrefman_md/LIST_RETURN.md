# LIST RETURN

> Shows execution status: current line, recently loaded programs, loaded modules, selected globals, and the return stack.

## Syntax

```
LIST [title] [LOCAL] RETURN
```

With `LOCAL`: also inserts `LIST LOCAL` output after each subroutine call in the stack, and lists matching normal variables at the end.

## Description

Displays:
- Currently executing line and statement number
- Last 10 programs loaded
- Loaded modules
- Currently selected global partition
- Return stack (call chain)

In the KCML Workbench, available as the LIST RETURN menu option.

## See Also

- `LIST LOCAL` — local variables in the current subroutine
- `$PROG` — program info system variable
- `LIST` — overview of LIST commands
