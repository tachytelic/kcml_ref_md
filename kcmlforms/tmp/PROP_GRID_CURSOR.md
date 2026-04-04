Cell (grid control property)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Used with other grid properties to change the properties of individual cells, rows and columns**

This object is used to allow properties to be changed for an individual cell, row or column. The cell position can first be set with the [*Cell()* method before any property changes can take place. Alternatively the row and column can more naturely be specified as arguments.](PROP_GRID_CELLXY.htm)

For example, the following would move the programming cell to row 4, column 5 and place some text into the cell. It will also set the background color of the cell to *DarkBlue*: .GridControl1.Cell(4,5).Text\$ = "A very warm summers day!" .GridControl1.Cell.BackColor = &.DarkBlue

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
