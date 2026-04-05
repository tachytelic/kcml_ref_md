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

### R7_DATE2J / R7_J2DATE (Legacy)

Legacy CALL functions using `DD/MM/YY` format. Still available for backward compatibility.

```kcml
REM DD/MM/YY to Julian
DIM julian
: CALL R7_DATE2J "04/04/26" TO julian
: PRINT julian
: $END
```
Output: `2461135`

```kcml
REM Julian to DD/MM/CCYY
DIM date$12
: CALL R7_J2DATE 2461135, 10 TO date$
: PRINT date$
: $END
```
Output: `04/04/2026`

Note: The second parameter to R7_J2DATE is the output width (8 for DD/MM/YY, 10 for DD/MM/CCYY).

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

## Century Handling (R7_DATE2J)

For legacy R7_DATE2J with 2-digit years, byte 48 of `$OPTIONS RUN` controls the century cutoff:
- If YY < cutoff value → 2000s
- If YY >= cutoff value → 1900s
- Default cutoff: HEX(20) = 32 (so 00-31 → 2000s, 32-99 → 1900s)

```kcml
REM Change cutoff to 1950 (00-49 → 2000s, 50-99 → 1900s)
STR($OPTIONS RUN, 48, 1) = HEX(32)
```
