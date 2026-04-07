# VT220 with Box Graphics

> KCML terminal configuration for DEC VT220 with soft-font box support.

## Description

`KTERM=vt220box` (also `vt320box`, `vt420box`)

Use this KTERM for genuine DEC VT220/320/420/510 terminals — they support soft fonts for box graphics simulation.

The TERMINFO assumes the soft font is loaded at login:

```sh
cat $KCMLADDR/vt220font     # for VT220/VT320
cat $KCMLADDR/vt420font     # for VT420/VT510 (higher resolution)
```

### Limitations

- VT220 clones may use a different character cell size — check the terminal's setup menu if overscore characters look wrong. Change cell size and reload the font.
- Emulators that do not support soft fonts: use plain `KTERM=vt220`.

### Note on Selfid

`Selfid` (terminal self-identification) may automatically detect VT220 capability and set `KTERM` to the `box` variant.

Keyboard mapping is identical to `KTERM=vt220`.

## See Also

- `TextTermVT220` — VT220 without soft fonts
- `TextTermSoftFont` — soft font box graphics
