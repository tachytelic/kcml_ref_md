# SUB / SUBC (binary subtraction operator)

> Performs binary subtraction on alpha string values, byte by byte.

## Syntax

```
alpha_receiver = alpha_receiver SUB alpha_operand
alpha_receiver = alpha_receiver SUBC alpha_operand
```

## Description

**`SUB`** — subtracts each byte of `alpha_operand` from the corresponding byte of `alpha_receiver`, working right to left. **No carry propagation** between bytes — each byte is treated independently.

**`SUBC`** — treats the entire `alpha_operand` as a single binary number and subtracts it from `alpha_receiver` with **carry propagation** across bytes (like a multi-byte integer subtraction).

If the operands differ in length, the shorter one is implicitly zero-extended from the left. If the result overflows the receiver's length, the leftmost excess bytes are truncated.

## Examples

```kcml
REM SUB — per-byte, no carry
DIM record$2
record$ = HEX(0410)
record$ = record$ SUB HEX(00F9)
REM  byte 1: 04 - 00 = 04; byte 2: 10 - F9 = 17 (wraps within byte)
```

```kcml
REM SUBC — full multi-byte subtraction with carry
DIM record$2
record$ = HEX(0410)
record$ = record$ SUBC HEX(00F9)
REM  0x0410 - 0x00F9 = 0x0317
DIM hex$4
HEXUNPACK record$ TO hex$
PRINT hex$     : REM  0317
```

```kcml
REM Chained operations
DIM Sector$4
Sector$ = Sector$ SUBC type$ SUBC record$ SUB flag$
```

## Notes

- `SUB` / `SUBC` operate on the **entire** string contents including trailing spaces.
- Use `SUBC` for multi-byte integer arithmetic; use `SUB` for per-byte transformations.
- Counterpart: `ADD` / `ADDC` for binary addition.

## See Also

- `ADD` / `ADDC` — binary addition on strings
- `OR` / `AND` / `XOR` — bitwise string operators
- `HEXUNPACK` — inspect binary string as hex
