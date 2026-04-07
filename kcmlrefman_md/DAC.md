# DAC (decimal add with carry)

> Performs BCD (Binary Coded Decimal) addition on two string values, with carry propagation, storing the result in the receiver.

## Syntax

```
alpha_receiver = [source] DAC alpha_operand
```

| Element | Description |
|---------|-------------|
| `source` | Optional: a string to use as one operand. If omitted, the receiver's current value is used. |
| `alpha_operand` | The BCD string to add |

## Description

`DAC` performs **decimal addition with carry** (BCD arithmetic) on two string values. Each byte is treated as a decimal digit (0–9). Carry propagates from right to left when the sum of a column exceeds 9.

Addition proceeds byte by byte from **right to left** (least significant digit first).

`DAC` is valid only in the alpha (string) expression portion of an assignment statement.

**Important:** Both operands must consist entirely of ASCII digit characters (`0`–`9`). Any other byte produces undefined results.

If the operand is shorter than the receiver, it is padded with leading zeros. If the result overflows the receiver length, the leftmost digits are truncated.

## Examples

### Basic BCD addition

```kcml
bytes$ = old$ DAC new$
bytes$ = old$ DAC HEX(0099)
```

### Using PACK/UNPACK with DAC

`DAC` is typically used alongside `PACK` and `UNPACK` to work with packed BCD numbers:

```kcml
UNPACK packed_num$ TO bcd$
bcd$ = bcd$ DAC increment$
PACK bcd$ TO packed_num$
```

## Notes

- `DAC` is for **decimal** (BCD) arithmetic. For binary arithmetic, see `ADD`/`ADDC`.
- For subtraction, see `DSC` (decimal subtract with carry).
- The operands must be valid BCD — any non-digit byte gives undefined results.

## See Also

- `DSC` — decimal subtract with carry
- `ADD` / `ADDC` — binary addition on string values
- `PACK` — convert decimal string to packed BCD
- `UNPACK` — convert packed BCD to decimal string
