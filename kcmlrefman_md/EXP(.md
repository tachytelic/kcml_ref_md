# EXP(

> Returns e raised to the power of the numeric expression (the natural exponential function).

## Syntax

```
EXP( numeric_expression )
```

| Parameter | Description |
|-----------|-------------|
| `numeric_expression` | The exponent |

Returns a numeric value. Valid wherever a numeric function is legal.

## Description

`EXP(` calculates eˣ, where e ≈ 2.71828... (Euler's number). It is the inverse of the natural logarithm `LOG(`.

## Examples

```kcml
: DIM x
: x = EXP(1)
: PRINT x
: $END
```

Output:
```
 2.718281828459
```

In expressions:
```kcml
Test = EXP(.723)
Junk = 17 + EXP(ABS(Temporary))
```

### Natural logarithm inverse

```kcml
: DIM x, y
: x = 5
: y = EXP(LOG(x))
: PRINT y
: $END
```

Output: `5` (within floating-point precision)

## See Also

- `LOG(` — natural logarithm (inverse of EXP()
- `LOG10(` — base-10 logarithm
- `^` — power operator (also computes exponentials for integer/rational powers)
