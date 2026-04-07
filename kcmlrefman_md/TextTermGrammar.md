# TERMINFO Grammar

> Format of KCML TERMINFO source files for Unix terminal configuration.

## Description

Primarily relevant to Unix KCML installations. Each entry in `TERMINFO/src` describes a terminal's capabilities.

### Format

Each line: `definition_code = definition_string`

- Definition codes are case-insensitive.
- Some codes take a numeric argument in parentheses: decimal, hex (`0x`), or octal (`0`).
- Blanks and tabs allowed before/after but not within a field.
- `#` starts a comment to end of line.
- Entirely blank lines are ignored.

### Escape sequences in definition strings

| Escape | Value | Description |
|--------|-------|-------------|
| `\e` or `\E` | 0x1B | Escape |
| `\r` | 0x0D | Carriage return |
| `\n` | 0x0A | Line feed |
| `\b` | 0x08 | Backspace |
| `\s` | 0x20 | Space |
| `\t` | 0x09 | Tab |
| `\\` | — | Backslash |
| `\^` | — | Caret |
| `\#` | 0x23 | Hash |
| `\0nn` | — | Octal (3 digits) |
| `\x1F` or `\0x1F` | — | Hexadecimal (2 digits) |
| `^h` | 0x08 | CTRL character (masked with 0x1F) |

Any other `\x` = `x` (escape is ignored).

### Sections

Each terminal entry has multiple sections covering:
- Boolean flags (`TextTermBoolean`)
- Keyboard definitions (`TextTermKybDefs`)
- Screen attributes (`TextTermAttrib`)
- Box graphics capabilities (`TextTermBox`)
- Color support (`TextTermColor`)

## See Also

- `TextTermBoolean` — boolean capability flags
- `TextTermKybDefs` — keyboard key definitions
- `TextTermAttrib` — text attribute sequences
- `TextTermIntro` — terminal overview
