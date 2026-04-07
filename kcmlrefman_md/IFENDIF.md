# IF ... END IF

> Executes a block of statements conditionally. Supports `ELSE`, `ELSE IF`, and unlimited nesting.

## Syntax

```
IF ( condition )
    statements
[ELSE IF ( condition )
    statements]
[ELSE
    statements]
END IF
```

Each `IF` must have a matching `END IF`.

## Description

`IF ... END IF` is the structured conditional form in KCML. If the condition is true, the body executes; if false, execution skips to `ELSE` (if present) or `END IF`.

There is no limit on the number of statements between `IF` and `END IF`.

### Numeric conditions

| Condition | Meaning |
|-----------|---------|
| `IF (x)` | True if x is non-zero |
| `IF (x == y)` | Equal |
| `IF (x <> y)` or `IF (x != y)` | Not equal (KCML stores as `<>`) |
| `IF (x < y)` | Less than |
| `IF (x > y)` | Greater than |
| `IF (x <= y)` | Less than or equal |
| `IF (x >= y)` | Greater than or equal |

### Alpha conditions

Alpha comparisons are byte-by-byte from left to right (binary order). Shorter strings are padded with trailing spaces before comparison.

```kcml
IF (name$ == "Smith")
IF (code$ < "M")
```

### Field variable conditions

Only `==` and `<>` are valid for field variables:

```kcml
IF (.field1 == .field2 OR .name$ <> .ref$)
```

### Logical operators

| Operator | Meaning |
|----------|---------|
| `AND` | Both conditions must be true; short-circuits (second not evaluated if first is false) |
| `OR` | Either condition must be true; short-circuits (second not evaluated if first is true) |
| `XOR` | Exactly one condition must be true; both always evaluated |

Parentheses group sub-expressions:

```kcml
IF ((x==1 AND y==1) OR (a==1 AND b==1))
```

### END condition (end-of-file test)

```kcml
IF (END)        REM true if previous READ# hit end-of-file
IF (NOT END)    REM true if previous READ# did NOT hit end-of-file
```

## Examples

```kcml
: DIM x, y, a$10, b$10
: x = 5 : y = 3
: IF (x > y)
:   PRINT "x>y is true"
: ELSE
:   PRINT "x>y is false"
: END IF
: IF (x == 5 AND y == 3)
:   PRINT "both conditions true"
: END IF
: IF (x == 99 OR y == 3)
:   PRINT "OR condition true"
: END IF
: a$ = "hello" : b$ = "world"
: IF (a$ < b$)
:   PRINT "a$ < b$ (alpha compare)"
: END IF
: $END
```

Output:
```
x>y is true
both conditions true
OR condition true
a$ < b$ (alpha compare)
```

### Cascaded ELSE IF

```kcml
IF (score >= 90)
    grade$ = "A"
ELSE IF (score >= 80)
    grade$ = "B"
ELSE IF (score >= 70)
    grade$ = "C"
ELSE
    grade$ = "F"
END IF
```

## Notes

- `IF ... END IF` is preferred over `IF ... THEN` for multi-statement bodies.
- `!=` is accepted as an alternative to `<>` but KCML always recreates it as `<>`.
- Conditions are evaluated left-to-right with short-circuit evaluation for `AND` and `OR`.
- `NOT` can precede any condition: `IF (NOT (x == y))`.

## See Also

- `IF ... THEN` — single-statement conditional (legacy form)
- `SELECT CASE` — multi-way branch
- `WHILE ... WEND` — conditional loop
- `REPEAT ... UNTIL` — post-test loop
