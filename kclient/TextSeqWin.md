Windowing

Control sequences have been defined which allows a window consisting of all or part of the screen together with the current cursor position to be saved at  any time. A later sequence can restore the screen exactly as it was at the  time of the original sequence. These sequences are automatically generated  by the [WINDOW](mk:@MSITStore:kcmlrefman.chm::/WINDOW.htm) and [\$RELEASE](mk:@MSITStore:kcmlrefman.chm::/$RELEASEfn.htm) commands of KCML. Each saved window is tagged with a unique number allowing multiple windows to be saved. Normally these will be nested and restored in reverse order.

The tag should contain the partition number in order that the tag is unique to the partition when the terminal is switched between partitions with \$RELEASE commands. Windows can optionally have borders and titles. The cursor is left invisible and positioned in the top left corner.

To open a window send the following sequence to the screen.

|             |                                            |
|-------------|--------------------------------------------|
| No border   | HEX(0209) tag dimensions HEX(0F)           |
| With border | HEX(0209) tag dimensions \[title\] HEX(0E) |

where tag is an ASCII number followed by an @ sign. The number should be \#PART times 10 plus the window number. If a window with that tag has already been saved then the original window is discarded.

The position and size of the window is coded into a 4 character dimensions sequence **RCDW** where each character represents the parameter of the window in binary plus 32

|     |                                          |
|-----|------------------------------------------|
| R   | Top left corner row (counting from 0)    |
| C   | top left corner column (counting from 0) |
| D   | depth in rows                            |
| W   | width in columns                         |

If a border is required then the depth and width must be at least 3 in order to allow for it.  For example

HEX(0209 313040 252A2840 0F)

opens a borderless window number 0 for partition 1 at row 5 column 10 with a depth of 8 and a width of 32.

HEX(0209 32303140 242F2A40);"WIN 1";HEX(0E)

opens window number 1 for partition 20 at row 4 column 15 with a depth of 10 and a width of 32. The title "WIN 1" is centered on the first line.

To close a window send

HEX(0209) tag HEX(0F)

The @ sign which was used as a delimiter for the tag when opening the window is not required when closing it. To close the bordered window of the previous example use

HEX(0209 323031 0F)
