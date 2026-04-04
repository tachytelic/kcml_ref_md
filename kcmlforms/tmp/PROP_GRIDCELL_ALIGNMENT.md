Alignment (gridcell control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Write<br />
only</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Left, Center, Right)*

**Used to align the contents of a cell**

Used to specify the alignment of the text within a particular cell, row or column of a grid. The available settings are ***Left,*** ***Center*** and ***Right.*** For example, the following would right align the text in cell 2 of row 6, but left align all the other cells of the row. All the other rows of the grid would be centered: .GridControl1.Cell.Alignment = &.Center .GridControl1.Cell(6, 0).Alignment = &.Left .GridControl1.Cell(6, 2).Alignment = &.Right

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **Left**.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
