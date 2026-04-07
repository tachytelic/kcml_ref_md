# LIST L

> Resolves the program and reports syntax errors and unmatched loop structures.

## Syntax

```
LIST [title] L
```

## Description

`LIST L` first resolves the program to catch syntax errors, then checks for structural problems:

- `FOR ... NEXT` — checks each FOR has a NEXT (and vice versa); index variable is not checked
- `REPEAT ... UNTIL` — checks pairing
- `WHILE ... WEND` — checks pairing
- `DO ... END DO` — checks pairing

Lines starting with `ERROR` must be fixed before the program can run. Lines starting with `WARNING` may cause runtime problems.

## Example output

```
LIST L
WARNING: line 00020 statement 2 possible NEXT BREAK
ERROR:   line 00021 statement 1 P31 Incomplete DO group
ERROR:   line 00020 statement 2 P31 Incomplete loop
WARNING: line 00010 statement 1 FOR without NEXT
```

- Line 20 statement 2: `BREAK` inside a `WHILE ... WEND` which is inside a `FOR ... NEXT`
- Line 21: `END DO` without a matching `DO`
- Line 20: `REPEAT` or `WHILE` without matching `UNTIL`/`WEND`
- Line 10: `FOR` without a matching `NEXT`

## See Also

- `LIST` — list program source
- `BREAK` — exit a loop
- `CONTINUE` — skip to next iteration
