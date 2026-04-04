Click (kcmledit control event)

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

**Called when the Ellipsis button is clicked**

This event is called if the user clicks on the Ellipsis button on a Edit control. The Ellipsis button is only set if the [*DropStyle* property is set to *Ellipsis*.](PROP_EDIT_DROPSTYLE.htm)

Note that when using dropdown ellipses within a grid control cell, the [*EllipsisClick()* event handler is used.](PROP_GRID_CLICK.htm)

##### Example:


     DEFEVENT Form1.editControl.Click()

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
