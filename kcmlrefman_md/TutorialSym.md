# Pointers with SYM()

> How to obtain and use symbol index values (pointers) to variables and subroutines, enabling fully generic routines that operate on any variable without knowing its name.

## Overview

Every KCML process maintains an internal **symbol table** — a mapping from variable names, constants, line numbers, and subroutine labels to their runtime representations. The `SYM(` function returns the integer **symbol index** for any named variable or subroutine in that table.

Storing a symbol index in a numeric variable gives you a pointer. You can then dereference the pointer with `SYM(*varname)` to read or write the original variable. This has two main uses:

1. **Generic subroutines** — a sort routine, for example, can accept symbol indices for the array and comparison function without needing to know their names at write time.
2. **Performance** — passing the symbol index of a large array into a subroutine passes a single integer rather than copying the entire array.

## Getting a Symbol Index

### Variables

```kcml
alpha        = SYM(abc$)      REM symbol index of a string scalar
alpha_array  = SYM(abc$())    REM symbol index of a string array
numeric      = SYM(abc)       REM symbol index of a numeric scalar
num_array    = SYM(abc())     REM symbol index of a numeric array
```

### Field variables

Field variables use a `.` prefix on the `SYM(` call:

```kcml
numeric_field       = SYM(.xyz)     REM symbol index of a field variable
numeric_field_array = SYM(.xyz())   REM symbol index of a field array
```

### Subroutines

```kcml
numeric_sub = SYM('calculate_totals)   REM subroutine returning a number
alpha_sub   = SYM('get_next_record$)   REM subroutine returning a string
```

Note the `$` suffix for string-returning subroutines — it is part of the symbol reference, not the variable name.

## Dereferencing a Symbol Index

### String variables

Use `SYM(*var)$` to dereference as a string scalar, or `SYM(*var)$()` for a string array:

```kcml
SYM(*alpha)$ = "Hello world!"           REM assign to abc$
SYM(*alpha_array)$() = ALL(HEX(FF))     REM fill abc$() with 0xFF bytes
PRINT SYM(*alpha_array)$(10)            REM read element 10 of abc$()
SYM(*alpha_array)$(10) = "Nice day"     REM write element 10
```

### Numeric variables

```kcml
SYM(*numeric) = total - discount        REM assign to abc
SYM(*numeric_array)() = ZER             REM zero the entire abc() array
```

### Field variables

Prefix `.` before `SYM(` when dereferencing a field variable:

```kcml
.SYM(*numeric_field) = (1,"######.##")          REM set field spec
.SYM(*numeric_field_array)(1) = (40,"####.##")  REM set element 1 of field array
```

### Subroutines

```kcml
GOSUB 'SYM(*numeric_sub)(figures, discount)
act_no = FLD('SYM(*alpha_sub)$(offset).account_no)
```

## Practical Example

A generic comparison pass to a sort routine:

```kcml
DIM names$(5)20
MAT READ names$()
DATA "Charlie","Alice","Bob","Eve","Dave"

REM get symbol indices
arr_sym  = SYM(names$())
cmp_sym  = SYM('compare_alpha$)

REM pass to a sort routine that accepts symbol indices
GOSUB 'generic_sort(arr_sym, cmp_sym, 5)

PRINT names$()
```

Inside `'generic_sort`, the routine uses `SYM(*arr_sym)$(n)` to access elements and `'SYM(*cmp_sym)$(a$, b$)` to call the comparison function — without knowing the actual names `names$` or `'compare_alpha$`.

## Combining SYM with FLD and DATA

`SYM(` can appear in most contexts where the variable type is valid:

```kcml
FLD(SYM(*alpha)$.SYM(*numeric_field_array)(1)) = 100
DATA LOAD BA T#1, (SYM(*numeric)) SYM(*alpha_array)$()
```

## SYMNAME( — Reverse Lookup

`SYMNAME(index)` returns the variable or subroutine name for a given symbol index. Useful for debugging or building diagnostic output:

```kcml
PRINT SYMNAME(alpha)         REM prints "abc$"
var_name$ = SYMNAME(test)
```

## Notes

- **Symbol indices are assigned at resolve time**, not at a fixed compile-time address. The index for any particular variable may differ between program runs depending on how many `COM` variables were previously defined and how many global subroutines are available.
- **Global variable indices are always negative.** All other variables and subroutines have positive indices. You can use this to distinguish them.
- **Deselecting or switching global partitions invalidates pointers to global variables.** Any stored symbol index for an `@`-prefixed variable becomes meaningless after `SELECT @PART` changes.
- **Array sizes are not copied** when passing a symbol index — the receiving routine operates directly on the original array. This is both the performance benefit and a potential hazard: bounds errors in the called routine affect the caller's data.
- See also: `SYM(`, `SYMNAME(`
