# COM CLEAR

> Converts common (`COM`) variables back to non-common (`DIM`) variables without changing their values.

## Syntax

```
COM CLEAR [variable_name]
```

| Form | Effect |
|------|--------|
| `COM CLEAR` | Converts **all** currently defined common variables to non-common |
| `COM CLEAR varname` | Converts `varname` and all common variables defined **after** it to non-common |
| `COM CLEAR non_common_var` | Converts all non-common variables defined **before** `non_common_var` to common |

## Description

`COM CLEAR` changes whether variables are persistent across `LOAD` statements. The dimensions and contents of the variables are left unchanged — only their common/non-common status changes.

After `COM CLEAR`, the affected variables will be lost on the next `LOAD` (just like regular `DIM` variables).

### Converting to common (reverse direction)

If a **non-common** variable name is specified, all non-common variables defined **before** the named variable are promoted to common. This allows fine-grained control over which variables persist.

## Examples

### Clear all common variables before load

```kcml
COM CLEAR : LOAD "PRG-1"
```

All previously defined common variables become non-common; after `LOAD "PRG-1"`, every variable is cleared.

### Clear a subset (from a named variable onwards)

```kcml
COM one, two, three, four(100), five(10)
...
COM CLEAR three
```

`three`, `four`, and `five` become non-common. `one` and `two` remain common.

## Notes

- `COM CLEAR` does not erase variable values — it only changes persistence status.
- After `COM CLEAR`, variables behave exactly like `DIM` variables: they are lost on the next `LOAD`.
- Use `COM CLEAR` before loading an unrelated program to avoid unintended data leakage through shared common variables.

## See Also

- `COM` — declare common (persistent) variables
- `DIM` — declare non-common variables
- `LOAD` — load a new program (COM variables survive; DIM variables do not)
- `CLEAR` — full environment reset
