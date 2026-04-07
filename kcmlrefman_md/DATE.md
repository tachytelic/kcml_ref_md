# DATE (function)

> Returns the current system date as a 6-character `"YYMMDD"` string.

## Syntax

```
DATE
```

Returns an alpha value — valid wherever an alpha expression is legal.

## Description

`DATE` returns the local system date formatted as `"YYMMDD"` (year, month, day — 2 digits each, no separators).

**Important:** `DATE` does not include century information. For century-aware date handling, use `$TODAY`, `#DATE`, or `CONVERT DATE` instead.

## Example

```kcml
: DIM d$10
: d$ = DATE
: PRINT "DATE="; d$
: $END
```

Output (run on 2026-04-07):
```
DATE=260407
```

### Combined with TIME

```kcml
now$ = DATE & TIME
```

## Notes

- Returns a 6-character string: `"YYMMDD"`. The year part is only 2 digits — use `$TODAY` for 4-digit year.
- Deprecated for new code; prefer `$TODAY` (returns `CCYYMMDD`) or `#DATE` (returns Julian day number).

## See Also

- `$TODAY` — today's date including century (`CCYYMMDD` format)
- `#DATE` — current date as a Julian day number
- `CONVERT DATE` — convert between ISO-8601 date strings and Julian numbers
- `TIME` — current time as `"HHMMSS"` string
- `$TIME` — current time with subsecond precision
