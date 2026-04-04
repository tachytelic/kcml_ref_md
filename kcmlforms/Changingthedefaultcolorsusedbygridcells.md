Changing the default colors used by Grid cells

Colors for grid cells are changed in much the same way as any other control. You can set the color of the whole grid or an individual cell, row or column. The [*Cell()*](tmp/PROP_GRID_CELLXY.htm) method is used to position to a particular row, column or cell and the [*BackColor* and](tmp/PROP_GENERIC_BACKCOLOUR.htm)

*TextColor* properties are used to set the actual colors. For example, the following would change the background and text colors of the cell at row 10, column 10:

.GridControl1.Cell(10,10).BackColor = &.DarkGreen .GridControl1.Cell.TextColor = &.White

To change the color of an entire row or column, a column or row value of zero is specified with the [*Cell()*](tmp/PROP_GRID_CELLXY.htm) method. For example, the following would change the background color and text colors for cells in column 6:

.GridControl1.Cell(0, 6).BackColor = &.DarkGray .GridControl1.Cell.TextColor = &.White

To assign a new color set to the entire grid the programming cell is positioned at row 0, column 0, for example:

.GridControl1.Cell(0, 0).BackColor = &.DarkMagenta .GridControl1.Cell.TextColor = &.White

This can also be achieved without using [*Cell()* method and the](tmp/PROP_GRID_CELLXY.htm)

*Cell* sub-property, for example:

.GridControl1.BackColor = &.DarkMagenta .GridControl1.TextColor = &.White
