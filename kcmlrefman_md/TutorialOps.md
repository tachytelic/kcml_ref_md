# KCML Operators

> Covers the full set of KCML operators: standard arithmetic and comparison operators, C-style shorthand assignment operators, increment/decrement operators, and ternary conditional expressions.

## Overview

As well as the standard operators found in most high-level languages, KCML provides shorthand assignment operators and ternary operators familiar to C programmers. These improve program readability and can also improve performance by reducing the number of variable references and intermediate assignments.

---

## Arithmetic and Comparison Operators

KCML supports the standard set of operators:

| Category | Operators |
|----------|-----------|
| Arithmetic | `+` `-` `*` `/` `^` (power) |
| Comparison (numeric) | `<` `>` `<=` `>=` `==` `<>` |
| Comparison (alpha) | `<` `>` `<=` `>=` `==` `<>` |
| Logical | `AND` `OR` `XOR` `NOT` |
| String concatenation | `&` |

**Note:** KCML uses `==` for equality testing (not `=`). A single `=` is always assignment.

---

## Shorthand Assignment Operators

The following compound assignment operators are all available:

| Operator | Equivalent to |
|----------|--------------|
| `x += expr` | `x = x + expr` |
| `x -= expr` | `x = x - expr` |
| `x *= expr` | `x = x * expr` |
| `x /= expr` | `x = x / expr` |
| `x++` | `x = x + 1` (post-increment) |
| `x--` | `x = x - 1` (post-decrement) |
| `++x` | `x = x + 1` (pre-increment) |
| `--x` | `x = x - 1` (pre-decrement) |

All of these operators may be used anywhere that a numeric expression is valid.

### Compound assignment example

```kcml
apple = 5
apple *= 5 + 1
PRINT apple
```

**Output:**
```
30
```

The operation and the assignment can also be combined into a single expression:

```kcml
apple = 5
PRINT apple *= 5 + 1
```

**Output:**
```
30
```

The expression `apple *= 5 + 1` performs the multiplication, stores the result in `apple`, and also returns the result value to the `PRINT` statement.

---

## Increment and Decrement Operators (`++` and `--`)

`++` increments a numeric variable by one; `--` decrements it. Both operators can appear as a **prefix** (before the variable) or a **postfix** (after the variable).

- **Postfix** — the variable is used first, then incremented or decremented:

```kcml
pear = apple++
orange = lemon--
```

This is equivalent to:

```kcml
pear = apple
apple = apple + 1
orange = lemon
lemon = lemon - 1
```

- **Prefix** — the variable is incremented or decremented first, then used:

```kcml
pear = ++apple
orange = --lemon
```

This is equivalent to:

```kcml
apple = apple + 1
pear = apple
lemon = lemon - 1
orange = lemon
```

### In loop conditions

Shorthand operators are particularly useful in loop termination conditions:

```kcml
DIM count
REPEAT
    PRINT count
UNTIL count++ == 10
```
<!-- UNTESTED -->

This counts from 0 to 10 (the post-increment means `count` is tested **before** being incremented, so the loop terminates when `count` reaches 10 and is then incremented to 11).

### With field variables

All shorthand operators can be used with numeric field variables, but **avoid prefix and postfix `++`/`--` on numeric fields in performance-sensitive loops**. Each use forces an unpack-change-repack cycle, which is significantly slower than a simple variable increment.

---

## Ternary Operator

The ternary operator allows `IF ... THEN ... ELSE` conditions to be embedded inline wherever a string or numeric expression is legal.

### Syntax

```
( condition ? true_value : false_value )
```

| Part | Description |
|------|-------------|
| `condition` | Any KCML boolean expression (numeric or alpha) |
| `?` | Separates the condition from the return values |
| `true_value` | Returned when condition is true |
| `:` | Separates the two return values |
| `false_value` | Returned when condition is false |

Parentheses are required around the entire ternary expression.

### Example — simple numeric ternary

```kcml
IF (abc < def) THEN result = 1000
ELSE result = 2000
```

can be written as:

```kcml
result = (abc < def ? 100 : 200) * 10
```

`result` is set to 1000 if `abc < def`, or 2000 otherwise.

### Example — ternary in a PRINT statement

```kcml
IF (total < 0) THEN disp$ = HEX(0E)
ELSE disp$ = HEX(0F)
PRINT "Total ="; disp$; total
```

can be rewritten as:

```kcml
PRINT "Total ="; (total < 0 ? HEX(0E) : HEX(0F)); total
```
<!-- UNTESTED -->

If `total` is negative, `HEX(0E)` switches the following output to bold text; otherwise `HEX(0F)` restores normal display.

### Nested ternary operators

Multiple ternary operators can be embedded within each other:

```kcml
ab = ((t1 = (s <> t ? jkl : 100) ? ps : 200) <> xr ? TRUE : FALSE)
```
<!-- UNTESTED -->

While this is syntactically valid, deeply nested ternaries reduce readability. Use `IF ... END IF` for complex branching.

---

## Operator Precedence

KCML follows standard operator precedence. Use parentheses to make order of evaluation explicit:

| Priority (high to low) | Operators |
|------------------------|-----------|
| 1 | Unary `-` `NOT` `++` `--` (prefix) |
| 2 | `^` (power) |
| 3 | `*` `/` |
| 4 | `+` `-` `&` |
| 5 | `<` `>` `<=` `>=` `==` `<>` |
| 6 | `AND` |
| 7 | `OR` `XOR` |

---

## Notes

- KCML uses `==` for equality tests, not `=`. Using `=` where `==` is intended is a common error that causes an assignment rather than a comparison.
- Shorthand operators (`+=`, `-=`, etc.) are equivalent to read-modify-write on the named variable and are slightly more efficient than writing `x = x + expr` explicitly.
- Prefix `++x` and postfix `x++` produce different results when embedded in expressions — match the behaviour you need carefully.
- Ternary expressions require parentheses; omitting them causes a syntax error or incorrect parsing.

## See Also

- `IF ... THEN` — standard conditional statement
- `IF ... END IF` — structured multi-line conditional
- `BOOL(` — convert numeric to TRUE/FALSE
- `AND`, `OR`, `NOT` — logical operators
- `FLD(` — field variable access (note `++`/`--` performance caveat)
