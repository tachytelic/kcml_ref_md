# MOD(

> Returns the remainder (modulus) when one number is divided by another.

## Syntax

```
MOD( numeric_expression, numeric_expression )
```

Returns a numeric value. Valid wherever a numeric function is legal.

## Description

`MOD(a, b)` returns `a MOD b` — the remainder after integer division of `a` by `b`.

## Examples

```kcml
: DIM x
: x = MOD(500, 7)
: PRINT "MOD(500,7)="; x    REM 3
: x = MOD(10, 3)
: PRINT "MOD(10,3)="; x     REM 1
: $END
```

Output:
```
MOD(500,7)= 3
MOD(10,3)= 1
```

Common use — day of week from Julian date:
```kcml
DIM julian, dow
CONVERT DATE "2026-04-07" TO julian
dow = MOD(julian, 7)    REM 0=Monday
```

## Notes

- `MOD(a, b)` is equivalent to `a - b * INT(a/b)`.
- Also available as the `MOD` infix operator: `a MOD b`.

## See Also

- `INT(` — floor integer
- `FIX(` — truncate toward zero
- `JulianDate` — Julian dates (day of week via MOD 7)
