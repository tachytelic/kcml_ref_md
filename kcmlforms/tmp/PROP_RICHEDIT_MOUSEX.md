MouseX (richedit control property)

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

**Position of mouse cursor at time of RightClick event**

This property returns the horizontal mouse position at the time a *[RightClick()](PROP_RICHEDIT_RCLICK.htm)* event was triggered for a RTF control. This property can be used in conjunction with the [*MouseY* property to position a control, normally a popup menu, onto the RTF editing area at the exact location where the mouse was right clicked. Note that the position is returned relative to the top left hand corner of the RTF control, therefore to place a control at the exact location where the user clicked you must add the](PROP_RICHEDIT_MOUSEY.htm) [*Top* and](PROPNUM_Y.htm) [*Left* properties of the control to the *MouseX* and *MouseY* properties. For example, the following would position a popup menu at the location of the right mouse click: -DEFEVENT Form1.RTFControl1.RightClick() .menu1.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top) END EVENT](PROPNUM_X.htm)

**Note:** It is recommended to use [*MouseFormX*](PROP_RICHEDIT_DLGMOUSEX.htm) for all future development as it saves having to factor in the control's own position (especially when the control is on a tab page).

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
