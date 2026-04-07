# LOCAL DIM

> Declares variables that are local in scope to the enclosing `DEFSUB` subroutine.

## Syntax

```
LOCAL DIM dim_element [, dim_element ...]
```

Where `dim_element` follows the same form as `DIM`:
- `VarName` — numeric scalar
- `VarName$length` — string of fixed length
- `VarName(dim1 [,dim2])` — numeric array
- `VarName$(dim)length` — string array
- `.fieldname = (start, spec)` — field variable

Scalars and basic strings can be initialized:
```
LOCAL DIM Value = 10
LOCAL DIM AlphaValue$ = "Hello!"
```

## Description

`LOCAL DIM` variables exist only within the active call to the enclosing `DEFSUB`. They are created on entry and destroyed on `RETURN`. Each recursive call or re-entry gets its own copy.

This is the KCML equivalent of local/automatic variables in C.

### Deferred allocation

Scalar string variables have their storage deferred until first use. If the first use is a `REDIM` assignment, no initial allocation is needed. Use explicit zero size to signal this:

```kcml
LOCAL DIM x$0    REM will be REDIM'd before use
REDIM x$ = "<" & tag$ & ">"
```

### REDIM with LOCAL DIM

LOCAL strings can be resized with `MAT REDIM` or the `REDIM` assignment:

```kcml
REDIM result$ = STR(buffer$, 1, LEN(buffer$))
```

This is useful when the size of an incoming argument is unknown.

**Performance note:** REDIM has overhead — fixed-size strings up to 200 bytes are faster.

## Examples

```kcml
DEFSUB 'new(number, size, data$())
    LOCAL DIM record$(number)size
    REM ... work with record$() ...
    RETURN size
END SUB

DEFSUB 'tagit(tag$)
    LOCAL DIM x$0
    REDIM x$ = "<" & tag$ & ">"
    RETURN x$
END SUB
```

## Notes

- LOCAL DIM variables are invisible outside the DEFSUB they are declared in.
- Arrays and field variables cannot be initialized in the `LOCAL DIM` declaration — only scalars and basic strings.
- `LIST LOCAL` shows the current values of all local variables.
- `LIST DIM` also shows locals (prefixed with `L`).

## See Also

- `DEFSUB` — define a subroutine
- `DIM` — declare non-local variables
- `COM` — common variables shared across LOADs
- `REDIM` — resize a string variable
- `LIST LOCAL` — display local variable values
