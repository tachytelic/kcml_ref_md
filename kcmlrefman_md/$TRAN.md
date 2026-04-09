# $TRAN(

> Performs character-by-character translation on a string — modifies the variable in place.

## Syntax

```
$TRAN(alpha_variable, translation_table [, HEX(hh)]) [R]
```

## Description

`$TRAN(` translates characters in `alpha_variable` using a translation table, **modifying the variable in place** (no assignment needed).

There are two modes controlled by the `R` suffix:

### R mode (find/replace pairs)

When `R` is specified, the translation table is a sequence of character pairs: the **first character** of each pair is the replacement, the **second** is the character to find.

```
$TRAN(s$, "LlUuOo")R
```
This replaces `l` → `L`, `u` → `U`, `o` → `O`.

### Table mode (no R — positional lookup)

Without `R`, each character's binary value + 1 is used as an index into the translation table. The character is replaced with the table character at that position. Characters whose binary value exceeds the table length are left unchanged. Useful for ASCII ↔ EBCDIC conversions.

### HEX mask

If `HEX(hh)` is specified, each character of the variable is AND-masked with `hh` before the translation lookup. Useful for stripping high bits.

## Examples

### Example 1 — Replace specific characters (R mode)
```kcml
01000 REM Replace lowercase l with uppercase L
: DIM s$50
: s$ = "Hello World"
: $TRAN(s$,"LlO0")R
: PRINT "After TRAN: " ; RTRIM(s$)
: $END
```
**Output:**
```
After TRAN: HeLLo WorLd
```
> The table `"LlO0"` means: replace `l` with `L`, replace `0` (digit zero) with `O`. Lowercase `o` is NOT replaced (it's a different character from digit `0`).

### Example 2 — Replace vowels with asterisks
```kcml
01000 REM Mask vowels in a string
: DIM s$50
: s$ = "Hello World"
: $TRAN(s$,"*a*e*i*o*u")R
: PRINT "Vowels replaced: " ; RTRIM(s$)
: $END
```
**Output:**
```
Vowels replaced: H*ll* W*rld
```

### Example 3 — Replace spaces with underscores
```kcml
01000 REM Convert spaces to underscores for a filename
: DIM s$30
: s$ = "Hello World Test"
: $TRAN(s$,"_ ")R
: PRINT "With underscores: " ; RTRIM(s$)
: $END
```
**Output:**
```
With underscores: Hello_World_Test
```
> Note: because strings are fixed-length and space-padded, trailing spaces also become underscores. Use `RTRIM(` before `$TRAN` if you only want to affect content characters.

## Notes

- `$TRAN(` modifies the variable **in place** — there is no return value. You do not write `result$ = $TRAN(...)`.
- In R mode the table can contain any number of pairs. Characters not found in the "from" positions are left unchanged.
- `$TRAN(` is particularly useful for: ASCII ↔ EBCDIC conversion, stripping control characters, bulk character substitution.
- Since strings are space-padded to their declared size, `$TRAN` with `R` mode will also translate trailing spaces if space is in the "from" set.

## See also

[$UPPER(]($UPPER.md), [$LOWER(]($LOWER.md)
