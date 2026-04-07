# LIBRARY (MODULE)

> Maps shared KCML library modules into/out of the current program's symbol space.

## Syntax

```
LIBRARY ADD name$ = filename$
LIBRARY REMOVE name$
LIBRARY REMOVE ALL
```

`MODULE` is the deprecated synonym; KCML always rewrites to `LIBRARY`.

## Description

`LIBRARY` generalizes `SELECT @PART` for shared globals:
- Multiple libraries can be active simultaneously.
- Shared text is memory-mapped from a file — no dedicated shared-memory partition required.
- Libraries can be added and removed at runtime.

### LIBRARY ADD

Appends a library to the module list. `name$` is the symbolic name used to later remove it. `filename$` must be a compiled library (created with `kc6` or `SAVE <G>`).

Library search order for `DEFSUB'` routines:
1. Currently executing library (or foreground if not in a library)
2. Library list from the start (foreground is first)

Foreground routines **override** library routines with the same name.

### Visibility

| Keyword | Visibility |
|---------|-----------|
| `PUBLIC DIM var` | Copied to foreground symbol table on load; persistent across `LOAD` |
| `PRIVATE DIM var` | Visible only within the library |

Fields, records, and constants are looked up when referenced (not copied at load time).

### Constructor

A library function named `'_Constructor()` is automatically called by `LIBRARY ADD` for initialization.

### Persistence

Libraries survive `LOAD` and `CLEAR P`. All libraries are dropped by `LIBRARY REMOVE ALL` or `CLEAR`.

### Compilation

Libraries can be built from multiple programs using the `kmake` utility (driven by an XMLbuild file). Each component can have its own constructor.

## Examples

```kcml
LIBRARY ADD "MK/libGb" = "./PROGS/MK/libGb"
LIBRARY REMOVE "MK/libGb"
LIBRARY REMOVE ENV("LIBRARY")
LIBRARY REMOVE ALL
```

## Notes

- Libraries are hardware-dependent (byte order, word size). Not interoperable between different platform types.
- `COM` in libraries is deprecated (use `PUBLIC DIM` instead).
- `PRIVATE`/`PUBLIC` visibility on `DEFSUB` was introduced in KCML 6.10.

## See Also

- `SELECT @PART` — legacy single-global mechanism
- `LIST M` — show loaded libraries
- `LIST '` — find subroutine references across libraries
