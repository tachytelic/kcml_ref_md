RightAction (gridcell control property)

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
*(Default, Ignore, Down, Click, ClickAndDblClick)*

**Specifies the default mouse action for a right click**

This property is used to specify what action is to be taken if the right mouse button is held down, clicked or double clicked on a grid cell. By default if *RightAction* is set, the mouse action will select an individual cell unless otherwise specified by the [*RightSelect* property, which can be used to allow whole rows or columns to be selected. To set *RightAction* for an individual row, column or cell you must use this property in conjunction with the](PROP_GRID_RIGHTSELECT.htm) [*Cell()* method. For example, the following would set the *RightAction* for all cells in row 5: .GridControl1.Cell(5,0).RightAction = &.Click](PROP_GRID_CELLXY.htm)

And to set this property for the whole grid the following would be used: .GridControl1.RightAction = &.Click

Available settings for *RightAction* are as follows:

|  |  |
|----|----|
| **Default** | Uses the setting that has been specified for either the row or column. |
| **Ignore** | Ignores any row or column settings. |
| **Click** | Clicking on a cell with the mouse can be used to select a cell. |
| **ClickAndDblClick** | Both Click and Double click can be used to select a cell. |
| **Down** | If the mouse button is held down then the mouse can be used to drag the cell selection box around. Although the selection box can only be dragged into a cell that has *Down* set. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **Ignore**.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
