Tag\$ (gridcell control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Per cell property for programmer use**

This property is a free text field which can be referenced and modified by the program without affecting the appearance of the grid. It allows for extra information of use to the programmer to be applied to any cell, row or column of the grid. Note that unlike grid cell properties applied to the client (where if the cell value is the default, then the non-default row, column or grid value is used instead), this will only return a value that is explicitly set for that cell, row or column.

##### Example:


     a$ = .gridcell.Tag$

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
