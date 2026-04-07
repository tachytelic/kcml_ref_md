# KCML Numeric Functions and Operations Reference

Complete reference for numeric operations and mathematical functions in KCML.

## Basic Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `^` | Exponentiation | `a ^ b` |

### Examples

```kcml
DIM a, b, result
: a = 10 : b = 3
: result = a + b     : REM 13
: result = a - b     : REM 7
: result = a * b     : REM 30
: result = a / b     : REM 3.333...
: result = a ^ b     : REM 1000
```

## Shorthand Operators

| Operator | Equivalent | Description |
|----------|------------|-------------|
| `+=` | `a = a + b` | Add and assign |
| `-=` | `a = a - b` | Subtract and assign |
| `*=` | `a = a * b` | Multiply and assign |
| `/=` | `a = a / b` | Divide and assign |
| `++` | `a = a + 1` | Increment |
| `--` | `a = a - 1` | Decrement |

### Shorthand Examples

```kcml
DIM count
: count = 10
: count += 5        : REM count = 15
: count -= 3        : REM count = 12
: count *= 2        : REM count = 24
: count /= 4        : REM count = 6
: count++           : REM count = 7
: count--           : REM count = 6
```

### Prefix vs Postfix Increment

```kcml
DIM a, b
: a = 5
: b = a++    : REM b = 5, then a = 6 (postfix)

: a = 5
: b = ++a    : REM a = 6, then b = 6 (prefix)
```

## Integer Functions

### INT( - Integer Part (Truncate Down)

```kcml
INT(numeric_expression)
```

Returns the greatest integer less than or equal to the value:

```kcml
INT(3.7)     : REM  3
: INT(-3.7)  : REM -4 (truncates DOWN)
: INT(3.0)   : REM  3
```

### FIX( - Integer Part (Truncate Toward Zero)

```kcml
FIX(numeric_expression)
```

Truncates toward zero (differs from INT for negatives):

```kcml
FIX(3.7)     : REM  3
: FIX(-3.7)  : REM -3 (truncates toward zero)
: FIX(3.0)   : REM  3
```

### INT vs FIX Comparison

| Value | INT() | FIX() |
|-------|-------|-------|
| 3.7 | 3 | 3 |
| -3.7 | -4 | -3 |
| 3.0 | 3 | 3 |
| -3.0 | -3 | -3 |

## Absolute Value

### ABS( - Absolute Value

```kcml
ABS(numeric_expression)
```

Returns the positive magnitude:

```kcml
ABS(5)       : REM 5
: ABS(-5)    : REM 5
: ABS(-3.14) : REM 3.14
```

## Mathematical Functions

### LOG( - Natural Logarithm

```kcml
LOG(numeric_expression)
```

Returns the natural logarithm (base e):

```kcml
LOG(2.718281828)  : REM ~1.0
: LOG(10)         : REM ~2.3026
```

### LGT( - Base 10 Logarithm

```kcml
LGT(numeric_expression)
```

Returns the base-10 logarithm:

```kcml
LGT(10)      : REM 1.0
: LGT(100)   : REM 2.0
: LGT(1000)  : REM 3.0
```

### EXP( - Natural Exponential

```kcml
EXP(numeric_expression)
```

Returns e raised to the power:

```kcml
EXP(1)       : REM ~2.718 (e)
: EXP(0)     : REM 1.0
: EXP(2)     : REM ~7.389
```

### SQR( - Square Root

```kcml
SQR(numeric_expression)
```

Returns the square root:

```kcml
SQR(4)       : REM 2.0
: SQR(2)     : REM ~1.414
: SQR(100)   : REM 10.0
```

## Trigonometric Functions

### Basic Trig Functions

| Function | Description |
|----------|-------------|
| `SIN(x)` | Sine (x in radians) |
| `COS(x)` | Cosine (x in radians) |
| `TAN(x)` | Tangent (x in radians) |

### Inverse Trig Functions

| Function | Description |
|----------|-------------|
| `ARCSIN(x)` | Arc sine |
| `ARCCOS(x)` | Arc cosine |
| `ARCTAN(x)` | Arc tangent |

### Examples

```kcml
DIM angle, result
: angle = #PI / 4      : REM 45 degrees in radians
: result = SIN(angle)  : REM ~0.707
: result = COS(angle)  : REM ~0.707
: result = TAN(angle)  : REM ~1.0
```

### Converting Degrees to Radians

```kcml
DEFFN radians(degrees) = degrees * #PI / 180
DEFFN degrees(radians) = radians * 180 / #PI

: angle_rad = FN radians(45)   : REM Convert 45° to radians
: angle_deg = FN degrees(#PI)  : REM Convert π to degrees (180)
```

## Random Numbers

### RND( - Random Number

```kcml
RND(numeric_expression)
```

Generates random number between 0 and 1:

- `RND(0)` - Returns first value in sequence (for reproducible results)
- `RND(1)` - Returns next random number

### Examples

```kcml
REM Random number 0-1
: random = RND(1)

REM Random integer 1-10
: dice = INT(RND(1) * 10) + 1

REM Random integer in range [min, max]
: DIM min = 5, max = 20
: random_int = INT(RND(1) * (max - min + 1)) + min
```

### Reproducible Random Sequence

```kcml
REM Start with same seed for reproducible tests
: dummy = RND(0)
: FOR i = 1 TO 5
:   PRINT RND(1)
: NEXT i
```

## Constants

### #PI - Pi Constant

```kcml
#PI    : REM 3.14159265359
```

### Boolean Constants

```kcml
TRUE   : REM Non-zero (1)
FALSE  : REM Zero (0)
```

### User-Defined Constants

```kcml
DIM _MAX_VALUE = 1000
DIM _EPSILON = 0.00001
DIM _TAX_RATE = 0.0825
```

## CONVERT Statement

### String to Number

```kcml
CONVERT alpha_variable TO numeric_receiver
```

Example:

```kcml
DIM value$10, number
: value$ = "123.45"
: CONVERT value$ TO number
: PRINT number + 10    : REM 133.45
```

### Number to Formatted String

```kcml
CONVERT numeric_expression TO alpha_receiver, (picture)
```

Picture format characters:

| Char | Meaning |
|------|---------|
| `#` | Digit placeholder |
| `.` | Decimal point |
| `,` | Thousands separator |
| `$` | Currency symbol |
| `+` | Show sign (+ or -) |
| `-` | Show sign (- only) |
| `^` | Exponential notation |

### CONVERT Examples

```kcml
DIM result$20, value
: value = 1234.567

: CONVERT value TO result$, (####.##)
: PRINT result$    : REM "1234.57"

: CONVERT value TO result$, ($#,###.##)
: PRINT result$    : REM "$1,234.57"

: CONVERT value TO result$, (-####.##)
: PRINT result$    : REM " 1234.57" (space for positive)

: CONVERT -value TO result$, (-####.##)
: PRINT result$    : REM "-1234.57"
```

### Scientific Notation

```kcml
DIM result$20
: CONVERT 123456.789 TO result$, (#.###^^^^)
: PRINT result$    : REM "1.235E+05"
```

## PRINTUSING - Formatted Output

```kcml
PRINTUSING format$, value1, value2, ...
```

Same format characters as CONVERT:

```kcml
price = 1234.56
: quantity = 42
: PRINTUSING "Price: $#,###.##  Qty: ###", price, quantity
: REM Output: Price: $1,234.56  Qty:  42
```

## Comparison Operators

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `<>` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

### Numeric Comparisons

```kcml
IF (a == b) THEN PRINT "Equal"
: IF (a <> 0) THEN PRINT "Not zero"
: IF (x >= min AND x <= max) THEN PRINT "In range"
```

## Ternary Operator

Inline conditional:

```kcml
result = (condition ? value_if_true : value_if_false)
```

Examples:

```kcml
max = (a > b ? a : b)
: sign = (x < 0 ? -1 : (x > 0 ? 1 : 0))
: discount = (quantity >= 10 ? 0.1 : 0)
```

## DIM( Function - Array Dimensions

Get array size:

```kcml
DIM(array, dimension)
```

Example:

```kcml
DIM data(100, 50)
: rows = DIM(data(), 1)     : REM 100
: cols = DIM(data(), 2)     : REM 50
```

## Useful Formulas

### Modulo (Remainder)

KCML has a built-in `MOD(` function:

```kcml
remainder = MOD(17, 5)    : REM Returns 2
```

General form:
```kcml
MOD(numeric_expression, numeric_expression)
```

Common uses:
```kcml
REM - Even/odd test
IF MOD(sv_i, 2) == 0 THEN PRINT "even"

REM - Wrap a counter at N
counter = MOD(counter + 1, total)

REM - Check divisible by N
IF MOD(value, 10) == 0 THEN PRINT "multiple of 10"
```

### Rounding to N Decimal Places

```kcml
DEFFN round(x, places) = INT(x * 10 ^ places + 0.5) / 10 ^ places

: rounded = FN round(3.14159, 2)  : REM 3.14
```

### Clamp Value to Range

```kcml
DEFFN clamp(x, min, max) = (x < min ? min : (x > max ? max : x))

: clamped = FN clamp(150, 0, 100)  : REM 100
```

### Linear Interpolation

```kcml
DEFFN lerp(a, b, t) = a + (b - a) * t

: mid = FN lerp(0, 100, 0.5)  : REM 50
```

## Common Error Codes

| Code | Error |
|------|-------|
| C60 | Numeric overflow |
| C62 | Division by zero |
| C63 | Zero divided by zero |
| C64 | Negative square root |
| C65 | Log of zero or negative |

### Safe Division

```kcml
DEFSUB 'safe_divide(a, b)
:   IF (b == 0) THEN RETURN 0
:   RETURN a / b
: END SUB
```

## See Also

- [date-functions.md](date-functions.md) - Date/time calculations
- [string-functions.md](string-functions.md) - CONVERT for number/string conversion
- [control-flow.md](control-flow.md) - FOR loops with numeric ranges
- [arrays-variables.md](arrays-variables.md) - Numeric arrays
