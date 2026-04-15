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
- The `#DATE` function returns the current date as a **Julian integer** directly — use `CONVERT DATE #DATE TO d$` to get an ISO string. (Note: `$TODAY` returns the YYYYMMDD string form.)

## R7_DATE2J / R7_J2DATE (broken in KCML 6.9+)

These legacy Rev7-era routines converted between `DD/MM/YY` strings and Julian integers. They are called with `CALL` and are **no longer functional in KCML 6.9** — the dispatch table contains the names but the underlying handler was removed. Calling them produces a runtime panic:

- `CALL R7_DATE2J date$, julian` → **S24.054**, exit 113
- `CALL R7_J2DATE julian, date$` → **S24.060**, exit 113

They were deprecated due to Y2K issues (2-digit year only). Debug binary analysis of KCML 7 confirms they were pure-arithmetic user functions (`uf_r7.c`) using an internal `GetJulianDate()` — they never called Unix date functions (`time()`, `localtime()`, etc.). strace confirms no OS date syscalls are made before the crash.

**Migration pattern** — replace `CALL R7_DATE2J oeh_date$, julian` with:

```kcml
REM oeh_date$ is DD/MM/YYYY (or "--/--/----" if blank)
DIM iso$12
: IF oeh_date$ <> "--/--/----" THEN DO
:   iso$ = STR(oeh_date$,7,4) & "-" & STR(oeh_date$,4,2) & "-" & STR(oeh_date$,1,2)
:   CONVERT DATE iso$ TO julian
: END DO
```

**Migration pattern** — replace `CALL R7_J2DATE julian, 10 TO date$` with:

```kcml
DIM iso$12
: CONVERT DATE julian TO iso$
: date$ = STR(iso$,9,2) & "/" & STR(iso$,6,2) & "/" & STR(iso$,1,4)
```

Both replacement patterns verified by execution on KCML 06.00.88.

## See Also

- `CONVERT DATE` — convert between ISO date strings and Julian day numbers
- `CONVERT TIME` — convert between time strings and seconds
- `$TODAY` — current date as YYYYMMDD string
- `#DATE` — current date as Julian integer
- `$MACHINE` — system information bytes
