# #DATE

> Returns today's date as a Julian day number.

## Syntax

```
#DATE
```

## Description

Returns the current date as a Julian value — a day number counted from a standard epoch date in 4716BCE. This is the format used by the KCML database `DATE` data type (stored as a 3-byte integer, `B3` format).

Julian dates are compatible with Microsoft application date types (VB, Excel, Access).

## Examples

```kcml
DIM today
today = #DATE
PRINT today           : REM  e.g.  2461138 (for 2026-04-07)
```

```kcml
REM Initialise a DBEdit control to today's date
.KCMLDBEdit1.Type$ = "D"
.KCMLDBEdit1.Text$ = #DATE
```

```kcml
REM Date arithmetic
DIM due
due = #DATE + 30    : REM  30 days from today
```

## Notes

- Use `CONVERT DATE` to convert between Julian dates and display strings.
- See `JulianDate` for the Julian date format and conversion examples.
- `DATE` (string function) returns date as `YYYYMMDD` text; `#DATE` returns a numeric Julian value.

## See Also

- `JulianDate` — Julian date format and arithmetic
- `CONVERT DATE` — convert Julian to/from display format
- `DATE` — current date as `YYYYMMDD` string
- `#TIME` — seconds since midnight
