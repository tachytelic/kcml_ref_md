# LET (assignment)

> Assigns the result of an expression to one or more variables. The `LET` keyword itself is **not permitted** in KCML — assignments are bare `variable = expression`.

## Syntax

### String assignment
```
string_var [, string_var ...] = string_expression
REDIM string_var = string_expression
```

### Numeric assignment
```
num_var [, num_var ...] = numeric_expression
```

### Field variable initialization
```
.field$ = ( start, length )
.field  = ( start, "pack_image" )
```

## Description

The assignment statement evaluates the right-hand side and assigns the result to all variables on the left.

### String assignment rules

- Strings are **fixed-length and space-padded** — if the result is shorter than the receiver, the remainder is padded with spaces.
- If the result is longer than the receiver, it is **truncated** at the receiver's length.
- Multiple receivers separated by commas all receive the same value.

```kcml
Two$, Reply$ = First$ & Second$ & STR(Third$, 1, 2)
```

### REDIM assignment

`REDIM var = expr` resizes `var` to match the length of the expression (trailing blanks stripped):

```kcml
REDIM result$ = STR(buffer$, 1, LEN(buffer$))
```

Useful with `LOCAL DIM` variables in subroutines when the argument size is unknown. Note: there is a performance overhead; fixed-size strings up to 200 bytes are faster.

### Numeric assignment and operator precedence

| Priority | Operators |
|----------|-----------|
| Highest | `^` (exponentiation) |
| | `-` (unary negation) |
| | `*`, `/` |
| Lowest | `+`, `-` |

```kcml
v1 = v2 + v3 / v4      REM divides v3/v4 first, then adds v2
v1 = (v2 + v3) / v4    REM adds first, then divides
```

Multiple numeric assignment:
```kcml
One, Two, Three = SIN(Abc) + cir * #PI
```

### Field variable initialization

```kcml
.Description$ = (2, 5)             REM string field: start=2, length=5
.Department$  = (7, 14 + Length)   REM dynamic length
.Value        = (Start, "-#.##")   REM numeric field with pack image
```

Field variables must start with `.`. After definition, use `FLD(var.field$)` to access the field.

## Examples

```kcml
: DIM One, Two$20, Reply$20, First$10, Second$10
: One = 123 * 45
: PRINT "One="; One
: First$ = "Hello"
: Second$ = " World"
: Two$, Reply$ = First$ & Second$
: PRINT Two$
: PRINT Reply$
: .Name$ = (1, 10)
: PRINT "Field start=1 len=10"
: $END
```

Output:
```
One= 5535
Hello World
Hello World
Field start=1 len=10
```

## Notes

- `LET variable = value` is **not valid** — KCML does not accept the `LET` keyword.
- All variables on the left side of a multi-assignment must be the same type (all string or all numeric).
- String result is truncated if longer than receiver, padded with spaces if shorter.
- `REDIM` avoids oversizing `LOCAL DIM` strings but has a performance cost.

## See Also

- `DIM` — declare variables
- `REDIM` — resize a variable
- `FLD(` — access a field within a string variable
- `STR(` — substring of a string variable
