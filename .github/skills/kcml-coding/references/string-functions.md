# KCML String Functions

## Embedding Double Quotes in Strings

Two consecutive double quotes inside a string literal produce a single literal `"` character:

```kcml
: PRINT "The double quote "" character!"
```
Output: `The double quote " character!`

This works in any string context — assignment, PRINT, IF comparisons:

```kcml
: IF abc$ == """" THEN ...       : REM tests if abc$ equals one double-quote
: STR(zyx$, 99, 2) = """"""     : REM assigns two double-quotes at position 99
```

### Embedding quotes in JSON or XML output

Two approaches — pick based on readability:

**Option 1: doubled quotes** (good for short/occasional quotes)
```kcml
: PRINT "  ""order_number"": """; RTRIM(STR(rec$, 18, 6)); ""","
```

**Option 2: `q$` variable holding `HEX(22)`** (better when quotes are dense)
```kcml
: DIM q$1
: q$ = HEX(22)
: PRINT "  "; q$; "order_number"; q$; ": "; q$; RTRIM(STR(rec$, 18, 6)); q$; ","
```

Both produce: `  "order_number": "016519",`

`HEX(22)` is the historic workaround predating the `""` documentation — both are valid KCML.

---

## Substring: STR()

Extract or modify part of a string. **This is the primary substring function in KCML.**

```kcml
STR(string$, start, length)
```

- `start` - 1-based position (default: 1)
- `length` - number of characters (default: rest of string)

### Examples

```kcml
DIM a$20
: a$ = "Hello World"
: PRINT STR(a$, 1, 5)    : REM "Hello"
: PRINT STR(a$, 7, 5)    : REM "World"
: PRINT STR(a$, 7)       : REM "World     " (rest of string)
: $END
```

### Assignment (Left-side)

```kcml
DIM a$20
: a$ = "Hello World"
: STR(a$, 1, 5) = "KCML "
: PRINT a$               : REM "KCML  World"
: $END
```

## Length: LEN()

Returns the defined length of a string variable (not trimmed length).

```kcml
DIM a$20
: a$ = "Hello"
: PRINT LEN(a$)          : REM 20 (defined size)
: PRINT LEN(STR(a$))     : REM 20 (same)
: $END
```

## Find: POS()

Find position of substring. Returns 0 if not found.

```kcml
POS(haystack$ = needle$)
```

```kcml
DIM text$50, pos
: text$ = "The quick brown fox"
: pos = POS(text$ = "quick")
: PRINT "Found at: "; pos    : REM 5
: pos = POS(text$ = "slow")
: PRINT "Not found: "; pos   : REM 0
: $END
```

## Case Conversion

```kcml
DIM a$20
: a$ = "Hello World"
: PRINT $UPPER(a$)       : REM "HELLO WORLD"
: PRINT $LOWER(a$)       : REM "hello world"
: $END
```

## String to Number: VAL()

```kcml
DIM num
: num = VAL("123.45")
: PRINT num              : REM 123.45
: $END
```

## Number to String: STR$()

```kcml
DIM s$20, num
: num = 123.45
: s$ = STR$(num)
: PRINT "Value: "; s$
: $END
```

## Fill String: ALL()

Create a string filled with a repeated character.

```kcml
DIM a$20
: a$ = ALL("*")
: PRINT a$               : REM "********************"
: $END
```

## Hexadecimal: HEX()

Create string from hex values.

```kcml
DIM esc$1, crlf$2
: esc$ = HEX(1B)         : REM Escape character
: crlf$ = HEX(0D0A)      : REM CR+LF
: $END
```

## Concatenation

Use `&` to join strings:

```kcml
DIM a$10, b$10, c$25
: a$ = "Hello"
: b$ = "World"
: c$ = a$ & " " & b$
: PRINT c$               : REM "Hello World"
: $END
```

## Trimming

KCML strings are fixed-length and padded with spaces. To work with trimmed strings:

```kcml
DIM a$20, trimmed$20, i
: a$ = "Hello     "  
: REM Find last non-space
: FOR i = LEN(a$) TO 1 STEP -1
:    IF STR(a$,i,1) <> " " THEN BREAK
: NEXT i
: trimmed$ = STR(a$, 1, i)
: PRINT "Trimmed length: "; i
: $END
```

## FLD() Function

Alternative to STR() that can be faster and more readable when working with record structures:

```kcml
FLD(string$, start, length)
```

Functionally equivalent to STR() but optimized for field access.
