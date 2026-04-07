# LIST DIM

> Lists all dimensioned variables (or a specific variable/pattern) with their current sizes and values.

## Syntax

```
LIST [title] DIM [variable | pattern]
LIST [title] COM [variable | pattern]
```

## Description

Shows all DIM'd variables in declaration order: common variables first (`C`), then non-common (`D`), then local (`L`). Each variable shows:
- Flag: `C` = COM, `D` = DIM, `L` = LOCAL
- Name and dimensions
- Current value (truncated to one line; non-printable bytes shown as `.`)

Field variables show `(start, specifier)`. Variables not yet used show `-`. Out-of-scope locals show `Out of scope`.

### Pattern matching

`*` = any string, `?` = any char, `[...]` = character class.

```
LIST DIM "A*"       REM matches A, A(, A$, APPLE$...
LIST DIM "A[0-9]$"  REM matches A0$..A9$
```

## Example output

```
C Fred$16     "Aard-vark       "
C N(12)       1,2,3,2,12,22,12,11,34,56,78,98
D .Type       (4, NUM(9,2))
D Big$10000   -
L temp$(2)10  "..........","........."
```

## See Also

- `LIST LOCAL` — local variables only
- `LIST V` — find variable references in source
- `COM` — common variables
- `DIM` — declare variables
