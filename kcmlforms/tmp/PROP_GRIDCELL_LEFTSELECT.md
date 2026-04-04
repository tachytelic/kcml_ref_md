LeftSelect (gridcell control property)

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

**Specifies the default selection for a left mouse click**

This property is used to determine how cells in a KCML Grid control are selected using the left mouse button. See [.RightSelect](PROP_GRID_RIGHTSELECT.htm) for how to handle the right mouse button. When a cell, row or column is selected its background color is changed to bring the cell, row or column to the users attention. This property is only effective if the [*LeftAction* property has been set accordingly. To set this property for an individual row, column or cell this property must be used in conjunction with the](PROP_GRID_LEFTACTION.htm) [*Cell()* method. For example, the following would set the *LeftSelect* property for all cells in row 5: .GridControl1.Cell(5, 0).LeftSelect = &.Cell](PROP_GRID_CELLXY.htm)

And to set this property for the whole grid the following would be used: .GridControl1.LeftSelect = &.Cell

Available settings for *LeftSelect*are as follows:

|  |  |
|----|----|
| Cell | Signifies that the left mouse button will select an individual cell only |
| Row | Signifies that the left mouse button will select the current row |
| Col | Signifies that the left mouse button will select the current column |
| None | The cell, row or column will not get selected though clicking a cell will give it focus. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **Cell**.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
