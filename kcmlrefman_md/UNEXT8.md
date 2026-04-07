# UNEXT8(

> Returns the byte index of the next Unicode character in a UTF-8 string.

## Syntax

```
UNEXT8(strexpr, byte_index)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `strexpr` | UTF-8 encoded string |
| `byte_index` | 1-based byte index of the **first byte** of the current character |

## Description

Returns the byte index of the first byte of the **next** character after the character at `byte_index`. Useful for iterating through UTF-8 strings character by character.

- Returns `0` if called for the last character.
- Returns `-1` if `byte_index` is out of range (< 1 or > string byte length).

The string must be valid UTF-8. Calling with an index pointing to a continuation byte (2nd or 3rd byte of a multibyte sequence) gives undefined results.

## Examples

```kcml
REM "$€£" = HEX(24 E282AC C2A3) — byte positions: $ at 1, € at 2, £ at 5
DIM a$7
a$ = HEX(24E282ACC2A3)
PRINT UNEXT8(a$, 1)   : REM  2  (€ starts at byte 2)
PRINT UNEXT8(a$, 2)   : REM  5  (£ starts at byte 5)
PRINT UNEXT8(a$, 5)   : REM  0  (£ is the last character)
```

```kcml
REM Iterate UTF-8 string
DIM pos
pos = 1
WHILE pos > 0 DO
  REM process character at pos
  pos = UNEXT8(a$, pos)
WEND
```

## See Also

- `UPREV8(` — previous character byte position
- `ULEN8(` — Unicode character count
- `TutorialUnicode` — UTF-8 in KCML
