Changing the width of a column in a Grid control

------------------------------------------------------------------------

To change the width of columns in a Grid control the

*ColWidth* property is used. For example, the following would change the width of all columns in the grid *GridControl1*:

.GridControl1.ColWidth = 130

To change the width of a particular column the [*Cell()*](tmp/PROP_GRID_CELLXY.htm) method is used to select the column. For example, the following could be used to change the width of cells in column 6:

.GridControl1.Cell(0, 6).ColWidth = 140

and to find out the current height of a column the following could be used:

CurColWidth = .GridControl1.Cell(6,0).ColWidth

Note that a value of zero is returned if the default column width is being used.

Setting a column's width to 0 does not hide it. Even though it may appear to be invisible the column will still feature in the grid's tab order and scrollbar calculation.
