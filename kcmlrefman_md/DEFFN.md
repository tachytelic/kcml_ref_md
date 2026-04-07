# DEFFN

> Defines a single-expression numeric function that can be called with `FN`.

## Syntax

```
DEFFN desc( numeric_scalar_var ) = expression
```

| Element | Description |
|---------|-------------|
| `desc` | Function identifier — either a single digit (0–9) or an alphanumeric name (first character must be a letter) |
| `numeric_scalar_var` | A single numeric variable used as the function's argument |
| `expression` | A numeric expression evaluated when the function is called |

## Description

`DEFFN` defines a named single-expression function. It is called with `FN desc(value)` from within any numeric expression.

- `DEFFN` can appear anywhere in the program without affecting program flow.
- The argument variable (`numeric_scalar_var`) holds the value passed from `FN`. Its contents are **not altered** by the call.
- If multiple `DEFFN` definitions exist for the same name, the **first** one in the program is used.
- When searching for a `DEFFN`, the currently selected global partition is searched before the foreground unless `KEEPSHARED` environment variable is set (in which case foreground is searched first).

## Examples

### Circular area function

```kcml
: DIM result
: DEFFN area(r) = 3.14159 * r * r
: result = FN area(5)
: PRINT "area(5)="; result
: result = FN area(10)
: PRINT "area(10)="; result
: $END
```

Output:
```
area(5)= 78.53975
area(10)= 314.159
```

### Celsius to Fahrenheit

```kcml
DEFFN CtoF(c) = c * 9/5 + 32

temp_f = FN CtoF(100)
```

### Using the #PI constant

```kcml
DEFFN area(radius) = #PI * radius ^ 2
```

## Notes

- `DEFFN` only supports **single-expression** numeric functions with one argument. For multi-statement or string-returning functions, use `DEFSUB` instead.
- The argument variable is a pass-by-value copy — changes inside the expression don't affect the caller's variable.
- `DEFFN` with a digit name (e.g. `DEFFN 1(x) = x*2`) is the old-style numeric form; symbolic names are preferred.

## See Also

- `FN` — call a function defined with `DEFFN`
- `DEFSUB` — define a multi-statement subroutine (preferred for complex logic)
- `DEFFN'` — deprecated subroutine entry point (use `DEFSUB` instead)
