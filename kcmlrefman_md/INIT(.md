# INIT(

> Fills one or more alpha variables with a repeated single character.

## Syntax

```
INIT( hex_literal | alpha_expression ) varlist
```

Where `varlist` is one or more alpha variables or arrays, separated by commas.

## Description

`INIT(` fills all bytes of each variable in `varlist` with the character specified in the argument. Only the **first character** of the argument is used — any additional characters are ignored.

`ALL(` is generally preferred over `INIT(` for the same purpose, as `ALL(` can be used in an alpha assignment expression. `INIT(` cannot appear on the right side of an assignment.

## Examples

```kcml
: DIM key$20
: INIT(HEX(2D)) key$
: PRINT "key$="; STR(key$, 1, 5)    REM prints -----
: $END
```

Output:
```
key$=-----
```

Fill multiple variables:

```kcml
INIT(HEX(FF)) place$(), record$
INIT(STR(as$, 1, 1)) fred$, area$()
```

## Notes

- Only the first character of the argument is used; the rest is ignored.
- `INIT(` modifies variables in-place — it cannot appear in an expression or on the right side of `=`.
- **Prefer `ALL(`**: `key$ = ALL(HEX(2D))` is equivalent and more flexible.
- Can be used with string arrays (`arr$()`) to fill every element.

## See Also

- `ALL(` — fill a string with a repeated byte (expression form, preferred)
- `ZER` — fill a numeric array with zeros
- `HEX(` — hex byte literal
