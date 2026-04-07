# Box Graphics (Terminal)

> How KCML draws boxes and lines on text terminals.

## Description

`PRINT BOX(depth, width)` draws a box using the terminal's built-in box-drawing capability. The cursor position is the top-left corner; the cursor does not move after drawing.

- Positive dimensions: draw.
- Negative dimensions: erase.
- Zero depth: horizontal line.
- Zero width: vertical line.

Horizontal box segments overwrite character cells but preserve the character underneath. Vertical segments bisect the character cell. Printing a new character on top of a box does not destroy the box. Boxes can only be removed with `HEX(03)` (clear screen) or negative-dimension `PRINT BOX(`.

## Character box fallback (`$BOXTABLE`)

Not all terminals support native KCML box drawing. The `$BOXTABLE` function specifies an alternative character-based scheme:

- First byte `HEX(00)`: native KCML box drawing (terminal capability).
- First byte `HEX(01)`: character simulation — the next 16 bytes define characters for each combination of N/S/E/W segments.

`$MACHINE` byte 4 = `G` on terminals with native box support.

## See Also

- `PRINT BOX(` — draw/erase boxes
- `TextTermCharBox` — character box layout reference
- `$BOXTABLE` — box character table
- `TextTermAttrib` — text attributes
