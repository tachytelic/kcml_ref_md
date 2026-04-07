# IF ... THEN

> Executes a single statement (or `DO` group) conditionally on one line.

## Syntax

```
IF ( condition ) THEN statement
IF ( condition ) THEN DO
    statements
END DO
```

The `statement` must be a **simple** KCML statement. Complex multi-line statements (`IF...END IF`, `FOR...NEXT`, `WHILE...WEND`, `REPEAT...UNTIL`) must not be used as the THEN target — use the structured `IF ... END IF` form instead.

## Description

`IF ... THEN` is the single-line conditional form, compatible with BASIC-2 style code. If the condition is true, the statement after `THEN` executes; otherwise it is skipped.

```kcml
IF (x == 5) THEN PRINT "x is 5"
IF (err <> 0) THEN GOSUB 2000
```

### DO group

To conditionally execute multiple simple statements, use a `DO` group:

```kcml
IF (x > 0) THEN DO
    total = total + x
    count++
END DO
```

### Warning: complex THEN targets

If a complex statement follows `THEN`, its body always executes because KCML skips only to the next `:` or end-of-line:

```kcml
REM BAD — the FOR loop body always runs regardless of condition:
IF (x > 0) THEN FOR i = 1 TO 10 ...
```

Use `IF ... END IF` for these situations.

## Examples

```kcml
: DIM x
: x = 5
: IF (x == 5) THEN PRINT "IF THEN: x is 5"
: IF (x <> 5) THEN PRINT "should not print"
: $END
```

Output:
```
IF THEN: x is 5
```

Conditional error check (common pattern in -p scripts):
```kcml
: IF ki_status <> 0 THEN PRINT "Read failed"
: IF ki_status <> 0 THEN $END
```

## Notes

- `IF ... THEN` is available for backward compatibility. Prefer `IF ... END IF` for clarity and safety.
- The `THEN` keyword is not used in `IF ... END IF` — do not mix the two forms.
- Only one statement binds to `THEN`. In `:` separated script mode, `$END` after a `THEN` conditional fires unconditionally — see the Conditional `$END` pattern in CLAUDE.md.

## See Also

- `IF ... END IF` — structured multi-statement conditional (preferred)
- `SELECT CASE` — multi-way branch
- `DO ... END DO` — statement group
