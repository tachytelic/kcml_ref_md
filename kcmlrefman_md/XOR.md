# XOR (bitwise string operator)

> Performs a bitwise XOR (exclusive OR) on two string operands, byte by byte.

## Syntax

```
result$ = alpha$ XOR beta$
result$ = XOR beta$       (XOR beta$ into result$, single receiver only)
```

## Description

Applies bitwise XOR to each corresponding byte of the two strings, left to right. XOR flips each bit that differs between the two operands.

- If `beta$` is shorter than `result$`: the remaining bytes of `result$` are **left unchanged**.
- If `beta$` is longer than `result$`: the operation terminates when the last byte of `result$` is processed.

The **entire** contents including trailing spaces are operated on for both operands.

`XOR` can also be used in `IF … THEN` statements to separate multiple boolean conditions (logical XOR).

## Examples

```kcml
DIM source$10
source$ = ALL(HEX(0F)) XOR HEX(13)
PRINT HEXOF(source$)    : REM  1C0F0F0F0F0F0F0F0F0F
REM  HEX(0F) XOR HEX(13) = HEX(1C) for byte 1; remaining bytes unchanged
```

```kcml
REM XOR for simple encryption/decryption (same key applied twice = original)
DIM plain$20, cipher$20, key$20
plain$ = "Secret message  "
key$ = ALL(HEX(A5))
cipher$ = plain$ XOR key$
plain$ = cipher$ XOR key$    : REM  decrypt
PRINT plain$
```

```kcml
REM Logical XOR in IF
IF a == 1 XOR b == 1 THEN PRINT "Exactly one is true"
```

## Notes

- Binary XOR: operates on bytes.
- Logical XOR: in `IF` conditions separates boolean expressions (TRUE XOR TRUE = FALSE).
- The `XOR beta$` form (no left operand) XORs `beta$` into the variable on the left of `=`; only one receiver allowed in this form.

## See Also

- `AND` — bitwise AND on strings
- `OR` — bitwise OR on strings
- `NOT` — bitwise NOT on string
- `HEXUNPACK` — inspect binary string as hex
