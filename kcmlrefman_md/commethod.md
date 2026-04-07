# Object Methods

> How to call methods on KCML objects.

## Syntax

```
object.Method([args])
result = object.Method([args])
OBJECT objvar = object.Method([args])
```

## Description

Methods are called using dot notation. They may return a numeric value, a string, or another object.

```kcml
rsTable.MoveNext()
List.AddString("Hello")
a$ = a.UpdateText(BYREF name$)
record.Open("Customers", OBJECT connect, ENUM adOpenForwardOnly)
```

## Argument modifiers

| Modifier | Effect |
|----------|--------|
| `BYREF varname` | Pass variable by reference — allows the method to modify it |
| `ENUM constname` | Pass a COM enumeration constant |
| `REDIM arr()` | Pass array and allow method to resize it |
| `INT(expr)` | Force argument as 32-bit signed integer (default for numbers) |
| `NUM(expr)` | Force argument as 64-bit floating-point double |
| `DIM(arr$())` | Force a string array to be passed as an array, not a single string |

By default:
- Scalar arguments are passed by value (object gets a copy).
- Strings and arrays are always passed by reference.
- Numbers are passed as 32-bit integers; use `NUM()` to force 64-bit float.

## Methods returning objects

```kcml
OBJECT rsTable = cnConnect.Open("SALES")
```

The `OBJECT` keyword is required to distinguish from a numeric `LET`.

## Named parameters (VBA/SOAP)

Pass parameters by name for VBA or SOAP objects where parameter names are significant:

```kcml
chart.ChartWizard(OBJECT range, ENUM xlDoughnut, "title" = title$, "extraTitle" = "Hello")
```

## Coercion examples

```kcml
REM Excel: get a single numeric value by reference
worksheet.Range("A9").Value(BYREF NUM(t))

REM Excel: get a 2D range as a string array
worksheet.Range("A3:D4").Value(DIM(a$()))

REM Excel: get a range resizing the target array
worksheet.Range("A10:D11").Value(REDIM NUM(t()))
```

## See Also

- `comprops` — object properties
- `comconst` — `ENUM` constants
- `comcompound` — chained method calls
- `comsubs` — passing objects to subroutines
- `comautomation` — VBA-specific issues
