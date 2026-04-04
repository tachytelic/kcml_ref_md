RowRequest (grid control event)

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

**Called when the user attempts to move beyond the last row if the DataPending property is set**

This event handler is used to add rows to the grid control when the user has attempted to move past the last row in the grid, i.e. by pressing the down arrow or the page down key or if the vertical scroll bar is moved to the very bottom. This event handler is only called when the [DataPending](PROP_GRID_DATAPENDING2.htm) property is set to *TRUE*. To add rows the event handler must first extend the grid by modifying the [Rows](PROP_GRID_ROWS.htm) property, then new data can then be placed into the rows. Once the new rows have been added the [DataPending](PROP_GRID_DATAPENDING2.htm) property must then be set again to make sure that the event handler is called again if necessary. To disable the event handler the [DataPending](PROP_GRID_DATAPENDING2.htm) property must be *FALSE*, which is the default setting.

See this [example program](../examplefillinggrid.htm) for a demonstration of filling a grid using this method.

##### Example:


     DEFEVENT Form1.gridControl.RowRequest()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
