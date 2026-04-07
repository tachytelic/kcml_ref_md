# DATA

> Embeds static data values in a program for sequential reading with `READ` or `MAT READ`.

## Syntax

```
DATA data-element [, data-element] ...
```

Where each `data-element` is one of:
- A numeric literal: `3.141`, `2`, `HEX(020402)`, `3E05`, `0x0123`
- A string literal: `"Red"`, `"Hello"`
- A field definition pair: `(start, length)` (for use with `FLD(`)

## Description

`DATA` stores a list of values in the program. When a `READ` statement executes, it takes the next sequential item from the `DATA` list and assigns it to a variable. The `DATA` pointer advances with each `READ`.

- Initially, the data pointer starts at the first item in the first `DATA` statement.
- `RESTORE` resets the pointer to the beginning of a specific `DATA` statement.
- If `READ` runs out of data, a runtime error occurs.

### Field definitions

`DATA` can also hold field definitions for use with `FLD(`. A field definition is a start/length pair in parentheses. If the start position is blank, it is calculated automatically from the previous field's end:

```kcml
DATA (1,10), (,5), (,8)
```

### Alignment

The parser does not strip redundant spaces from `DATA` statements, so columns can be aligned for readability:

```kcml
DATA  9876.89, 67281.7, 1324.8
DATA    48.02,  8971.2,    1.9
```

## Examples

### Basic READ loop

```kcml
100 DATA 10, 20, 30, "Hello"
200 DIM a, b, c, s$10
300 READ a, b, c
400 PRINT a; b; c
500 READ s$
600 PRINT s$
700 END
```

Output:
```
 10  20  30
Hello
```

### Hex and mixed data

```kcml
DATA 2, 4, 6, HEX(7C), "Red", 3E05
DATA HEX(020402), HEX(020400)
DATA 0x0123, 0x9078, 0x1452
```

### RESTORE to re-read

```kcml
100 DATA 1, 2, 3
200 READ a, b, c
300 RESTORE 100
400 READ x, y, z
```

After `RESTORE 100`, the pointer resets to line 100; `x`, `y`, `z` get 1, 2, 3 again.

## Notes

- `DATA` is a **program-mode-only** statement — it requires a numbered program and is not available in `-p` script mode (`A07 Illegal immediate mode statement`).
- `DATA` is evaluated at resolve time; expressions must be resolvable then.
- Multiple `DATA` statements are treated as one continuous list.

## See Also

- `READ` — read values from the DATA list into variables
- `MAT READ` — read values from DATA into an array
- `RESTORE` — reset the DATA pointer
- `FLD(` — access field variables
