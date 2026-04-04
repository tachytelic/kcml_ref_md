Changing the default fonts used by Grid cells

Fonts for grid cells are changed in much the same way as any other control. Firstly you must have a font set object available. Font set objects are generated when the default font for any control is changed. Once a font set object has been created it can then be modified and assigned to individual rows, columns or cells. The [*Cell()* method is used to position to a particular row, column or cell and the](tmp/PROP_GRID_CELLXY.htm)

*Font* property is used to assign the new font set to the cell(s). For example, the following would assign new a new font set to the cell at row 10, column 10:

.GridControl1.Cell(10,10).Font = &.dlgfont1

<span style="font-family: Courier New,monospace; "> </span>To assign a new font set to an entire row or column, a column or row value of zero is specified with

*Cell().* For example, the following would assign a new font set to column 6:

.GridControl.Cell(0, 6).font = &.dlgfont1

To assign a new font set to the entire grid the programming cell is positioned at row 0, column 0, for example:

.GridControl.Cell(0, 0).font = &.dlgfont1

This can also be achieved by not specifying the

*Cell()* method, for example:

.GridControl1.font = &.color1
