Character boxes

Not all terminals can draw boxes in the true KCML manner described above so the [\$BOXTABLE]($BOXTABLE.htm) function is provided to allow an alternative box drawing scheme to be specified. On UNIX versions the value of the [\$BOXTABLE]($BOXTABLE.htm) is specified in the *TERMINFO* description for that terminal and can be changed within a program. If the first byte of [\$BOXTABLE]($BOXTABLE.htm) is HEX(00) then the terminal is presumed to be able to draw true **KCML** boxes as described above. Byte 4 of the [\$MACHINE]($MACHINE.htm) system variable is set to \`G' on such terminals and blank on all others.

If the first byte of \$BOXTABLE is HEX(01) then **KCML** will use characters to simulate boxes and the next 16 bytes of the variable define the characters to be used assuming the terminal to be able to draw crosses and corners through the middle of a character cell. The segments are assumed to start at the centre of a character cell and extend vertically and horizontally to the points of the compass. For instance a vertical bar character (HEX(78) in the VT100 graphics font) would be inserted into byte 14 as it uses both the north and the south segments. A top left corner symbol would be defined in byte 8 because it uses only the south and east segments and so on.

| Byte | N   | S   | E   | W   |
|------|-----|-----|-----|-----|
| 2    |     |     |     |     |
| 3    |     |     |     | \*  |
| 4    |     |     | \*  |     |
| 5    |     |     | \*  | \*  |
| 6    |     | \*  |     |     |
| 7    |     | \*  |     | \*  |
| 8    |     | \*  | \*  |     |
| 9    |     | \*  | \*  | \*  |
| 10   | \*  |     |     |     |
| 11   | \*  |     |     | \*  |
| 12   | \*  |     | \*  |     |
| 13   | \*  |     | \*  | \*  |
| 14   | \*  | \*  |     |     |
| 15   | \*  | \*  |     | \*  |
| 16   | \*  | \*  | \*  |     |
| 17   | \*  | \*  | \*  | \*  |

\$BOXTABLE Byte settings for character boxes

Because these boxes actually occupy the cell rather than overlaying it KCML will only draw a box segment in a character cell if the character is blank. Character boxes also extend one row lower than regular boxes though if this would take the box off the bottom of the screen then the box is clipped.

On many terminals (e.g. VT100 and Wyse 50) it is necessary to use a special font to access the graphics characters. The sequences to select and deselect this font should be specified using the *BoxStart* and *BoxEnd* keywords in the *TERMINFO* for the terminal.
