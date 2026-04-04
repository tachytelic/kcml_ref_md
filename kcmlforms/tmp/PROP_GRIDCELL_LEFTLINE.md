LeftLine (gridcell control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, NoLine, NormalLine, SolidLine, ThickLine, Join)*

**Specifies the style for the vertical line to the left of the cell**

This property is used to change the line type for the separator line that appears to the left of the current cell or cells specified by the [*Cell()* method. It can also be used to join two cells together horizontally. See also the](PROP_GRID_CELLXY.htm) [.TopLine](PROP_GRIDCELL_TOPLINE.htm) property.

Available types are:

|  |  |
|----|----|
| Default | Default behaviour. If applied to a cell, then any non-default style for the row or column or whole grid is used instead. If all these are Default, then the behaviour is the same as **NormalLine**. |
| NormalLine | Use the normal thin separator line |
| SolidLine | Use a bolder version of NormalLine but keep the same thickness |
| ThickLine | Use a thicker, bolder separator line |
| NoLine | No separator line |
| Join | Consolidate the two separated cells into one |

For example, the following would change the line to the left of all cells in column 4 to be a thick line: .GridControl1.Cell(0, 4).LeftLine = &.ThickLine

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **NormalLine**.

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
