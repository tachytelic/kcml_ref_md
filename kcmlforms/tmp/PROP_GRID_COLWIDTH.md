ColWidth (grid control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the column width**

It can be used to set the column width of the grid column containing the current cell. The width is expressed in [Dialog Box Units](/DialogBoxUnitsDLUs.htm).

This property will return zero until a column width is explicitely set under program control whereupon it will return the last value set on any column for the grid. Use [ColWidth](PROP_GRIDCELL_COLWIDTH.htm) instead

The [ColSize](PROP_GRID_COLSIZE.htm) enumerated property can be used to tell the grid to size columns automatically according to various rules.

Setting a column's width to 0 does not hide it. Even though it may appear to be invisible the column will still feature in the grid's tab order and scrollbar calculation.

##### Example:


     n = .gridControl.ColWidth

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
