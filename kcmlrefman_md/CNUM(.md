# CNUM(

> Converts a string representation of a number to a KCML numeric value.

## Syntax

```
CNUM( string_expression )
```

| Parameter | Description |
|-----------|-------------|
| `string_expression` | A string containing a number in integer, float, or exponential notation |

## Description

`CNUM(` parses a string and returns its numeric value. It handles:
- Integer numbers: `"1234"` → 1234
- Floating point: `"1234.1234"` → 1234.1234
- Negative numbers: `"-1234"` → −1234
- Exponential notation: `"12e2"` → 1200

Decoding stops at the first non-numeric character, so the string does not need to be space-padded or stripped.

Only the first 32 characters of the string are used for the conversion.

`CNUM(` is valid wherever a numeric expression is legal.

## Examples

```kcml
ret = CNUM("1234")
ret = CNUM("1234.1234")
ret = CNUM("-1234")
ret = CNUM("12e2")
```

## Notes

- `CNUM(` may not be available in all KCML versions (not present in KCML 06.00.88). For older versions, use `CONVERT alpha TO numeric` instead.
- If the string contains no valid number at the start, the result is 0.
- The alternative `CONVERT str$ TO num` statement achieves the same result but requires that the entire string be a valid number.

## See Also

- `CONVERT` — convert between string and numeric representations
- `STR(` — string manipulation function
