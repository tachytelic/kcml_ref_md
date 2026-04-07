# VT220 / VT320 / VT420 Terminal

> KCML terminal configuration for DEC VT220 and compatible terminals.

## Description

`KTERM=vt220` (also `vt320`, `vt420` — aliases provided)

20 hardware function keys plus full editing keypad. VT320, VT420, and VT510 are all treated identically to VT220.

A default `SCREEN.vt220` file maps block graphic characters to a solid graphic.

Multinational characters available in the range `HEX(80)`–`HEX(FF)`.

### HALT key warning

The backspace key on many VT220s sends DEL (`HEX(7F)`) not backspace. Configure stty so HALT is not DEL:

```sh
stty intr '^c' quit '^r'
```

### Keyboard mapping

| KCML key | VT220 key |
|----------|-----------|
| RECALL | FIND |
| EDIT | SELECT |
| INSERT | INSERT |

Function keys SF1–SF20 map to VT220 F1–F20; shifted variants available.

## See Also

- `TextTermVT220box` — VT220 with soft font box graphics
- `TextTermVT100` — VT100
- `TextTermHalt` — HALT/RESET setup
