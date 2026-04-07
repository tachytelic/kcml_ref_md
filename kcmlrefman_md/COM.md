# COM

> Declares common (persistent) variables that survive `LOAD` statements and are shared across program chains.

## Syntax

```
COM com-element [, com-element] ...
```

Where each `com-element` is one of:

```
array_name(dim1 [, dim2])              — numeric array
array_name$(dim1 [, dim2]) [length]    — alpha array
scalar_name$ [length]                  — alpha scalar (default length 16)
scalar_name [= expression]             — numeric scalar with optional init
.field_name$=(position, length)        — alpha field variable
.field_name=(position, "image")        — numeric field variable
```

## Description

`COM` is similar to `DIM` but the declared variables are **common** — they persist when a new program is loaded with `LOAD`. This makes `COM` variables the standard mechanism for passing data between programs in a multi-program KCML application.

Key differences from `DIM`:

| Feature | DIM | COM |
|---------|-----|-----|
| Survives `LOAD` | No | Yes |
| Cleared by `CLEAR` | Yes | Yes |
| Cleared by `RUN` | Yes | No |
| Cleared by `CLEAR N` | Yes | No |

`COM` variables are only cleared by:
- `CLEAR` (full)
- `CLEAR V`
- `LOAD RUN`
- `COM CLEAR`

### Redeclaring COM variables

If the same `COM` variable is declared in a later program with the same dimensions, no error occurs. Conflicting dimensions cause a runtime error.

### Initialising COM variables

Numeric and alpha scalars can be initialised at resolve time:

```kcml
COM test=100, news=10*first
COM beta=INT(abc/2)
COM Test$ = "ABCDE"
COM Letter$1000 = HEX(FFFE FDFC)
COM .Name$=(1,35), Number=(35,"####")
```

Any variables referenced in the initialiser expression must have been previously `COM`ed before the current program was loaded.

### Deferred-size arrays

```kcml
COM table$(0,0)20
```

A zero-dimension `COM` allocates no space at resolve time. Space is allocated later with `MAT REDIM` or similar.

### COM in libraries (KCML 6.01+)

Variables declared as `COM` in a KCML library are copied to the foreground program when the library is loaded with `LIBRARY ADD`. These copies persist even if the library is later unloaded.

### Converting COM to DIM

`COM CLEAR` converts `COM` variables back to non-common `DIM` variables without altering their values.

## Examples

### Passing data between programs

First program:
```kcml
COM rows=20, columns=40
LOAD "PROGRAM"
```

Second program:
```kcml
COM table$(rows+1, columns+1)20
```

`table$` is dimensioned 21×41 with 20 bytes per element, using values passed from the first program.

### Various COM declarations

```kcml
COM sample(12,4), test(8), number_of_records, .name$
COM fred$(from(1)*2, from(2)*2)length, .total$=(start, "-#####.##")
COM abc$(20), files$(100)10, as(9,2)
COM abc=50, zyx=INT(90/def), newl$(50)16
```

## Notes

- Declaring the same `COM` variable twice in the same program is fine if dimensions match; conflicting re-declarations cause an error.
- Use `COM` sparingly — overuse of common variables makes programs hard to reason about. For data within a single program, use `DIM`.
- `$OPTIONS` byte 38 set to `HEX(01)` enforces explicit declaration of all variables.

## See Also

- `DIM` — declare non-common (local) variables
- `COM CLEAR` — convert COM variables back to DIM
- `LOAD` — load a new program (COM variables survive this)
- `CLEAR` — full environment reset (clears COM variables)
- `MAT REDIM` — resize a COM array at runtime
- `LIST DIM` — list all declared variables
