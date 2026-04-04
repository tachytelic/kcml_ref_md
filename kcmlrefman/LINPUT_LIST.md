LINPUT LIST

------------------------------------------------------------------------

General Form:\
\
     LINPUT LIST alpha-receiver\
\

------------------------------------------------------------------------

The LINPUT LIST statement is used to generate efficient menus.

This statement is only relevant when developing text based applications.

The alpha receiver must be at least 9 bytes long and be terminated with one or more HEX(FF) characters. It consists of 6 control bytes and one or more groups of three bytes called triplets. Each triplet defines a menu position with the first bytes as the column (0-79), the second byte the row (0-23) and the third byte a tag character (usually the first character of the corresponding menu text).

If running under Microsoft Windows, either using KClient or the Windows DW terminal emulator, the mouse can be used to perform the tasks detailed below:

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| **Left Click** | **Left Double Click** | **Left Drag** | **Right Click** | **Right Double Click** | **Right Drag** |
| Positions cursor and makes selection | Positions cursor and makes selection. If cursor is off selection then action carriage return. | Positions cursor and makes selection | Abort | Abort | Positions cursor and then aborts |

 

LINPUT LIST control bytes

|  |  |
|----|----|
| **Byte** | **Description** |
| 1 | Initial index of triplet where the cursor is to be initially positioned. Will normally be HEX(01) for the first index. |
| 2 | Symbol to use for the menu acceptance character. Possible choices are HEX(82) for a right pointing triangle or HEX(8B) for a block character. |
| 3 | Symbol to use to erase the block. This will usually be HEX(20). |
| 4 | Returned as index of the triplet corresponding to the menu position when RETURN or a function key was pressed. |
| 5 | Returned as either HEX(00) if RETURN or CANCEL was pressed or HEX(FD) if a function key terminated the menu. |
| 6 | Returned as the value of the character pressed e.g. HEX(0D) for RETURN or HEX(7F) for SHIFT TAB/FN. |

\
When LINPUT LIST is executing, KCML itself moves the cursor between triplet positions. Pressing the space-bar will move the cursor and the acceptance block to the next triplet wrapping round when it gets to the end. Backspace reverses the direction. Pressing RETURN or a function key will terminate the LINPUT LIST and return the current triplet index and character pressed in the control bytes. Any other key will be searched for in the list of tag characters for each triplet. If found then the cursor will advance to the next matching triplet position. A bleep will sound if there is no match.

Example:

DIM menu\$100\
PRINT HEX(0306)\
menu\$=HEX(0182 2020 2020 0505 3105 0632 0507      33FF FFFF FF)\
PRINT AT(5,7);"1st option";AT(6,7);"2nd option";AT(7,7);"3rd option"\
LINPUT LIST menu\$

This example would print a menu of 3 options. Pressing the first character of any option displayed would take the cursor to that option. Pressing RETURN would select the option.

PRINT HEXOF(STR(menu\$,4,1))

Would return the position of the selected option.

Syntax examples:

LINPUT LIST menu\$\
LINPUT LIST FLD(menu\$.account\$)
