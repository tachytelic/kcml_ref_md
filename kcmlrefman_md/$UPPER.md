# $UPPER(

> Converts an alpha string to uppercase.

## Syntax

```
alpha_receiver = $UPPER(alpha_expression)
```

## Description

`$UPPER(` translates every character in the alpha expression to its uppercase equivalent and stores the result in the receiver variable. Non-alphabetic characters (digits, punctuation, spaces) are passed through unchanged.

On Unicode systems the translation covers all Unicode characters that have case. On older non-Unicode systems the codepage is controlled by byte 50 of `$OPTIONS RUN`:

| Byte value | Codepage |
|------------|----------|
| `HEX(00)` | US ASCII 7-bit (default) |
| `HEX(01)` | ISO Latin-1 (Western European) |
| `HEX(02)` | User-defined (set via `$UPPER() = table$`) |

### Advanced forms

```
alpha_receiver = $UPPER()       REM Extract current translation table
$UPPER() = alpha_expr           REM Set a user-defined 256-byte translation table
```

## Examples

### Example 1 — Basic uppercase
```kcml
01000 REM Basic $UPPER usage
: DIM s$50, r$50
: s$ = "Hello World"
: r$ = $UPPER(s$)
: PRINT "Upper: " ; RTRIM(r$)
: $END
```
**Output:**
```
Upper: HELLO WORLD
```

### Example 2 — Mixed alphanumeric — digits and symbols unchanged
```kcml
01000 REM Numbers and symbols pass through unchanged
: DIM s$50, r$50
: s$ = "abc123XYZ"
: r$ = $UPPER(s$)
: PRINT "Original: " ; RTRIM(s$)
: PRINT "Upper: " ; RTRIM(r$)
: $END
```
**Output:**
```
Original: abc123XYZ
Upper: ABC123XYZ
```

### Example 3 — Case-insensitive comparison pattern
```kcml
01000 REM Normalise input before comparing
: DIM input$30, norm$30
: input$ = "yes"
: norm$ = $UPPER(input$)
: IF RTRIM(norm$) == "YES" THEN PRINT "Confirmed"
: IF RTRIM(norm$) <> "YES" THEN PRINT "Not confirmed"
: $END
```
**Output:**
```
Confirmed
```

## Notes

- `$UPPER(` does **not** modify the source variable — it returns a new value into the receiver.
- Cannot be nested directly inside other functions (e.g. `RTRIM($UPPER(s$))` causes a syntax error). Assign to an intermediate variable first.
- Added in KCML 5.0. User-defined tables and `$UPPER()` forms added in KCML 6.00. Unicode support in KCML 6.20.

## See also

[$LOWER(]($LOWER.md)
