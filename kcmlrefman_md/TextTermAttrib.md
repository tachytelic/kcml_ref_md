# Text Attributes

> How to apply bold, blink, reverse video, and underline to terminal output.

## Description

Text attributes are applied using control sequences embedded in the output stream:

1. **Define attribute**: send `HEX(0204 xx yy 0F)` — sets the pending attribute.
2. **Enable attribute**: send `HEX(0E)` — switches on the previously defined attribute.
3. **Disable attribute**: send `HEX(0F)` — restores default characters. A carriage return also disables attributes.
4. `HEX(0E)` again re-enables the last defined attribute.

### Attribute byte `xx` (brightness/blink)

| Value | Effect |
|-------|--------|
| `00` | Not bright, not blink |
| `02` | Bright |
| `04` | Blink |
| `08` | Bright + Blink |

### Attribute byte `yy` (reverse/underline)

| Value | Effect |
|-------|--------|
| `00` | Normal |
| `01` | Reverse video |
| `02` | Underline |
| `03` | Reverse + underline |

Invalid digit values are treated as `00`.

## Examples

```kcml
REM Print "Hello" in bold
PRINT HEX(0204 0200 0F) & HEX(0E) & "Hello" & HEX(0F)
```

```kcml
REM Print "Warning" in blink + reverse
PRINT HEX(0204 0401 0F) & HEX(0E) & "Warning" & HEX(0F)
```

## Notes

- Attribute support depends on the terminal's TERMINFO definition.
- KClient supports all attributes.
- A `HEX(03)` (clear screen) also resets attributes.

## See Also

- `TextTermColor` — color support
- `TextTermBox` — box graphics
- `TextTermIntro` — terminal overview
