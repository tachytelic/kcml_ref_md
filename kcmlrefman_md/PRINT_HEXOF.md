# PRINT HEXOF(

> Prints the hexadecimal representation of an alpha variable's bytes.

## Syntax

```
PRINT HEXOF(alpha_var)
PRINT HEXOF(-alpha_var)    (spaced pairs)
PRINT HEXOF(+alpha_var)    (hex + ASCII side-by-side)
```

`HEXOF(` can appear anywhere in a `PRINT` statement alongside `AT(`, `BOX(`, `TAB(`.

## Description

Prints each byte of `alpha_var` as two hex digits. **Trailing spaces (`HEX(20)`) are also printed** (unlike `HEXUNPACK` which stops at the content length).

| Prefix | Output format |
|--------|---------------|
| (none) | Continuous hex string: `414243...` |
| `-` | Spaced pairs: `41 42 43 ...` |
| `+` | Hex pairs on left, ASCII equivalent on right (16 bytes per line) |

## Examples

```kcml
DIM test$8
test$ = "ABCDEFG "
PRINT HEXOF(-test$)
REM   4142 4344 4546 4720
```

```kcml
PRINT HEXOF(+test$)
REM   4142 4344 4546 4720
REM   *ABCDEFG *
```

```kcml
REM Inspect a binary record field
DIM rec$20
rec$ = HEX(00010203FFFEFD00)
PRINT HEXOF(-rec$)      : REM  0001 0203 FFFE FD00 2020 2020 2020 2020 2020 2020
```

## Notes

- Trailing spaces (the padding of a fixed-length string) **are** included in the hex output.
- Use `HEXUNPACK` when you need a hex string in a variable rather than printed output.
- The `+` form is useful for debugging binary data — shows both hex and printable ASCII.

## See Also

- `HEXUNPACK` — binary string to hex text variable
- `HEXPACK` — hex text to binary string
- `PRINT` — base print statement
