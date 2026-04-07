# FN

> Calls a function defined with `DEFFN` or a subroutine defined with `DEFSUB`.

## Syntax

```
FN desc( numeric_expression )
FN 'label( args )
```

| Form | Calls |
|------|-------|
| `FN desc(value)` | A `DEFFN` function identified by `desc` |
| `FN 'label(args)` | A `DEFSUB` subroutine used as a function |

Valid wherever a numeric expression is legal.

## Description

`FN` invokes a previously defined function and returns its value:
- For `DEFFN`: evaluates the single expression defined in the `DEFFN` statement.
- For `DEFSUB`: executes the subroutine and returns the value assigned to `RETURN`.

If multiple `DEFFN` definitions exist for the same name, the first one in the program is used.

`FN` can also be used inside a `DEFFN` expression to call other functions:

```kcml
DEFFN position(X) = FN 1(X) + 2 * FN has(X)
```

## Examples

### With DEFFN

```kcml
: DIM result
: DEFFN area(r) = 3.14159 * r * r
: result = FN area(5)
: PRINT "area(5)="; result
: $END
```

Output: `area(5)= 78.53975`

### Integer numeric label

```kcml
DEFFN 1(x) = x * x
start1 = FN 1(45 * act) + FN 2(45)
```

### With DEFSUB (function-style)

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

## See Also

- `DEFFN` — define a single-expression numeric function
- `DEFSUB` — define a multi-statement subroutine (can be used as function)
- `GOSUB'` — call a subroutine by label (void, not function-style)
