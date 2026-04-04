MouseY (grid control property)

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
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the Y coordinate of the last mouse click to left/right click event handlers**

This property is used to return the vertical mouse position at the time a [*LeftClick() or [RightClick()](PROP_GRID_RIGHTCLICK.htm)* event was triggered for a KCML grid control. This property can be used in conjunction with the](PROP_GRID_LEFTCLICK.htm) [*MouseX* property to position a popup menu onto the grid at the exact location where the mouse was clicked. Note that the position is returned relative to the top left hand corner of the picture button. Therefore to place a control at the exact location where the user clicked you must add the](PROP_BUTTON_MOUSEX.htm) [*Top* and](PROPNUM_Y.htm) [*Left* positions of the control to the *MouseX* and *MouseY* properties. For example, the following event handler would place a menu at the location of the last left mouse click: -DEFEVENT Form1.GridControl1.LeftClick() .menu1.TrackPopup(..top + ..MouseY, ..left + ..MouseX) END EVENT](PROPNUM_X.htm)

**Note:** It is recommended to use [*MouseFormY*](PROP_GRID_DLGMOUSEY.htm) for all future development as it saves having to factor in the control's own position (especially when the control is on a tab page).

**Note:** The [*LeftAction* and](PROP_GRID_LEFTACTION.htm) [*RightAction* properties must be set appropriately to activate the](PROP_GRID_RIGHTACTION.htm) [*LeftClick()* and](PROP_PICBUTTON_CLICK.htm) [*RightClick()* event handlers.](PROP_GRID_RIGHTCLICK.htm)

 

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
