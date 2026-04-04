Introduction to programming with the Grid control

There are two different methods in which cells in a grid control are referenced.

- The first is the visible selection made by the user selecting a cell either with the mouse or the keyboard, or directly under program control. In Grid control terms these are referred to as ***Cursor*** operations and the word cursor tends to appear as part of property and method names that reference the user selection box. A typical cursor operation executed within a program is to find out the current location of the cell selection box.
- The second method of referencing cells is the current cell driven by the programmer. Many grid properties refer to the current cell, so a typical programming sequence will select the current cell then proceed to set the text and other properties before moving onto the next cell. In grid terms these are referred to ***Cell*** operations.

When changing the properties of cells it is possible to change them for an individual cell, row or column, or the entire grid. To change the entire grid you simply specify the control name followed by the property name, for example the following would be used to change the row height and column width of all cells within the control *GridControl1* thus:

.GridControl1.RowHeight = 20 .GridControl1.ColWidth = 120

To change the properties of an individual cell, row or column, the

*Cell()* method is used to position the programming selection cell to the specified coordinates and change the properties of that cell. For example, the following would place some text into the cell at row 6, column 3:

.GridControl1.Cell(6,3).Text\$ = "Hello World!"

Once the programming cell has been specified with the [*Cell()* method, subsequent property changes for that cell can use the](tmp/PROP_GRID_CELLXY.htm)

*Cell* sub-property, this saves having to respecify the cell location for each property change, for example the following would place some text into a cell and change the cells background and text colors:

.GridControl1.Cell(6,3).Text\$ = "Hello World!" .GridControl1.Cell.BackColor = &.DarkBlue .GridControl1.Cell.TextColor = &.White

To operate on a whole row the column value should be specified as zero with the

*Cell()* method. And to operate on a whole column the row value should be specified as zero. For example, the following would change the background and text colors of all cells in row 8:

.GridControl1.Cell(8,0).BackColor = &.DarkBlue .GridControl1.Cell.TextColor = &.White

Note that specifying a row and column value of 0 with

*Cell()* method will operate on the entire grid, therefore

.GridControl1.Cell(0, 0).BackColor = &.DarkBlue .GridControl1.Cell.TextColor = &.White

would have the same effect as

.GridControl1.BackColor = &.DarkBlue .GridControl1.TextColor = &.White

Precedence

When setting properties in a grid, they can be set by cell, by row, by column or for the whole grid. The value to use depends on the grid cell [precedence](GridCellPrecedence.htm) rules.
