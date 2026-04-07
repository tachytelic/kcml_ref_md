# Magna Falcon Terminal

> KCML terminal configuration for the Magna Falcon.

## Description

`KTERM=magna`

Dual-mode terminal (VT100 or Wang 2536 personality). KCML switches automatically to Wang personality on startup and restores VT100 on exit or SHELL escape.

```sh
export TERM=vt100     # Unix applications use VT100
export KTERM=magna    # KCML uses Wang personality
```

### Flow control

Works with XON/XOFF or Wang flow control. In XON/XOFF mode, a special convention allows all function keys including SF17 and SF19.

### HALT key

HALT sends XOFF — must not be used. Redefine:

```sh
stty intr '^y' quit '^r'
```

### Capabilities

- 16 function keys + editing keys
- Color model: attributes remapped to colors
- Supports window save/restore in terminal memory (speeds up WINDOW OPEN/CLOSE)
- Late model monochrome screens: also support window save/restore

## Notes

- Both Shift and Ctrl must be pressed together for Ctrl key combinations.
- Coexists with VT100 applications (Word, Uniplex, etc.) by switching personalities.

## See Also

- `TextTermIntro` — terminal overview
- `TextTermSpx` — Spectrix SPX701 (similar dual-mode)
