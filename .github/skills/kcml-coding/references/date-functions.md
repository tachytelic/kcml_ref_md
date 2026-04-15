# KCML Date Functions

## Overview

KCML uses **Julian dates** internally - day numbers counted from January 1, 4716 BCE. This makes date arithmetic simple (just add/subtract integers).

## Key Functions

### CONVERT DATE (Recommended)

Modern built-in statement using ISO-8601 format (`YYYY-MM-DD`).

```kcml
REM String to Julian
DIM julian
: CONVERT DATE "2026-04-04" TO julian
: PRINT julian
: $END
```
Output: `2461135`

```kcml
REM Julian to String
DIM date$12
: CONVERT DATE 2461135 TO date$
: PRINT date$
: $END
```
Output: `2026-04-04`

```kcml
REM Round-trip: today as ISO string
DIM j, d$12
: j = #DATE
: CONVERT DATE j TO d$
: PRINT d$
: $END
```

```kcml
REM How many days between two dates?
DIM j1, j2, diff
: CONVERT DATE "2026-01-01" TO j1
: CONVERT DATE "2026-04-15" TO j2
: diff = j2 - j1
: PRINT diff               : REM 104
: $END
```
REM Verified by execution: result = 104

### R7_DATE2J / R7_J2DATE (Legacy — broken in KCML 6.9+)

`R7_DATE2J` and `R7_J2DATE` are **Kerridge-proprietary routines** from the Rev7/Wang BASIC-2 compatibility layer. They are called with `CALL`, introduced in KCML 3.00.

**Internal implementation (from debug binary analysis of KCML 7):**
- Implemented in `uf_r7.c` as KCML User Functions (UF), not as wrappers around Unix C library calls
- `R7_DATE2J` calls an internal `GetJulianDate(day, month, year)` function from `jdate.h` — pure arithmetic, no OS date syscalls (`time()`, `localtime()`, `mktime()` etc. are never called)
- `R7_J2DATE` uses internal `pnum()` formatting helpers to write day/month/year back to the output string
- strace confirms: no OS-level date/time syscalls occur before the crash

**Calling conventions and which forms crash in KCML 6.9:**

The S24 sub-code varies by calling convention — it is not a fixed code per function. Tested on KCML 06.00.88:

| Call form | Result |
|-----------|--------|
| `CALL R7_DATE2J date$ TO julian` | **Works** — returns correct Julian |
| `CALL R7_DATE2J date$, julian` | **S24.054** panic |
| `CALL R7_J2DATE julian, width TO date$` | **Works** — returns correct DD/MM/YY[YY] |
| `CALL R7_J2DATE julian TO date$` | **S24.053** panic |
| `CALL R7_J2DATE julian, date$` | **S24.060** panic |

The ERP global subroutine `unpack_date` uses a form without the `TO` clause, which causes **S24.062** at runtime. The crash is not the function being entirely absent — the `TO`-clause forms still function correctly — but calling convention mismatches with the removed handler variants panic.

**Why they were deprecated:** They only handle 2-digit years (`DD/MM/YY`), with century windowing controlled by `$OPTIONS RUN` byte 48. The default cutoff is HEX(20) = 32 (years 00–31 → 2000s, 32–99 → 1900s). This is inherently Y2K-unsafe for any date storage beyond 2031.

**R7_DATE2J** — converts `DD/MM/YY` (2-digit year, `TO` form only) to Julian integer:
```kcml
CALL R7_DATE2J date$ TO julian
```

**R7_J2DATE** — converts Julian integer to a date string (`TO` form with width only):
```kcml
CALL R7_J2DATE julian, 10 TO date$   : REM width 8=DD/MM/YY, 10=DD/MM/CCYY
```

#### Migration: replacing R7_DATE2J when upgrading to KCML 6.9

ERP date fields are typically stored as `DD/MM/YYYY` (10-char, 4-digit year). R7_DATE2J cannot handle this format anyway (it only accepts 2-digit years), so the correct replacement is to rearrange the string to ISO `YYYY-MM-DD` format and use `CONVERT DATE`.

Pattern verified from production code — handles the common ERP case where a blank/null date is stored as `--/--/----`:

```kcml
REM oeh_date$ is DD/MM/YYYY (e.g. "15/04/2026") or "--/--/----" if not set
REM Replaces: CALL R7_DATE2J oeh_date$ TO date_raised
DIM Date_Raised2$12, date_raised
: date_raised = 0
: IF oeh_date$ <> "--/--/----" THEN DO
:   STR(Date_Raised2$,,4)  = STR(oeh_date$, 7, 4)  : REM YYYY
:   STR(Date_Raised2$,5,1) = "-"
:   STR(Date_Raised2$,6,2) = STR(oeh_date$, 4, 2)  : REM MM
:   STR(Date_Raised2$,8,1) = "-"
:   STR(Date_Raised2$,9,2) = STR(oeh_date$,,2)      : REM DD
:   CONVERT DATE Date_Raised2$ TO date_raised
: END DO
```

`Date_Raised2$` ends up as `YYYY-MM-DD` which `CONVERT DATE` accepts directly. `date_raised` is left as 0 if the field was blank.

For the reverse direction (Julian to `DD/MM/YYYY`), replace `CALL R7_J2DATE j, 10 TO date$` with:

```kcml
REM Replaces: CALL R7_J2DATE julian, 10 TO date$
REM Produces DD/MM/YYYY from a Julian integer
DIM iso$12, date$12
: CONVERT DATE julian TO iso$              : REM -> YYYY-MM-DD
: date$ = STR(iso$,9,2) & "/" & STR(iso$,6,2) & "/" & STR(iso$,1,4)
```

## Comparison

| Function | Format | Type | Example |
|----------|--------|------|---------|
| `CONVERT DATE str TO num` | ISO `YYYY-MM-DD` | Statement | `CONVERT DATE "2026-04-04" TO j` |
| `CONVERT DATE num TO str` | ISO `YYYY-MM-DD` | Statement | `CONVERT DATE j TO d$` |
| `CALL R7_DATE2J str TO num` | `DD/MM/YY` | Call | `CALL R7_DATE2J "04/04/26" TO j` |
| `CALL R7_J2DATE num, width TO str` | `DD/MM/YY[YY]` | Call | `CALL R7_J2DATE j, 10 TO d$` |

## Getting Today's Date

```kcml
REM Method 1: $TODAY returns YYYYMMDD string
DIM today$8
: today$ = $TODAY
: PRINT "Today (YYYYMMDD): "; today$
: $END
```

```kcml
REM Method 2: #DATE returns Julian integer
DIM julian, iso$12
: julian = #DATE
: CONVERT DATE julian TO iso$
: PRINT "Today (ISO): "; iso$
: $END
```

```kcml
REM Extract year/month/day from $TODAY (YYYYMMDD)
DIM today$8, yr$4, mo$2, dy$2
: today$ = $TODAY
: yr$ = STR(today$, 1, 4)
: mo$ = STR(today$, 5, 2)
: dy$ = STR(today$, 7, 2)
: PRINT "Year="; yr$; " Month="; mo$; " Day="; dy$
: $END
```
<!-- UNTESTED -->

## Date Arithmetic

Julian dates make arithmetic trivial:

```kcml
DIM today, future$12, past$12
: today = #DATE
: CONVERT DATE today + 30 TO future$
: CONVERT DATE today - 7 TO past$
: PRINT "Today + 30 days: "; future$
: PRINT "Today - 7 days:  "; past$
: $END
```

```kcml
REM Is an invoice overdue? (due date vs today)
DIM due_julian, today_julian, days_late
: CONVERT DATE "2026-03-01" TO due_julian
: today_julian = #DATE
: days_late = today_julian - due_julian
: IF days_late > 0 THEN PRINT "Overdue by "; days_late; " days" ELSE PRINT "Not overdue"
: $END
```
<!-- UNTESTED -->

```kcml
REM Find the first day of next month
DIM j, d$12, yr$4, mo$2, nm$12
: j = #DATE
: CONVERT DATE j TO d$
: yr$ = STR(d$, 1, 4)
: mo$ = STR(d$, 6, 2)
: DIM m
: m = VAL(mo$) + 1
: DIM nm_s$10
: IF m > 12 THEN m = 1 : DIM y : y = VAL(yr$) + 1 : CONVERT y TO yr$,(####)
: CONVERT m TO mo$,(##) : IF STR(mo$,1,1) == " " THEN STR(mo$,1,1) = "0"
: nm$ = yr$ & "-" & mo$ & "-01"
: PRINT nm$
: $END
```
<!-- UNTESTED -->

## Day of Week

```kcml
DIM julian, dow, days$(7,10)
: MAT READ days$()
: DATA "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
: julian = #DATE
: dow = MOD(julian, 7) + 1
: PRINT "Today is: "; days$(dow)
: $END
```

```kcml
REM Is a given date a weekday? (1=Mon ... 5=Fri are weekdays)
DIM j, dow
: CONVERT DATE "2026-04-07" TO j
: dow = MOD(j, 7) + 1          : REM 1=Mon, 7=Sun
: IF dow <= 5 THEN PRINT "Weekday" ELSE PRINT "Weekend"
: $END
```
<!-- UNTESTED -->

```kcml
REM Day-of-week for an ISO date string
DIM j, d, days$(7,10)
: MAT READ days$()
: DATA "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
: CONVERT DATE "2026-04-06" TO j
: d = MOD(j, 7) + 1
: PRINT RTRIM(days$(d))        : REM "Monday"
: $END
```
<!-- UNTESTED -->

## Microsoft Excel/VBA Conversion

To convert between KCML Julian and Microsoft dates (Excel, VBA, Access):

```kcml
REM Microsoft date to Julian: add 2415019
DIM ms_date, julian
: ms_date = 46120  : REM Excel date for 2026-04-04
: julian = ms_date + 2415019
: PRINT "Julian: "; julian
: $END

REM Julian to Microsoft date: subtract 2415019
DIM julian, ms_date
: julian = 2461135
: ms_date = julian - 2415019
: PRINT "Excel date: "; ms_date
: $END
```

## Getting the Current Time

Use `#TIME` (integer) and `CONVERT TIME` — do NOT use `$TIME` for display.

```kcml
: DIM t, t$10
: t = #TIME
: CONVERT TIME t TO t$
: PRINT "Time: "; t$
: $END
```
Output: `Time: 09:41:47`

- `#TIME` returns seconds since midnight as an integer
- `CONVERT TIME integer TO string$` formats as `HH:MM:SS`
- `$TIME` returns a 4-byte packed binary value — looks like garbage when printed, do not use for display

This mirrors `#DATE` / `CONVERT DATE` exactly.

```kcml
REM Timestamp for a log entry: "2026-04-07 09:41:47"
DIM ts$20, d$12, t$10
: CONVERT DATE #DATE TO d$
: CONVERT TIME #TIME TO t$
: ts$ = RTRIM(d$) & " " & RTRIM(t$)
: PRINT ts$
: $END
```
<!-- UNTESTED -->

```kcml
REM Extract hours and minutes from #TIME
DIM t, hrs, mins
: t = #TIME
: hrs  = INT(t / 3600)
: mins = INT(MOD(t, 3600) / 60)
: PRINT "Hour="; hrs; " Min="; mins
: $END
```
<!-- UNTESTED -->

---

## Century Handling (R7_DATE2J — KCML 6 only)

Applicable only when R7_DATE2J is still in use (KCML 6 and earlier). In KCML 6.9+ this function is unavailable — see the migration pattern above instead.

For legacy R7_DATE2J with 2-digit years, byte 48 of `$OPTIONS RUN` controls the century cutoff:
- If YY < cutoff value → 2000s
- If YY >= cutoff value → 1900s
- Default cutoff: HEX(20) = 32 (so 00–31 → 2000s, 32–99 → 1900s)

```kcml
REM Change cutoff to 1950 (00-49 -> 2000s, 50-99 -> 1900s)
STR($OPTIONS RUN, 48, 1) = HEX(32)
```
