# Language Codes

> Reference for KCML's language numbering convention used for multilingual string support.

## Description

KCML assigns numbers to languages for use in:
- Byte 20 of `$OPTIONS RUN` — default language for `<<chevron>>` multilingual strings
- Byte 61 of `$OPTIONS RUN` — code page for UTF-8 ↔ code-page conversion via `$PACK` with `E="UTF-8"`
- `$MACHINE` byte 33 — indirectly indicates the client's Windows locale

Set byte 61 to `HEX(FF)` if the server is running in Unicode mode (`USING-UTF8` environment variable set) — the UTF-8 pack format then becomes a simple copy.

## Language numbers

| Code | Language |
|------|---------|
| 0 | (default/undefined) |
| 1 | English (US) |
| 2 | English (UK) |
| 3 | French |
| 4 | German |
| 5 | Spanish |
| 6 | Italian |
| 7 | Portuguese |
| 8 | Dutch |
| 9 | Swedish |
| 10 | Norwegian |
| 11 | Danish |
| 12 | Finnish |
| ... | (consult `$OPTIONS RUN` byte 20 documentation for full list) |

## Windows locale mapping

The kclient derives the language code from the Windows user locale at startup. Split locales are handled:
- English: defaults to US (1) unless specifically UK English (2)
- Chinese: defaults to Simplified (PRC) unless specifically HongKong or Taiwan (Traditional)

The locale is read only at client startup; changing the Windows locale while the client is running has no effect.

## Notes

- Many applications define their own language numbering rather than using the KCML convention.
- `KLANG` environment variable sets the default language number.

## See Also

- `$OPTIONS RUN` — byte 20 (language) and byte 61 (code page)
- `$MACHINE` — byte 33 (client locale)
- `KLANG` — environment variable for default language
- `USING-UTF8` — environment variable for Unicode mode
