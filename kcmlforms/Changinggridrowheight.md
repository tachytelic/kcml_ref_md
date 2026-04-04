Changing the height of rows within a Grid control

To change the height of rows in a Grid control the

*RowHeight* property is used. For example, the following would change the height of all rows in the grid *GridControl1*:

.GridControl1.RowHeight = 130

To change the height of a particular row the [*Cell()*](tmp/PROP_GRID_CELLXY.htm) method is used to select the row. For example, the following could be used to change the height of cells in row 6:

.GridControl1.Cell(6,0).RowHeight = 40

and to find out the current height of a row the following could be used:

CurRowHeight = .GridControl1.Cell(6,0).RowHeight

Note that a value of zero is returned if the default row height is being used.

Setting a row's height to 0 does not hide it. Even though it may appear to be invisible the row will still feature in the grid's tab order and scrollbar calculation.
