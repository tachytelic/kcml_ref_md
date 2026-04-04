ColWidth (gridcell control property)

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
<td>Write<br />
only</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the column width**

It can be used to set the column width of the grid column containing the current cell. The width is expressed in [Dialog Box Units](/DialogBoxUnitsDLUs.htm).

The [ColSize](PROP_GRID_COLSIZE.htm) enumerated property can be used to tell the grid to size columns automatically according to various rules.

Setting a column's width to 0 does not hide it. Even though it may appear to be invisible the column will still feature in the grid's tab order and scrollbar calculation.

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

##### Example:


     .gridcell.ColWidth = n

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
