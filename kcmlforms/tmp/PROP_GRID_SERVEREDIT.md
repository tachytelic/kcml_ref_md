ServerEdit (grid control event)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the grid cell gets focus (if AutoEdit set to ServerEdit)**

This event can only occur when a grid is in AutoEdit mode and the [AutoEdit](PROP_GRID_AUTOEDIT.htm) property of the current cell was set to the **ServerEdit** enumeration. The event is triggered when a cell with that property becomes the current cell. Typically the program will then bring up a child form within the event handler. If the handler sets the [ValidateText\$](PROP_GRID_VALIDATETEXT.htm) property and returns TRUE then KCML will check ValidateText\$ against [Text\$](PROPSTR_TITLE.htm) and throw a [EditValidate()](PROP_GRID_VALIDATE.htm) event if they are different. If that EditValidate() event returns FALSE then the cell stays the current cell, the text is reset and a new ServerEdit event is thrown. If, on the other hand, the validate event succeeds and returns TRUE, focus shifts to the next cell that will take focus.

##### Example:


     DEFEVENT Form1.gridControl.ServerEdit()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
