# KCML Subroutines Reference

Complete reference for defining and calling subroutines in KCML.

## DEFSUB - Define a Subroutine

### Basic Syntax

```kcml
DEFSUB 'subroutine_name(parameters)
:   REM Subroutine body
:   LOCAL DIM local_vars
:   REM ... code ...
: END SUB
```

### Simple Example

```kcml
DEFSUB 'greet(name$)
:   PRINT "Hello, "; name$; "!"
: END SUB

REM Call it:
: 'greet("World")
```

### With Return Value

String functions end with `$`:

```kcml
DEFSUB 'format_name$(first$, last$)
:   RETURN last$ & ", " & first$
: END SUB

REM Usage:
: full_name$ = 'format_name$("John", "Doe")
```

Numeric functions without `$`:

```kcml
DEFSUB 'calculate_tax(amount, rate)
:   RETURN amount * rate / 100
: END SUB

REM Usage:
: tax = 'calculate_tax(100, 8.5)
```

## Parameters

### Pass by Value (Default)

Values are copied into local variables:

```kcml
DEFSUB 'double(x)
:   x = x * 2         : REM Only changes local copy
:   RETURN x
: END SUB

: value = 5
: result = 'double(value)  : REM result = 10
: PRINT value              : REM value still = 5
```

### Pass by Reference (BYREF)

Changes affect the original variable:

```kcml
DEFSUB 'increment(BYREF x)
:   x = x + 1         : REM Changes original!
: END SUB

: value = 5
: 'increment(BYREF value)
: PRINT value              : REM value = 6
```

### Returning Multiple Values with BYREF

```kcml
DEFSUB 'divide_with_remainder(dividend, divisor, BYREF quotient, BYREF remainder)
:   quotient = INT(dividend / divisor)
:   remainder = dividend - (quotient * divisor)
: END SUB

REM Usage:
: DIM q, r
: 'divide_with_remainder(17, 5, BYREF q, BYREF r)
: PRINT "17 / 5 = "; q; " remainder "; r
```

### Array Parameters

```kcml
DEFSUB 'sum_array(values())
:   LOCAL DIM total, i
:   total = 0
:   FOR i = 1 TO DIM(values(), 1)
:     total = total + values(i)
:   NEXT i
:   RETURN total
: END SUB

REM Usage:
: DIM numbers(5)
: numbers(1) = 10 : numbers(2) = 20 : numbers(3) = 30
: total = 'sum_array(numbers())
```

### Optional Parameters

Parameters with default values:

```kcml
DEFSUB 'format_number(value, decimals = 2, prefix$ = "$")
:   LOCAL DIM result$30
:   CONVERT value TO result$, (prefix$ & "####.##")
:   RETURN result$
: END SUB

REM Call with all parameters:
: s$ = 'format_number$(123.456, 2, "£")

REM Call with defaults:
: s$ = 'format_number$(123.456)         : REM Uses decimals=2, prefix$="$"
: s$ = 'format_number$(123.456, 3)      : REM Uses prefix$="$"
```

## LOCAL DIM - Local Variables

Declare variables that exist only within the subroutine:

```kcml
DEFSUB 'process_data(input$)
:   LOCAL DIM temp$100, i, count
:   LOCAL DIM buffer$(10)    : REM Local array
:   REM ... use temp$, i, count, buffer$ ...
:   REM Variables are destroyed when subroutine returns
: END SUB
```

### Initializing Local Variables

```kcml
DEFSUB 'counter()
:   LOCAL DIM count = 0      : REM Initialize to 0
:   LOCAL DIM name$ = "default"
:   count = count + 1
:   RETURN count
: END SUB
```

## RETURN Statement

### Return Without Value

```kcml
DEFSUB 'log_message(msg$)
:   PRINT $TIME; " - "; msg$
:   RETURN                  : REM Exit subroutine
: END SUB
```

### Return with Value

```kcml
DEFSUB 'max(a, b)
:   IF (a > b) THEN RETURN a
:   RETURN b
: END SUB
```

### Early Return

```kcml
DEFSUB 'find_position(items$(), search$)
:   LOCAL DIM i
:   FOR i = 1 TO DIM(items$(), 1)
:     IF (items$(i) == search$) THEN RETURN i
:   NEXT i
:   RETURN 0    : REM Not found
: END SUB
```

## Calling Subroutines

### As Statement

```kcml
'my_subroutine(arg1, arg2)
```

### In Expression

```kcml
result = 'calculate(x, y) * 2
name$ = "Hello " & 'get_name$()
```

### With GOSUB Keyword (Deprecated)

```kcml
GOSUB 'my_routine(args)    : REM Old style, still works
'my_routine(args)          : REM Preferred modern style
```

## PUBLIC and PRIVATE

Control visibility in libraries:

```kcml
PUBLIC DEFSUB 'api_function(x)
:   REM Visible outside library
: END SUB

PRIVATE DEFSUB 'internal_helper(x)
:   REM Only visible within this library
: END SUB
```

## DEFFN - Simple Inline Functions

For simple one-expression functions:

```kcml
DEFFN area(radius) = #PI * radius ^ 2
DEFFN celsius(fahrenheit) = (fahrenheit - 32) * 5 / 9

REM Usage with FN:
: circle_area = FN area(10)
: temp_c = FN celsius(98.6)
```

## Recursive Subroutines

```kcml
DEFSUB 'factorial(n)
:   IF (n <= 1) THEN RETURN 1
:   RETURN n * 'factorial(n - 1)
: END SUB

REM Usage:
: fact = 'factorial(5)    : REM Returns 120
```

## Passing Functions as Parameters

```kcml
DEFSUB 'apply(BYREF 'func, value)
:   RETURN 'func(value)
: END SUB

DEFSUB 'double(x)
:   RETURN x * 2
: END SUB

DEFSUB 'square(x)
:   RETURN x * x
: END SUB

REM Usage:
: result = 'apply(BYREF 'double, 5)   : REM Returns 10
: result = 'apply(BYREF 'square, 5)   : REM Returns 25
```

## Pattern: Database Access (from libKI)

```kcml
DEFSUB 'db_read_record(handle, key$, BYREF record$, BYREF status)
:   LOCAL DIM err
:   CALL KI_READ handle, key$, record$ TO status, err
:   IF (status <> 0) THEN DO
:     PRINT "Read error: "; err
:   ENDDO
: END SUB
```

## Pattern: Error-Safe Wrapper

```kcml
DEFSUB 'safe_open(filename$, mode$, BYREF stream)
:   LOCAL DIM success = FALSE
:   TRY
:     OPEN #stream, filename$, mode$
:     success = TRUE
:   CATCH ERR 82, 83
:     PRINT "Cannot open: "; filename$
:   END TRY
:   RETURN success
: END SUB

REM Usage:
: DIM stream = 1
: IF ('safe_open("data.txt", "r", BYREF stream)) THEN DO
:   REM File is open on stream
:   CLOSE #stream
: ENDDO
```

## Pattern: String Builder

```kcml
DEFSUB 'build_csv_line$(fields$())
:   LOCAL DIM result$1000, i, sep$
:   result$ = ""
:   sep$ = ""
:   FOR i = 1 TO DIM(fields$(), 1)
:     result$ = result$ & sep$ & fields$(i)
:     sep$ = ","
:   NEXT i
:   RETURN result$
: END SUB
```

## CALL - External Functions

Call external library functions:

```kcml
CALL function_name arg1, arg2 TO result

REM Database example:
: CALL KI_OPEN path$, mode TO handle, status
: CALL KI_READ handle, key$, buffer$ TO status, error
: CALL KI_CLOSE handle TO status
```

## $DECLARE - DLL/Shared Library Functions

Access Windows DLLs or Unix shared libraries:

```kcml
$DECLARE 'MessageBox(INT(), STR(), STR(), INT()) = "user32.MessageBoxA"

REM Usage:
: ret = 'MessageBox(0, "Hello", "Title", 0)
```

### Server-Side Execution

Prefix with asterisk for server-side:

```kcml
$DECLARE 'chmod(STR(), INT()) = "*"   : REM Unix chmod on server
```

## Best Practices

1. **Use END SUB** - Required for $COMPLIANCE level 1+
2. **Use LOCAL DIM** - Avoid polluting global namespace
3. **Document parameters** - Comment what each parameter does
4. **Use BYREF sparingly** - Only when returning multiple values
5. **Keep functions focused** - One function, one task
6. **Use meaningful names** - `'calculate_total` not `'ct`
7. **Handle errors** - Use TRY/CATCH in functions

## Common Patterns

### Initialization Subroutine

```kcml
DEFSUB 'initialize()
:   COM CLEAR          : REM Clear common variables
:   'setup_defaults()
:   'load_config()
: END SUB
```

### Callback Pattern

```kcml
DEFSUB 'for_each(items$(), BYREF 'callback)
:   LOCAL DIM i
:   FOR i = 1 TO DIM(items$(), 1)
:     'callback(items$(i))
:   NEXT i
: END SUB

DEFSUB 'print_item(item$)
:   PRINT "Item: "; item$
: END SUB

REM Usage:
: 'for_each(my_items$(), BYREF 'print_item)
```

## See Also

- [arrays-variables.md](arrays-variables.md) - Array parameters
- [error-handling.md](error-handling.md) - Error handling in subroutines
- [control-flow.md](control-flow.md) - Loops and conditionals
