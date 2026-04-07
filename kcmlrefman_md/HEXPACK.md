# HEXPACK

> Converts an ASCII hex-digit string into its binary equivalent (each two hex characters → one byte).

## Syntax

```
HEXPACK dest_variable FROM source_variable
```

| Element | Description |
|---------|-------------|
| `dest_variable` | Alpha variable to receive binary data (should be half the source length) |
| `source_variable` | Alpha variable containing ASCII hex digit pairs |

## Description

`HEXPACK` converts each pair of hexadecimal ASCII characters in `source_variable` into a single binary byte in `dest_variable`. Trailing spaces in `source_variable` are ignored.

The destination should be at least half the length of the source. If too short, an error results. If longer, extra bytes are left unchanged.

This is the inverse of `HEXUNPACK`.

## Examples

```kcml
: DIM pb$2, pa$8, ph$4
: pb$ = HEX(6FC9)
: HEXUNPACK pb$ TO pa$       REM pa$ = "6FC9"
: HEXPACK ph$ FROM pa$       REM ph$ = HEX(6FC9) (2 bytes)
: HEXUNPACK ph$ TO pa$       REM back to "6FC9"
: PRINT "Round-trip="; STR(pa$,1,4)
: $END
```

Output:
```
Round-trip=6FC9
```

Supports arrays and substrings:
```kcml
HEXPACK junk1$ FROM junk2$
HEXPACK point$() FROM table$()
HEXPACK STR(pot$, 1, 4) FROM STR(pan$, 10, 8)
```

## Notes

- Input characters must be valid hex digits (`0–9`, `A–F`, `a–f`). Invalid characters cause a runtime error.
- Trailing spaces in the source are ignored.
- Destination must be half the length of the significant source (or longer; extra bytes unchanged).
- Use `HEXPACK` to convert user-entered or text-based hex data into binary for storage or transmission.

## See Also

- `HEXUNPACK` — convert binary bytes to ASCII hex digits (inverse operation)
- `HEX(` — embed binary bytes as a literal
