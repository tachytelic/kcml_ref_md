Cell (grid control method)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Cell(int, int) Method

**Used with other grid properties to change the properties of individual cells, rows and columns**

|      |                 |
|------|-----------------|
| Int1 | Row position    |
| Int2 | Column position |

This method is used in conjunction with other grid control properties. The method moves the programming cell (not the cursor) to the specified cell or range of cells and the subsequent property then operates on that cell or cells. Normally if properties are set without the *Cell* method then the whole grid is operated on. For example, the following would change the row height for every row in the grid: .GridControl1.RowHeight = 120

To change the properties of an individual cell, row or column, you must specify the *Cell()* method followed by the row and column of the cell(s) that you wish to reference. Once the cell position has been set, subsequent property changes for the cell(s) need only specify the *Cell* subproperty. For example, the following would move the programming cell to row 4, column 5 and place some text into the cell. It will also set the background color of the cell to *DarkBlue*: .GridControl1.Cell(4,5).Text\$ = "A very warm summers day!" .GridControl1.Cell.BackColor = &.DarkBlue ...

Setting the row or column values to zero will force subsequent property changes to work on all cells in the specified row or column, for example the following would set the background color of all cells in column 5 to *DarkBlue* and the text color to *White*: .gridControl1.Cell(0, 5).BackColor = &.DarkBlue .gridControl1.Cell.TextColor = &.White ...

Note that if both the row and column values are set to zero then subsequent property changes will operate on the entire grid, for example: .gridControl1.Cell(0, 0).BackColor = &.DarkBlue .gridControl1.Cell.TextColor = &.White ...

The cell selected this way is nothing to do with the cursor or user input focus rectangle.

Be aware that KCML instantiates only one cell at a time in the server event handling code and as a consequence the following code will not work as you might expect. Grid.Cell(x1,y1).Text\$=Grid.Cell(x2,y2).Text\$ Instead it will have to be expressed as a\$=Grid.Cell(x1,y1).Text\$ Grid.Cell(x2,y2).Text\$=a\$

Effectively you cannot use a Cell() method more than once in the same statement.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
