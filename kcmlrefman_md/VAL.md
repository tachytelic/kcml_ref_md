# VAL(

> Converts a binary string to a numeric value. Inverse of BIN(.

## Syntax

```
VAL(alpha_expr, n)
VAL(alpha_expr)    (n defaults to 1)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `alpha_expr` | Binary string (up to 6 bytes) |
| `n` | Number of bytes to convert (1–6); negative = signed (two's complement) |

## Description

Reads `|n|` bytes from `alpha_expr` and interprets them as a binary integer:
- Positive `n`: unsigned integer.
- Negative `n`: signed two's complement integer.

The inverse operation is `BIN(`.

### Precision warning

6-byte strings allow values up to 0xFFFFFFFFFFFF (281,474,976,710,655 = 15 digits), which exceeds KCML's 13-digit numeric precision. Limit to 5 bytes or ensure 6-byte values stay below ~1.0E13.

## Examples

```kcml
PRINT VAL("ABC", 3)     : REM  0x414243 = 4276803
PRINT VAL(HEX(0100), 2) : REM  256
PRINT VAL(HEX(FF), -1)  : REM  -1  (signed 1-byte)
PRINT VAL(HEX(7F), -1)  : REM  127 (signed max for 1 byte)
```

```kcml
test = VAL(alpha$(1))     : REM  1-byte unsigned
test1 = VAL("ABC", 3)     : REM  3-byte unsigned
test1 = VAL(array$(2), -3): REM  3-byte signed
IF VAL(temp$, 6) > test(count) THEN PRINT "Large"
```

## Notes

- `VAL(` reads from the start of the string — only the first `|n|` bytes are used.
- To read from an offset, use `STR(`: `VAL(STR(buf$, offset, n), n)`.
- Use `VAL(` for reading binary packed integers; for BCD-packed decimals, use `UNPACK`.

## See Also

- `BIN(` — numeric to binary string (inverse)
- `UNPACK` — BCD to numeric
- `HEX(` — hex literal to binary string
