TabSkip (gridcell control property)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
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
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, None, Forward, Back)*

**Specifies whether to skip this cell when tabbing**

The **TabSkip** property is used to specify how cells in a grid respond to the Tab key. .gridControl1.Cell(3, 5).TabSkip = &.Forward

The following TabSkip options are available.

|  |  |
|----|----|
| Default | Take the value from the surrounding grid using the [precedence](../GridCellPrecedence.htm) rules. In the event that the property has not been defined for the row, column or grid then it will have the same effect as **None**. |
| None | Pressing Tab moves focus to the cell from the previous one. Pressing Shift-Tab moves focus back to the cell from the next one. |
| Forward | The cell refuses focus from the previous cell and passes it to the next cell that doesn't have **TabSkip** set to **Forward**. If no other cell accepts focus, the focus will not change. Pressing Shift-Tab to move focus back to the cell from the next cell is unaffected. |
| Back | The cell accepts a Tab forward from the previous cell but will refuse focus coming back from the next cell via Shift-Tab and pass it the previous tab that doesn't have **TabSkip** set to **Back**. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **None**.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
