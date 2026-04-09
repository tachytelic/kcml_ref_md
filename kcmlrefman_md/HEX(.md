# HEX(

> A literal that embeds arbitrary binary bytes into a string, specified as hexadecimal digit pairs.

## Syntax

```
HEX( hh [hh ...] )
```

Where each `hh` is exactly two hexadecimal digits (`0–9`, `A–F`). An odd number of digits causes a runtime error.

Valid wherever an alphanumeric literal is legal.

## Description

`HEX(` allows 8-bit (1-byte) characters — including non-printable control characters — to be embedded in KCML programs. Each pair of hex digits represents one byte.

This is the standard way to embed characters that cannot be typed from the keyboard, such as:
- Escape sequences for terminal control
- Null bytes, line feeds, carriage returns
- Quote characters (instead of `CHR$(34)`, use `HEX(22)`)

## Examples

```kcml
: PRINT "HEX(41)=["; HEX(41); "]"
: $END
```

Output:
```
HEX(41)=[A]
```

### Common uses

```kcml
PRINT HEX(03)              REM clear screen / home cursor
PRINT HEX(07)              REM terminal bell
output$ = HEX(22) & text$ & HEX(22)    REM wrap in double-quotes
IF (ch$ = HEX(0A))         REM test for line-feed character
```

### Multi-byte sequences

```kcml
PRINT HEX(0307)            REM clear screen (03) then bell (07) — two bytes
output$ = HEX(020402000F) & string$    REM five-byte escape sequence prefix
```

### Quote embedding

Two verified approaches for embedding a double-quote in a string:

```kcml
msg$ = "He said " & HEX(22) & "hello" & HEX(22)
REM produces: He said "hello"
```

```kcml
msg$ = "He said ""hello"""
REM produces: He said "hello"
```

`""` (two consecutive double-quotes) inside a string literal is interpreted as a single literal `"`. This is often more readable than `HEX(22)` when building structured text such as JSON. Verified by execution.

## Notes

- `HEX(22)` and `""` (double double-quote) are both valid ways to embed a double-quote character. **Do not use `CHR$(34)`** — that syntax is not valid in KCML.
- Exactly two hex digits per byte — `HEX(9)` is an error; use `HEX(09)`.
- `HEX(` is a **literal**, not a function — it cannot be called with a variable argument. To convert a variable's binary value to hex text, use `HEXUNPACK`.

## See Also

- `HEXUNPACK` — convert binary bytes to a hex digit string
- `HEXPACK` — convert a hex digit string to binary bytes
- `ALL(` — fill a string with a repeated byte
- `CHR$(` — not available in KCML; use `HEX(` instead
