MouseFormX (generic control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
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
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the current mouse position within a Click() event in absolute form coordinates.**

This property returns the horizontal mouse position at the time a click event was triggered for a control. This property can be used in conjunction with the [*MouseFormY* property to position a control, normally a popup menu, onto the control at the exact location where the mouse button was clicked. The position is returned relative to the top left hand corner of the form. For example, the following would position a popup menu at the location of the right mouse click: -DEFEVENT Form1.RTFControl1.RightClick() .menu1.TrackPopup(..MouseFormX, ..MouseFormY) END EVENT](PROP_GENERIC_DLGMOUSEY.htm)

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
