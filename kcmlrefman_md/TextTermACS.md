# ACS Terminal

> KCML terminal configuration for ACS terminals.

## Description

`KTERM=ACS`

The ACS terminal operates in two modes depending on flow control. For KCML:
- Set terminal type to **ANSI** for normal operation.
- Or set to **DW** (Wang 2336 mode) if the computer supports Wang flow control.

### Key mapping notes

| Key | Notes |
|-----|-------|
| RESET | Not implemented; sends `@` |
| SHIFT RESET | Not implemented; sends `?` |
| HALT | Sends XOFF — hangs until Ctrl-Q |
| SHIFT HALT | Same as HALT |

### Capabilities

- 16 function keys + editing keys (in ANSI mode)
- Attributes may have issues (set `ACSfix=TRUE` in TERMINFO)

## Notes

- The HALT key behaviour is a known limitation of ACS in ANSI mode.
- If Wang flow control is available, use `KTERM=wang` instead.

## See Also

- `TextTermIntro` — terminal overview
- `TextTermBoolean` — `ACSfix` flag
