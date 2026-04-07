# LOG(

> Returns the natural (base e) logarithm of a numeric expression.

## Syntax

```
LOG( numeric_expression )
```

Returns a numeric value. Valid wherever a numeric function is legal.

## Description

`LOG(` computes ln(x) — the natural logarithm (base e ≈ 2.71828...). The argument must be positive.

## Examples

```kcml
: DIM x
: x = LOG(1)
: PRINT "LOG(1)="; x
: x = LOG(2.718281828459)
: PRINT "LOG(e)="; x
: x = LOG(100)
: PRINT "LOG(100)="; x
: $END
```

Output:
```
LOG(1)= 0
LOG(e)= 1
LOG(100)= 4.605170185988
```

Common use:

```kcml
Test = LOG(.723)
value1 = 17 + LOG(ABS(temp))
```

## Notes

- `LOG(` is base **e** (natural log). For base 10, use `LGT(`.
- The argument must be strictly positive. Passing 0 or a negative number is a runtime error.
- Use `ABS(` to guard against negative inputs.

## See Also

- `LGT(` — base 10 logarithm
- `EXP(` — e raised to a power (inverse of LOG)
- `ABS(` — absolute value
