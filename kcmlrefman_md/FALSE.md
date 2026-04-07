# FALSE

> A boolean constant with the numeric value zero.

## Syntax

```
FALSE
```

A numeric keyword that evaluates to 0. Valid wherever a numeric expression is legal.

## Description

`FALSE` is a predefined constant equal to 0. It can be used to initialise or test boolean-style variables, or as the condition of a `REPEAT ... UNTIL FALSE` loop (infinite loop).

## Examples

### Initialise a flag

```kcml
: PRINT "FALSE="; FALSE
: $END
```

Output: `FALSE= 0`

### Set a variable

```kcml
Variable = FALSE
IF (variable = FALSE) THEN PRINT "not set"
```

### Infinite loop (repeat forever)

```kcml
REPEAT
    'ProcessNext()
    IF done THEN BREAK
UNTIL FALSE
```

## Notes

- `FALSE = 0`. Any zero numeric value is considered false in KCML conditions.
- `TRUE = 1` (or any non-zero value is true).
- Prefer `IF (x)` rather than `IF (x = TRUE)` — any non-zero value is truthy.

## See Also

- `TRUE` — boolean constant equal to 1 (non-zero)
- `BOOL(` — convert a numeric/string to a boolean condition
- `COND(` — evaluate a condition and return 0/1
