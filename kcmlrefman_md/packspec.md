# $PACK Field Specifiers

> Mnemonic field type codes for use in `$PACK`, `$UNPACK`, `$FORMAT`, and `FLD()` definitions.

## Description

These specifiers were introduced in KCML 6.10. They can be used in `DEFRECORD FLD` statements and in the extended form of `$PACK`/`$UNPACK`. They are preferred over the older BASIC-2 compatible hex codes.

## Field specifiers

| Specifier | Description |
|-----------|-------------|
| `CHAR(n)` | UTF-8 character string of exactly `n` bytes |
| `TEXT(x,y)` | UTF-8 multiline string: `y` lines × `x` bytes max, total `x×y` bytes. Forms treat this as a multiline edit. |
| `LANG(x,y)` | UTF-8 multilanguage string: array of `y` strings × `x` bytes. Active string is determined by `$OPTIONS RUN` byte 20 (1-based; out-of-range uses string 1). |
| `INT(n)` | Signed integer in `n` bytes (max 6 bytes; inefficient above 4) |
| `UINT(n)` | Unsigned integer in `n` bytes (max 6 bytes) |
| `NUM(p,s)` | Signed packed BCD with precision `p` and optional scale `s` (max precision 13 in KCML 6.10) |
| `UNUM(p,s)` | Unsigned packed BCD (max precision 13) |
| `FP` | KCML internal floating-point format (machine-independent). Was `SY8` in some KCML 6.0 builds. Not recommended for database rows as the format may change. |
| `DATE` | Julian date in 3 bytes. Replaces legacy `MD` format. |
| `TIME` | Seconds since midnight. Replaces legacy `MT` format. |
| `BOOL` | Y/N boolean returning numeric `TRUE`/`FALSE` |
| `MB` | Legacy Y/N boolean returning string value |
| `TIMESTAMP` | Millisecond timestamp (6 bytes) |
| `HEX` | Hexadecimal field |

## Notes

- `KI_DESCRIBE_COL` now returns these new pack codes rather than the 2-byte hex strings used by KCML 5 and earlier KCML 6 versions — this may require application changes.
- Bit-count format `HEX(FBxxxxxx)` is now only available via `$UNPACK(E="BITS(xxxxxx)")`.
- Informix money format `HEX(FCxx)` is now only available via `$PACK(E="X")`.

## See Also

- `$PACK` — pack data into a string buffer
- `$UNPACK` — unpack data from a string buffer
- `$FORMAT` — format data using field specifiers
- `FLD(` — field access in records
- `DEFRECORD` — record definition
