RightSelect (gridcell control property)

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
*(Default, Cell, Row, Col, None)*

**Specifies the default selection for a right mouse click**

This property is used to determine how cells in a Grid control may be selected using the right mouse button. See [.LeftSelect](PROP_GRID_LEFTSELECT.htm) for how to handle the left mouse button. This property is only effective if the [*RightAction* property has been set accordingly. To set this property for an individual row, column or cell you must use this property in conjunction with the](PROP_GRID_RIGHTACTION.htm) [*Cell()* method. For example, the following would set the *RightSelect* property for all cells in row 5: .GridControl1.Cell(5, 0).RightSelect = &.Cell](PROP_GRID_CELLXY.htm)

And to set this property for the whole grid the following would be used: .GridControl1.RightSelect = &.Cell

Available settings for *RightSelect* are as follows:

|  |  |
|----|----|
| Cell | Signifies that the right mouse button will select an individual cell only |
| Row | Signifies that the right mouse button will select the current row |
| Col | Signifies that the right mouse button will select the current column |
| None | The cell, row or column will not get selected though clicking a cell will give it focus. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **Cell**.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
