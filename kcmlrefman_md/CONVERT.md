# CONVERT

> Converts between string and numeric representations, with optional picture-format control for the numeric-to-string direction.

## Syntax

```
CONVERT alpha_variable TO numeric_receiver
CONVERT numeric_expression TO alpha_receiver, (picture)
```

| Element | Description |
|---------|-------------|
| `alpha_variable` | A string containing a valid ASCII number |
| `numeric_receiver` | A numeric variable to receive the parsed value |
| `numeric_expression` | A numeric value to format |
| `alpha_receiver` | A string variable to receive the formatted result |
| `picture` | A format string in parentheses controlling the output layout |

## Description

### Form 1: String to number

Parses a string containing an ASCII number and stores the result in a numeric variable. The string must contain a valid number; if it does not, a recoverable error occurs.

```kcml
CONVERT total$ TO new_total
CONVERT STR(actual$, 4, 6) TO new_number
```

### Form 2: Number to string with picture

Converts a numeric expression to a formatted string. The picture string controls the exact layout.

#### Picture format rules

| Picture character | Effect |
|------------------|--------|
| `#` | One digit position |
| `.` | Decimal point |
| `,` | Thousands separator |
| `$` | Dollar sign (or currency) at that position |
| `-` (leading/trailing) | Show `-` for negatives, space for positives |
| `+` (leading/trailing) | Show real sign for all values |
| `--` (trailing) | Append `DB` for negatives, spaces for positives |
| `++` (trailing) | Append `CR` for negatives, spaces for positives |
| `^^^^` | Exponential format (`E+nn`) |

If no sign character is given, the absolute value is used with no sign.

## Examples

### Number to string

```kcml
: DIM s$20, n
: CONVERT 159.9 TO s$,(###.##)
: PRINT s$
: CONVERT -42.5 TO s$,(-###.##)
: PRINT s$
: CONVERT 1234567 TO s$,(#,###,###)
: PRINT s$
: $END
```

Output:
```
159.90
-042.50
1,234,567
```

### String to number

```kcml
: DIM s$20, n
: s$ = "3.14"
: CONVERT s$ TO n
: PRINT "n="; n
: $END
```

Output:
```
n= 3.14
```

### Accounting format (debit/credit)

```kcml
CONVERT old TO balance$, ($###,###.###--)
```

Shows `DB` for negative values; `  ` (two spaces) for positives.

### Using a field variable target

```kcml
CONVERT old TO FLD(record$.entry$), (picture1$)
```

## Notes

- The picture string is enclosed in parentheses, not quotes: `(###.##)` not `"###.##"`.
- `CONVERT` with no picture uses the string's exact contents and requires a valid number; for more lenient parsing see `CNUM(`.
- Exponential format requires exactly four `^` characters: `#.##^^^^`.

## See Also

- `CNUM(` — lenient string-to-number function (stops at first non-numeric char)
- `CONVERT DATE` — convert between ISO date strings and Julian day numbers
- `CONVERT TIME` — convert between ISO time strings and seconds-since-midnight
- `STR(` — string extraction
