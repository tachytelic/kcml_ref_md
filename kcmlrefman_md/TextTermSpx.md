# Spectrix SPX701 Terminal

> KCML terminal configuration for the Spectrix SPX701.

## Description

`KTERM=spx701`

Dual-mode terminal (VT100 or Wang 2336 personality). Configure as VT100 + XON/XOFF:

```sh
export TERM=vt100
export KTERM=spx701
```

KCML automatically switches to Wang personality on startup and restores VT100 on exit or during SHELL escapes.

### XON/XOFF limitations

- SF17 and SF19 conflict with XON/XOFF — cannot be used in XON/XOFF mode.
- Extended bi-directional flow control prevents lower-case w/x/y from being underscored in `LINPUT`.

### HALT key

HALT sends XOFF — must not be used. Redefine:

```sh
stty intr '^c' quit '^r'
```

### Capabilities

- 16 function keys + editing keys
- Color model: maps attributes (bright/blink) to colors
- `SpecTerm=TRUE` in TERMINFO for flow control workaround

## See Also

- `TextTermIntro` — terminal overview
- `TextTermMagna` — Magna Falcon (similar dual-mode terminal)
