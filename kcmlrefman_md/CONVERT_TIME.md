# CONVERT TIME

> Converts between ISO time strings (`HH:MM:SS`) and KCML time values (seconds since midnight).

## Syntax

```
CONVERT TIME numeric_expression TO alpha_receiver
CONVERT TIME alpha_expression TO numeric_receiver
```

| Form | Direction |
|------|-----------|
| `CONVERT TIME numeric TO string` | Seconds-since-midnight → `"HH:MM:SS"` string |
| `CONVERT TIME string TO numeric` | `"HH:MM:SS"` string → seconds-since-midnight |

## Description

`CONVERT TIME` converts between two time representations:

- **ISO time string**: `"HH:MM:SS"` format (e.g. `"09:30:00"`)
- **KCML time value**: A count of seconds since midnight (local time). This is the format used by the KCML database `TIME` data type, which stores the value as a 4-byte integer (`B4` format).

Valid time values are 0–86399 (00:00:00 to 23:59:59). A value of −1 represents NULL and converts to a blank string; a blank string converts to −1.

## Examples

### String to seconds

```kcml
: DIM itime, s$20
: CONVERT TIME "09:30:00" TO itime
: PRINT "secs="; itime
: $END
```

Output:
```
secs= 34200
```

(9 × 3600 + 30 × 60 = 34200)

### Seconds to string (round-trip)

```kcml
: DIM itime, s$20
: CONVERT TIME "09:30:00" TO itime
: CONVERT TIME itime TO s$
: PRINT "back="; s$
: $END
```

Output:
```
back=09:30:00
```

### Form control initialisation

```kcml
CONVERT TIME Itime$ TO itime
.editControl1.Type$ = "T"
.editControl1.Text$ = itime
```

The KCML form edit control with `.Type$="T"` stores times as seconds-since-midnight.

## Notes

- Values outside 0–86399 cause an X71 error.
- −1 is treated as NULL (converts to blank string and vice versa); this means time differences are limited to a maximum of +23:59:59.
- `#TIME` returns the current time as seconds since midnight.

## See Also

- `#TIME` — current time as seconds since midnight
- `TIME` — time arithmetic
- `CONVERT DATE` — convert between ISO date strings and Julian day numbers
- `CONVERT` — general string/numeric conversion
