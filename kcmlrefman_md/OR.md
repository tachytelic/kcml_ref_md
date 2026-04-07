# OR (bitwise string operator)

> Performs a bitwise OR on two string operands, byte by byte.

## Syntax

```
result$ = string1$ OR string2$
```

## Description

Applies a bitwise OR to each corresponding byte of `string1$` and `string2$`. The result has the same length as the longer operand; the shorter operand is effectively padded with null bytes.

Used for bit-mask operations on binary data and for combining flag bytes.

## Examples

```kcml
DIM a$4, b$4, c$4
a$ = HEX(0F0F0F0F)
b$ = HEX(F0F0F0F0)
c$ = a$ OR b$
DIM hex$8
HEXUNPACK c$ TO hex$
PRINT hex$           : REM  FFFFFFFF
```

```kcml
REM Set bit 0 in a flag byte
DIM flags$1
flags$ = HEX(06)          : REM  00000110
flags$ = flags$ OR HEX(01): REM  set bit 0 → 00000111
HEXUNPACK flags$ TO hex$
PRINT hex$                : REM  07
```

## Notes

- Both operands must be alpha (string) variables; numeric operands require conversion via `HEX(` or packing.
- The result length equals the longer of the two operands.
- Counterparts: `AND` (bitwise AND on strings), `XOR` (bitwise XOR on strings), `NOT` (bitwise complement).

## See Also

- `AND` — bitwise AND on strings
- `XOR` — bitwise XOR on strings
- `NOT` — bitwise NOT on string
- `HEX(` — hex literal to binary string
- `HEXUNPACK` — binary string to hex text
