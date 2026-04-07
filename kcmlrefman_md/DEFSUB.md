# DEFSUB

> Defines a structured subroutine with local variables and an argument list.

## Syntax

```
[PUBLIC | PRIVATE] DEFSUB 'label [([BYREF] dim_element [, [BYREF] dim_element] ...)]
    [LOCAL DIM ...]
    ...
[END SUB]
```

| Element | Description |
|---------|-------------|
| `label` | Symbolic subroutine name (up to 120 alphanumeric chars, first char a letter; underscores allowed) |
| `dim_element` | Argument: same syntax as `DIM` — scalar, array, string with length, field variable |
| `BYREF` | Pass argument by reference instead of by value |
| `PUBLIC` / `PRIVATE` | Visibility in libraries. `PUBLIC` = accessible from foreground/other libs. `PRIVATE` = library-internal only. |

## Description

`DEFSUB` is the modern replacement for `DEFFN'`. It defines a subroutine with **local variables** — all arguments and `LOCAL DIM` variables are created fresh on each call and discarded on `RETURN`.

Called with `GOSUB 'label(args)` or used as a function expression `FN 'label(args)`.

### Argument handling

Each argument passed from the call is copied into a **local variable** with the same dimensions and type. Changes to argument variables inside the subroutine do not affect the caller's variables, unless `BYREF` is used.

Argument sizes:
- Numeric scalars: use a name or name with `= expression`
- String scalars: sized to match the caller's string unless explicitly dimensioned in the `DEFSUB` line
- Arrays: sized to match the caller's array

```kcml
DEFSUB 'Get_Rec(Reclen, Another$Reclen)
```
Here `Another$` is dimensioned to `Reclen` bytes — the first argument value is used in the dimension expression.

### END SUB scope

When `END SUB` is present, all `LOCAL DIM` statements between `DEFSUB` and `END SUB` are considered local variables. Without `END SUB`, local variable scope is less well-defined. Always use `END SUB`.

### RETURN value

A subroutine can return a value by assigning to `RETURN`:

```kcml
DEFSUB 'square(n)
    RETURN = n * n
END SUB

result = FN 'square(5)
```

## Examples

### Void subroutine

```kcml
DEFSUB 'greet(name$)
    PRINT "Hello, "; name$
END SUB

GOSUB 'greet("World")
```

### Function-style with return value

```kcml
DEFSUB 'max(a, b)
    IF a > b
        RETURN = a
    ELSE
        RETURN = b
    END IF
END SUB

biggest = FN 'max(10, 20)
```

### BYREF parameter

```kcml
DEFSUB 'increment(BYREF counter)
    counter = counter + 1
END SUB

DIM count
count = 5
GOSUB 'increment(BYREF count)
PRINT count
```

Output: `6`

### Local variables

```kcml
DEFSUB 'process(data$)
    LOCAL DIM i, temp$20
    FOR i = 1 TO 10
        temp$ = STR(data$, i, 1)
        PRINT temp$
    NEXT i
END SUB
```

## Notes

- `DEFSUB` is a **program-mode statement** — requires a numbered program, not available in `-p` script mode.
- Always use `END SUB` to clearly define the subroutine's scope.
- For single-expression numeric functions, `DEFFN` is simpler. For all other cases, use `DEFSUB`.
- `PRIVATE DEFSUB` in a library prevents name clashes; use it for all internal-only subroutines.

## See Also

- `DEFFN'` — deprecated subroutine definition (use `DEFSUB` instead)
- `GOSUB'` — call a subroutine
- `RETURN` — return from a subroutine (optionally with a value)
- `LOCAL DIM` — declare local variables inside `DEFSUB`
- `BYREF` — pass an argument by reference
- `END SUB` — close a `DEFSUB` block
