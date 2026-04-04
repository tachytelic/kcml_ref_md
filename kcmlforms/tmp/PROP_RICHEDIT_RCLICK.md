RightClick (richedit control event)

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

**Called when the user right clicks on the control**

This event is called when the user right clicks on a on the RTF control.

This event handler can be used to display popup menus by calling the [*TrackPopup()* menu control method, for example: - DEFEVENT Form1.rtfControl1.RightClick() .menu1.TrackPopup(..MouseX + ..Left, ..MouseY + ..Top) END EVENT](PROP_MENU_TRACKPOPUP.htm)

 

 

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
