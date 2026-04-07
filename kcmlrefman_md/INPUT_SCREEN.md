# INPUT SCREEN

> Captures a portion of the current text-mode screen into an alpha variable for later restoration with `PRINT SCREEN`.

## Syntax

```
INPUT SCREEN alpha_receiver [, AT(row, column)] [, BOX(depth, width)]
```

| Element | Description |
|---------|-------------|
| `alpha_receiver` | Alpha variable to receive the screen data |
| `AT(row, col)` | Starting position (default: 0, 0) |
| `BOX(depth, width)` | Size to capture (defaults to full screen) |

**Note:** Text-mode only. Not supported in graphical forms environments, DBCS code pages, or UTF-8 Unicode mode.

## Description

`INPUT SCREEN` copies the screen content from the specified position and size into `alpha_receiver`. This can later be passed to `PRINT SCREEN` to restore the display — equivalent to `WINDOW OPEN`/`CLOSE`.

The screen is read row-by-row, `depth+1` rows and `width+1` columns (the +1 is a BASIC-2C compatibility quirk).

Defaults when omitted:
- `AT`: (0, 0)
- `BOX`: full screen (`MaxRow` × `MaxCol-1`)

So these two are equivalent on a 24×80 screen:
```kcml
INPUT SCREEN a$()
INPUT SCREEN a$(), AT(0,0), BOX(24,79)
```

### Data format

The captured data in `alpha_receiver` consists of:

| Bytes | Content |
|-------|---------|
| 1–80 | Header (terminal ID, screen size, cursor position, video mode, etc.) |
| Section 1 | Character data: (depth+1) × (width+1) bytes |
| Section 2 | Video attribute + box-graphic data: same size |
| Section 3 | Color attribute data: same size |

**Total for full 24×80 screen**: 80 + 25×80×3 = 6,080 bytes

```kcml
DIM screen$(80 + 25 * 80 * 3)
INPUT SCREEN screen$()
```

**Note:** The 25th row must be captured even though it cannot be written, because `PRINT BOX(24,80)` requires overscore box attributes on that row.

### Header bytes (bytes 1–80)

| Bytes | Description |
|-------|-------------|
| 1–29 | Terminal ID message |
| 30–65 | Reserved (HEX(00)) |
| 66 | Number of valid sections captured |
| 67 | Screen lines (normally 24) |
| 68 | Screen columns (normally 80) |
| 69 | AT row |
| 70 | AT column |
| 71 | BOX depth |
| 72 | BOX width |
| 75 | Current attribute (reverse, blink, bright, underline flags) |
| 76 | Video mode |
| 77 | Alternate character set status |
| 78 | Cursor status (off / steady / blinking) |
| 79 | Cursor row |
| 80 | Cursor column |

### Video attribute flags (Section 2)

| Bit | Meaning |
|-----|---------|
| HEX(80) | Alternate character set |
| HEX(40) | Reverse video |
| HEX(20) | Blink |
| HEX(10) | Bright |
| HEX(08) | Underline |
| HEX(04) | Left horizontal box segment |
| HEX(02) | Right horizontal box segment |
| HEX(01) | Vertical box segment |

### Color attribute (Section 3)

High nibble = background color (0x0–0x7), low nibble = foreground color (0x0–0x7). If color is not in use, each byte is HEX(07) (black background, white foreground).

## Examples

```kcml
REM Save the full screen
DIM screen$(6080)
INPUT SCREEN screen$()
REM ... do something with the screen ...
PRINT SCREEN screen$()    REM restore it

REM Save a window region
DIM win$188
INPUT SCREEN win$, AT(5,5), BOX(5,5)
REM ... draw over it ...
PRINT SCREEN win$         REM restore the window
```

Using a field variable:
```kcml
INPUT SCREEN FLD(window$.window_2$), AT(4,4)
```

## Notes

- `INPUT SCREEN` is for **text-mode only** — not supported in GUI/forms environments.
- Not supported with DBCS or UTF-8 mode.
- Screen dumps can also be triggered by `SIGUSR2` signal; the file `scrndxxx` (where `xxx` is `#PART`) is written to the current directory (or `SCREENDIR`).
- `SCREENDIR` environment variable redirects where screen dump files are saved.

## See Also

- `PRINT SCREEN` — restore a captured screen
- `WINDOW OPEN` / `WINDOW CLOSE` — save and restore screen regions
- `PRINT AT` — position text on screen
- `BOX` — draw a box on screen
