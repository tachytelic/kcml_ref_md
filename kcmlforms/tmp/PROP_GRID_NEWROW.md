NewRow (grid control property)

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

**Returns the row cursor will move to if current validate returns TRUE**

This property will return the row the cursor will move to if a [Validate()](PROP_GRID_VALIDATE.htm) event is accepted on the assumption that the event is triggered by the cursor moving to another cell in the grid. The column for the new cell can be obtained form the [NewRow](PROP_GRID_NEWCOL.htm) property.

For grids with the [AutoEdit](PROP_GRID_AUTOEDIT.htm) property enabled the [EditRowNotify()](PROP_GRID_EDITROWNOTIFY.htm) event will be triggered when the cursor is about to move between rows. The NewRow property can be inspected in this event handler to get the intended row. If the event handler returns FALSE movement can be blocked. The NewRow value can be used to lock and refresh the corresponding database row.

The property is only valid within a Validate() or [EditRowNotify()](PROP_GRID_EDITROWNOTIFY.htm) event.

##### Example:


     n = .gridControl.NewRow

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
