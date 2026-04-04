CursorCol (grid control property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the cursor column position to left/right click event handlers**

This property is used in conjunction with the [CursorRow](PROP_GRID_CROW.htm) property to retrieve the current location of the user cell selection rectangle or cursor following a [CursorMove()](PROP_GRID_CURSORMOVE.htm) event. For example: CurrentRow = .GridControl1.CursorRow CurrentCol = .GridControl1.CursorCol

To move the cursor to a specific location use the [MoveCursor()](PROP_GRID_MOVECURSOR.htm) method as this propety is read-only.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
