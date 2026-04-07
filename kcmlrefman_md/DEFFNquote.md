# DEFFN' (subroutine entry point)

> **Deprecated.** Defines a subroutine entry point. Use `DEFSUB` instead.

## Syntax

```
DEFFN 'label [(variable [, variable] ...)]
    ...
RETURN
```

| Element | Description |
|---------|-------------|
| `label` | An integer (0–9999) or symbolic name (up to 120 alphanumeric characters, first char must be a letter; underscores allowed) |
| `variable` | Optional argument variables — alpha, numeric, field, pointer, or array |

## Description

`DEFFN'` defines a subroutine entry point, called with `GOSUB'`. When called, KCML scans for the matching `DEFFN'` label and continues execution from there. `RETURN` transfers control back to the statement after the `GOSUB'`.

**This statement is deprecated and replaced by `DEFSUB`.** Use `DEFSUB` for all new code. `DEFFN'` is documented here for reading existing programs.

### Key differences from DEFSUB

| Feature | DEFFN' | DEFSUB |
|---------|--------|--------|
| Local variables | No (shares caller's scope) | Yes (automatic with END SUB) |
| Argument handling | Passed by reference (shared) | Passed by value (local copy) |
| Status | Deprecated | Current |

With `DEFFN'`, arguments are passed to the same variables used in the `DEFFN'` definition — changes to those variables inside the subroutine affect the caller directly (similar to `BYREF`). With `DEFSUB`, arguments are copied into local variables.

### Symbolic vs integer labels

- **Symbolic labels** (e.g. `DEFFN 'calc(...)`) can be called from within expressions as functions.
- **Integer labels** (e.g. `DEFFN 1000(...)`) cannot be used in expressions.
- Symbolic names: up to 120 alphanumeric characters; first character must be a letter; underscores allowed, spaces not.

### Array and field arguments

```kcml
'calc(first, second, name$(), .balance)
...
DEFFN 'calc(a, b, tmp$(), .newbal)
```

Arrays and field variables can be passed. Argument count and type must match exactly.

## Example

```kcml
100 GOSUB 'greet("Hello")
200 STOP
300 DEFFN 'greet(msg$)
310     PRINT msg$
320 RETURN
```

## Notes

- `DEFFN'` is found extensively in older KCML source code (like the `.Bre` files in `kcml_source/PF/`).
- For new code, always use `DEFSUB` / `END SUB` with local variables.
- KCML evaluates all arguments of a `GOSUB'` with symbolic labels before passing them; integer label calls evaluate arguments one at a time.

## See Also

- `DEFSUB` — modern subroutine definition (preferred)
- `GOSUB'` — call a subroutine defined with `DEFFN'` or `DEFSUB`
- `RETURN` — return from subroutine
- `LOCAL DIM` — declare local variables inside `DEFSUB`
- `BYREF` — pass arguments by reference
