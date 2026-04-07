# SELECT PRECISION

> Sets the tolerance for numeric equality comparisons.

## Syntax

```
SELECT PRECISION numeric_expr
prec$ = SELECT PRECISION
```

## Description

KCML stores numbers in binary floating-point. Due to representation errors, `1.23456 * 100000` may not equal exactly `123456`. The PRECISION setting defines "sufficiently close" — two numbers differing by less than the precision value are treated as equal.

Default precision: `1E-10`.

Used as a function (right-hand side), returns the current precision as a string.

## Examples

```kcml
SELECT PRECISION 1E-8
IF 1 == 1 + 1E-9 THEN PRINT "True"   : REM  True (diff < 1E-8)
```

```kcml
SELECT PRECISION 1E-5
PRINT SELECT PRECISION     : REM  1E-05
```

```kcml
prec$ = SELECT PRECISION
PRINT "Current precision is: "; prec$
```

## Notes

- Looser precision (larger value) allows more floating-point "noise" to be treated as equal — useful for financial arithmetic with accumulated rounding.
- Tighter precision (smaller value) may cause comparisons to fail due to floating-point representation.
- Default `1E-10` is appropriate for most programs.

## See Also

- `SELECT` — overview
- `ROUND(` — explicit rounding
