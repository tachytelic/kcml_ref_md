# LGT(

> Returns the common (base 10) logarithm of a numeric expression.

## Syntax

```
LGT( numeric_expression )
```

Returns a numeric value. Valid wherever a numeric function is legal.

## Description

`LGT(` computes log₁₀(x). The argument must be positive — passing zero or a negative number causes a runtime error. Use `ABS(` to ensure a positive argument when needed.

## Examples

```kcml
: DIM x
: x = LGT(100)
: PRINT "LGT(100)="; x
: x = LGT(1000)
: PRINT "LGT(1000)="; x
: x = LGT(ABS(-50))
: PRINT "LGT(ABS(-50))="; x
: $END
```

Output:
```
LGT(100)= 2
LGT(1000)= 3
LGT(ABS(-50))= 1.698970004336
```

Expression use:

```kcml
value_1 = 17 + LGT(ABS(temp))
```

## Notes

- `LGT(` is base 10. For natural log (base e), use `LOG(`.
- The argument must be strictly positive. Passing 0 or a negative number is a runtime error.
- Use `ABS(` to guard against negative inputs: `LGT(ABS(x))`.

## See Also

- `LOG(` — natural (base e) logarithm
- `EXP(` — e raised to a power
- `ABS(` — absolute value
