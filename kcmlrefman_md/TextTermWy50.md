# Wyse 30 / Wyse 50 Terminal

> KCML terminal configuration for Wyse 30 and Wyse 50 terminals.

## Description

`KTERM=wy30` or `KTERM=wy50`

Common inexpensive terminals with some significant limitations.

### Setup requirements

Attributes occupy screen space — KCML uses the terminal's write-protect mode for attributes. Set write-protect modes in the terminal setup menu (recommended: WPRT = dim, no underline, reverse).

### Limitations

- No box graphics or alternative fonts (`HEX(80)`–`HEX(FF)`).
- Some line graphic characters available between `HEX(10)` and `HEX(1F)`.
- Backspace and left arrow send the same code — KCML treats both as backspace.
- Default TERMINFO assumes 16 function key keyboard; edit for 12-key VT220/AT keyboards.

### Optional character box simulation

A box table is defined in TERMINFO but disabled by default. To enable:

```kcml
STR($BOXTABLE, 1, 1) = HEX(01)
```

### Other features

- Local printing: **supported**.
- `RobustFlow=TRUE` in TERMINFO needed for Redhaw variant of Wyse 50.

## See Also

- `TextTermWy60` — Wyse 60 and above (more capable)
- `TextTermBox` — box graphics
- `TextTermIntro` — terminal overview
