DropDown (gridcell control property)

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
*(Default, NoDrop, DropFocus, DropEnabled, DropAlways)*

**Determines if a dropdown list is enabled**

Used to instruct an editable grid cell to act as either a regular edit control or as a drop down list box. This property is a design time only property and can therefore not be changed under program control.

Available styles are as follows:

|  |  |
|----|----|
| NoDrop | Setting this style means that the control will act as a standard Edit control with no drop down capabilities. |
| DropFocus | Setting this style means that the control can have a drop down list but the down arrow used to signify that the control has drop down capabilities is not displayed until the control gets focus. |
| DropEnabled | Setting this style means that the control can have a drop down list. The down arrow used to signify that the control has drop down capabilities is only displayed if the control is enabled. |
| DropAlways | Setting this style will display the down arrow at all times. |

In practice, the drop down is part of the edit and can only appear when a cell is being edited, which means that the cell has focus and is enabled anyway.

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **NoDrop**.

##### Example:


     .gridcell.DropDown = &.Default

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
