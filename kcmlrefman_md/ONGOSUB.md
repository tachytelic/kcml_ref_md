# ON … GOSUB / ON … GOTO

> Computed branch — selects a target from a list based on a numeric value.

## Syntax

```
ON expr GOSUB line1 [, line2 ...]
ON expr GOTO  line1 [, line2 ...]
```

## Description

Evaluates `expr` (must be a positive integer 1, 2, 3, …). Uses the result as a 1-based index into the comma-separated list of line numbers.

- **`ON … GOTO`** — jumps unconditionally to the selected line.
- **`ON … GOSUB`** — calls the selected line as a subroutine; execution returns after the corresponding `RETURN`.

If `expr` is 0, negative, or greater than the number of targets, the statement is skipped (no branch).

## Examples

```kcml
DIM choice
choice = 2
ON choice GOSUB 1000, 2000, 3000
PRINT "Back from subroutine"
$END

1000 PRINT "Option 1" : RETURN
2000 PRINT "Option 2" : RETURN
3000 PRINT "Option 3" : RETURN
```

Output:
```
Option 2
Back from subroutine
```

```kcml
DIM day
day = 3
ON day GOTO 100, 200, 300, 400, 500, 600, 700
100 PRINT "Monday"    : GOTO 999
200 PRINT "Tuesday"   : GOTO 999
300 PRINT "Wednesday" : GOTO 999
999 $END
```

## Notes

- Legacy statement — prefer `IF/END IF` blocks or `SELECT CASE` in new code.
- Out-of-range `expr` (0 or > list count) causes the entire `ON` statement to be skipped — not an error.
- For label-based dispatch see `GOSUB'`.

## See Also

- `GOSUB` — unconditional subroutine call (line number)
- `GOSUBquote` — label-based subroutine call
- `GOTO` — unconditional branch
- `ON … SELECT` — conditional SELECT based on numeric value
