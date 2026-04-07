# ELSE

> Provides an alternative statement or block to execute when the preceding `IF ... THEN` or `ON ... GOSUB` condition was false.

## Syntax

```
IF condition THEN statement : ELSE statement
IF condition THEN DO ... END DO : ELSE DO ... END DO
```

## Description

`ELSE` is placed immediately after an `IF ... THEN`, `ON ... GOSUB`, or `ON ... SELECT` statement. It executes its statement (or `DO` group) when the previous condition was false and the previous branch was not taken.

For multi-statement else blocks, use `ELSE DO ... END DO`.

For the modern structured form, use `IF ... ELSE ... END IF` (see `IF`).

## Example

```kcml
IF count > 10 THEN PRINT "Over" : ELSE PRINT "Under"
```

With DO group:
```kcml
IF count > 10 THEN DO
    PRINT "Over"
    count = 0
END DO : ELSE DO
    PRINT "Under"
    count++
END DO
```

## Notes

- `ELSE` here is the single-line form used with `IF ... THEN`. The structured `IF ... ELSE ... END IF` form (documented in `IF`) is generally preferred.
- `ELSE` can follow `ON ... GOSUB` or `ON ... SELECT` to execute when no branch is taken.

## See Also

- `IF` — conditional statement (covers both `IF ... THEN` and `IF ... END IF` forms)
- `DO` — `DO ... END DO` group for multiple statements
- `ON ... GOSUB` — multi-way branch
- `ON ... SELECT` — multi-way select
