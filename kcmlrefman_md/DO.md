# DO ... END DO (DO Group)

> Groups multiple statements into a single compound statement so they can be used as the body of an `IF THEN`, `ELSE`, or `ERROR` clause.

## Syntax

```
DO [statement] ... END DO
```

or equivalently:

```
DO [statement] ... ENDDO
```

| Element | Description |
|---------|-------------|
| `statement` | One or more KCML statements to be treated as a group |

## Description

A **DO group** is a block of statements that KCML treats as a single statement. This allows multiple statements to appear as the target of an `IF THEN`, `ELSE`, or `ERROR` clause — contexts that otherwise accept only a single statement.

DO groups may be nested to a depth of over 50. Each `DO` is paired with its corresponding `ENDDO` (or `END DO`) at resolve time; a mismatch causes a resolve-time error.

The KCML editor automatically indents DO groups to make the structure visually clear.

A DO group can span multiple lines.

**Note:** Jumping into a DO group with `GOTO` is allowed by the runtime but is very bad programming practice.

## Examples

### DO group in an ERROR clause

```kcml
OPEN #stream, "MainFile","r+"
ERROR DO
    'DisplayError()
    'Prompt()
END DO
```

Both `'DisplayError()` and `'Prompt()` are called whenever an error occurs on the `OPEN` statement. Without the DO group, only a single statement could follow `ERROR`.

### DO group in an IF THEN clause

```kcml
IF x > 0 THEN DO
    PRINT "Positive"
    count = count + 1
END DO
```

Both the `PRINT` and the assignment execute only when `x > 0`.

### Nested DO groups

```kcml
IF condition1 THEN DO
    IF condition2 THEN DO
        'Inner()
    END DO
    ELSE DO
        'Outer_else()
    END DO
END DO
```

DO groups can be freely nested up to a depth of over 50.

## Notes

- For multi-line conditional logic, consider using the structured `IF ... END IF` statement instead. It is generally clearer than `IF THEN DO ... END DO` for complex branches.
- DO groups are specifically for use with `IF THEN`, `ELSE`, and `ERROR`; they are not loops.
- `ENDDO` and `END DO` are interchangeable.
- The loop-like appearance of `DO ... ENDDO` can be confusing: this is **not** a `DO WHILE` loop. For conditional looping see `WHILE ... WEND` or `REPEAT ... UNTIL`.

## See Also

- `IF ... THEN` — single-statement conditional; can use a DO group as its body
- `IF ... END IF` — structured multi-line conditional (recommended over `IF THEN DO`)
- `ELSE` — alternative clause following `IF THEN`
- `ERROR` — error handler clause; can use a DO group as its handler body
