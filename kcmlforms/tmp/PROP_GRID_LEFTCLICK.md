LeftClick (grid control event)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the user left clicks on a cell**

This event is called if the user left clicks on a Grid control cell and if the [*LeftAction* property is set appropriately.](PROP_GRID_LEFTACTION.htm)

This event handler is commonly used to activate grid cell editing by calling either the [*EditCell(), [EditGrid()](PROP_GRID_EDITGRID.htm),* or](PROP_GRID_EDITCELL.htm) [*EditRow()* methods, for example: - DEFEVENT Form1.GridControl1.LeftClick() ..EditGrid(..CursorRow, ..CursorCol) END EVENT](PROP_GRID_EDITROW.htm)

Note that this event handler can also be used to display popup menus by calling the [*TrackPopup()* menu control method.](PROP_MENU_TRACKPOPUP.htm)

 

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
