# LIST LOCAL

> Lists local variables in the current subroutine with their dimensions and values.

## Syntax

```
LIST [title] LOCAL [variable | pattern]
```

## Description

Similar to `LIST DIM` but shows only `LOCAL DIM` variables. Non-printing characters are shown as `.`. Accepts the same wildcard patterns as `LIST DIM`.

In the KCML Workbench, this is available via the Variables option in the LIST RETURN dialog.

## Example output

```
LIST LOCAL
L  FRED$16    "Aard-vark "
L  NA(12)     1,2,3,2,12,22,12,11,34,56,78,98
L  A9         1.8
L  .TYPE      (4,0X6002)
L  .NAME$     (30,25)
```

## See Also

- `LIST DIM` — all variables (not just local)
- `LIST RETURN` — call stack
- `LOCAL DIM` — declare local variables
- `DEFSUB` — subroutine definitions
