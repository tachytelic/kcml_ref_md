# KCML Data Types Reference

KCML is a dynamically-typed BASIC variant with implicit type conversion between numeric and string data.

## Numeric Variables

Numeric variables store floating-point numbers. They are declared without a suffix:

```kcml
DIM count, total, price
: count = 10
: total = 3.14159
: price = 99.95
: $END
```

### Numeric Ranges

- Uses 64-bit floating point (IEEE 754 double precision)
- Range: approximately ±1.7E±308
- Precision: about 15-16 significant decimal digits

### Initialization

```kcml
DIM x = 100                     : REM Initialize on declaration
DIM a, b = 50, c = 25          : REM Multiple with defaults
: $END
```

## String Variables

String variables store text data. They are declared with a `$` suffix and a maximum length:

```kcml
DIM name$30                     : REM Up to 30 characters
DIM address$100                 : REM Up to 100 characters
: name$ = "John Smith"
: $END
```

### String Length

The number after `$` specifies the maximum length. Strings are **fixed-length** and padded with spaces:

```kcml
DIM short$5
: short$ = "Hello World"        : REM Truncated to "Hello"
: short$ = "Hi"                 : REM Stored as "Hi   " (padded)
: $END
```

### Empty Strings

```kcml
DIM text$20
: text$ = ""                    : REM Empty (all spaces)
: IF text$ = " " THEN PRINT "Empty or space-padded"
: $END
```

### String Functions

Use `LEN()` to get actual content length (excluding trailing spaces):

```kcml
DIM s$10
: s$ = "Hello"
: PRINT LEN(s$)                 : REM 5 (not 10)
: $END
```

## Arrays

Arrays store multiple values of the same type. Declared with parentheses:

```kcml
DIM numbers(10)                 : REM 10 numeric elements
DIM names$20(50)                : REM 50 strings, each max 20 chars
: $END
```

### Array Indexing

Arrays are **1-based** by default:

```kcml
DIM values(5)
: values(1) = 100
: values(2) = 200
: values(5) = 500
: PRINT values(3)               : REM 0 (uninitialized)
: $END
```

### Multi-Dimensional Arrays

```kcml
DIM matrix(10, 10)              : REM 10x10 grid
DIM cube(5, 5, 5)               : REM 3D array
: matrix(1, 1) = 100
: matrix(5, 3) = 75
: $END
```

### Dynamic Arrays

```kcml
DIM dynamicSize
: dynamicSize = 100
DIM arr(dynamicSize)            : REM Size determined at runtime
: $END
```

## Field Variables

Field variables use dot notation to access data within record structures:

```kcml
DIM record$100
: record.name$ = "Smith"
: record.age = 30
: record.salary = 50000.00
: $END
```

### Field Definitions

Fields are defined within a record buffer:

```kcml
: FIELD record$ WITH name$30, age, salary
: name$ = "John Doe"
: age = 25
: salary = 45000
: $END
```

## Constants

Constants use underscore prefix and cannot be changed after initialization:

```kcml
DIM _MAX_SIZE = 100
DIM _PI = 3.14159
DIM _COMPANY_NAME$30 = "Acme Corp"

: PRINT _MAX_SIZE               : REM 100
: REM _MAX_SIZE = 200           : REM Error - cannot modify constant
: $END
```

## Variable Scope

### LOCAL Variables (Default)

Variables declared with DIM are local to the current subroutine:

```kcml
SUB ProcessData()
   DIM temp = 100               : REM Local to this SUB
   : PRINT temp
: END SUB
: $END
```

### PUBLIC Variables

PUBLIC variables are accessible from any subroutine in the program:

```kcml
PUBLIC DIM globalCounter = 0

SUB IncrementCounter()
   : globalCounter++
: END SUB

: GOSUB IncrementCounter
: PRINT globalCounter           : REM 1
: $END
```

### PRIVATE Variables

PRIVATE restricts visibility to the current module:

```kcml
PRIVATE DIM moduleData$50

: moduleData$ = "Internal use only"
: $END
```

## COM Variables (Persistent)

COM variables survive program LOAD and CHAIN operations:

```kcml
COM DIM sharedValue = 0
COM DIM userName$30

: sharedValue = 100
: userName$ = "Admin"
: LOAD "nextprogram.kcml"       : REM Values persist
: $END
```

### COM Variable Uses

- Pass data between chained programs
- Maintain state across program loads
- Share configuration settings

See [Global Variables](global-variables.md) for more details on COM.

## Type Conversion

### Automatic Conversion

KCML automatically converts between types in many contexts:

```kcml
DIM num = 42
DIM text$10
: text$ = num                   : REM Converts to "42"
: PRINT "Value: " & num         : REM Num converted to string
: $END
```

### Explicit Conversion

Use `STR()` for numeric to string:

```kcml
DIM n = 123.45
DIM s$20
: s$ = STR(n)
: PRINT s$                      : REM "123.45"
: $END
```

Use `VAL()` for string to numeric:

```kcml
DIM s$10 = "99.5"
DIM n
: n = VAL(s$)
: PRINT n + 0.5                 : REM 100
: $END
```

### CONVERT Statement

For formatted conversion:

```kcml
DIM price = 1234.56
DIM formatted$20
: CONVERT price TO formatted$,"$###,###.##"
: PRINT formatted$              : REM "$  1,234.56"
: $END
```

## Hexadecimal Data

Use `HEX()` function for hex values:

```kcml
DIM byte$1
: byte$ = HEX(FF)               : REM Byte value 255
: byte$ = HEX(00)               : REM Null byte
: byte$ = HEX(0D0A)             : REM CR+LF
: $END
```

### Binary Operations

```kcml
DIM flags$1
: flags$ = HEX(00)
: flags$ = OR HEX(01)           : REM Set bit 0
: flags$ = OR HEX(08)           : REM Set bit 3
: PRINT ASC(flags$)             : REM 9 (binary 00001001)
: $END
```

## Special Values

### Null Strings

```kcml
DIM empty$1
: empty$ = HEX(00)              : REM Actual null character
: IF ASC(empty$) = 0 THEN PRINT "Null byte"
: $END
```

### Quotes in Strings

Use `HEX(22)` for embedded quotes:

```kcml
DIM msg$50
: msg$ = "He said " & HEX(22) & "Hello" & HEX(22)
: PRINT msg$                    : REM He said "Hello"
: $END
```

## Declaration Modes

### Implicit Declaration

By default, variables can be used without DIM:

```kcml
: x = 100                       : REM Auto-created as numeric
: name$ = "Test"                : REM Error - strings need DIM
: $END
```

### Explicit Declaration Mode

Use `OPTION EXPLICIT` to require all variables be declared:

```kcml
: OPTION EXPLICIT
DIM count
: count = 10                    : REM OK
: REM total = 20                : REM Error - undeclared
: $END
```

## See Also

- [Arrays and Variables](arrays-variables.md) - Array operations
- [Global Variables](global-variables.md) - COM and persistent variables
- [Formatting](formatting.md) - PRINT USING and CONVERT
- [Operators](operators.md) - Type conversion in expressions
