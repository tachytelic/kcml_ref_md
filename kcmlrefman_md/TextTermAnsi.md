# ANSI Console (SCO UNIX)

> KCML terminal configuration for the ANSI console on SCO UNIX.

## Description

`KTERM=ansi`

Used for the console screen on PC implementations of SCO UNIX. Also available as a PC terminal emulation. Supports color.

When using the DW device driver, full box and block graphics are available. Otherwise only type-1 boxes (via `$BOXTABLE`) are supported.

An alternative font is supplied and installed by `kcmladmin` that reproduces the Wang character set in text mode.

### Default keyboard mapping

| KCML key | PC keyboard key |
|----------|----------------|
| SF1 | F1 |
| SF10 | F10 |
| SF11 | Shift+F1 |
| SF20 | Shift+F10 |

## See Also

- `TextTermIntro` — terminal overview
- `TextTermBox` — box graphics
- `TextTermColor` — color support
