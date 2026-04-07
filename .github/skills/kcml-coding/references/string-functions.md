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

Find position of the **first matching character**. Returns 0 if not found.

```kcml
POS(haystack$ = needle$)
```

**CRITICAL: POS only matches a single character.** If `needle$` is more than one character, only the first character is used. POS is NOT a substring search.

```kcml
DIM text$26
: text$ = "abcdefghijklmnopqrstuvwxyz"
: PRINT POS(text$ = "o")    : REM 15  (finds 'o', ignores rest of needle)
: PRINT POS(text$ = "oxyz") : REM 15  (same result - only 'o' is used)
: $END
```

Search from the end using `-`:
```kcml
: PRINT POS(-text$ = "o")   : REM 15  (last 'o' — same here, only one 'o')
```

### Substring search — use MAT SEARCH

POS cannot do substring matching. Use `MAT SEARCH` instead.

---

## Substring Search: MAT SEARCH

Scans an alpha variable for substrings matching a relational operator. Returns byte position of first match into a numeric variable, or 0 if not found.

```kcml
MAT SEARCH search_var, operator search_string TO result [STEP step]
```

- `search_var` — plain alpha variable to search (no function calls — must be a variable)
- `operator` — `==`, `<>`, `<`, `<=`, `>`, `>=`
- `search_string` — use `STR(needle$,,len)` to fix exact length and avoid trailing-space mismatches
- `result` — numeric variable (position) or numeric array (all positions)
- `STEP` — optional: bytes to skip between comparisons (default 1); use for fixed-width field arrays

### Basic contains-check (verified working)

```kcml
DIM desc$30, needle$30, found, nl
: desc$ = "Trial print Invoice"
: needle$ = "print"
: nl = LEN(RTRIM(needle$))
: MAT SEARCH desc$, == STR(needle$,,nl) TO found
: PRINT found              : REM 7 — position of "print", or 0 if not found
: $END
```

### Case-insensitive search

`MAT SEARCH` is case-sensitive. Lower both strings before searching:

```kcml
DIM desc$30, needle$30, found, nl
: desc$ = STR(sp_rec$, 17, 30)
: desc$ = $LOWER(desc$)
: needle$ = $LOWER(user_input$)
: nl = LEN(RTRIM(needle$))
: MAT SEARCH desc$, == STR(needle$,,nl) TO found
: IF found == 0 THEN row_match = 0
: $END
```

### Find all occurrences (array result)

When `result` is a numeric array, MAT SEARCH fills it with all match positions; the last entry is 0:

```kcml
DIM text$100, hits(20), nl, needle$10
: text$ = "one cat and one dog and one fish"
: needle$ = "one"
: nl = LEN(RTRIM(needle$))
: MAT SEARCH text$, == STR(needle$,,nl) TO hits()
: FOR i = 1 TO 20
:   IF hits(i) == 0 THEN BREAK
:   PRINT "Found at: "; hits(i)
: NEXT i
: $END
```

### Searching fixed-width field arrays (STEP)

When records are packed into a single string at fixed offsets, STEP skips to the next field:

```kcml
REM Search 5 x 6-byte name fields packed into names$
DIM names$30, target$6, ptr$2
: names$ = "steve fred  alan  john  bill  "
: target$ = "alan"
: MAT SEARCH names$, == STR(target$,,6) TO ptr$ STEP 6
: PRINT VAL(ptr$, 2)       : REM 13 (byte position), or use ELEMENT for array index
: $END
```

### Key rules

- `search_var` must be a plain variable — assign `STR()` or `$LOWER()` results to a variable first, then pass that variable
- Always use `STR(needle$,,len)` not bare `needle$` — bare variable includes trailing spaces and will fail to match
- `LEN(RTRIM(needle$))` gives the correct length for fixed-length string variables

### WARNING: Never use STR() on the left side of POS()

`POS(STR(rec$, 17, 30) = "X")` looks like a character search but is actually **silent data corruption**. KCML parses `STR(rec$, 17, 30) = "X"` as a substring *assignment* (writing "X" into rec$ at position 17). Always assign to a local variable first:

```kcml
DIM desc$30
: desc$ = STR(rec$, 17, 30)
: IF POS(desc$ = ".") == 0 THEN ...   : REM safe
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

## Numeric to String: CONVERT

**`&` is type-strict** — concatenating a numeric with `&` causes a compile-time syntax error. Convert numeric to string first using `CONVERT`:

```kcml
CONVERT numeric_expr TO string$,(picture)
```

The `picture` format uses `#` for digit positions:

```kcml
DIM count, label$40, num_s$10
: count = 42
: CONVERT count TO num_s$,(####)    : REM " 42" (right-aligned, leading spaces)
: label$ = "Count " & LTRIM(num_s$) : REM "Count 42"
: $END
```

Common picture formats:
- `(##)` — 0 to 99
- `(####)` — 0 to 9999
- `(######)` — large integers
- `(###.##)` — decimal with 2 places
- `($###,###.##-)` — currency with sign

**Always use `LTRIM()` after CONVERT** — the picture pads with leading spaces to fill digit positions.

### CONVERT alpha to numeric

```kcml
DIM total, amount$10
: amount$ = "159.90"
: CONVERT amount$ TO total    : REM total = 159.9
: $END
```

Generates a recoverable error if the string is not a valid number.

---

## Concatenation

Use `&` to join strings (both operands must be strings — see CONVERT above for numeric):

```kcml
DIM a$10, b$10, c$25
: a$ = "Hello"
: b$ = "World"
: c$ = a$ & " " & b$
: PRINT c$               : REM "Hello World"
: $END
```

## Trimming

KCML strings are fixed-length and padded with spaces. Use the built-in trim functions:

```kcml
DIM a$20
: a$ = "  Hello  "
: PRINT RTRIM(a$)        : REM "  Hello"  (removes trailing spaces)
: PRINT LTRIM(a$)        : REM "Hello  "  (removes leading spaces)
: PRINT LTRIM(RTRIM(a$)) : REM "Hello"    (both ends)
: $END
```

Manual trimming when the built-ins are unavailable:

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
