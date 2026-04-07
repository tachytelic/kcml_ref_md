# DIM(

> Returns the declared size of an array dimension, or the occurs count of a field variable.

## Syntax

```
DIM( array_name, dimension )
DIM( field )
```

| Parameter | Description |
|-----------|-------------|
| `array_name` | A numeric, alpha, or field array variable (with `()`) |
| `dimension` | `1` for the first dimension, `2` for the second |
| `field` | A numeric or string field variable (KCML 6.10+) |

Returns a numeric value. Valid wherever a numeric expression is legal.

## Description

`DIM(` returns the current declared size of the specified dimension of an array.

- Returns `0` if a second dimension is requested for a one-dimensional array.
- From KCML 6.10+, `DIM(field)` returns the `OCCURS` count of a field variable (1 if no OCCURS is specified).

## Examples

### Array dimensions

```kcml
: DIM arr(5,3), s(10)
: PRINT "DIM(arr,1)="; DIM(arr(),1)
: PRINT "DIM(arr,2)="; DIM(arr(),2)
: PRINT "DIM(s,1)="; DIM(s(),1)
: PRINT "DIM(s,2)="; DIM(s(),2)
: $END
```

Output:
```
DIM(arr,1)= 5
DIM(arr,2)= 3
DIM(s,1)= 10
DIM(s,2)= 0
```

### Using DIM( to bound a loop

```kcml
FOR loop = 1 TO DIM(record(),2)
    ...
NEXT loop

size = DIM(flow(),1) * 2
```

### Field occurs (KCML 6.10+)

If `.a` is `(1, "DATE")` and `.b` is `(2, "DATE*5")`:
```kcml
DIM(.a)    REM = 1
DIM(.b)    REM = 5
```

## Notes

- The array variable must be passed with `()` to distinguish it from a scalar: `DIM(arr(),1)` not `DIM(arr,1)`.
- Returns `0` for the second dimension of a 1D array.

## See Also

- `DIM` — declare array variables
- `COM` — declare common array variables
- `MAT REDIM` — resize an array at runtime
- `LIST DIM` — list all declared variables and their dimensions
