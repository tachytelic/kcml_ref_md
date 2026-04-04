Box graphics

KCML provides the [PRINT BOX(](PRINT_BOX(.htm) function which allows the programmer to draw lines and boxes on the screen, for example:

PRINT BOX(depth, width)

will print a box whose top left corner is at the current cursor position and which extends *depth* rows down and *width* columns across. The cursor is not moved. By specifying a zero depth a horizontal line can be drawn and similarly a zero width will result in a vertical line. Horizontal box segments overscore the characters in the row leaving the existing character in place. Vertical box segments bisect the character cell and overlay the character. As boxes are attributes of the characters they overlay rather than characters in their own right, printing another character on top of a box will not obliterate the box. Boxes can only be removed with the HEX(03) control sequence which clears the whole screen or by explicitly removing the box with another [PRINT BOX(](PRINT_BOX(.htm) where the width and depth parameters are negative. Thus

PRINT BOX(-depth, -width)

will remove the box from the previous example.
