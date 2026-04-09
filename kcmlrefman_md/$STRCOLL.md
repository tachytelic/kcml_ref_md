# $STRCOLL(

> Compares two strings using a locale-aware collating sequence.

## Syntax

```
numeric_receiver = $STRCOLL(alpha_expression1, alpha_expression2)
```

## Description

`$STRCOLL(` compares two strings and returns:

| Result | Meaning |
|--------|---------|
| `-1` | First string is less than second |
| `0` | Strings are equal |
| `1` | First string is greater than second |

The difference from a plain `==` or `<` comparison is that `$STRCOLL(` uses a **locale collating sequence**, which handles language-specific sort ordering (e.g. accented characters in European languages sort correctly relative to unaccented ones).

The active collating sequence is determined by byte 50 of `$OPTIONS RUN`:
- `HEX(00)` — US ASCII (default)
- `HEX(01)` — ISO Latin-1 (Western European)
- `HEX(02)` — User-defined

KCML has built-in collating sequences for US ASCII and ISO Latin-1.

## Examples

### Example 1 — Basic alphabetic comparison
```kcml
01000 REM Compare strings alphabetically
: DIM r
: r = $STRCOLL("apple","banana")
: PRINT "apple vs banana: " ; r
: r = $STRCOLL("banana","apple")
: PRINT "banana vs apple: " ; r
: r = $STRCOLL("same","same")
: PRINT "same vs same: " ; r
: $END
```
**Output:**
```
apple vs banana: -1 
banana vs apple:  1 
same vs same:  0 
```

### Example 2 — Case sensitivity
```kcml
01000 REM Case matters in default ASCII collation
: DIM r
: r = $STRCOLL("ABC","abc")
: PRINT "ABC vs abc: " ; r
: r = $STRCOLL("abc","ABC")
: PRINT "abc vs ABC: " ; r
: $END
```
**Output:**
```
ABC vs abc: -1 
abc vs ABC:  1 
```
> In ASCII collation, uppercase letters have lower code points than lowercase, so "ABC" sorts before "abc".

### Example 3 — Use in a sort decision
```kcml
01000 REM Use $STRCOLL to determine sort order
: DIM a$20, b$20, r
: a$ = "Smith"
: b$ = "Jones"
: r = $STRCOLL(a$, b$)
: IF r < 0 THEN PRINT RTRIM(a$) ; " sorts before " ; RTRIM(b$)
: IF r > 0 THEN PRINT RTRIM(b$) ; " sorts before " ; RTRIM(a$)
: IF r == 0 THEN PRINT "Equal"
: $END
```
**Output:**
```
Jones sorts before Smith
```

## Notes

- For plain byte-by-byte comparison, use `==`, `<`, `>` operators directly — they are faster.
- `$STRCOLL(` is most useful when sorting strings that contain accented or non-ASCII characters where locale ordering matters.
- On Unicode KCML systems, full Unicode collation is used automatically.

## See also

[$STRCOL(]($STRCOL.md)
