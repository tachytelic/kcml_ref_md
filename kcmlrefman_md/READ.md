# READ

> Assigns values from DATA statements to variables sequentially.

## Syntax

```
READ variable [, variable ...]
```

## Description

`READ` reads values from `DATA` statements in program order and assigns them to the listed variables. The data pointer advances with each read.

- If `READ` needs more values than remain in the current `DATA` statement, it continues into the next `DATA` statement found later in the program.
- If `READ` consumes fewer values than are in a `DATA` statement, the next `READ` picks up where the previous one left off.
- Variable types must match data types (alpha to alpha, numeric to numeric).
- `RESTORE` resets the data pointer.

## Examples

```kcml
READ abc, def, abc$, def$
PRINT abc, def, abc$, def$
DATA 120.10, 1000, "HELLO!", "GOODBYE!"
```

Output:
```
 120.10   1000  HELLO! GOODBYE!
```

```kcml
REM Reading into arrays
READ act(1), temp(count), test$(4)
DATA 10, 20, "Alpha"
```

```kcml
REM Multi-pass data reading with RESTORE
FOR pass = 1 TO 3
  RESTORE
  READ x, y
  PRINT x + y
NEXT pass
DATA 10, 20
```

```kcml
REM Read entire string array
READ file$()
DATA "first.txt", "second.txt", "third.txt"
```

## Notes

- `DATA` statements can appear anywhere in the program — `READ` searches forward from the current pointer position.
- A `RUN` or `LOAD` resets the data pointer to the first `DATA` value.
- For matrix operations, see `MAT READ`.

## See Also

- `DATA` — define constant data
- `RESTORE` — reset the data pointer
- `MAT READ` — read an entire array from DATA
