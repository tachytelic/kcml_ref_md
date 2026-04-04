## Line numbers

By default the workbench will not display any line numbers in a program. To reveal the line numbers use the Line Number toggle option on the [Line menu](Line_Menu.htm).

When enabled, line numbers are displayed at the left of the screen, possibly together with an @ prefix to denote global or a - prefix to denote a referenced line. Apart from [compatibility issues](wbcompat.htm#compat40), lines and statements may be of any practical length.

To go to a particular line or statement within a line in the editor or debugger window press F2 to go to the command window and just enter the line number or the line number, a comma and the statement number withing the line.

There are menu options on the [Line Menu](Line_Menu.htm) to **add** a line number to the current statement (a suitable line number is automatically generated), **delete** the line number from the current statement, **Edit** a line number or to **remove all** line numbers from the currently selected block. It is not possible to delete the first line number of the program. It is possible to move the cursor into the line number error to modify it (using the option **Edit** line number from within the Line menu). In this case the new line number must fit in with surrounding line numbers, the line will not be moved and the user will not be able to leave the line number until a correct line number is entered.

An alternative way of creating or editing line numbers is simply to type them in the statement field as the first thing on the line. If that line already has a line number then, provided the new number is plausible, it will replace the old one. The above line number restrictions still apply.

Backspacing into a line number field from the beginning of a statement deletes the line number.
