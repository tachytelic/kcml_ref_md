# STR(

> Extracts or references a substring of an alpha variable. Can be used on both sides of an assignment.

## Syntax

```
STR(alpha_expr)                    (entire string)
STR(alpha_expr, start)             (from start to end)
STR(alpha_expr, start, length)     (substring)
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| `alpha_expr` | Source string variable or expression |
| `start` | 1-based start position (default: 1) |
| `length` | Number of bytes (default: rest of string including trailing spaces) |

## Description

`STR(` defines a substring reference. It is valid:
- **As an r-value** (right of `=`): extracts bytes from the source.
- **As an l-value** (left of `=`): writes bytes into the source at the specified position. If the value assigned is shorter than `length`, the remainder is space-padded.

`LEN(STR(var$))` returns the **declared length** of `var$` (its total allocated size).

`FLD(` is preferred over `STR(` for named field access — it is more readable and often faster.

## Examples

```kcml
DIM name$30, part$10
name$ = "John Smith          "
PRINT STR(name$, 1, 4)      : REM  John
PRINT STR(name$, 6)         : REM  Smith         (to end, includes spaces)
PRINT LEN(STR(name$))       : REM  30  (declared length)
```

```kcml
REM Assignment into a substring (l-value)
STR(area$,, 1) = HEX(02)      : REM  set first byte
STR(temp$, 2) = ALL(HEX(FF))  : REM  fill from byte 2 to end with HEX(FF)
STR(test$, count, 10) = STR(object$, count, 10)  : REM  copy 10 bytes
```

```kcml
REM Conditional check of a byte
IF STR(average$,, 1) == HEX(FF) THEN PRINT "Flag set"
```

```kcml
REM Find declared string length
DIM buf$512
PRINT LEN(STR(buf$))    : REM  512
```

## Notes

- **Trailing spaces are included** when `length` is omitted — `STR(var$, 5)` goes to the end including all padding.
- `STR(var$, 1, LEN(var$))` gives the content without trailing spaces.
- `FLD(` is equivalent but more readable for named record fields.

## See Also

- `FLD(` — field reference (preferred for named fields)
- `LEN(` — content length (excludes trailing spaces)
- `POS(` — find character position
