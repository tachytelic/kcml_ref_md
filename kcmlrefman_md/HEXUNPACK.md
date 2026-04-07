# HEXUNPACK

> Converts a binary string to a printable ASCII hex-digit string (each byte → two hex characters).

## Syntax

```
HEXUNPACK source_variable TO dest_variable
```

| Element | Description |
|---------|-------------|
| `source_variable` | Alpha variable containing binary data |
| `dest_variable` | Alpha variable to receive the hex digits (must be at least twice as long) |

## Description

`HEXUNPACK` converts each byte in `source_variable` to two uppercase hexadecimal ASCII characters in `dest_variable`. The destination should be at least twice the length of the source. If `dest_variable` is too short, an error results. If longer, the remaining bytes are left unchanged.

This is the inverse of `HEXPACK`.

## Examples

```kcml
: DIM pb$2, pa$8
: pb$ = HEX(6FC9)
: HEXUNPACK pb$ TO pa$
: PRINT "HEXUNPACK: ["; STR(pa$,1,4); "]"
: $END
```

Output:
```
HEXUNPACK: [6FC9]
```

### Extracting a packed date field

```kcml
: DIM hex$12, date$10, rec$512
: REM rec$ contains a 4-byte packed date at offset 82
: HEXUNPACK STR(rec$, 82, 4) TO hex$
: date$ = STR(hex$, 7, 2) & "/" & STR(hex$, 5, 2) & "/" & STR(hex$, 1, 4)
: PRINT date$    REM prints DD/MM/YYYY
```

Supports arrays and substrings:
```kcml
HEXUNPACK junk1$ TO junk2$
HEXUNPACK point$() TO table$()
HEXUNPACK STR(pot$, 1, 4) TO STR(pan$, 10, 8)
```

## Notes

- Output characters are uppercase hex digits (`0–9`, `A–F`).
- Destination must be exactly double the length of the source for exact fit; a longer destination is OK (extra bytes unchanged).
- Use `HEXUNPACK` to display or log binary data in readable form.
- Use `HEXPACK` to convert back from hex digits to binary.

## See Also

- `HEXPACK` — convert ASCII hex digits to binary bytes (inverse operation)
- `HEX(` — embed binary bytes as a literal
- `STR(` — extract a substring
