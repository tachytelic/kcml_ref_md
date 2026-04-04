NewCol (grid control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the column cursor will move to if current validate returns TRUE**

This property will return the column the cursor will move to if a [Validate()](PROP_GRID_VALIDATE.htm) event is accepted on the assumption that the event is triggered by the cursor moving to another cell in the grid. The row for the new cell can be obtained form the [NewRow](PROP_GRID_NEWROW.htm) property.

The property is only valid within a Validate() or [EditRowNotify()](PROP_GRID_EDITROWNOTIFY.htm) event.

##### Example:


     n = .gridControl.NewCol

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
