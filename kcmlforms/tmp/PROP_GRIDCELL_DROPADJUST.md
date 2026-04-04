DropAdjust (gridcell control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Adjust placement of edit button**

The **DropAdjust** property can be used to adjust the width of a drop down associated with editing a grid cell. This is particularly useful if the cell is quite narrow, containing perhaps a single letter code, but that the drop down list contains descriptions as well. The DropAdjust property is interpreted as follows:

|  |  |
|----|----|
| 0 | Default. If this is specified for a cell, then the values for row and then column are used. |
| 1 | Normal behaviour. The drop down button appears on the right-hand side within the cell |
| 2 | The drop down button appears just to the right of the cell. The drop down has the same width as the cell and the drop down button |
| \> 2 | The drop down button appears just to the right of the cell. The value is added to the width of the cell to give the width of the drop down. |

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

##### Example:


     .gridcell.DropAdjust = n

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
