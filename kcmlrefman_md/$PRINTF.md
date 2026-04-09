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

## Notes

- Not all C `printf` specifiers work — `%e`, `%x`/`%X` zero-padding, and `%+` sign flags are not reliably supported.
- Zero-padding (`%05d`) does not work as expected — KCML uses space-padding for `%d`.
- The primary use case in the documentation is socket stream naming: `$PRINTF("#%d", n)` → `#5`.
- For PRINTUSING-style numeric formatting into a string, use [$FMT(]($FMT.md) instead.

## See also

[$FMT(]($FMT.md), [OPEN](OPEN.md)
