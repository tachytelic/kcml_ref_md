# KEYIN

> Reads a single character from an input device (usually the keyboard). Text-mode applications only.

## Syntax

```
KEYIN [#stream | /device | <addr_var>] receiver$ [,, line_fn]
KEYIN [#stream | /device | <addr_var>] receiver$, line_std, line_fn
KEYIN PAUSE ON [/device]
KEYIN PAUSE OFF [/device]
```

| Form | Behaviour |
|------|-----------|
| No line numbers or `,,line_fn` | **Blocking**: waits for a character. If `line_fn` specified, jumps there if a function key was pressed. |
| Two line numbers `line_std, line_fn` | **Polling**: checks once and moves on if nothing ready. Jumps to `line_std` for a standard char, `line_fn` for a function key. |

## Description

`KEYIN` receives one character from an input device. Without an explicit device, it reads from the `INPUT` device (default: keyboard).

**Blocking form**: execution pauses until a character arrives. If `,,line_fn` is given and a function key is pressed, jumps to `line_fn`.

**Polling form** (two line numbers): checks once; if nothing is ready, continues to the next statement. This form should only be used to clear the input buffer or occasionally check for a break key — not as a main input loop.

When `Ctrl+BREAK` is pressed:
- Reading from keyboard: waits for a character before acting on the interrupt.
- Reading from any other device: interrupts immediately (receiver byte value is unpredictable).

### PAUSE ON / OFF

`KEYIN PAUSE ON /device` and `KEYIN PAUSE OFF /device` control whether KCML pauses processing for terminal input.

### Mouse support (Windows / KClient)

| Mouse action | Key code |
|-------------|----------|
| Left click (down/up) | HEX(F1) / HEX(F2) |
| Left double-click | HEX(F1), HEX(F2) |
| Left drag | HEX(F1) down, HEX(F7) while dragging, HEX(F2) up |
| Right click (down/up) | HEX(F4) / HEX(F5) |
| Right double-click | HEX(F4), HEX(F5) |
| Right drag | HEX(F4) down, HEX(F7) dragging, HEX(F5) up |

## Examples

```kcml
KEYIN key_9$                   REM wait for any key
KEYIN #27, test$,, 420         REM stream 27; jump to 420 on function key
KEYIN /01C, temp$, 5000, 17000 REM device 01C; poll: 5000 std, 17000 fn
KEYIN <address$>, temp$        REM device from variable
KEYIN next_point$, 400, 400    REM poll; both branches go to 400
KEYIN PAUSE ON /001
KEYIN PAUSE OFF /001
```

## Notes

- `KEYIN` is for **text-mode** applications only. Not applicable in graphical forms environments.
- Use the polling form sparingly — it is intended for buffer-clearing, not main input loops.
- For full line input, use `LINPUT` or `LINPUT+`.
- For single-character input in modern code, use `KEYIN` within a screen event handler.

## See Also

- `LINPUT` — full-line input with editing
- `LINPUT+` — enhanced multi-line input
- `SELECT INPUT` — redirect the input device
- `$BREAK` — break/interrupt handling
