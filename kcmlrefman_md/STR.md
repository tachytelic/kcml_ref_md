# STR(

> Extracts or targets a substring within an alpha variable.

## Syntax

```
STR(alpha_expression [, [start] [, length]])
```

| Parameter | Description |
|-----------|-------------|
| `alpha_expression` | The string to operate on |
| `start` | Starting byte position (1-based). Defaults to 1 |
| `length` | Number of bytes to extract. Defaults to remainder of string including trailing spaces |

## Description

`STR(` defines a substring of an alpha expression. It is valid **on either side of an assignment**:

- **Right side** — extracts a substring: `sub$ = STR(s$, 3, 5)`
- **Left side** — overwrites a portion of a string in place: `STR(s$, 3, 5) = "XXXXX"`

When `STR(` is used on the left side and the replacement value is shorter than the specified length, the remainder of the substring is padded with trailing spaces.

**Getting the declared size:** `LEN(STR(var$))` (with no start/length) returns the total declared allocation of `var$`, not its content length.

`FLD(` is the preferred alternative when working with structured records — it is more readable and typically faster.

## Examples

### Example 1 — Extracting substrings
```kcml
01000 REM Extract parts of a string by position
: DIM s$20, sub$10
: s$ = "Hello World"
: sub$ = STR(s$, 7, 5)
: PRINT "STR(s$,7,5): " ; RTRIM(sub$)
: sub$ = STR(s$, 1, 5)
: PRINT "STR(s$,1,5): " ; RTRIM(sub$)
: $END
```
**Output:**
```
STR(s$,7,5): World
STR(s$,1,5): Hello
```

### Example 2 — Overwriting part of a string (left-side assignment)
```kcml
01000 REM Modify a substring in place
: DIM t$20
: t$ = "AAAAAAAAAA"
: STR(t$,3,3) = "BBB"
: PRINT "After STR assign: " ; RTRIM(t$)
: REM Overwrite first byte with a control byte
: STR(t$,,1) = HEX(02)
: PRINT "First byte set to HEX(02)"
: $END
```
**Output:**
```
After STR assign: AABBBAAAAA
First byte set to HEX(02)
```

### Example 3 — Get declared size with LEN(STR())
```kcml
01000 REM Get declared size vs content length
: DIM name$50
: name$ = "Smith"
: PRINT "Content LEN: " ; LEN(name$)
: PRINT "Declared size: " ; LEN(STR(name$))
: REM Fill entire allocated space with a byte
: STR(name$) = ALL(HEX(FF))
: PRINT "All FF: declared size = " ; LEN(STR(name$))
: $END
```
**Output:**
```
Content LEN:  5 
Declared size:  50 
All FF: declared size =  50 
```

## Notes

- `STR(` is 1-based — position 1 is the first byte.
- Omitting `start` defaults to position 1. Omitting `length` takes the rest of the string **including trailing spaces**.
- When using `STR(` on the left side, if the replacement is shorter than `length`, the gap is space-padded.
- Consider `FLD(` instead of `STR(` for named record fields — same semantics but readable and faster.
- `STR(var$,,1)` is a common idiom for reading/writing a single byte at position 1.

## See also

[LEN(](LEN.md), [FLD(](FLD.md), [ALL(](ALL.md), [HEXUNPACK](HEXUNPACK.md)
