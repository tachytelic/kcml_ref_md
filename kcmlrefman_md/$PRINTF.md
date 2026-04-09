# $PRINTF(

> Formats a string using C-style printf format specifiers.

## Syntax

```
alpha_receiver = $PRINTF(format$, arg1 [, arg2 ...])
```

## Description

`$PRINTF(` formats one or more arguments into a string using C-style `printf` format specifiers. It is used primarily in socket and stream programming where KCML stream names must be constructed dynamically, but is also useful as a general-purpose string formatter.

### Supported format specifiers

| Specifier | Meaning | Example |
|-----------|---------|---------|
| `%d` | Decimal integer | `%d` → `42` |
| `%s` | String | `%s` → `hello` |
| `%f` | Floating-point | `%f` → `3.141590` |
| `%.Nf` | Float with N decimal places | `%.2f` → `3.14` |
| `%Ns` | String right-padded to width N | `%10s` → `        hi` |
| `%-Ns` | String left-padded to width N | `%-10s` → `hi        ` |

Multiple `%` placeholders can appear in a single format string. Not all C printf specifiers are supported — in particular, `%e` (scientific), `%x`/`%X` (hex with zero-padding), and flag characters like `+` and `0` may not behave as expected.

### Stream naming use case

The primary documented use of `$PRINTF(` is in socket programming, to construct the file name for `OPEN #` when promoting a connection socket to a message socket:

```kcml
OPEN #MsgStream, $PRINTF("#%d", ConnectStream), "@"
```

This builds the string `#5` (or whichever stream number) to pass to `OPEN`.

## Examples

### Example 1 — Basic integer and string formatting
```kcml
01000 REM Basic $PRINTF( usage
: DIM r$50
: r$ = $PRINTF("Value: %d", 42)
: PRINT RTRIM(r$)
: r$ = $PRINTF("Name: %s", "World")
: PRINT RTRIM(r$)
: r$ = $PRINTF("Float: %.2f", 3.14159)
: PRINT RTRIM(r$)
: $END
```
**Output:**
```
Value: 42
Name: World
Float: 3.14
```

### Example 2 — String alignment
```kcml
01000 REM String width alignment
: DIM r$30
: r$ = $PRINTF("[%10s]", "hi")
: PRINT RTRIM(r$)
: r$ = $PRINTF("[%-10s]", "hi")
: PRINT RTRIM(r$)
: $END
```
**Output:**
```
[        hi]
[hi        ]
```

### Example 3 — Multiple arguments
```kcml
01000 REM Format multiple values into one string
: DIM r$60
: r$ = $PRINTF("%d + %d = %d", 3, 4, 7)
: PRINT RTRIM(r$)
: r$ = $PRINTF("Pi to 4 dp: %.4f", 3.14159)
: PRINT RTRIM(r$)
: $END
```
**Output:**
```
3 + 4 = 7
Pi to 4 dp: 3.1416
```

### Example 4 — JSON output using ^ placeholder and $TRAN (verified pattern)

`$PRINTF` supports `\n` in format strings, producing a real newline character. Combined with a placeholder character for double-quotes and a single `$TRAN` pass at the end, this gives readable JSON-building code without the `q$` variable juggling of the old approach.

**Why not use a `NL$` variable for newlines?** KCML's `PRINT` tracks the current column and wraps at ~80 characters. A `NL$` variable containing `HEX(0A)` resets the column counter correctly, but the wrap logic then inserts extra newlines mid-field in long output. `\n` inside a `$PRINTF` format string bypasses this — the newlines arrive pre-embedded in the string value and `PRINT` does not re-wrap them. Verified by execution.

**Why not `RTRIM` on string arguments?** `$PRINTF %s` uses the logical (content) length of a string, not the full DIM'd width. Trailing spaces are stripped automatically. Verified by execution.

**Inline `& $PRINTF(...)` works** — `$PRINTF` can be used inline in a `&` expression without a temporary variable. Verified by execution.

```kcml
01000 REM Build a JSON object from a KISAM record -- ^ placeholder pattern
: DIM ki_status, handle, ki_sym, ki_dataptr$6, ki_key$64, rec$512
: DIM json$1024, d_hex$8, v_num, tran_tbl$2
: REM tran_tbl$ -- R-mode $TRAN table, replacement then find
: tran_tbl$ = HEX(22) & "^"
: REM ... (open KISAM file, read record into rec$ -- see KISAM reference) ...
: REM ================================================================
: REM Pattern 1 -- string field (1 line)
: REM   $PRINTF %s strips trailing spaces from the fixed-length STR() slice
: json$ = "{"
: json$ = json$ & $PRINTF("\n  ^part_no^: ^%s^,",     STR(rec$, 20, 15))
: json$ = json$ & $PRINTF("\n  ^description^: ^%s^,", STR(rec$, 36, 30))
: REM Pattern 2 -- 4-byte packed date (YYYYMMDD) formatted as DD/MM/YYYY (2 lines)
: HEXUNPACK STR(rec$, 10, 4) TO d_hex$
: json$ = json$ & $PRINTF("\n  ^created_on^: ^%s/%s/%s^,", STR(d_hex$,7,2), STR(d_hex$,5,2), STR(d_hex$,1,4))
: REM Pattern 3 -- IBM packed decimal, 8 bytes, 6 decimal places (2 lines)
: UNPACK (#########.######) STR(rec$,513,8) TO v_num
: json$ = json$ & $PRINTF("\n  ^on_hand^:%.6f,", v_num)
: UNPACK (#########.######) STR(rec$,577,8) TO v_num
: json$ = json$ & $PRINTF("\n  ^local_cost^:%.6f", v_num)
: json$ = json$ & $PRINTF("\n}")
: REM Single pass -- replace all ^ with double-quote then output
: $TRAN(json$, tran_tbl$)R
: PRINT RTRIM(json$)
: $END
```

**Output:**
```json
{
  "part_no": "00963",
  "description": "SEAL*",
  "created_on": "13/03/2013",
  "on_hand":300.000000,
  "local_cost":0.720000
}
```

> **Warning:** Never put `:` or `"` inside a `REM` line. KCML treats `:` as a statement separator even inside `REM` text, and `"` starts a string literal. This applies throughout the script but is easy to forget in comment-heavy code.

## Notes

- Not all C `printf` specifiers work — `%e`, `%x`/`%X` zero-padding, and `%+` sign flags are not reliably supported.
- Zero-padding (`%05d`) does not work as expected — KCML uses space-padding for `%d`.
- The primary use case in the documentation is socket stream naming: `$PRINTF("#%d", n)` → `#5`.
- For PRINTUSING-style numeric formatting into a string, use [$FMT(]($FMT.md) instead.
- `\n` in format strings produces a real newline (ASCII 10) in the result string.
- `%s` strips trailing spaces from KCML fixed-length string variables — no `RTRIM` needed.
- `$PRINTF(...)` can be used inline in `&` string concatenation expressions.

## See also

[$FMT(]($FMT.md), [OPEN](OPEN.md)
