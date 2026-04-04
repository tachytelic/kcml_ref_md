Color control

HEX(02 02 04 a b c d e f 0E/0F)

where *a, b, c, d, e* and *f* represent letters in the range A to P to control the attributes:

|     |                        |
|-----|------------------------|
| a   | Foreground (dim) color |
| b   | Background color       |
| c   | Bright color           |
| d   | Underline/Blink color  |
| e   | Box graphic color      |
| f   | Window background      |

Changing color does not effect any colors already on the screen but takes effect with the next character written. All 16 possible colors can be on the screen at once. However color information is not saved when a window is opened or when setup mode is entered. When the screen is restored the default colors are used to redraw it.

If less than 6 letters are specified then only the colors corresponding to the letters sent are changed, the others are restored to their default values. Thus by specifying no colors at all with a **HEX(02 02 04 0F)** the original color palette can be restored. In a similar way sending a period in place of a color letter will reset that color in the palette to its default color. A program can request the current palette from the PC by sending

HEX(020204);"?";HEX(0F)

and using KEYIN to catch the reply of color letters followed by a carriage return.

The colors available are:

| Code | Color          |
|------|----------------|
| A    | Black          |
| B    | Blue           |
| C    | Green          |
| D    | Cyan           |
| E    | Red            |
| F    | Magenta        |
| G    | Brown          |
| H    | White          |
| I    | Grey           |
| J    | Bright blue    |
| K    | Bright green   |
| L    | Bright cyan    |
| M    | Bright red     |
| N    | Bright magenta |
| O    | Yellow         |
| P    | Bright white   |
