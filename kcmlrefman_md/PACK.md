# PACK (statement)

> Packs a numeric value into a BCD (Binary Coded Decimal) string field using a format image.

## Syntax

```
PACK image, numeric_expr TO alpha_var
PACK image TO alpha_var
```

Where `image` is a format string like `"###.##"` or a numeric field variable with a pack format.

## Description

Converts a numeric value to a packed BCD representation and stores it in the destination alpha variable. The image string uses `#` for digit positions and `.` for the decimal point.

The result length (in bytes) is determined by the image: roughly `(digits + 1) / 2` bytes.

`PACK` is the inverse of `UNPACK` — `PACK` numeric→BCD, `UNPACK` BCD→numeric.

### Image syntax

| Character | Meaning |
|-----------|---------|
| `#` | One decimal digit |
| `.` | Decimal point (implied, stored in metadata) |
| Numeric count | `PACK "5.2"` = 5 digits total, 2 decimal places |

## Examples

```kcml
DIM packed$4, val
val = 12345.67
PACK "######.##", val TO packed$
```

```kcml
REM Round-trip: pack then unpack
DIM price$4, amount
amount = 999.99
PACK "####.##" TO price$        : REM pack current value of amount? — more common:
amount = 1234.56
PACK "######.##", amount TO price$
UNPACK price$ TO amount
PRINT amount                    : REM  1234.56
```

```kcml
REM Using a declared field with pack image
DIM rec$20
DIM price$ = FLD(rec$, 1, 4) FORMAT "####.##"
price$ = PACK(price$)           : REM PACK( function form — see PACKfn
```

## Notes

- BCD packing is used for compact numeric storage in fixed-length records (KISAM files).
- The `PACK` statement form and the `PACK(` function form serve different purposes — the statement packs *to* a variable; `PACK(` returns the format specifier string of a field.
- Field declarations in record layouts often carry an implicit pack image set at `DIM` time.
- Use `UNPACK` to retrieve the numeric value from a packed field.

## See Also

- `UNPACK` — BCD string to numeric
- `PACKfn` — `PACK(` function: returns packing specifier for a field
- `FLD(` — field declaration within a record
