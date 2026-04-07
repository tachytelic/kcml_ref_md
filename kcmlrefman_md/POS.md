# POS(

> Returns the position of the first character in a string satisfying a relation, or the start position of a field variable.

## Syntax

```
POS(alpha_var relop char)
POS(-alpha_var relop char)
POS(.field_var)
```

## Description

**Form 1 — character search:** Scans `alpha_var` left-to-right and returns the 1-based position of the first character satisfying the relation (`=`, `<>`, `<`, `>`, `<=`, `>=`). If no character satisfies the relation, returns 0. Only the first character of the comparison string is used.

**Form 2 — reverse search:** A leading minus sign (`-`) causes the scan to go right-to-left, returning the position of the *last* character satisfying the relation.

**Form 3 — field position:** `POS(.field$)` returns the byte offset (1-based) of `field$` within its parent record string. Used with `FLD(` to locate fields at runtime.

## Examples

```kcml
DIM test$26
test$ = "HELLO WORLD"
PRINT POS(test$ = "O")       : REM  5  (first O)
PRINT POS(-test$ = "O")      : REM  8  (last O in "HELLO WORLD")
PRINT POS(test$ == " ")      : REM  6  (space)
PRINT POS(test$ > "M")       : REM  first char > M
```

Output:
```
 5
 8
 6
```

```kcml
DIM alpha$26
alpha$ = "abcdefghijklmnopqrstuvwxyz"
PRINT POS(alpha$ = "o")      : REM  15
PRINT POS(alpha$ > "t")      : REM  21  (u is first char > t)
PRINT POS(alpha$ = "z") + 1  : REM  27  (past end — can test for not found: 0)
```

```kcml
REM Field position form
DIM rec$100, name$30, age$3
name$ = FLD(rec$, 1, 30)
age$  = FLD(rec$, 31, 3)
PRINT POS(.name$)   : REM  1
PRINT POS(.age$)    : REM  31
```

## Notes

- Returns 0 if the relation is not satisfied by any character.
- Only the **first character** of the comparison operand is used even if a longer string is given.
- The minus-sign (reverse) form returns the position of the **last** matching character.
- `POS(.field$)` complements `LEN(.field$)` — together they give offset and length of any declared field.

## See Also

- `FLD(` — extract a substring field
- `LEN(` — length of a string or field
