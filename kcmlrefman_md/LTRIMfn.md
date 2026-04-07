# LTRIM(

> Removes leading characters from the left side of a string. Removes spaces by default.

## Syntax

```
LTRIM( alpha_expression [, char$] )
```

| Argument | Description |
|----------|-------------|
| `alpha_expression` | The string to trim |
| `char$` | Optional: character to trim (default: space `HEX(20)`) |

Returns an alpha string. Valid wherever an alpha expression is legal.

## Description

`LTRIM(` strips all occurrences of the specified character from the left end of the string. Only the first character of `char$` is used. If omitted, spaces are trimmed.

## Examples

```kcml
: DIM a$20, b$20
: a$ = "   Hello"
: b$ = LTRIM(a$)
: PRINT "LTRIM="; b$; " len="; LEN(b$)

: a$ = "XXXHello"
: b$ = LTRIM(a$, "X")
: PRINT "LTRIM X="; b$; " len="; LEN(b$)
: $END
```

Output:
```
LTRIM=Hello len= 5
LTRIM X=Hello len= 5
```

With a specific byte:
```kcml
Size = WRITE #1, LTRIM(Buffer$, HEX(FF))
FLD(Record$.Result$) = LTRIM(Buffer$)
```

## Notes

- Only the **first character** of `char$` is used; extra characters are ignored.
- To trim from the right, use a similar pattern or the equivalent RTRIM function (if available).
- `LTRIM(` does not modify the original variable — it returns a new value.

## See Also

- `STR(` — substring extraction
- `LEN(` — content length
