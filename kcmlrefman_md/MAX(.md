# MAX(

> Returns the highest value from a list of expressions or array elements.

## Syntax

```
MAX( expr [, expr ...] )
MAX( array() [, expr ...] )
```

Returns a numeric or string value. Valid wherever a numeric or string expression is legal.

## Description

Returns the maximum value from all arguments. If an array is passed, each element is treated as a separate argument.

## Examples

```kcml
: DIM a(3), x
: a(1)=5 : a(2)=3 : a(3)=8
: x = MAX(a(), 20)
: PRINT "MAX(a,20)="; x    REM 20 (20 > 8)
: $END
```

Output: `MAX(a,20)= 20`

More examples:
```kcml
amsl = MAX(500, test)
result = MAX(cat(), 20)
test$ = MAX(string1$, string2$, one$)    REM string comparison
```

## See Also

- `MIN(` — minimum value
- `ABS(` — absolute value
