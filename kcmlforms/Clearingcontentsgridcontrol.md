Clearing the contents of cells within a Grid control

There are two ways of clearing the contents of a grid control. Thr

*Reset()* method can be used to reset the grid to its original design time settings. For example:

.GridControl1.Reset()

To remove the contents of an individual cell, row or column the [*Clear()* method is used. The](tmp/PROP_GRID_CLEAR.htm)

*Cell()* method is used to specify the cell, row or column that is to be cleared. For example, the following would clear the contents of the cell at row 6, column 5:

.GridControl1.Cell(6, 5).Clear()

To clear the contents of an entire row or column, a column or row value of zero is specified with the [*Cell()*](tmp/PROP_GRID_CELLXY.htm) method*.* For example, the following would clear the contents of column 6:

.GridControl1.Cell(0, 6).Clear()

To clear the contents of all cells within the grid the

*Clear()* method is executed after the programming cell is positioned at row 0, column 0, for example:

.GridControl1.Cell(0, 0).Clear()

<span style="font-family: Courier New,monospace; "> </span>Note that the

*Clear()* method only removes the contents of cells, all other property settings are left unchanged.
