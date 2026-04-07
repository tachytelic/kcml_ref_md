# HP 700/9x Terminal

> KCML terminal configuration for HP 700/9x terminals.

## Description

`KTERM=hp` or `KTERM=hpterm`

Standard console on IBM RS/6000 (AIX). AT-style keyboard with 12 function keys; no soft font capability.

### Known limitation

If a character is overwritten, the new character **inherits the attributes** of the previous character. This makes text attributes unusable in native mode.

### Recommendation

Use the terminal in its **EM100** (VT100 emulation) or **EM2200** (VT220 emulation) personalities instead of native HP mode.

- **Local printer support**: not available in native mode.
- **Function keys**: only 8 available.

## Default keyboard mapping

| KCML key | IBM 3151 equivalent |
|----------|---------------------|
| SF0 | Shift+Ctrl+F12 |
| SF1 | F1 |
| SF11 | Shift+F1 |
| EDIT/CANCEL | HOME |
| HELP | ESC+ESC |

## See Also

- `TextTermIntro` — terminal overview
- `TextTerm3151` — IBM 3151 terminal
