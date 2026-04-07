# AND (bitwise string operator)

> Performs a bitwise AND on each byte of the receiver variable against the operand, storing the result back in the receiver.

## Syntax

```
alpha_receiver = [source AND] operand
alpha_receiver = AND operand
```

| Element | Description |
|---------|-------------|
| `alpha_receiver` | The string variable that receives the result. Its entire contents (including trailing spaces) are operated on. |
| `source` | Optional: another string. If present, the AND is between `source` and `operand`, with the result stored in `receiver`. |
| `operand` | A string value, hex literal, `ALL(`, or alpha variable. |

## Description

`AND` performs a **byte-by-byte bitwise AND** across the receiver variable and the operand, left to right:
- If the operand is **shorter** than the receiver, the remaining bytes of the receiver are left unchanged.
- If the operand is **longer** than the receiver, the operation stops at the last byte of the receiver.
- Trailing spaces in both the receiver and operand **are** included in the operation.

`AND` is valid only in the alpha (string) assignment expression — not in numeric expressions or conditions. (For boolean AND in conditions, use the `AND` keyword inside `IF`.)

## Examples

### Strip high bit from every byte (7-bit ASCII masking)

```kcml
: DIM s$4
: s$ = HEX(FF FF FF FF)
: s$ = AND ALL(HEX(7F))
: PRINT s$
: $END
```

### Convert lowercase to uppercase (clear bit 5)

```kcml
: DIM s$4
: s$ = HEX(61 62 63 64)
: s$ = AND ALL(HEX(DF))
: PRINT s$
: $END
```

Output:
```
ABCD
```

### Mask first two bytes, zero remaining

```kcml
: DIM s$4, mask$4
: s$ = HEX(41 42 43 44)
: mask$ = HEX(FF FF 00 00)
: s$ = s$ AND mask$
: PRINT s$
: $END
```

Output: `AB  ` (first two bytes kept, last two zeroed to null/space)

### Source-form three-operand AND

```kcml
: DIM result$4, a$4, mask$4
: a$ = HEX(61 62 63 64)
: mask$ = ALL(HEX(DF))
: result$ = a$ AND mask$
: PRINT result$
: $END
```

## Notes

- `AND` (bitwise string operator) is distinct from `AND` used in `IF` conditions (which is a logical boolean operator).
- Use `ALL(HEX(xx))` to create a uniform mask across a string of any length.
- `AND` is equivalent to `BOOL 8`.
- Related operators: `OR` (BOOL E), `XOR` (BOOL 6).

## See Also

- `OR` — bitwise OR on string variables
- `XOR` — bitwise exclusive OR on string variables
- `BOOL` — generalised bitwise operator (16 logical functions)
- `ALL(` — create a string filled with one repeated byte
- `HEX(` — create a string from hex byte literals
