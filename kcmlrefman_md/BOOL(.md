# BOOL(

> Converts a numeric or string expression to a boolean TRUE/FALSE value for use in conditional expressions.

## Syntax

```
BOOL( expression )
```

| Parameter | Description |
|-----------|-------------|
| `expression` | A numeric or string expression |

## Description

`BOOL(` converts an expression to a boolean and is used in place of a conditional expression in `IF`, `UNTIL`, `WHILE`, and similar constructs.

**Numeric argument:**
- `0` → FALSE
- Non-zero (any value) → TRUE

**String argument:**
- First character `Y`, `y`, `T`, `t`, or `1` → TRUE
- First character `N`, `n`, `F`, `f`, or `0` → FALSE

`BOOL(` is a **conditional expression**, not a value-returning function. It is valid inside `IF`, `UNTIL`, and `WHILE` conditions but **cannot** be assigned to a variable directly. (See Notes.)

## Examples

### Boolean flag check

```kcml
: DIM x
: x = 42
: IF BOOL(x) THEN PRINT "truthy"
: x = 0
: IF BOOL(x) THEN PRINT "zero truthy"
: PRINT "done"
: $END
```

Output:
```
truthy
done
```

### In a loop condition

```kcml
: DIM end_loop
: end_loop = 0
: REPEAT
:   PRINT "looping"
:   end_loop = 1
: UNTIL BOOL(end_loop)
: $END
```

### String-based flag

```kcml
: DIM flag$1
: flag$ = "Y"
: IF BOOL(flag$) THEN PRINT "flag is yes"
: $END
```

## Notes

- `BOOL(` is a conditional expression, not an assignment function. Writing `flag = BOOL(x)` causes a syntax error. To assign a boolean integer, use `IF (x) THEN flag = 1 ELSE flag = 0`.
- Heavily used in real KCML code as documented in CLAUDE.md: `BOOL(x)` returns TRUE/FALSE from a numeric.
- For the bitwise string `BOOL` operator (16 logical functions), see `BOOL` (operator).

## See Also

- `BOOL` — bitwise string operator
- `COND(` — another conditional function
- `IF` — conditional statement
- `TRUE`, `FALSE` — boolean constants
