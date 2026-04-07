# ROTATE

> Rotates the bits of each byte (or the entire value) of an alpha variable.

## Syntax

```
ROTATE (alpha_var, n)
ROTATEC(alpha_var, n)
```

Where `-8 < n < 8`.

## Description

**`ROTATE`** — rotates each **byte** of `alpha_var` independently by `n` bit positions. All bytes are operated on, including trailing spaces.

**`ROTATEC`** — rotates the **entire** value of `alpha_var` as one multi-byte unit by `n` bit positions.

- Positive `n`: rotate **left** (bits shifted toward MSB).
- Negative `n`: rotate **right** (bits shifted toward LSB).

## Examples

```kcml
DIM test$1
test$ = HEX(0F)       : REM  00001111
ROTATE(test$, 4)
DIM hex$2
HEXUNPACK test$ TO hex$
PRINT hex$            : REM  F0  (rotated left by 4: 11110000)
```

```kcml
REM Byte-by-byte rotate on a multi-byte string
DIM data$4
data$ = HEX(01020304)
ROTATE(data$, 1)      : REM  each byte rotated left 1: 02 04 06 08
```

```kcml
REM Whole-value rotate
DIM bytes$2
bytes$ = HEX(0102)
ROTATEC(bytes$, -2)   : REM  rotate entire 16-bit value right 2
```

## Notes

- Rotation is circular — bits that fall off one end reappear at the other.
- `ROTATE` vs `ROTATEC`: use `ROTATE` for per-byte operations, `ROTATEC` when the bytes form a single multi-byte integer.
- `n` must be in the range `-7` to `7` (exclusive of ±8).

## See Also

- `OR` — bitwise OR on strings
- `AND` — bitwise AND on strings
- `XOR` — bitwise XOR on strings
- `HEXUNPACK` — binary to hex text
