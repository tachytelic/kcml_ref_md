# COND(

> Evaluates a condition expression and returns a numeric 1 (TRUE) or 0 (FALSE).

## Syntax

```
COND( condition [operator condition] ... )
```

Where `condition` can be a numeric comparison, string comparison, or boolean expression, and `operator` is `AND`, `OR`, or `NOT`.

## Description

`COND(` is the numeric-returning counterpart to `BOOL(`. Where `BOOL(` is a conditional expression (usable only in `IF`/`UNTIL`/`WHILE`), `COND(` converts a condition to a numeric value that can be **assigned to a variable**, used in expressions, or stored for later use.

- Returns `1` (TRUE) if the condition is true
- Returns `0` (FALSE) if the condition is false

`COND(` is valid wherever a numeric expression is valid.

Conditions can mix numeric and string comparisons connected with `AND`, `OR`, and `NOT`.

## Examples

### Store a condition result

```kcml
: DIM age, result, height
: DIM sex$1
: age = 20 : height = 6.6 : sex$ = "M"
: result = COND(age < 25)
: PRINT "age<25 result="; result
: result = COND(age > 25)
: PRINT "age>25 result="; result
: $END
```

Output:
```
age<25 result= 1
age>25 result= 0
```

### Combined conditions

```kcml
age = 20
height = 6.6
sex$ = "M"
result = COND(age < 25 AND sex$ == "M")
IF (BOOL(result) AND height > 6)
    type$ = "TALL MALE"
END IF
```

### Complex expressions

```kcml
testing = COND(abc < 10 OR tmp$ = STR(a$,,2))
tmp = COND(NOT a <= 10 AND tmp$ = z$ OR B = 6)
```

## Notes

- Use `COND(` when you need to store or compute a boolean result as a number for later use with `BOOL(`.
- The complementary function `BOOL(` converts an already-numeric 0/1 value (or a string) back into a boolean condition for `IF`/`UNTIL`.
- `COND(` accepts the same condition syntax as `IF`, including mixed alpha and numeric comparisons.

## See Also

- `BOOL(` — convert a numeric/string value to a boolean conditional
- `IF` — conditional statement
- `TRUE`, `FALSE` — boolean constants
