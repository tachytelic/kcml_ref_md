# KCML Operators Reference

Complete reference for all operators available in KCML.

## Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `result = a + b` |
| `-` | Subtraction | `result = a - b` |
| `*` | Multiplication | `result = a * b` |
| `/` | Division | `result = a / b` |
| `^` | Power/Exponent | `result = 2 ^ 3` (= 8) |

### Example

```kcml
DIM a, b, result
: a = 10
: b = 3
: PRINT "Add: "; a + b           : REM 13
: PRINT "Sub: "; a - b           : REM 7
: PRINT "Mul: "; a * b           : REM 30
: PRINT "Div: "; a / b           : REM 3.333...
: PRINT "Pow: "; 2 ^ 8           : REM 256
: $END
```

## Comparison Operators

| Operator | Description |
|----------|-------------|
| `=` or `==` | Equal to |
| `<>` or `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

### Numeric Comparisons

```kcml
DIM x = 10
: IF (x == 10) THEN PRINT "Equals 10"
: IF (x <> 5) THEN PRINT "Not 5"
: IF (x > 5) THEN PRINT "Greater than 5"
: IF (x <= 10) THEN PRINT "At most 10"
: $END
```

### String Comparisons

String comparisons are performed byte-by-byte from left to right based on ASCII values:

```kcml
DIM a$10, b$10
: a$ = "Apple"
: b$ = "Banana"
: IF (a$ < b$) THEN PRINT "Apple comes before Banana"
: IF ("B" > "A") THEN PRINT "B > A (66 > 65)"
: $END
```

## Logical Operators (in Conditions)

| Operator | Description |
|----------|-------------|
| `AND` | Both conditions must be true |
| `OR` | Either condition must be true |
| `XOR` | Exactly one condition must be true |
| `NOT` | Negates a condition |

### Short-Circuit Evaluation

- `AND`: If first condition is false, second is not evaluated
- `OR`: If first condition is true, second is not evaluated
- `XOR`: Both conditions are always evaluated

```kcml
DIM x = 5, y = 10
: IF (x > 0 AND y > 0) THEN PRINT "Both positive"
: IF (x > 100 OR y > 5) THEN PRINT "At least one true"
: IF (x > 3 XOR y > 20) THEN PRINT "Exactly one true"
: IF (NOT x == 0) THEN PRINT "x is not zero"
: $END
```

### Grouping with Parentheses

```kcml
DIM a = 1, b = 1, c = 0, d = 0
: IF ((a == 1 AND b == 1) OR (c == 1 AND d == 1)) THEN
:    PRINT "First pair or second pair both equal 1"
: ENDIF
: $END
```

## String Bitwise Operators

In string expressions, AND/OR/XOR perform character-by-character bitwise operations:

| Operator | Description |
|----------|-------------|
| `AND` | Bitwise AND on each byte |
| `OR` | Bitwise OR on each byte |
| `XOR` | Bitwise XOR on each byte |

### Masking with AND

```kcml
DIM test$10
: test$ = "Hello"
: test$ = AND HEX(DF)          : REM Convert to uppercase
: PRINT test$                   : REM "HELLO"
: $END
```

### Setting Bits with OR

```kcml
DIM flags$1
: flags$ = HEX(00)
: flags$ = OR HEX(01)          : REM Set bit 0
: flags$ = OR HEX(04)          : REM Set bit 2
: PRINT ASC(flags$)            : REM 5 (binary 00000101)
: $END
```

## String Concatenation

The `&` operator joins strings:

```kcml
DIM first$20, last$20, full$50
: first$ = "John"
: last$ = "Smith"
: full$ = first$ & " " & last$
: PRINT full$                   : REM "John Smith"
: $END
```

### Shorthand Concatenation

```kcml
DIM result$50
: result$ = "Hello"
: result$ = & " World"         : REM Append to result$
: PRINT result$                 : REM "Hello World"
: $END
```

## Shorthand Operators

C-style compound assignment operators for concise code:

| Operator | Equivalent |
|----------|------------|
| `+=` | `x = x + n` |
| `-=` | `x = x - n` |
| `*=` | `x = x * n` |
| `/=` | `x = x / n` |
| `++` | `x = x + 1` |
| `--` | `x = x - 1` |

### Compound Assignment

```kcml
DIM total = 100
: total += 50                   : REM Now 150
: total -= 25                   : REM Now 125
: total *= 2                    : REM Now 250
: total /= 5                    : REM Now 50
: PRINT total
: $END
```

### Increment/Decrement

```kcml
DIM count = 0
: count++                       : REM Now 1
: count++                       : REM Now 2
: PRINT count                   : REM 2
: count--                       : REM Now 1
: PRINT count                   : REM 1
: $END
```

### Prefix vs Postfix

- **Prefix** (`++x`): Increment first, then use value
- **Postfix** (`x++`): Use value first, then increment

```kcml
DIM x = 5, a, b
: a = x++                       : REM a=5, x becomes 6
: PRINT "a="; a; " x="; x
: b = ++x                       : REM x becomes 7, b=7
: PRINT "b="; b; " x="; x
: $END
```

### In Loops

```kcml
DIM i = 0
: WHILE i < 5 DO
:    PRINT i++                  : REM Prints 0,1,2,3,4
: WEND
: $END
```

## Ternary Operator

The ternary operator allows inline IF-THEN-ELSE:

```
(condition ? value_if_true : value_if_false)
```

### Basic Usage

```kcml
DIM x = 10, result
: result = (x > 5 ? 100 : 0)
: PRINT result                  : REM 100
: $END
```

### In Expressions

```kcml
DIM score = 75, grade$10
: grade$ = (score >= 70 ? "Pass" : "Fail")
: PRINT grade$                  : REM "Pass"
: $END
```

### Nested Ternary

```kcml
DIM score = 85, grade$2
: grade$ = (score >= 90 ? "A" : (score >= 80 ? "B" : (score >= 70 ? "C" : "F")))
: PRINT grade$                  : REM "B"
: $END
```

### In PRINT Statements

```kcml
DIM balance = -50
: PRINT "Status: "; (balance < 0 ? "Overdrawn" : "OK")
: $END
```

## MOD Function

Returns the remainder after division:

```kcml
DIM a, b
: a = 17
: b = 5
: PRINT MOD(a, b)               : REM 2 (17 = 5*3 + 2)
: PRINT MOD(10, 3)              : REM 1
: PRINT MOD(20, 4)              : REM 0 (evenly divisible)
: $END
```

### Common Uses

```kcml
DIM i
: FOR i = 1 TO 10
:    IF MOD(i, 2) = 0 THEN PRINT i; " is even"
: NEXT i
: $END
```

## Operator Precedence

From highest to lowest:

1. `^` (exponentiation)
2. `*`, `/` (multiplication, division)
3. `+`, `-` (addition, subtraction)
4. `<`, `>`, `<=`, `>=`, `=`, `<>` (comparison)
5. `NOT`
6. `AND`
7. `OR`, `XOR`

Use parentheses to override precedence:

```kcml
DIM result
: result = 2 + 3 * 4            : REM 14 (not 20)
: result = (2 + 3) * 4          : REM 20
: PRINT result
: $END
```

## See Also

- [Control Flow](control-flow.md) - Using operators in conditions
- [String Functions](string-functions.md) - String manipulation
- [Numeric Functions](numeric-functions.md) - Math functions
