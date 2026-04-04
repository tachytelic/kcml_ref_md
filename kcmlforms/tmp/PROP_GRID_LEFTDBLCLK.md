LeftDblClk (grid control event)

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

**Called when the user left double clicks on a cell**

This event is called if the user left double clicks on a cell within a grid control. This event handler is only available if the [*LeftAction* property is set appropriately.](PROP_GRID_LEFTACTION.htm)

Note that the [*LeftClick()* event handler is called prior to this event handler when the user double clicks on a cell.](PROP_GRID_LEFTCLICK.htm)

##### Example:


     DEFEVENT Form1.gridControl.LeftDblClk()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
