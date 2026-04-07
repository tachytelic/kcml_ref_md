# Julian Dates

> Reference article explaining how KCML represents and converts dates as Julian day numbers.

## Description

Julian dates are day numbers counted from a standard epoch (1200 GMT on January 1, 4716 BCE in the proleptic Julian calendar). This standard is widely used in astronomy and sciences because:

- Date arithmetic (days between two dates) is a simple subtraction.
- The day of the week (Monday = 0) is `julian_date MOD 7`.
- No need to account for leap years or varying month lengths.

**KCML's Julian implementation** differs slightly from the astronomical definition:
- Counts from **midnight** (not noon at 1200 GMT).
- Uses **local timezone** rather than GMT. The timezone offset is in bytes 43–44 of `$MACHINE`.

## Usage in KCML

Julian dates are used by the KCML database **DATE** data type, stored as a 3-byte integer (`B3` format).

Convert between ISO date strings and Julian numbers with `CONVERT DATE`:

```kcml
: DIM julian, date$12
: CONVERT DATE "2026-04-07" TO julian
: PRINT "2026-04-07 = julian "; julian
: CONVERT DATE julian TO date$
: PRINT "julian back = "; date$
: $END
```

Output:
```
2026-04-07 = julian  2461138
julian back = 2026-04-07
```

## Microsoft date compatibility

Microsoft applications (VBA, Excel, Access) count days from 0 = 1899-12-30. To convert:

```kcml
CONVERT DATE Vbdate + 2415019 TO VBdate$
```

Note: Excel for Macintosh uses a 1904-based scheme — a different offset applies.

## Day-of-week calculation

```kcml
DIM julian, dow
CONVERT DATE "2026-04-07" TO julian
dow = julian MOD 7       REM 0=Monday, 1=Tuesday, ..., 6=Sunday
PRINT "Day of week: "; dow
```

## Use with form controls

The KCML Edit control with `.Type$="D"` receives and displays dates as Julian values:

```kcml
DIM idate$12, jdate
CONVERT DATE "2026-04-07" TO jdate
.editDate.Type$ = "D"
.editDate.Text$ = jdate
```

## Notes

- KCML Julian dates differ from astronomical Julian dates by ½ day (midnight vs. noon).
- Timezone is local — byte 43–44 of `$MACHINE` gives the UTC offset.
- The `#DATE` function returns the current date in YYMMDD format, not Julian. Use `CONVERT DATE` to get the Julian equivalent.

## See Also

- `CONVERT DATE` — convert between ISO date strings and Julian day numbers
- `CONVERT TIME` — convert between time strings and seconds
- `DATE` — current date as YYMMDD string
- `#DATE` — current date function
- `$MACHINE` — system information bytes
