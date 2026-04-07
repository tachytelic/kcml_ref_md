# LIST '

> Finds all references to a subroutine label (DEFSUB'/DEFFN'/$DECLARE') in the program.

## Syntax

```
[@]LIST [title] ' [subroutine_name [*]]
```

## Description

Without a subroutine name: lists all subroutine labels in the program.
With a name: lists the definition and all call sites.
With `*`: shows full statement text for definition and all calls.

```
LIST 'open_file$ *
1000 DEFFN'  open_file$(handle, name$, initial$())
       -  00100 :::'Open_file$(fd,tmp$,nm$())
       -  00900 ::a$='Open_file$(newfd,tmp$,user$)

LIST 'open_file$
01000 DEFFN'  OPEN_FILE$
     - 00100 00900
```

Supports the same wildcard patterns as `LIST DIM`.

## Examples

```kcml
LIST '
@LIST '16
LIST 'numeric
LIST '"sort_f????"
@LIST title$ 'openfile$ *
```

## See Also

- `DEFSUB` — define a subroutine
- `DEFFN` — define a function
- `LIST FROM'` — list from the start of a subroutine
- `LIST V` — find variable references
