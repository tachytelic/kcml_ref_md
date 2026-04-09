# $CRC(

> Calculates a 32-bit CRC (Cyclic Redundancy Check) for a string.

## Syntax

```
alpha_receiver = $CRC(alpha_expression [, start_value$])
```

## Description

`$CRC(` computes a 32-bit CRC over every byte of `alpha_expression` (including trailing spaces) and stores the 4-byte binary result in `alpha_receiver`. The receiver must be at least 4 bytes long.

CRCs are widely used for data integrity checking in communications and file transfer — if the CRC of received data matches the CRC of the original, the data is intact.

An optional second argument `start_value$` (must be at least 4 bytes) seeds the CRC with a custom starting value. If omitted, the conventional seed `HEX(FFFFFFFF)` is used. This allows chained CRC calculations across multiple chunks of data.

`$CRC(` can only appear on the **right-hand side** of an assignment. It cannot be combined with `&`, `AND`, `OR`, or other string operators in the same expression.

## Examples

### Example 1 — Basic CRC of a string
```kcml
01000 REM Calculate CRC and display as hex
: DIM data$50, crc$4, hex$12
: data$ = "Hello World"
: crc$ = $CRC(data$)
: HEXUNPACK crc$ TO hex$
: PRINT "CRC of Hello World: " ; RTRIM(hex$)
: $END
```
**Output:**
```
CRC of Hello World: EE1CE8E0
```

### Example 2 — CRC is deterministic and sensitive to content
```kcml
01000 REM Same data gives same CRC, different data gives different CRC
: DIM d1$50, d2$50, c1$4, c2$4, h1$12, h2$12
: d1$ = "Hello World"
: d2$ = "Hello World!"
: c1$ = $CRC(d1$)
: c2$ = $CRC(d2$)
: HEXUNPACK c1$ TO h1$
: HEXUNPACK c2$ TO h2$
: PRINT "CRC of 'Hello World':  " ; RTRIM(h1$)
: PRINT "CRC of 'Hello World!': " ; RTRIM(h2$)
: $END
```
**Output:**
```
CRC of 'Hello World':  EE1CE8E0
CRC of 'Hello World!': A095E349
```

### Example 3 — Data integrity check pattern
```kcml
01000 REM Verify data integrity using CRC
: DIM original$100, received$100, c1$4, c2$4, h1$10, h2$10
: original$ = "Important data payload"
: received$ = "Important data payload"
: c1$ = $CRC(original$)
: c2$ = $CRC(received$)
: IF c1$ == c2$ THEN PRINT "Data integrity OK"
: IF c1$ <> c2$ THEN PRINT "Data corruption detected!"
: $END
```
**Output:**
```
Data integrity OK
```

## Notes

- The result is a **4-byte binary value** — use `HEXUNPACK` to display it as hex.
- All bytes including trailing spaces are included in the CRC. If comparing CRCs, ensure both strings have the same declared length or trim consistently.
- To chain CRC calculations: pass the result of the first as `start_value$` of the next.
- Cannot be used in the same expression as `&`, `AND`, `OR`.
