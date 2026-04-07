# KCML Key Codes

> Key codes returned by `KEYIN` for function keys and special editing keys.

## Description

`KEYIN` returns either a regular key (the character's code-page value) or a function key code for special keys. Regular keys include `RETURN`, `BACKSPACE`, and `CTRL` combinations — these are all in the range `HEX(00)`–`HEX(1F)`. KCML 5+ supports the full 8-bit ANSI Latin-1 code page; regular keys can be `HEX(20)` or above (e.g. `HEX(F6)` for `Ö` on a German keyboard).

KCML supports up to 32 numbered function keys (`HEX(00)`–`HEX(1F)`). On KClient with 12 hardware keys, SHIFT and CTRL extend coverage.

## Editing function key codes

| Code | TERMINFO keyword | Explanation |
|------|-----------------|-------------|
| `HEX(42)` | `prev` | Previous page |
| `HEX(43)` | `next` | Next page |
| `HEX(4A)` | `insert` | Insert |
| `HEX(49)` | `delete` | Delete |
| `HEX(46)` | `north` | Up arrow |
| `HEX(45)` | `south` | Down arrow |
| `HEX(4C)` | `east` | Right arrow |
| `HEX(4D)` | `west` | Left arrow |
| `HEX(4F)` | `dectab` | Obsolete; often Ctrl-T |
| `HEX(48)` | `pferase` | Clear to end of line; usually Ctrl-E |
| `HEX(50)` | `shiftcancel` | Usually Shift-Home |
| `HEX(52)` | `shiftprev` | Shift-Previous page |
| `HEX(53)` | `shiftnext` | Shift-Next page |
| `HEX(5A)` | `shiftinsert` | Shift-Insert |
| `HEX(59)` | `shiftdelete` | Shift-Delete |
| `HEX(56)` | `shiftnorth` | Shift-Up |
| `HEX(55)` | `shiftsouth` | Shift-Down |
| `HEX(5C)` | `shifteast` | Shift-Right |
| `HEX(5D)` | `shiftwest` | Shift-Left |
| `HEX(5F)` | `recall` | Obsolete |
| `HEX(61)` | `autoinsert` | Ctrl-A |
| `HEX(62)` | `paste` | Ctrl-V |
| `HEX(63)` | `mark` | Ctrl-K |
| `HEX(7B)` | `cuatab` | TAB in CUA mode |
| `HEX(7C)` | `gl` | Usually Ctrl-G |
| `HEX(7D)` | `shiftgl` | Usually Ctrl-Z |
| `HEX(7E)` | `tab` | Sent by Shift-TAB in CUA mode |
| `HEX(7F)` | `shifttab` | Esc in CUA mode; Shift-TAB otherwise |
| `HEX(F0)` | `cancel` | Home / Cancel |

## Notes

- The distinction between regular keys and function keys blurs at `HEX(00)`–`HEX(1F)`.
- CUA mode is enabled by the `CuaMode` TERMINFO flag — it remaps Esc → `HEX(7F)`, TAB → `HEX(7B)`, Shift-TAB → `HEX(7E)`.

## See Also

- `KEYIN` — read a key from the terminal
- `vkcodes` — Windows virtual key codes
- `TextTermKybDefs` — TERMINFO keyboard definitions
- `TextTermKybMap` — keyboard key mapping
