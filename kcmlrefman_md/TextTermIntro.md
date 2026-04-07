# Introduction to Text Terminals

> Overview of how KCML interacts with text-mode terminals.

## Description

KCML programs interact with terminals via a standard interface: all terminals appear to KCML as 8-bit ASCII terminals with 16 dedicated function keys (F0–F15, shifted F16–F31), four arrow keys, and editing keys (CANCEL, INSERT, DELETE, NEXT, PREV, etc.).

KCML translates hardware-specific key sequences from the underlying terminal into virtual key codes. Function keys return values above 255 to `KEYIN`. Editing keys return specific high-byte codes:

| Key | Code | Key | Code |
|-----|------|-----|------|
| AUTOINSERT | — | INSERT | — |
| CANCEL | HEX(F0) | NEXT | — |
| DELETE | HEX(49) | PREV | — |
| EAST (→) | HEX(4C) | EXECUTE | HEX(82) |
| NORTH (↑) | — | PASTE | — |
| SOUTH (↓) | — | WEST (←) | — |

### Terminal identification

The `KTERM` environment variable specifies which TERMINFO entry to use. KCML ships TERMINFO descriptions for common terminals (VT100, VT220, KClient, etc.).

## On Unix

Terminal capabilities are described in a TERMINFO source file (`TERMINFO/src`) compiled with the KCML `terminfo` tool. The file defines key sequences, screen control sequences, and boolean capabilities.

## On Windows (KClient)

KClient is the native terminal — full keyboard, screen, GUI forms, and 132-column support. `KTERM=Kclient`.

## See Also

- `TextTermGrammar` — TERMINFO source file format
- `TextTermAttrib` — text attributes (bold, blink, reverse)
- `TextTermBox` — box graphics
- `TextTermKclient` — KClient terminal
- `KEYIN` — read a keypress
