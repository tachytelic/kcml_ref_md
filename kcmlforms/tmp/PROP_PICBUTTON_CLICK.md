Click (picbutton control event)

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

**Called when the button is clicked**

This event handler is called each time a Picture control is clicked. Note that the [*MouseX* and](PROP_BUTTON_MOUSEX.htm) [*MouseY* properties are passed into this event handler. These properties contain the location of the mouse pointer at the time the *Click()* event occured. These properties can be used to place controls onto the picture, alternatively a popup menu can be displayed with the](PROP_BUTTON_MOUSEY.htm) [*TrackPopup()* menu method.](PROP_MENU_TRACKPOPUP.htm)

##### Example:


     DEFEVENT Form1.picControl.Click()

##### See also:

Other [picbutton](picbutton.htm) properties, methods and events and [generic](generic.htm) properties and methods.
