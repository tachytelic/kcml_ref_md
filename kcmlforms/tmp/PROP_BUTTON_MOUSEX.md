MouseX (picbutton control property)

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

**Returns the current mouse position within a Click() event**

This property is used to return the horizontal mouse position at the time a [*Click()*](PROP_PICBUTTON_CLICK.htm) event was triggered. This property can be used in conjunction with the [*MouseY* property to position a popup menu onto the button at the exact location where the mouse was clicked. Note that the position is returned relative to the top left hand corner of the button. Therefore to place a control at the exact location where the user clicked you must add the](PROP_BUTTON_MOUSEY.htm) [*Top* and](PROPNUM_Y.htm) [*Left* positions of the control to the *MouseX* and *MouseY* properties. For example, the following event handler would place a menu at the location of the last left mouse click: -DEFEVENT Form1.picControl1.LeftClick() .menu1.TrackPopup(..top + ..MouseY, ..left + ..MouseX) END EVENT](PROPNUM_X.htm)

**Note:** It is recommended to use [*MouseFormX*](PROP_BUTTON_DLGMOUSEX.htm) for all future development as it saves having to factor in the control's own position (especially when the control is on a tab page).

 

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
