# MIN(

> Returns the lowest value from a list of expressions or array elements.

## Syntax

```
MIN( expr [, expr ...] )
MIN( array() [, expr ...] )
```

Returns a numeric or string value. Valid wherever a numeric or string expression is legal.

## Description

Returns the minimum value from all arguments. If an array is passed, each element is a separate argument.

## Examples

```kcml
: DIM a(3), x
: a(1)=5 : a(2)=3 : a(3)=8
: x = MIN(a(), 20)
: PRINT "MIN(a,20)="; x    REM 3 (3 is smallest)
: $END
```

Output: `MIN(a,20)= 3`

More examples:
```kcml
answer = MIN(500, test)
result = MIN(cat(), 20, cat)
test$ = MIN(string1$, string2$, HEX(FF))
```

## See Also

- `MAX(` — maximum value
