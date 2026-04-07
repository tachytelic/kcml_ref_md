# ALL(

> Creates a string of repeated characters — every byte set to the specified value.

## Syntax

```
ALL( character [, length] )
```

Where `character` is one of:
- A single-character string literal: `ALL(" ")`, `ALL("-")`
- A hex literal: `ALL(HEX(20))`, `ALL(HEX(00))`
- An alpha variable (first character is used)

| Parameter | Description |
|-----------|-------------|
| `character` | The character to repeat. If more than one character is specified, only the first is used. |
| `length` | Optional numeric expression specifying the output length in bytes. If omitted, the length of the receiver variable is used. |

## Description

`ALL(` fills a string with a single repeated byte. It is valid only in:
- The alpha (string) portion of an assignment statement
- `PRINT` statements

If only one argument is given, the result fills the entire length of the receiver variable. If a `length` argument is given, exactly that many bytes are produced.

Common uses:
- Initialise arrays to spaces: `library$() = ALL(" ")`
- Fill with null bytes: `rec$ = ALL(HEX(00))`
- Draw separator lines: `line$ = ALL("-")`
- Bitwise operations on whole strings: `type$ = AND ALL(HEX(7F))`

## Examples

### Fill string with spaces (explicit hex)

```kcml
: DIM s$20
: s$ = ALL(HEX(20))
: PRINT "["; s$; "]"
: $END
```

Output:
```
[                    ]
```

### Fill with dashes (uses receiver length)

```kcml
: DIM t$10
: t$ = ALL("-")
: PRINT "["; t$; "]"
: $END
```

Output:
```
[----------]
```

### Fill with explicit length

```kcml
: DIM u$20
: u$ = ALL("X", 5)
: PRINT "["; u$; "]"
: $END
```

Output:
```
[XXXXX               ]
```
(5 X's; remaining 15 bytes of `u$` are unchanged/spaces)

### Initialise whole array to null

```kcml
DIM rec$(100)80
rec$() = ALL(HEX(00))
```

### Bitwise mask — strip high bit from every character

```kcml
: DIM s$4
: s$ = HEX(FF FF FF FF)
: s$ = AND ALL(HEX(7F))
: PRINT s$
: $END
```

## Notes

- `ALL(HEX(00))` is the standard way to null-fill a string. (See also CLAUDE.md: `ALL(HEX(00))` = null-filled string.)
- Only the **first character** of the argument is used; `ALL("AB")` is the same as `ALL("A")`.
- When used with `STR(` on the left side, the length comes from the `STR(` range.

## See Also

- `HEX(` — create a string from hex byte literals
- `AND`, `OR`, `XOR` — bitwise string operators that commonly use `ALL(` as the operand
- `STR(` — extract or assign substrings
