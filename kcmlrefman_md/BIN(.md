# BIN(

> Converts a numeric integer to its binary (packed byte) representation as a string.

## Syntax

```
alpha_receiver = ... BIN( numeric_expression [, bytes] ) ...
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | The integer value to convert. Only the integer portion is used. |
| `bytes` | Optional. Integer from −6 to +6 specifying the number of bytes to produce. Positive = unsigned; negative = signed two's complement. Default is 1 if omitted. |

## Description

`BIN(` packs an integer into a binary string of 1–6 bytes. It is the counterpart to `VAL(` (which unpacks binary strings back to numbers).

`BIN(` is valid **only** in the alpha (string) expression portion of an assignment statement — not in PRINT or numeric expressions.

### The `bytes` argument

| Sign of `bytes` | Interpretation |
|-----------------|---------------|
| Positive | Unsigned binary. The value is stored as a positive integer. |
| Negative | Signed two's complement. Allows negative values. |
| Omitted | Equivalent to 1 (one unsigned byte). |

Only the integer portion of `bytes` is used. Values outside the range −6 to +6 cause a runtime error.

**Precision note:** 6-byte strings can represent values up to 0xFFFFFFFFFFFF (281,474,976,710,655), which has 15 digits — exceeding KCML's 13-digit precision. Restrict to 5 bytes or ensure values stay below approximately 1.0×10¹³ when using 6 bytes.

Up to 10 `BIN(` calls are allowed per statement.

## Examples

### Round-trip with VAL(

```kcml
: DIM s$6, v
: s$ = BIN(65, 1)
: v = VAL(s$, 1)
: PRINT "BIN(65,1) -> VAL="; v
: s$ = BIN(1000, 2)
: v = VAL(s$, 2)
: PRINT "BIN(1000,2) -> VAL="; v
: s$ = BIN(-1, -2)
: v = VAL(s$, -2)
: PRINT "BIN(-1,-2) -> VAL="; v
: $END
```

Output:
```
BIN(65,1) -> VAL= 65
BIN(1000,2) -> VAL= 1000
BIN(-1,-2) -> VAL=-1
```

### In assignment expressions

```kcml
care$ = BIN(variable1 * 4, 3)
string$ = BIN(character1, -apple1)
```

### Storing a record field in binary

```kcml
: DIM rec$20, count
: count = 12345
: STR(rec$, 1, 4) = BIN(count, 4)
: $END
```

## Notes

- `BIN(` can only appear on the right-hand side of an alpha assignment; not valid in PRINT or numeric contexts.
- Pair with `VAL(` to decode: `v = VAL(string$, bytes)` where `bytes` matches the sign/size used in `BIN(`.
- Maximum 10 `BIN(` functions per statement.

## See Also

- `VAL(` — convert a binary string back to a numeric value
- `HEX(` — create a string from hex byte literals
- `HEXUNPACK` — convert a binary string to a hex string representation
