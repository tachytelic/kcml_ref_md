# PRINT BOX(

> Draws or erases a box or line on the text screen.

## Syntax

```
PRINT [AT(row, col);] BOX(height, width [, fill])
```

`BOX(` can appear anywhere in a `PRINT` statement alongside `AT(`, `TAB(`, `HEXOF(`.

## Parameters

| Parameter | Description |
|-----------|-------------|
| `height` | Number of rows (positive = draw, negative = erase) |
| `width` | Number of columns (positive = draw, negative = erase) |
| `fill` | Optional: fill percentage 0–100 for page printers (0 = no fill, 100 = solid) |

## Description

Uses the current cursor position (set by a preceding `AT(`) as the **top-left corner** of the box.

- Both positive: draw the box.
- Both negative: erase the box.
- Height = 0: draw/erase a **horizontal line** of the given width.
- Width = 0: draw/erase a **vertical line** of the given height.

The optional `fill` parameter applies only on page printers with GPD capabilities defined — it fills the box region with a grey pattern rather than drawing its outline.

Boxes can be simulated on terminals that do not support them natively using `$BOXTABLE`.

## Examples

```kcml
REM Draw a 5×5 box at row 10, col 10
PRINT AT(10,10); BOX(5,5)
```

```kcml
REM Erase the same box
PRINT AT(10,10); BOX(-5, -5)
```

```kcml
REM Horizontal line across the screen (row 5, starting col 5, 74 wide)
PRINT AT(5,5); BOX(0, 74)
```

```kcml
REM Box with a title
PRINT AT(10,10); BOX(10,10); box_title$
```

```kcml
REM Erase a region then draw a new box
PRINT AT(4,10); BOX(-5,-10); AT(4,7); BOX(0,20)
```

## Notes

- Only relevant for text-mode (terminal) applications.
- When printing to a file (`PRINT #stream`), `BOX(` is silently ignored.
- `fill` is only effective if `GpdHorizBox` / `GpdVertBox` printer capabilities are configured.

## See Also

- `PRINT AT(` — cursor positioning
- `PRINT` — base print statement
- `$BOXTABLE` — box character substitution table
- `WINDOW` — high-level window management
