# SELECT ON ALARM GOSUB

> Traps timeout errors from `$ALARM` and calls a subroutine handler.

## Syntax

```
SELECT ON ALARM GOSUB label
SELECT ON ALARM GOSUB 'subroutine_name
```

## Description

When a timeout error (`I92`) triggered by `$ALARM` is detected, KCML calls the specified subroutine. On `RETURN` from the handler, execution resumes with the statement following the timed-out statement.

An optional `LIST "/path"` or similar can be combined on the same `SELECT`.

## Examples

```kcml
SELECT ON ALARM GOSUB 9010
$ALARM 30              : REM  set 30-second timeout
LINPUT "Enter name: ", name$
$ALARM 0               : REM  cancel alarm
$END

9010 PRINT "Timeout — using default"
     name$ = "Unknown"
     RETURN
```

```kcml
SELECT ON ALARM GOSUB 'alarm_trap
SELECT ON ALARM GOSUB 'test, LIST "/tmp/fred"
```

## Notes

- The alarm timeout is set with `$ALARM`.
- The handler receives control when any blocking statement (LINPUT, KEYIN, etc.) times out.
- On return from the handler, execution continues after the timed-out statement.

## See Also

- `$ALARM` — set a timeout
- `SELECT ON ALERT` — handle ALERT signals
- `SELECT` — overview
