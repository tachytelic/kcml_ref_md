# #TIME

> Returns the number of seconds since midnight (local time).

## Syntax

```
#TIME
```

## Description

Returns a numeric value representing the number of seconds elapsed since midnight, local time. Returns a value between 0 and 86399.

Commonly used with form controls (DBEdit, KCML Grid) that accept a time value via the `Type$ = "T"` property.

## Examples

```kcml
DIM secs
secs = #TIME
PRINT secs         : REM  e.g. 50400 for 14:00:00
```

```kcml
REM Initialise a DBEdit control to the current time
.KCMLDBEdit1.Type$ = "T"
.KCMLDBEdit1.Text$ = #TIME
```

```kcml
REM Simple elapsed-time measurement
DIM t_start, t_end
t_start = #TIME
REM ... some work ...
t_end = #TIME
PRINT "Elapsed: "; t_end - t_start; " seconds"
```

```kcml
REM Convert to HH:MM:SS
DIM secs, h, m, s, ts$8
secs = #TIME
h = INT(secs / 3600)
m = INT((secs - h * 3600) / 60)
s = secs - h * 3600 - m * 60
PRINT h; ":"; m; ":"; s
```

## Notes

- Returns an integer number of seconds; sub-second precision is not available via `#TIME`.
- At midnight the value resets to 0 — elapsed-time calculations that span midnight will give negative results.
- `#DATE` returns the current date as a Julian day number; the two can be combined for a full date-time value.
- `TIME` (string function) returns the time as a `HHMMSS` string.

## See Also

- `#DATE` — current date as Julian day number
- `TIME` — current time as `HHMMSS` string
- `CONVERT DATE` — convert Julian to/from display format
