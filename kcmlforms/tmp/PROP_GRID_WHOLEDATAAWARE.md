WholeDataAware (grid control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**The entire grid is data aware against a single data record**

A typical use of data awareness on grids is to have one data record per grid row. The [*DataField*](PROP_DATAFIELD_CELL.htm) property is typically set for columns and the [*DataAwareRow*](PROP_GRID_DATAAWAREROW.htm) method is called to update a grid row from the current record. However, there are cases where the entire grid is represented by a single data record and individual cells have the [*DataField*](PROP_DATAFIELD_CELL.htm) property set. In these cases the *WholeDataAware* property should be set to TRUE. No method is needed to update the data as it is permamently bound to the single data source, and so all updates can take place automatically as they do for dbedits.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
