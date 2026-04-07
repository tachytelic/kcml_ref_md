# LIST LOAD

> Lists all programs currently in memory with their line ranges and modification status.

## Syntax

```
LIST [title] LOAD
```

## Description

Shows each loaded program with:
- Name and file path
- Current line range (after any editing)
- Original line range (as loaded)
- `LOAD` command used
- Whether lines have been added, removed, or the program is "pure" (unchanged)

## Example output

```
LIST LOAD
PROGS/SL/pmenu
now contains lines 10000-19999 originally 10000-19999
loaded with - LOAD "SL/pmenu" 10000,19999
program is pure

PROGS/SL/MENU
now contains lines 1100-3000 originally 1000-2090
loaded with - LOAD "SL/MENU"
program lines have been removed,added
```

## See Also

- `LIST ADD` — show which lines were added/modified
- `LOAD` — load a program into memory
