Changing the number of rows and columns in a Grid control

The number of rows and columns in a Grid control can be specified by the [*Rows* and](tmp/PROP_GRID_ROWS.htm)

*Cols* properties. For example, the following would set the grid to 10 rows and 10 columns:

.GridControl1.Rows = 10 .GridControl1.Cols = 10

and to find out how many rows and columns the grid currently has the following could be used:

CurRows = .GridControl1.Rows CurCols = .GridControl1.Cols

<span style="font-family: Courier New,monospace; "> </span>Increasing the number of rows will add additional blank rows to the end of the grid. Decreasing the number of rows will cause cells beyond the new number of rows to be deleted. Increasing the number of columns will add additional blank columns to the right hand side of the grid and decreasing the number of columns will cause cells beyond the new number of columns to be deleted.

Note that the

*ChangeRowCol()* method is used to insert and delete rows and columns.
