# ULEN8(

> Returns the number of Unicode characters in a UTF-8 encoded string.

## Syntax

```
ULEN8(strexpr)
```

## Description

Counts the number of **Unicode characters** (code points) in a UTF-8 encoded string, ignoring trailing spaces (unless the string is wrapped in `STR(`).

Unlike `LEN(` which counts bytes and returns minimum 1, `ULEN8(` returns 0 for a string of only spaces.

The string must be valid UTF-8. The `HEX(FE)` and `HEX(FF)` bytes cannot appear in a UTF-8 string.

## Examples

```kcml
REM ASCII-only string (each char is 1 byte)
DIM s$5
s$ = "Hello"
PRINT ULEN8(s$)     : REM  5
```

```kcml
REM UTF-8 multibyte characters
REM "$€£" = HEX(24 E282AC C2A3)  — 3 Unicode chars, 7 UTF-8 bytes
DIM a$7
a$ = HEX(24E282ACC2A3)
PRINT ULEN8(a$)     : REM  3
PRINT LEN(a$)       : REM  7 (byte count)
```

## Notes

- Use `ULEN8(` for character-count operations on multilingual text.
- Use `LEN(` for byte-count operations (e.g. buffer sizes).
- See `TutorialUnicode` for the UTF-8 encoding scheme.

## See Also

- `LEN(` — byte length of string
- `UNEXT8(` — next character byte position in UTF-8
- `UPREV8(` — previous character byte position in UTF-8
- `TutorialUnicode` — Unicode and UTF-8 in KCML
