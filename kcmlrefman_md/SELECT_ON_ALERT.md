# SELECT ON ALERT / SELECT OFF ALERT

> Enables or disables the ALERT interrupt handler.

## Syntax

```
SELECT ON ALERT GOSUB label
SELECT OFF ALERT
```

## Description

`SELECT ON ALERT GOSUB label` — when an `$ALERT` signal is received, the program branches to the specified subroutine.

`SELECT OFF ALERT` — disables the ALERT interrupt handler.

**Processed at resolve time only** — only the first `SELECT ON ALERT` in the program takes effect.

### Unix UID requirement

For a process to receive an `$ALERT` signal, the effective UID of both the foreground and global processes must be the same. On some Unix variants (SCO, Unix 5.4), this requires setting the SUID bit on the KCML executable.

## Examples

```kcml
SELECT ON ALERT GOSUB 9000
REM  ... program runs, can receive ALERT signals ...
$END

9000 PRINT "Alert received"
     RETURN
```

```kcml
ON test SELECT OFF ALERT, SELECT PRINT /005
```

## Notes

- Only the **first** `SELECT ON ALERT` in the program is active (processed at resolve time).
- `SELECT OFF ALERT` can be toggled at runtime.

## See Also

- `$ALERT` — send an alert signal
- `SELECT ON ALARM GOSUB` — timeout handler
- `SELECT` — overview
