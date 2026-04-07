# & (Concatenation operator)

> Joins two string values end-to-end (without intervening characters) and assigns the result to the receiver.

## Syntax

```
alpha_receiver = [alpha_operand] & alpha_operand [& ...]
alpha_receiver = & alpha_operand
```

| Form | Effect |
|------|--------|
| `a$ = b$ & c$` | Concatenate `b$` and `c$`, store in `a$` |
| `a$ = & b$` | Append `b$` to `a$` (shorthand; `a$` is both receiver and first operand) |

## Description

The `&` operator concatenates two alpha strings. Trailing spaces are trimmed from each operand before concatenation — so `"Hello   " & "World"` produces `"Hello World"`.

**Special case:** If a variable contains only spaces, exactly one space is retained. For example, if `sample1$` is all spaces, then `sample1$ = sample1$ & "A"` sets `sample1$` to `" A"`.

Multiple `&` operators can be chained in one statement. They can also be mixed with other alpha operators like `AND` in the same expression.

`&` is valid only in the alpha (string) expression portion of an assignment statement.

## Examples

### Basic concatenation

```kcml
: DIM a$20, b$20, c$40
: a$ = "Hello"
: b$ = "World"
: c$ = a$ & " " & b$
: PRINT c$
: $END
```

Output: `Hello World`

### Shorthand append

```kcml
: DIM a$20
: a$ = "Hello"
: a$ = & "!"
: PRINT a$
: $END
```

Output: `Hello!`

### Mixed with AND operator

```kcml
map$ = page$ & chapter$(1) AND HEX(4F)
```

### Concatenation in subroutine argument

```kcml
'update(prefix$ & suffix$)
```

### Return concatenated value from DEFSUB

```kcml
DEFSUB 'tagit(tag$)
    RETURN = "<" & tag$ & ">"
END SUB
```

## Notes

- Trailing spaces are trimmed from each operand before joining. To preserve trailing spaces, pad explicitly or use `STR(` with a fixed range.
- The `=&` shorthand (`a$ = & b$`) is equivalent to `a$ = a$ & b$` but cannot be used with multiple receiver variables on the left.

## See Also

- `STR(` — extract a substring by position and length
- `AND`, `OR` — bitwise string operators that can be mixed with `&`
- `PRINT` — multiple values in a PRINT statement are effectively concatenated for display
