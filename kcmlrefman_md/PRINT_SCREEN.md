# PRINT SCREEN

> Restores a saved screen image (captured with INPUT SCREEN) to the display.

## Syntax

```
PRINT SCREEN alpha_var [, AT(row, col)] [, BOX(depth, width)]
```

## Description

Displays the contents of an alpha variable previously saved with `INPUT SCREEN`. The variable holds the screen character data (and optionally attribute data) in a binary format with an 80-byte header.

Output is printed row by row starting at the specified AT position, for the given BOX dimensions. The screen area is cleared first using the current video attribute, then the saved content is rendered according to the video parameters stored in the variable's header.

If `AT` or `BOX` are not specified, the values stored in the header (from the original `INPUT SCREEN` call) are used.

If the alpha variable is too small to hold all sections, missing sections are defaulted (e.g. if attributes are missing, normal video is used; if characters are missing, spaces are assumed). If `alpha_var` contains fewer than 80 bytes, nothing is displayed.

## Examples

```kcml
REM Save and restore a screen region
DIM screen$152
PRINT AT(0,0); BOX(5,5)
FOR count = 1 TO 5
  PRINT "  Test"
NEXT count
INPUT SCREEN screen$, AT(0,0), BOX(5,5)
PRINT SCREEN screen$, AT(10, 37)    : REM redisplay at different position
```

```kcml
REM Restore to original position (uses stored AT/BOX from header)
PRINT SCREEN screen1$
```

```kcml
REM Restore a named window
PRINT SCREEN wind$(2), AT(10, column)
```

## Notes

- Only relevant for text-mode (terminal) applications.
- Avoid specifying a `BOX` that differs from the one used with `INPUT SCREEN` — unpredictable results may occur.
- Together with `INPUT SCREEN`, this forms the basis of KCML window management in text mode.

## See Also

- `INPUT SCREEN` — capture a screen region to a variable
- `PRINT AT(` — position cursor for printing
- `PRINT BOX(` — draw a box on screen
- `WINDOW` — high-level window management
