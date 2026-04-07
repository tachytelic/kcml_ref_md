# MAT READ (READ array)

> Reads values from DATA statements into array variables. Program mode only.

## Syntax

```
[MAT] READ array_name [(dim1 [,dim2])[length]] [, ...]
```

## Description

Assigns values from `DATA` statements into arrays, row by row, left to right within each row. Arrays may be optionally redimensioned in the same statement.

Data is read from the first `DATA` statement unless `RESTORE` specifies a different line. An error occurs if there is insufficient data, or if a value type does not match the array type.

**Note:** `DATA` is a program-mode construct and causes an `A07` error in `-p` script mode.

## Example

```kcml
DIM array(2,2), string$(2)7
READ array(), string$()
MAT PRINT array(), string$()
DATA 1, 2, 3, 4, "hello", "goodbye"
```

Output:
```
 1   2
 3   4
 hello
 goodbye
```

## See Also

- `DATA` — define inline data
- `READ` — read scalar values from DATA
- `RESTORE` — reset DATA read pointer
