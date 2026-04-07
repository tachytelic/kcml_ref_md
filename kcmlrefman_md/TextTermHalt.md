# HALT and RESET Keys

> How to configure the HALT and RESET interrupt keys for KCML terminals.

## Description

**HALT** interrupts a running program and enters the KCML debugger. If the program is blocked on input, a key may be needed to unblock it before HALT takes effect.

**RESET** is a more drastic halt — cannot continue after RESET; interrupts programs blocked on devices or locks.

### KClient / WDW / WKCML

- HALT = `Ctrl+BREAK`
- RESET = `Ctrl+Alt+BREAK`
- Fixed; cannot be changed.

HALT and RESET are disabled if programming is disabled. They can be individually disabled via `$OPTIONS` bytes 13 (HALT) and 12 (RESET).

### Text-mode terminals (VT100 etc., NT client-server)

- HALT = `Ctrl-C` (fixed)
- RESET = `Ctrl-\` (fixed)

### Unix terminals

HALT and RESET are not in the TERMINFO mechanism — they map to Unix `interrupt` and `quit` signals. Configure with `stty`:

```sh
stty intr '^c' quit '^r'   # HALT = Ctrl-C, RESET = Ctrl-R
```

Place in `~/.profile` for persistent configuration.

Avoid setting `susp` (suspend) as it can interfere with KCML.

## See Also

- `TextTermIntro` — terminal overview
- `$OPTIONS` — byte 12/13 for HALT/RESET enable
