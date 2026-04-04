LinesPerRow (gridcell control property)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
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
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the number of lines for this row**

This grid cell property can only be applied to rows and overrides the [*LinesPerRow* property set for the whole grid. It is typically applied to the fixed row of a grid to keep it at, say, a single line high whilst allowing the main body of a grid to have rows, say, 2 lines high.](PROP_GRID_LINESPERROW.htm)

Normally having differently sized rows automatically forces the [*NoIntegralHeight* property to be set internally. However, if only the fixed row height is changed using this property, then this will not happen.](PROP_GRID_NOINTEGRALHEIGHT.htm)

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

##### Example:


     .gridcell.LinesPerRow = n

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
