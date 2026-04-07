# 132-Column Support

> How to enable 132-column wide-screen mode in KCML.

## Description

Only KClient and the Kerridge Windows DW terminal emulator fully support 132-column mode. Some modern DEC and Wyse terminals also support it (incompatible with soft-font boxes).

### Enabling 132-column mode

1. Set `$OPTIONS` byte 17 = `HEX(01)`.
2. Set screen width: `SELECT PRINT /005(132)` (or `SELECT LIST /005(132)` or `SELECT CO /005(132)`).
3. Clear the screen: `PRINT HEX(03)`.

`$MACHINE` byte 8 reflects the current width (80 or 132) as a binary byte after a width change — provided the TERMINFO entry defines a `Col132` sequence.

### Restoring 80-column mode

```kcml
SELECT PRINT /005(80)
PRINT HEX(03)
```

`$MACHINE` byte 8 resets to 80.

### TERMINFO entries with 132-column support

KClient, kcml, wdw, DW, magna, vt100, vt220, wy60, wy160, wy99.

The screen table size increases from 6KB to 10KB on 132-column terminals.

## See Also

- `TextTermKclient` — KClient terminal
- `$OPTIONS` — byte 17
- `$MACHINE` — byte 8 (screen width)
- `SELECT CO` / `SELECT PRINT` — set device width
