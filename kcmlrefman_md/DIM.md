# DIM

> Declares variables, arrays, and constants in a KCML program, specifying their dimensions, string lengths, and optional initial values.

## Syntax

```
[PRIVATE | PUBLIC] DIM dim-element [, dim-element] ...
```

Where each `dim-element` is one of:

```
array_name(dim1 [, dim2])                    — numeric array
array_name$(dim1 [, dim2]) [length]          — alpha array
scalar_name$ [length]                        — alpha scalar (default length 16)
scalar_name [= expression]                   — numeric scalar with optional init
.field_name$=(position, length)              — alpha field variable
.field_name=(position, "image")              — numeric field variable
```

| Element | Description |
|---------|-------------|
| `array_name` | Name of a numeric or alpha array variable |
| `dim1`, `dim2` | Positive integer expressions giving the array dimensions, evaluated at resolve time |
| `length` | Positive integer expression giving the maximum length in bytes of each alpha element; defaults to 16 if omitted |
| `expression` | Numeric or string value used to initialise a scalar at resolve time |

## Description

`DIM` is a declaration statement processed during the **resolve phase** — when the program is loaded and prepared for execution. At execution time the `DIM` statement itself is skipped.

Variables declared with `DIM` are:
- Marked as **non-common**: they are dropped when a `LOAD` is executed.
- Reinitialised whenever the program is restarted with `RUN`.

Because `DIM` runs at resolve time, any expressions used (for dimensions, lengths, or initialisers) must be evaluable at resolve time. Variables referenced inside a `DIM` expression must therefore either be constants or have been previously declared with `COM` before the current program was loaded.

Space for arrays and string scalars is **not** allocated at resolve time; it is allocated on the first reference during execution. This minimises memory usage when some variables are never reached due to branching.

Scalar numeric variables and string variables will be **automatically declared** by KCML if encountered without a prior `DIM`. This is allowed for backward compatibility but is considered poor practice because misspelled variable names become silent bugs. Explicit declaration of all variables is strongly recommended (see **Enforcing Explicit Declaration** below).

A variable may be declared more than once provided each declaration is identical.

## Parameters / Clauses

### Specifying Dimensions and Lengths

Array dimensions and string lengths are numeric expressions evaluated at resolve time. The following functions are valid inside these expressions: `INT(`, `MAX(`, `MIN(`, `SGN(`, and similar numeric functions.

### Initialising Variables

Scalar numeric and string variables (and constants) can be initialised by appending `= expression` to the declaration:

```kcml
DIM test=100, news=10*first
DIM beta=INT(abc/2)
```

String scalars can be initialised with a literal string or with `HEX(`. If no length is specified with the declaration, the string is sized to match the initialiser. To reserve more space than the initialiser occupies, add an explicit length:

```kcml
DIM Test$ = "ABCDE"
DIM Letter$1000 = HEX(FFFE FDFC)
```

Field variables can also be initialised via `DIM`:

```kcml
DIM .Name$=(1,35), Number=(35,"####")
```

### Resizing Arrays at Runtime

Array dimensions can be changed during execution using:

| Statement | Effect |
|-----------|--------|
| `MAT REDIM` | Explicitly resize an array |
| `LET REDIM` | Resize via assignment |
| `MAT CON(dims)` | Fill with constants and resize |
| `MAT IDN(dims)` | Set to identity matrix and resize |
| `MAT ZER(dims)` | Zero array and resize |
| `MAT READ(dims)` | Read data into array with new dimensions |

If an array is `DIM`ed with size zero, no space is allocated at resolve time. This defers allocation until the size is known:

```kcml
DIM one(0), two(2,2)
MAT REDIM one(20)
MAT two = CON(32,33)
```

### PUBLIC and PRIVATE Scope

| Keyword | Effect |
|---------|--------|
| `PRIVATE` | Visible only within the library. Prevents name clashes with variables in other libraries. Has no effect in foreground programs. Use wherever possible. |
| `PUBLIC` | Default. In a library, declares a **library variable** that is instantiated in the foreground program and persists across `LOAD` statements (like `COM` variables). If the defining library is unloaded, the variable reverts to a normal non-persisting variable. |

The `PUBLIC` keyword is not required in foreground programs but is encouraged when public library variables are used to make intent clear.

### Enforcing Explicit Declaration

Several mechanisms can enforce that all scalar variables are declared before use:

| Method | Scope |
|--------|-------|
| `$COMPLIANCE 2` (or greater) in a program | Applies to that program only |
| Byte 38 of `$OPTIONS` set to `HEX(01)` | Applies system-wide to all programs |
| KCML Workbench editor | Underlines undeclared variables in red |

Note: parameters of a `DEFSUB` are implicitly declared as local variables by the `DEFSUB` itself and must **not** appear in a `LOCAL DIM`.

### Variable Case

KCML is case-insensitive for variable names but preserves the case used in the `DIM` statement. This behaviour can be overridden by setting the `HEX(01)` bit of byte 40 of `$OPTIONS LIST`.

## Examples

### Basic array and string declaration

```kcml
DIM abc$(20), files$(100)10, as(9,2)
```

Declares:
- `abc$` — alpha scalar, 20 bytes
- `files$` — 100-element alpha array, 10 bytes per element
- `as` — 9×2 numeric array

### Mixed declaration with field variables

```kcml
DIM abc$(20), files$(100)10, as(9,2), .field1$=(10,10)
```

### Initialised scalars

```kcml
DIM abc=50, zyx=INT(90/def), newl$(50)16
```

### Deferred-size array

```kcml
DIM one(0), two(2,2)
MAT REDIM one(20)
MAT two = CON(32,33)
```

### Initialised string and hex literal

```kcml
DIM Test$ = "ABCDE"
DIM Letter$1000 = HEX(FFFE FDFC)
```

### Field variable initialisation

```kcml
DIM .field1=(1, "-#####.###"), afield$=(2,96), nline=SGN(abc)
```

## Notes

- `DIM` is evaluated at resolve time, not at execution time. Expressions in `DIM` must be resolvable before the program runs.
- A `DIM`-declared variable is non-common and is lost on `LOAD`.
- Declaring a variable with `DIM` after an identical `DIM` is allowed; conflicting re-declarations cause an error.
- In libraries, prefer `PRIVATE DIM` for internal-only variables to avoid name clashes.
- Avoid relying on automatic scalar declaration; it can mask typos.

## Compatibility

Prior to KCML 6.10, array dimensions and maximum alpha element lengths were limited to 65,535. From KCML 6.10 onward, available memory is the only limit.

## See Also

- `COM` — declare common (persistent) variables
- `LOCAL DIM` — declare local variables within a subroutine
- `COM CLEAR` — clear common variables
- `DEFSUB` — define a subroutine with local parameters
- `DIM(` — function returning the declared dimension of an array
- `LIST DIM` — list all dimensioned variables
- `MAT REDIM` — resize an array at runtime
- `$OPTIONS` — system options including byte 38 (force declaration) and byte 40 (variable case)
- `$COMPLIANCE` — enforce stricter programming standards
