# SYM(

> Returns a unique index number for a variable or subroutine, enabling indirect access by index.

## Syntax

```
index = SYM(variable)
index = SYM(variable$)
index = SYM(variable())
index = SYM(.field_var)
index = SYM('subroutine)

SYM(*index) = value           (indirect numeric assignment)
SYM(*index)$ = value$         (indirect alpha assignment)
PRINT SYM(*index)             (indirect numeric read)
PRINT SYM(*index)$            (indirect alpha read)
SYM(*index)(row, col) = val   (indirect array element)
'SYM(*index)(args)            (indirect subroutine call)
```

## Description

`SYM(var)` returns an opaque integer index identifying the variable or subroutine within the current program. The index can be stored and used later to access the variable or call the subroutine indirectly.

The index is valid only for the current program. A `LOAD` may invalidate non-COM variable indices. COM variable and library subroutine indices persist across `LOAD` (KCML 6.20+).

The Workbench recognises SYM values in tooltips and dereferences them for display.

### Variable types and usage

| Symbol type | Get index | Use index |
|-------------|-----------|-----------|
| Numeric | `n = SYM(a)` | `SYM(*n) = 100` / `PRINT SYM(*n)` |
| Alpha | `n = SYM(a$)` | `SYM(*n)$ = "TEST"` / `PRINT SYM(*n)$` |
| Numeric array | `n = SYM(a())` | `SYM(*n)(1,4) = 100` |
| Alpha array | `n = SYM(a$())` | `SYM(*n)$(1,4) = "TEST"` |
| Numeric field | `n = SYM(.a)` | `.SYM(*n) = (4, "##.##")` |
| Alpha field | `n = SYM(.a$)` | `.SYM(*n)$ = (4, 10)` |
| Subroutine | `n = SYM('calc)` | `'SYM(*n)(args)` |

## Examples

```kcml
REM Indirect variable access
DIM count
count = 42
DIM n
n = SYM(count)
PRINT SYM(*n)        : REM  42
SYM(*n) = 100
PRINT count          : REM  100
```

```kcml
REM Used heavily in KISAM reads (ki_sym pattern)
DIM rec$512, ki_sym
ki_sym = SYM(rec$)
CALL KI_READ_NEXT handle, 1, ki_sym TO ki_status, ki_dataptr$, ki_key$
```

```kcml
REM Indirect subroutine dispatch
DIM handlers(3), i
handlers(1) = SYM('open_file)
handlers(2) = SYM('save_file)
handlers(3) = SYM('close_file)
i = 2
'SYM(*handlers(i))()
```

## Notes

- `SYM(` is used in KISAM file access: `ki_sym = SYM(rec$)` must be pre-assigned before calling `KI_READ_NEXT` — do **not** pass `SYM()` inline.
- `SYMNAME(n)` returns the variable name corresponding to an index.
- The `*` prefix dereferences an index: `SYM(*n)` means "the variable whose index is n".

## See Also

- `SYMNAME(` — get variable name from SYM index
- `KI_READ_NEXT` — KISAM record read (uses SYM)
