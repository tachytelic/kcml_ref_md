SelChange (grid control event)

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

**Called when a new item is selected in the drop down portion of the control**

This event is called if the user clicks on an item in a grid cells drop down list box thus selecting it. The event handler can determine the item selected with the [*Index* property.](PROP_GENERIC_DATAPTR.htm)

##### Example:


     DEFEVENT Form1.gridControl.SelChange()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
