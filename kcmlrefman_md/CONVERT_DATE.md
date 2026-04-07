# CONVERT DATE

> Converts between ISO-8601 date strings (`CCYY-MM-DD`) and Julian day numbers.

## Syntax

```
CONVERT DATE numeric_expression TO alpha_receiver
CONVERT DATE alpha_expression TO numeric_receiver
```

| Form | Direction |
|------|-----------|
| `CONVERT DATE numeric TO string` | Julian day number → `"CCYY-MM-DD"` string |
| `CONVERT DATE string TO numeric` | `"CCYY-MM-DD"` string → Julian day number |

## Description

`CONVERT DATE` converts between two date representations:

- **ISO-8601 string**: `"CCYY-MM-DD"` format (e.g. `"2024-03-15"`). The full 4-digit year is required; 2-digit abbreviation is not permitted.
- **Julian day number**: A numeric count of days (the same Julian date format used throughout KCML and in the KCML ODBC driver).

The ISO format used here (`CCYY-MM-DD`) is the same format used by the KCML ODBC driver.

## Examples

### String to Julian

```kcml
: DIM julian, s$20
: CONVERT DATE "2024-03-15" TO julian
: PRINT "julian="; julian
: $END
```

Output:
```
julian= 2460385
```

### Julian to string (round-trip)

```kcml
: DIM julian, s$20
: CONVERT DATE "2024-03-15" TO julian
: CONVERT DATE julian TO s$
: PRINT "back="; s$
: $END
```

Output:
```
back=2024-03-15
```

### Form control initialisation

```kcml
CONVERT DATE Idate$ TO JDate
.editControl1.Type$ = "D"
.editControl1.Text$ = JDate
```

The KCML form edit control with `.Type$="D"` stores dates as Julian numbers.

### Offset by days

```kcml
CONVERT DATE Vbdate + 2415019 TO VBdate$
```

## Notes

- Always use the full 4-digit year (`CCYY`); 2-digit years are not accepted.
- The `#DATE` system variable returns the current date as a Julian number, which can be converted to a string with `CONVERT DATE`.

## See Also

- `#DATE` — current date as a Julian number
- `DATE` — date arithmetic functions
- `CONVERT TIME` — convert between ISO time strings and seconds-since-midnight
- `CONVERT` — general string/numeric conversion
