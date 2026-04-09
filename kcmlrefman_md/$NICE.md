# $NICE(

> Gets or sets the Unix process scheduling priority (nice factor).

## Syntax

```
numeric_receiver = $NICE(numeric_expression)
```

## Description

`$NICE(` interacts with the Unix process scheduling priority (the "nice" value). Higher nice values mean lower priority — the process yields CPU time more readily to other processes.

| Value | Meaning |
|-------|---------|
| 20 | Default KCML priority |
| 21–40 | Lower than normal (more "nice" to other processes) |
| 1–19 | Higher than normal (requires superuser) |
| 0 | Query current nice value without changing it |

**If `$NICE(` fails, it returns `-1`.**

Passing `0` returns the current nice value without changing it.

Only the superuser (root) can decrease the nice factor (raise priority). Regular users can only increase it.

Child processes inherit the nice factor of their parent.

> **Note:** This function is ignored on Windows versions of KCML.

## Examples

### Example 1 — Query current nice value
```kcml
01000 REM Get current process priority
: DIM n
: n = $NICE(0)
: PRINT "Current nice value: " ; n
: $END
```
**Output:**
```
Current nice value:  20
```

### Example 2 — Lower priority for a background job
```kcml
01000 REM Reduce priority for a long-running batch process
: DIM old_nice, new_nice
: old_nice = $NICE(0)
: PRINT "Priority before: " ; old_nice
: new_nice = $NICE(5)
: PRINT "Priority after raising nice by 5: " ; $NICE(0)
: $END
```

### Example 3 — Check for failure
```kcml
01000 REM Handle $NICE failure gracefully
: DIM result
: result = $NICE(10)
: IF result == -1 THEN PRINT "Failed to set nice value"
: IF result <> -1 THEN PRINT "Nice set, was: " ; result
: $END
```

## Notes

- Only useful on Unix/Linux KCML — silently ignored on Windows.
- You can only increase the nice value (lower priority) unless running as root.
- Useful in batch reporting or background data-import programs to avoid impacting interactive users on the same system.
