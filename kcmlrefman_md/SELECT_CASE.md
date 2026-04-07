# SELECT CASE

> Multi-way conditional — compares an expression against a series of CASE values.

## Syntax

```
SELECT CASE expr
CASE value1 [, value1a ...]
  statements
CASE value2
  statements
CASE ELSE
  statements
END SELECT
```

## Description

Evaluates `expr` once, then compares it against each `CASE` expression in order. When a match is found, the statements in that case execute, then control jumps to the statement after `END SELECT`.

- `CASE ELSE` is optional but acts as a catch-all; it must be the last `CASE` before `END SELECT`.
- A single `CASE` can list multiple comma-separated values.
- `expr` and `CASE` expressions must be the same type (numeric or string).
- Boolean expressions are numeric (TRUE=1, FALSE=0).
- Directly executing a `CASE` statement (e.g. via `GOTO`) transfers control to after `END SELECT`.

## Examples

```kcml
DIM status
status = 2
SELECT CASE status
CASE 1
  PRINT "Active"
CASE 2, 3
  PRINT "Suspended or Closed"
CASE ELSE
  PRINT "Unknown"
END SELECT
```

Output:
```
Suspended or Closed
```

```kcml
REM String case
DIM code$4
code$ = "ERR"
SELECT CASE TRIM(code$)
CASE "OK"
  PRINT "Success"
CASE "ERR", "FAIL"
  PRINT "Error"
CASE ELSE
  PRINT "Unknown code: "; TRIM(code$)
END SELECT
```

```kcml
REM Multiple values in one CASE
SELECT CASE day
CASE 1, 7
  PRINT "Weekend"
CASE 2, 3, 4, 5, 6
  PRINT "Weekday"
END SELECT
```

## Notes

- Unlike some languages, KCML `SELECT CASE` does **not** fall through — only the first matching case executes.
- Prefer `SELECT CASE` over long `IF/END IF` chains for readability.
- See also `SELECT` (the device-selection statement) — different from `SELECT CASE`.

## See Also

- `IF / END IF` — structured conditional
- `ON … GOSUB` — computed branch by index
- `SELECT` — device/parameter selection (different statement)
