# GOSUB' (label form)

> Calls a named subroutine or function defined with `DEFSUB` (or `$DECLARE`). The preferred modern subroutine call mechanism.

## Syntax

```
[GOSUB] 'label [( [BYREF] arg [, [BYREF] arg] ... )]
```

Function form (returns a value):
```
'label( args )           REM numeric result
'label$( args )          REM alpha result
```

| Element | Description |
|---------|-------------|
| `label` | Integer or symbolic name (up to 120 alphanumeric chars + underscore) |
| `GOSUB` | Optional keyword — deprecated, omit in new code |
| `BYREF` | Pass argument by reference (changes in sub affect caller) |

## Description

`GOSUB'` transfers execution to the `DEFSUB` (or `$DECLARE`) statement with the matching label. On `RETURN`, execution resumes after the `GOSUB'` call site.

The `GOSUB` keyword is optional and deprecated — the preferred form is just `'label(args)`.

### Subroutine vs function use

- **Subroutine** (void): `'ProcessRecords(list$(), count)`
- **Numeric function**: `result = 'max(a, b)`
- **Alpha function**: `name$ = 'FormatName$(first$, last$)`

The alpha function form requires a `$` suffix on the label at the call site.

### Arguments

- Arguments are passed by value by default (a copy is made).
- Use `BYREF` to pass by reference: changes to the parameter in the subroutine update the original variable.
- The number of arguments at the call site may be *less* than the `DEFSUB` parameter count, provided the extra parameters at the end were initialised (optional parameters).
- Arrays are passed as `arr$()` or `arr()`.
- Field variables are passed as `.fieldname`.

### Returning a value

Inside a `DEFSUB`, assign to `RETURN` to set the return value:

```kcml
DEFSUB 'square(n)
    RETURN = n * n
END SUB

result = 'square(7)    REM result = 49
```

## Examples

### Basic void subroutine

```kcml
'PrintLine(title$, value)

DEFSUB 'PrintLine(label$, n)
    PRINT label$; " = "; n
END SUB
```

### Function returning numeric value

```kcml
DEFSUB 'max(a, b)
    IF a > b
        RETURN = a
    ELSE
        RETURN = b
    END IF
END SUB

biggest = 'max(10, 20)
PRINT biggest    REM prints 20
```

### Passing arrays and BYREF

```kcml
'ClearList(items$(), count)

DEFSUB 'ClearList(arr$(), BYREF n)
    DIM i
    FOR i = 1 TO n
        arr$(i) = ""
    NEXT i
    n = 0
END SUB
```

### Alpha function

```kcml
name$ = 'Greeting$(user$)

DEFSUB 'Greeting$(who$)
    RETURN = "Hello, " & who$
END SUB
```

## Notes

- The `GOSUB` prefix is deprecated. Write `'label(args)` not `GOSUB 'label(args)`.
- Labels are case-insensitive. `'GetNext` and `'getnext` refer to the same subroutine.
- The underscore `_` may be used in labels: `'get_next_record`.
- If a function form is called as a void statement, the return value is discarded.
- Calling an alpha function (`'label$`) in a numeric context or vice versa causes a runtime error.

## See Also

- `DEFSUB` — define a subroutine or function body
- `RETURN` — return from subroutine (optionally with a value)
- `BYREF` — pass argument by reference
- `$DECLARE'` — declare an external subroutine reference
- `GOSUB` — legacy line-number subroutine call
