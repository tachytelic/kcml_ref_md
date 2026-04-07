# ADD / ADDC (binary string add operator)

> Performs byte-by-byte or multi-byte binary addition on two string values, storing the result in the receiver.

## Syntax

```
alpha_receiver = [source] ADD  alpha_operand
alpha_receiver = [source] ADDC alpha_operand
```

| Element | Description |
|---------|-------------|
| `ADD` | Add without carry propagation between bytes (each byte is independent) |
| `ADDC` | Add with carry propagation (treats the strings as a single multi-byte binary number) |
| `source` | Optional: a string to use as one operand. If omitted, the receiver's current value is used. |
| `alpha_operand` | The string to add |

## Description

`ADD` and `ADDC` perform binary addition on string values and are valid only in the alpha (string) expression portion of an assignment statement.

### ADD — no carry

Addition is performed **byte by byte, right to left**, with no carry between bytes. Each byte is treated as an independent 8-bit value. Any overflow within a byte wraps around.

### ADDC — with carry

`ADDC` treats the entire string as a **single binary integer** (big-endian, most-significant byte first). Carry propagates between bytes from right to left. This is useful for incrementing packed binary counters.

### Length handling

- If the operand is shorter than the receiver, it is implicitly extended with leading zeros.
- If the result is longer than the receiver, the leftmost overflow bytes are truncated.

Up to multiple `ADDC` expressions can be chained in one statement.

## Examples

### ADDC — increment a packed 4-byte binary counter

```kcml
: DIM a$4, b$4
: a$ = BIN(255, 4)
: b$ = BIN(1, 4)
: a$ = a$ ADDC b$
: PRINT "255+1="; VAL(a$, 4)
: a$ = BIN(256, 4)
: b$ = BIN(1, 4)
: a$ = a$ ADDC b$
: PRINT "256+1="; VAL(a$, 4)
: $END
```

Output:
```
255+1= 256
256+1= 257
```

### ADD syntax examples from manual

```kcml
variable$ = ADD HEX(FFFC)
variable$ = ADDC ALL(section$)
FLD(record1$.type$) = flag1$ ADDC other$
see$ = ADDC saw$ ADDC record$ ADDC record$
```

## Notes

- `ADD` (no carry) is unusual — it adds each byte independently with no ripple. Most uses of binary arithmetic on strings want `ADDC`.
- Pair with `BIN(` to create binary strings and `VAL(` to read them back as numbers.
- For BCD (decimal) packed arithmetic, see `DAC` (decimal add with carry) and `DSC` (decimal subtract with carry).

## See Also

- `DAC` — decimal add with carry (BCD arithmetic)
- `DSC` — decimal subtract with carry
- `BIN(` — convert a number to a packed binary string
- `VAL(` — convert a packed binary string back to a number
- `PACK`, `UNPACK` — BCD/packed decimal conversion
