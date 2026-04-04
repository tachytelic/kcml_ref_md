RowHeight (grid control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the row height**

This property is used to specify the height of rows in a Grid control. This property can be used to change the height of all rows within the grid or the height of an individual row. For example, the following would set the height of all cells within the specified grid control: .GridControl1.RowHeight = 100

To change the height of an individual row this property is used in conjunction with the [*Cell()* method. For example: .GridControl1.Cell(Row, Col).RowHeight = 120](PROP_GRID_CELLXY.htm)

<span style="font-family: Courier New,monospace; "> </span>This property can also be used to return the height of the specified row, for example: Height = .GridControl1.Cell(6,0).RowHeight

A value of zero is returned to signify that the row is using the default row height.

Setting a row's height to 0 does not hide it. Even though it may appear to be invisible the row will still feature in the grid's tab order and scrollbar calculation.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
