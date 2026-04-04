Inserting text into a Grid cell

------------------------------------------------------------------------

To insert text into a specific cell in a Grid control you must first use the [*Cell()* method to move to the required cell then change the](tmp/PROP_GRID_CELLXY.htm)

*Text\$* property. For example, the following section of code inserts random numbers into a 10 by 10 grid:

.GridControl1.Rows = 10 .GridControl1.Cols = 10 row = 1 Column = 1 WHILE row++ \<= .GridControl1.Rows DO WHILE Column++ \<= .GridControl1.cols DO CONVERT INT(RND(1) \* 1000) TO Cell\$, (####) .GridControl1.Cell(Row, Column).Text\$ = Cell\$ WEND Column = -1 WEND
