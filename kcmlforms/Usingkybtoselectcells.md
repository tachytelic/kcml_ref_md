Using the keyboard to select cells

------------------------------------------------------------------------

Normally the mouse is used to select cells within a grid. However, it is sometimes useful to allow the keyboard to make a cell selection. This can be done by navigating to the desired cell using the arrow keys, HOME, END etc and then pressing the spacebar. This will trigger a Click() event, provided the cell is not editable.

For a more exact control of the selection process, you can arrange to be notified if any key is pressed in a cell. If the [*Char()* event handler exists then it is called each time a key is pressed while the grid control is in focus. This event handler can then be used to determine which character was pressed and act upon it accordingly. The last character pressed within the grid is placed into the](tmp/PROP_GRID_CHAR.htm)

*LastChar\$* property. For example, the following event handler would be called if a key was pressed in the grid control. If the 'B' key was pressed then a new color set is assigned to the background color of the cell, if any other key was pressed then the default beep would be sounded:

\- DEFEVENT Form1.GridControl1.Char() IF (..LastChar\$ == "B") ..Cell(..CursorRow, ..CursorCol).BackColor = &.DarkMagenta ELSE .form.Beep(0) END IF END EVENT
