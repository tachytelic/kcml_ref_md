Inserting and deleting rows and columns

------------------------------------------------------------------------

To insert new rows and columns into a grid control, the

*ChangeRowCol()* method is used. This method requires the row and column position where the new cells are to be inserted, and the number of rows and columns to add. Negative values are used to remove rows and columns. The following are some examples:

|  |  |
|----|----|
| .GridControl1.ChangeRowCol(3, 1, 1, 0) | Would insert a new row at row 3. |
| .GridControl1.ChangeRowCol(1, 3, 0, 2) | Would insert two new columns at column 3. |
| .GridControl1.ChangeRowCol(3, 3, 1, 1) | Would insert a new row at row 3 and a new column at column 3. |
| .GridControl1.ChangeRowCol(1, 3, 0, -2) | Deletes columns 2 and 3. |
| .GridControl1.ChangeRowCol(3, 1, -1, 0) | Deletes row 3. |

 

This method is particularly useful when used in conjunction with the [*EditRow()* and](tmp/PROP_GRID_EDITROW.htm) [*EditGrid()* methods. For example the following would insert a new row into the grid and turn on editing for the row. Note that the](tmp/PROP_GRID_EDITGRID.htm) [*LeftClick()* event handler is enabled with the](tmp/PROP_GRID_LEFTCLICK.htm) [*LeftAction* property. Note that once the row has been inserted the](tmp/PROP_GRID_LEFTACTION.htm) [*LeftAction* and](tmp/PROP_GRID_LEFTACTION.htm) [*LeftSelect* properties are set immediately to enable the](tmp/PROP_GRID_LEFTSELECT.htm)

*LeftClick()* event handler for the new row.

\- DEFEVENT Form1.GridControl1.LeftClick() .GridControl1.ChangeRowCol(..CursorRow, ..CursorCol, 1, 0) .GridControl1.Cell(..CursorRow, ..CursorCol).LeftAction = &.Click .GridControl1.Cell.LeftSelect = &.Row .GridControl1.EditRow(..CursorRow, ..CursorCol) END EVENT
