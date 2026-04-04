DropDown (kcmledit control event)

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

**Called before the drop down portion of the control is displayed**

This event is called when the drop down section of and edit control is displayed. This allows the drop down list to be filled on demand rather than filling all drop down control before the form is displayed. Note that the [*DropStyle* property must be set accordingly to enable the drop down section of the control.](PROP_EDIT_DROPSTYLE.htm)

If the [*DropDownFilled* property is TRUE then this event handler will be ignored.](PROP_KCMLEDIT_DROPDOWNDIRTY.htm)

##### Example:


     DEFEVENT Form1.editControl.DropDown()

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
