MoveCell (grid control method)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> MoveCell(int, int) Method

**Moves the programming cell to the specified cell**

***Int1***      Row value\
***Int2***      Column value

This method is used to move the programming cell to the specified row and column. This method is used prior to a change in the cells properties. For example, the following would be used to place some text into the cell at row 10, column 10: .GridControl1.MoveCell(10,10) .GridControl1.Cell.Text\$ = "Have a nice day!"

<span style="font-family: Courier New,monospace; "> </span>Specifying either a row or column value of zero will operate on an entire column or row respectively. For example, the following would change the background color of row five: .GridControl1.MoveCell(5,0) .GridControl1.Cell.BackColor = &.DarkGreen

<span style="font-family: Courier New,monospace; "> </span>Note that the [*Cell()* method can also be used to move the programming cell to the required position, for example the following could be used instead of the examples above: .GridControl1.Cell(10,10).Text\$ = "Have a nice day!" .GridControl1.Cell(5,0).BackColor = &.DarkGreen](PROP_GRID_CELLXY.htm)

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
