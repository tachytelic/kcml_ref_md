EllipsisClick (grid control event)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the Ellipses button is clicked**

This event is called if the user clicks on the Ellipsis button within an grid control cell. The Ellipsis button is only displayed if the cells [*DropStyle* property is set to *Ellipsis*.](PROP_EDIT_DROPSTYLE.htm)

 

##### Example:


     DEFEVENT Form1.gridControl.EllipsisClick()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
