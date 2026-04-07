# Wyse 60, 99, 120, 160, 325 Terminals

> KCML terminal configuration for Wyse 60 and compatible terminals.

## Description

`KTERM=wy60` (also `wy99`, `wy120`, `wy160`, `wy325`)

Supported from Wyse 60 upward (except Wyse 75 and 370). TERMINFO has entries for wy60, wy99, wy120, wy160, wy325.

For unlisted models: set the terminal to its highest Wyse mode and use `KTERM=wy160`.

### Adding new Wyse models to TERMINFO

Edit the TERMINFO/src line:
```
[wy60|wy99|wy120|wy160|wy325]
```
Add the new model name, then recompile with `tik`.

### Brightness note

These terminals have **dim** but no **bright** attribute. The default TERMINFO uses dim for normal text and normal for bright. Adjust the brightness controls accordingly, or edit the TERMINFO `AttribOn`/`AttribOff` entries.

### Keyboard

Default: 16 function key keyboard. For 12-key AT keyboard: modify TERMINFO to remap SF12–SF15 and SF28–SF31.

### With soft font box graphics

Use `KTERM=wynnnbox` — see `TextTermWy60box`.

## See Also

- `TextTermWy60box` — Wyse 60 with soft font boxes
- `TextTermWy50` — Wyse 30/50 (limited)
- `TextTermSoftFont` — soft font details
