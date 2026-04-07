# TERMINFO Keyboard Definitions

> Key definition codes for KCML TERMINFO entries.

## Key definition codes (selection)

| Code | KEYIN value | Description |
|------|-------------|-------------|
| `AnsiKey` | Complex | SCO console 3-char ESC sequences (`\E[x`) |
| `AutoInsert` | — | Toggle auto-insert mode |
| `Cancel` | HEX(F0) | Editor cancel/mode change |
| `Clear` | HEX(81) | Editor: types "CLEAR " |
| `Complex(n)` | complex key n | Returns complex key n; remappable via `$KEYBOARD` |
| `Continue` | HEX(84) | Editor: types "CONTINUE " |
| `DeadKey(n)` | HEX(FF) + n | Two-character sequence (e.g. compose keys) |
| `Dectab` | HEX(5F) | Function key `pf(0x5F)` |
| `Delete` | HEX(49) | Delete character at cursor |
| `East` | HEX(4C) | Right arrow |
| `Edit` | — | Synonym for Cancel |
| `Erase` | HEX(E5) | Delete to end of line |
| `Execute` | HEX(82) | Terminates LINPUT |
| `pf(n)` | complex key n | Function key returning value n |

### Function key numbering

F0–F15 = keys 0–15; shifted = 16–31. The `pf(n)` code directly maps a key sequence to function key value n.

## See Also

- `TextTermGrammar` — TERMINFO file format
- `TextTermBoolean` — boolean capability flags
- `KEYIN` — read a keypress (returns key codes)
- `$KEYBOARD` — keyboard remapping
