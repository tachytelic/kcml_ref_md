# Date and Time Functions in KCML

> Overview of date, time, timestamp, and timezone handling in KCML.

## Date representation

| Form | Function/Variable | Format |
|------|------------------|--------|
| Julian day number (numeric) | `#DATE` | Integer (e.g. 2461138 for 2026-04-07) |
| ISO-8601 date string | `CONVERT DATE` | `YYYY-MM-DD` |
| Date as YYYYMMDD | `$TODAY` | `"20260407"` |
| Date as YYMMDD (deprecated) | `DATE` | `"260407"` |

All date functions use **local time**.

## Time representation

| Form | Function | Format |
|------|---------|--------|
| Seconds since midnight (numeric) | `#TIME` | Integer 0–86399 |
| ISO-8601 time string | `CONVERT TIME` | `HH:MM:SS` |
| Time as HHMMSS | `TIME` | `"140000"` |

All time functions use **local time**.

## Timestamps

`$TIMESTAMP` returns the current date and time as milliseconds since 0000 GMT year 0000 (one day before 1 Jan 0001) as a 6-byte unsigned binary string. This is **GMT** (UTC), not local time, on platforms that support timezones.

## Timezone information

Both Unix and Windows understand timezones and can hold system times in GMT with local time calculated from the timezone setting.

- **Unix**: Use the `TZ` environment variable in `.profile` to set the timezone per process.
- **Windows NT**: Set the timezone per user with a profile.
- **Windows 95/98**: Always operates on local time; does not distinguish GMT from local.

### Timezone offset in $MACHINE

Bytes 43–44 of `$MACHINE` contain the difference in minutes between local time and GMT, as a 2-byte signed integer.

- Negative = east of Greenwich
- Positive = west of Greenwich
- Includes daylight saving time bias

```kcml
DIM TZoffset
TZoffset = VAL(STR($MACHINE, 43), -2)
```

Examples:
- UK in summer (BST): `-60`
- UK in winter (GMT): `0`
- US Eastern in summer (EDT): `240`
- US Eastern in winter (EST): `300`

The timezone offset in `$MACHINE` is recalculated each time `TIME`, `DATE`, or `$TIME` is called.

## See Also

- `#DATE` — current date as Julian day number
- `#TIME` — current time as seconds since midnight
- `CONVERT DATE` — convert Julian to/from display format
- `CONVERT TIME` — convert seconds to HH:MM:SS
- `$TIMESTAMP` — millisecond timestamp (GMT)
- `$TODAY` — current date as YYYYMMDD string
- `$MACHINE` — system capability and configuration string
