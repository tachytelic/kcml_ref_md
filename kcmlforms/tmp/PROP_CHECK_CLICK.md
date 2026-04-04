Click (checkbox control event)

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

**Called when the used clicks on the checkbox**

This event is called if the check box is selected. The [*State* property can be used within the event handler to determine if the control is check or unchecked.](PROP_BUTTON_STATE.htm)

##### Example:


     DEFEVENT Form1.cbControl.Click()

##### See also:

Other [checkbox](checkbox.htm) properties, methods and events and [generic](generic.htm) properties and methods.
