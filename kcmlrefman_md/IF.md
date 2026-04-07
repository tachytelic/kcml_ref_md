# IF

> Conditionally executes one or more statements based on a boolean expression; covers both `IF ... THEN` (single-statement) and `IF ... END IF` (structured multi-line) forms.

---

## IF ... END IF (Structured Form)

### Syntax

```
IF (condition)
    ...
[ELSE IF (condition)
    ...]
[ELSE
    ...]
END IF
```

| Element | Description |
|---------|-------------|
| `condition` | A boolean expression. See **Conditions** below. |
| `ELSE IF` | Optional additional branch; may be repeated for cascaded logic |
| `ELSE` | Optional default branch executed when no preceding condition is true |
| `END IF` | Required closing keyword; must be paired with the opening `IF` |

#### Description

`IF ... END IF` is the **recommended** form for multi-statement conditional logic. If the condition is true, the statements between `IF` and the matching `ELSE` or `END IF` execute. If the condition is false and an `ELSE` or `ELSE IF` clause is present, the alternative branch executes.

There is no limit to the number of statements between `IF ... END IF`. Each `IF` must have a corresponding `END IF`; a missing `END IF` causes a runtime error.

The KCML editor automatically indents the body of `IF ... END IF` blocks.

---

## IF ... THEN (Single-Statement Form)

### Syntax

```
IF condition THEN statement
```

or with a DO group for multiple statements:

```
IF condition THEN DO
    ...
END DO
```

| Element | Description |
|---------|-------------|
| `condition` | A boolean expression |
| `statement` | Any simple KCML statement except `DATA` or an image (`%`) statement |

#### Description

`IF ... THEN` executes a single statement (or `DO` group) when the condition is true. It is provided for compatibility with other languages; the structured `IF ... END IF` form is generally recommended instead.

**Important:** The statement following `THEN` must be either a `DO` group or a simple single statement. Do **not** use a complex multi-line statement (such as another `IF ... THEN DO`, `IF ... END IF`, `WHILE ... WEND`, `REPEAT ... UNTIL`, or `FOR ... NEXT`) directly after `THEN`. KCML will skip to the next colon or end of line, meaning the body of the inner statement will always execute regardless of the outer condition. Use `IF ... END IF` for these situations.

---

## Conditions

### Numeric Comparisons

| Condition | True when |
|-----------|-----------|
| `IF (x)` | `x` is non-zero |
| `IF (x==y)` | `x` equals `y` |
| `IF (x<y)` | `x` is less than `y` |
| `IF (x>y)` | `x` is greater than `y` |
| `IF (x<=y)` | `x` is less than or equal to `y` |
| `IF (x>=y)` | `x` is greater than or equal to `y` |
| `IF (x<>y)` | `x` is not equal to `y` (`!=` is accepted as input but stored as `<>`) |

Each side of a numeric condition is fully evaluated before the comparison takes place.

### Alpha (String) Comparisons

Alpha comparisons work byte by byte from left to right, using binary character values (e.g. `"B" > "A"` because `HEX(42) > HEX(41)`). If the two strings differ in length, the shorter one is padded with trailing spaces before comparison. All comparison operators are valid for alpha expressions.

### Field Variable Comparisons

Both alpha and numeric field variables can be tested with `IF`, but **only** `==` and `<>` may be used:

```kcml
IF (.field1 == .field2 OR .name$ <> .re$)
...
END IF
```

### Logical Operators

Multiple conditions may be combined using:

| Operator | Meaning |
|----------|---------|
| `AND` | Both conditions must be true. If the first is false, the second is **not** evaluated (short-circuit). |
| `OR` | Either condition must be true. If the first is true, the second is **not** evaluated (short-circuit). |
| `XOR` | Exactly one condition must be true. **Both** conditions are always evaluated. |

Parentheses may be used to control grouping:

```kcml
IF ((x==1 AND y==1) OR (a==1 AND b==1))
...
END IF
```

### The END Condition

`END` can be used in place of any condition to test whether the previous `READ #` statement reached the end-of-file marker:

```kcml
IF (END)
```

`NOT END` tests that the end of file has **not** been reached:

```kcml
IF (NOT END)
```

---

## Examples

### Simple structured IF

```kcml
IF (x > 0)
    PRINT "Positive"
END IF
```

### IF with ELSE

```kcml
IF (score >= 50)
    PRINT "Pass"
ELSE
    PRINT "Fail"
END IF
```

### Cascaded ELSE IF

```kcml
IF (grade >= 90)
    PRINT "A"
ELSE IF (grade >= 80)
    PRINT "B"
ELSE IF (grade >= 70)
    PRINT "C"
ELSE
    PRINT "Below C"
END IF
```

### Grouped conditions with parentheses

```kcml
IF ((x==1 AND y==1) OR (a==1 AND b==1))
    'ProcessMatch()
END IF
```

True if both `x` and `y` are 1, or both `a` and `b` are 1.

### String comparison

```kcml
IF (old$==new$ AND was==1)
    'Update()
END IF
```

### Exclusive-or condition

```kcml
IF (old$==new$ XOR was==1)
    'HandleExclusive()
END IF
```

### End-of-file test

```kcml
REPEAT
    READ #stream, record$
    IF (END)
        BREAK
    END IF
    'Process(record$)
UNTIL FALSE
```

### IF ... THEN single-statement form

```kcml
IF count > 10 THEN PRINT "Over limit"
```

### IF ... THEN with DO group

```kcml
IF count > 10 THEN DO
    PRINT "Over limit"
    count = 0
END DO
```

---

## Notes

- `IF ... END IF` is the recommended form for all multi-statement conditional logic.
- `IF ... THEN` is provided for compatibility; restrict it to simple single-statement cases.
- Never put a complex loop or block construct directly after `THEN` — the body will always execute. Use `IF ... END IF` instead.
- Conditions are evaluated left to right; `AND` and `OR` short-circuit.
- `XOR` always evaluates both sides, unlike `AND` and `OR`.
- The `END` keyword in a condition is specifically for end-of-file detection after `READ #`; it is unrelated to the `END IF` keyword.

---

## See Also

- `ELSE` — alternative branch in an `IF` statement
- `DO ... END DO` — groups multiple statements as the body of `IF THEN`
- `AND`, `OR`, `XOR` — logical operators
- `BREAK` — exit a loop from within a conditional
- `REPEAT ... UNTIL` — post-condition loop
- `WHILE ... WEND` — pre-condition loop
- `READ #` — file read statement (sets the `END` condition)
