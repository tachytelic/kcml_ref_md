# DSC (decimal subtract with carry)

> Performs BCD (Binary Coded Decimal) subtraction on two string values, with borrow propagation, storing the result in the receiver.

## Syntax

```
alpha_receiver = [source] DSC alpha_operand
```

| Element | Description |
|---------|-------------|
| `source` | Optional: a string to use as the minuend. If omitted, the receiver's current value is used. |
| `alpha_operand` | The BCD string to subtract (the subtrahend) |

## Description

`DSC` performs **decimal subtraction with borrow** (BCD arithmetic). It is the counterpart to `DAC` (add). Each byte is treated as a decimal digit (0–9). Borrow propagates from right to left.

Subtraction proceeds byte by byte from **right to left**. `DSC` is valid only in the alpha (string) expression portion of an assignment statement.

**Important:** Both operands must consist entirely of ASCII digit characters (`0`–`9`). Any other byte produces undefined results.

If the operand is shorter than the receiver, it is padded with leading zeros. If the result overflows, the leftmost bytes are truncated.

## Examples

```kcml
color$ = count$ DSC bytes$
paint$ = field$ DSC HEX(0099)
```

## Notes

- `DSC` is for **decimal** (BCD) arithmetic. For binary subtraction, combine `ADDC` with two's complement.
- For BCD addition, see `DAC`.
- Operands must be valid BCD — any non-digit byte gives undefined results.

## See Also

- `DAC` — decimal add with carry
- `ADD` / `ADDC` — binary addition on string values
- `PACK` — convert decimal string to packed BCD
- `UNPACK` — convert packed BCD to decimal string
