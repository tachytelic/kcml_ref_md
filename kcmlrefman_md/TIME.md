# TIME

> Returns the current system time as an 8-character string.

## Syntax

```
time$ = TIME
```

## Description

Returns the current local system time as an 8-byte string in the format `HHMMSScc` (hours, minutes, seconds, centiseconds). Accuracy depends on the OS — may be accurate only to seconds on some systems.

Returns a string (not a number) — store in an alpha variable.

## Examples

```kcml
DIM current$8
current$ = TIME
PRINT current$        : REM  e.g.  14302567  (14:30:25.67)
```

```kcml
REM Combine date and time for a timestamp
DIM stamp$16
stamp$ = DATE & TIME
PRINT stamp$          : REM  e.g.  20260407143025
```

```kcml
REM Extract hours and minutes
DIM t$8
t$ = TIME
PRINT STR(t$, 1, 2)   : REM  hours (HH)
PRINT STR(t$, 3, 2)   : REM  minutes (MM)
PRINT STR(t$, 5, 2)   : REM  seconds (SS)
```

## Notes

- Returns **local time**, not GMT.
- Format is always `HHMMSScc` — no delimiters.
- For higher-level time operations, see `$TIME` and `CONVERT #TIME`.
- `DATE & TIME` gives a 16-byte date+time concatenation.

## See Also

- `DATE` — current date as 8-byte string (`YYYYMMDD`)
- `$TIME` — system time variable
- `CONVERT #TIME` — convert time to formatted string
- `JulianDate` — date arithmetic
