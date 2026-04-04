Setting the mouse action for cells in a grid

------------------------------------------------------------------------

It is possible to configure the default mouse action for either the entire grid or individual rows, columns and cells. For example you may wish to allow users to select some cells and not others. This is done with the [*LeftAction*,](tmp/PROP_GRID_LEFTACTION.htm) [*RightAction*,](tmp/PROP_GRID_RIGHTACTION.htm) [*LeftSelect*](tmp/PROP_GRID_LEFTSELECT.htm) and [*RightSelect* properties. The](tmp/PROP_GRID_RIGHTSELECT.htm) [*LeftAction* and](tmp/PROP_GRID_LEFTACTION.htm) [*RightAction* properties determine what mouse action is allowed while the](tmp/PROP_GRID_RIGHTACTION.htm) [*LeftSelect* and](tmp/PROP_GRID_LEFTSELECT.htm) [*RightSelect* properties determine whether the whole row, column or cell is to be selected. To set the action for individual rows, columns or cells these properties must be used in conjunction with the](tmp/PROP_GRID_RIGHTSELECT.htm)

*Cell()* method. For example, the following would set the mouse action for the cell at row 4, column 6:

.GridControl1.Cell(4, 6).LeftAction = &.Click .GridControl1.Cell.LeftSelect = &.Cell

To set these properties for an entire row or column a column or row value of zero is specified with the

*Cell()* method*.* For example, the following would set the mouse action for all cells in column 6:

.GridControl1.Cell(0, 6).LeftAction = &.Click .GridControl1.Cell.LeftSelect = &.Cell

And to set the mouse action for all cells within a grid the properties are specified without the

*Cell()* method, for example:

.GridControl1.LeftAction = &.Click .GridControl1.LeftSelect = &.Cell

However, the same result could be achieved with the

*Cell()* method by specifying a row and column value of zero, for example:

.GridControl1.Cell(0, 0).LeftAction = &.Click .GridControl1.Cell.LeftSelect = &.Cell

Setting the [*LeftAction* property to *&.Click* means that the left mouse button must be clicked on a new cell to move the selection box. Setting](tmp/PROP_GRID_LEFTACTION.htm) [*LeftAction* to *&.Down* would allow the mouse to drag the selection box around the grid if the left button was held down. Note that the](tmp/PROP_GRID_LEFTACTION.htm)

*LeftClick()* event handler is called if a cell is clicked or if the selection box is dragged into a new cell. In the example below the LeftClick() event handler is used to change the background color of cells as a cell is selected.

\- DEFEVENT Form1.GridControl1.LeftClick() .color1.Red = 0 .color1.Green = 255 .color1.Blue = 0 ..MoveCell(..CursorRow, ..CursorCol) ..Cell.BackColor = &.color1 END EVENT

[Click here](Examplemouseactionforgrid.htm) for an example program
