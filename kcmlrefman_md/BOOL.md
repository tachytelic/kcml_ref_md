# BOOL (bitwise string operator)

> Performs one of 16 possible bitwise logical operations on corresponding bytes of two string values, storing the result in the receiver.

## Syntax

```
alpha_receiver = [source] BOOL h operand
```

| Element | Description |
|---------|-------------|
| `alpha_receiver` | The string variable that receives the result |
| `source` | Optional: a string operand. If omitted, the receiver's current value is used as one side of the operation. |
| `h` | A single hex digit (`0`–`9` or `A`–`F`) selecting the logical function. Must be surrounded by spaces. |
| `operand` | A string value, hex literal, `ALL(`, or alpha variable |

## Description

`BOOL` applies a byte-by-byte logical function across two strings. The 16 possible operations are selected by the hex digit `h`.

- If the operand is **shorter** than the receiver, remaining bytes are left unchanged.
- If the operand is **longer** than the receiver, the operation stops at the end of the receiver.
- Trailing spaces in both operands are included.

`BOOL` is valid only in the alpha (string) expression portion of an assignment statement.

### Logical function table

| `h` | Binary | Logical Function |
|-----|--------|-----------------|
| `0` | 0000 | null (zero) |
| `1` | 0001 | NOR (not OR) |
| `2` | 0010 | operand does not imply receiver |
| `3` | 0011 | complement of receiver |
| `4` | 0100 | receiver does not imply operand |
| `5` | 0101 | complement of operand |
| `6` | 0110 | XOR (exclusive OR) |
| `7` | 0111 | NAND (not AND) |
| `8` | 1000 | AND |
| `9` | 1001 | equivalence (XNOR) |
| `A` | 1010 | receiver = operand (copy operand to receiver) |
| `B` | 1011 | receiver implies operand |
| `C` | 1100 | operand = receiver (copy receiver to operand... stores in receiver unchanged) |
| `D` | 1101 | operand implies receiver |
| `E` | 1110 | OR |
| `F` | 1111 | identity (no change) |

Common shortcuts:
- `BOOL 8` = `AND`
- `BOOL E` = `OR`
- `BOOL 6` = `XOR`

## Examples

### Set specific bits (OR equivalent)

```kcml
STR(was$, 4, 2) = BOOL E HEX(2F)
```

### XOR to toggle bits

```kcml
now$ = then$ BOOL 6 ALL(HEX(4F))
```

### NAND

```kcml
test1$ = test21$ BOOL 7 HEX(FF)
```

### Three-operand form

```kcml
test$ = BOOL A HEX(7F)
```

## Notes

- The hex digit `h` must be surrounded by spaces: `BOOL A HEX(7F)`, not `BOOLA`.
- The named operators `AND`, `OR`, `XOR` are more readable for common operations; use `BOOL` for the other 13 functions.
- For the boolean conditional function `BOOL(`, see `BOOL(` (function).

## See Also

- `AND` — bitwise AND (equivalent to `BOOL 8`)
- `OR` — bitwise OR (equivalent to `BOOL E`)
- `XOR` — bitwise XOR (equivalent to `BOOL 6`)
- `BOOL(` — boolean conditional function
- `ALL(` — fill a string with one repeated byte
- `HEX(` — create a string from hex literals
