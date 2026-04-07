# VT100 Terminal

> KCML terminal configuration for DEC VT100 and VT100-compatible terminals.

## Description

`KTERM=vt100`

One of the most widely supported terminal types. Many third-party terminals and PC emulators offer VT100 compatibility.

### Limitations

- Only 4 hardware function keys (F1–F4).
- No soft font capability.
- Supports line drawing (ACS graphics) for character-box simulation.

### Keyboard mapping (VT100)

| KCML key | VT100 key |
|----------|-----------|
| INSERT | F1 |
| DELETE | F2 |
| EDIT | F3 |
| RECALL | (varies) |

### Notes

- Many terminals and emulators provide VT100 personality — use `KTERM=vt100` for these.
- For terminals with a VT220 personality, use `KTERM=vt220` for more function keys.
- HALT and RESET must be configured with `stty` — see `TextTermHalt`.

## See Also

- `TextTermVT220` — VT220 (more function keys, soft fonts)
- `TextTermHalt` — HALT/RESET key setup
- `TextTermIntro` — terminal overview
