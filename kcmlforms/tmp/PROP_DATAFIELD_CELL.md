DataField (gridcell control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Specifies the SYM of the column field name that is to be bound to the control. Deprecated.**

This applies to data bound grid cells and is identical to the [DataField](PROP_DATAFIELD.htm) generic property.

For most data aware grids, each row of the grid is represented by one data record. The DataField property is normally applied to columns rather than individual cells because all grid rows will have the same layout. However, (in 6.00 onwards) the DataField property can be applied to individual cells. This would make sense if the whole grid was represented by a single data record (e.g. if it was replacing a number of dbedit controls), in which case the [*WholeDataAware*](PROP_GRID_WHOLEDATAAWARE.htm) property should be set.

The value returned from this property will be the SYM of the field as defined in the DEFFORM. This is the decorated name including the occurs. To get the actual data source, data field and occurs, 6.00 introduced the [*GetDataField()* method.](PROP_GRIDCELL_GETDATAFIELD.htm)

In 6.10 the [*SetDataField()*](PROP_GRIDCELL_SETDATAFIELD.htm) method was introduced to make it easy to set this property.

##### Example:


     .gridcell.DataField

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
