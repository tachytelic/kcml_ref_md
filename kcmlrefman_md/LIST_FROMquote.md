# LIST FROM'

> Lists from the first line of a named subroutine.

## Syntax

```
[@]LIST [title] FROM 'subroutine-name
```

## Description

Lists the program starting at the first line of the `DEFSUB '` subroutine with the given label. If `@` is used, lists from the currently selected global partition.

In the KCML Workbench, the same operation is available by clicking/actioning a subroutine label in the editor.

## See Also

- `DEFSUB` — define a subroutine
- `LIST` — list program source
- `LIST RETURN` — show call stack with subroutine locations
