# LIST TRAP

> Lists all currently active TRAP breakpoints (including watchpoints and subroutine traps).

## Syntax

```
LIST [title] TRAP [*]
```

With `*`: lists the full statement text at each trap location (program must be resolved).

## Description

Shows all active TRAPs by line and statement number. With `*`, also shows the full source of each trapped line.

```
LIST TRAP *
 LINE  STAT
 ----  ----
 00010 FOR count=1 TO length
 09000 :::STR(beta$,2,3)=code$

 SUBROUTINE
 ----------
 'GET
 00030 :::DEFFN'open_file(fd, name$, p) - executes

 VARIABLE
 --------
 BA$
```

In the KCML Workbench, trapped lines are flagged in the left-hand margin.

## See Also

- `TRAP` — set a breakpoint
- `LIST` — overview of LIST commands
