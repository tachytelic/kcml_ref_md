Heading\$ (gridcell control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Specifies heading text for columns**

This property is used to set the heading text for the specified column. This property should be used in conjunction with the [*FixedRows* property to place a fixed heading at the the top of each column. Headings remain visible if the control is scrolled or if the contents of a column is cleared or if the contents of the whole grid is cleared with the](PROP_GRID_FIXEDROWS.htm) [*Clear()* method.](PROP_GRID_CLEAR.htm)

To set a heading for a column the [*Cell()* method is used to position to the relevant column. For example, the following would set the heading for column 6: .GridControl1.FixedRows = 1 .GridControl1.Cell(0, 6).Heading\$ = "A Nice Heading"](PROP_GRID_CELLXY.htm)

This property should be used rather than just setting [Text\$](PROPSTR_TITLE.htm) for the fixed columns so that [Clear()](PROP_GRID_CLEAR.htm) can be used to clear the grid contents but preserve the headings. Clear() and [Reset()](PROP_GRID_RESET.htm) will ignore text set with Heading\$ but [Reset(1)](PROP_GRID_RESET2.htm) will blank any Heading\$ properties. It also allows [Type\$](PROPSTR_TYPE.htm) to be set for a column without any effect on the heading.

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
