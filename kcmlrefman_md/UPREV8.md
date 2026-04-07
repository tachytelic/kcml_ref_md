# UPREV8(

> Returns the byte index of the previous Unicode character in a UTF-8 string.

## Syntax

```
UPREV8(strexpr, byte_index)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `strexpr` | UTF-8 encoded string |
| `byte_index` | 1-based byte index of the **first byte** of the current character |

## Description

Returns the byte index of the first byte of the **previous** character before the character at `byte_index`. Useful for iterating through UTF-8 strings in reverse.

- Returns `0` if called for the first character.
- Returns `-1` if `byte_index` is out of range.

## Examples

```kcml
REM "$€£" = HEX(24 E282AC C2A3) — byte positions: $ at 1, € at 2, £ at 5
DIM a$7
a$ = HEX(24E282ACC2A3)
PRINT UPREV8(a$, 5)   : REM  2  (€ is before £ at byte 2)
PRINT UPREV8(a$, 2)   : REM  1  ($ is before € at byte 1)
PRINT UPREV8(a$, 1)   : REM  0  ($ is the first character)
```

```kcml
REM Iterate UTF-8 string in reverse
DIM s$, pos, len_bytes
len_bytes = LEN(STR(s$))
pos = UPREV8(s$, len_bytes + 1)   : REM  start from last character
WHILE pos > 0 DO
  REM process character at pos
  pos = UPREV8(s$, pos)
WEND
```

## See Also

- `UNEXT8(` — next character byte position
- `ULEN8(` — Unicode character count
- `TutorialUnicode` — UTF-8 in KCML
