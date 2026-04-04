Clear (grid control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Clear() Method

**Clears the contents of the grid control**

This method is used to clear the contents of cells within a Grid control. The [MoveCell()](PROP_GRID_MOVECELL.htm) method should be used to position the programming cell to the required location. Note that **Clear()** should always be used in conjunction with the [*Cell* control. For example, the following would clear the contents of all cells in row 6: .GridControl1.Cell(6, 0).Clear()](PROP_GRID_CELLXY.htm)

To clear the entire grid, use .GridControl1.Clear()

**Note:** Only clearing the whole grid is currently supported.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
