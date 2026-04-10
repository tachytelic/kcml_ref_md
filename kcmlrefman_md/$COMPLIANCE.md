# $COMPLIANCE

> Sets the language compliance level that a KCML program adheres to, controlling which coding rules are enforced at compile and runtime.

## Syntax

```
$COMPLIANCE compliance-level
```

Where `compliance-level` is an integer (0–3).

## Description

`$COMPLIANCE` must appear as one of the first statements in a program. Only `REM`, `$ID`, or blank lines may precede it.

Each compliance level is a superset of the one below it — Level 2 enforces everything Level 1 does, plus its own additional rules.

The compliance level of the currently executing program can be inspected at runtime via byte 57 of the `$MACHINE` string.

Future KCML versions will introduce higher compliance levels to encourage stricter programming standards.

## Compliance Levels

### Level 0 (default)

No special compliance requirements. Behaviour is identical to programs that do not include a `$COMPLIANCE` statement.

### Level 1

- All `DEFSUB` blocks require a matching `ENDSUB` statement.
- Execution is permitted to skip over `DEFSUB...ENDSUB` blocks (i.e. they are not executed inline if fallen into).
- Subroutines may be nested inside one another.
- `FINALLY` clauses are executed after a `RETURN` or a `THROW`.

### Level 2

Includes all Level 1 requirements, plus:

- All variables must be explicitly declared with `DIM` before use.

This allows stricter variable discipline to be enforced in new programs without requiring existing Level 0/1 software to be modified.

### Level 3

Includes all Level 2 requirements, plus:

- `GOTO` is not permitted.
- References to line numbers in statements such as `RESTORE LINE` or `$OPEN` are not permitted.
- `WHILE TRANS` blocks are permitted.
- `$RELEASE` statements are prohibited.

## Future Enforcement

Out-of-scope local variable usage will eventually be restricted at higher compliance levels. Currently this is not enforced; access to local variables outside their scope is only possible through nested subroutines.

## Examples

### Enforce explicit DIMension of all variables

```kcml
$COMPLIANCE 2
: DIM name$30, count
: name$ = "Smith"
: count = 1
```

Without `$COMPLIANCE 2`, undeclared variables are silently auto-created. With it, any reference to an undeclared variable raises a compile error.

### Check compliance level at runtime

```kcml
: DIM machine$256, level
: machine$ = $MACHINE
: level = ASC(STR(machine$, 57, 1))
: PRINT "Compliance level:"; level
```

## Notes

- `$COMPLIANCE` is a **compile-time directive** — it affects how the source is parsed and resolved, not just runtime behaviour.
- Only one `$COMPLIANCE` statement is permitted per program.
- It must appear before any executable statements (only `REM`, `$ID`, or blank lines may precede it).

## See Also

- `$ID` — program identification header directive
- `$MACHINE` — system information string (byte 57 = compliance level)
- `DEFSUB` / `ENDSUB` — structured subroutine blocks (required at Level 1+)
- `DIM` — variable declaration (required at Level 2+)
