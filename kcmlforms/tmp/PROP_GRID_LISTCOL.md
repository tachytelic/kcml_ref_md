ListCol (grid control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the column used for the listbox during the current cell edit**

In the grid [SelChange()](PROP_GCOMBO_SELCHANGE.htm) event, it is often necessary to access the grid listbox that generated the event. However, the listbox may not belong to the current cell being edited, but instead belong to the current row or column, or even the entire grid. The [ListRow](PROP_GRID_LISTROW) and **ListCol** properties can be used to reference the listbox being for the current cell.

##### Example:


     n = .gridControl.ListCol

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
