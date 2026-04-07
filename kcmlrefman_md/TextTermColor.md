# Screen Colors (Terminal)

> How to configure foreground, background, and attribute colors on color terminals.

## Description

KClient and many terminal emulators support color. Color is set via the control sequence:

```
HEX(0202 04 aa bb cc dd ee ff gg 0F)
```

| Byte | Role |
|------|------|
| `aa` | Foreground color |
| `bb` | Background color |
| `cc` | Bold color |
| `dd` | Blink color |
| `ee` | Box graphics color |
| `ff` | Window background (see WINDOW) |
| `gg` | Window border (see WINDOW) |

### Color codes

| Code | Color | Code | Color |
|------|-------|------|-------|
| A | Black | I | Grey |
| B | Blue | J | Bright blue |
| C | Green | K | Bright green |
| D | Cyan | L | Bright cyan |
| E | Red | M | Bright red |
| F | Magenta | N | Bright magenta |
| G | Yellow/Brown | O | Bright yellow |
| H | White | P | Bright white |

## Example

```kcml
REM Set white text on blue background
PRINT HEX(020204) & "HP" & HEX(0F)
```

## Notes

- Color support is defined in the terminal's TERMINFO entry.
- KClient uses the native Windows code page and supports all colors.
- Color state persists until changed or `HEX(03)` (clear screen) is sent.

## See Also

- `TextTermAttrib` — text attributes
- `WINDOW` — KCML window management
- `TextTermKclient` — KClient terminal
