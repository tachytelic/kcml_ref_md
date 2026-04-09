# $LOWER(

> Converts an alpha string to lowercase.

## Syntax

```
alpha_receiver = $LOWER(alpha_expression)
```

## Description

`$LOWER(` translates every character in the alpha expression to its lowercase equivalent and stores the result in the receiver variable. Non-alphabetic characters (digits, punctuation, spaces) are passed through unchanged.

On Unicode systems the translation covers all Unicode characters that have case. On older non-Unicode systems the codepage is controlled by byte 50 of `$OPTIONS RUN`:

| Byte value | Codepage |
|------------|----------|
| `HEX(00)` | US ASCII 7-bit (default) |
| `HEX(01)` | ISO Latin-1 (Western European) |
| `HEX(02)` | User-defined (set via `$LOWER() = table$`) |

### Advanced forms

```
alpha_receiver = $LOWER()       REM Extract current translation table
$LOWER() = alpha_expr           REM Set a user-defined 256-byte translation table
```

## Examples

### Example 1 — Basic lowercase
```kcml
01000 REM Basic $LOWER usage
: DIM s$50, r$50
: s$ = "Hello World"
: r$ = $LOWER(s$)
: PRINT "Lower: " ; RTRIM(r$)
: $END
```
**Output:**
```
Lower: hello world
```

### Example 2 — Mixed alphanumeric
```kcml
01000 REM Numbers and symbols pass through unchanged
: DIM s$50, r$50
: s$ = "abc123XYZ"
: r$ = $LOWER(s$)
: PRINT "Original: " ; RTRIM(s$)
: PRINT "Lower: " ; RTRIM(r$)
: $END
```
**Output:**
```
Original: abc123XYZ
Lower: abc123xyz
```

### Example 3 — Normalise before storing
```kcml
01000 REM Normalise a product code to lowercase for storage
: DIM code$20, stored$20
: code$ = "PROD-ABC-001"
: stored$ = $LOWER(code$)
: PRINT "Stored as: " ; RTRIM(stored$)
: $END
```
**Output:**
```
Stored as: prod-abc-001
```

## Notes

- `$LOWER(` does **not** modify the source variable — it returns a new value into the receiver.
- Cannot be nested directly inside other functions (e.g. `RTRIM($LOWER(s$))` causes a syntax error). Assign to an intermediate variable first.
- Added in KCML 5.0. User-defined tables and `$LOWER()` forms added in KCML 6.00. Unicode support in KCML 6.20.

## See also

[$UPPER(]($UPPER.md)
