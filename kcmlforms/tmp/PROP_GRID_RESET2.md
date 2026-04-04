Reset (grid control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Reset(int) Method

**Resets the grid to its default design time configuration**

This method is used to clear the contents of the grid and reset the grid back to the design time sizes. The Reset(int) method includes all operations of the [Clear()](PROP_GRID_CLEAR.htm) method. Increasing values of the level parameter provide increasing levels of what information is cleared. This Reset() method was introduced in KCML 6.00. For earlier versions use [Reset()](PROP_GRID_RESET.htm) with no arguments, which is equivalent to Reset(0).

| Method | Effect |
|----|----|
| Clear() | Remove all Text from cells. Heading\$ properties are left untouched. All per cell data aware information is removed. |
| Reset(), Reset(0) | As Clear(), but the grid is reset to its design time number of rows and columns, and fixed number of rows and columns. Design time size means the size of the grid at the end of the [Create()](PROP_FORM_CREATE.htm) event. |
| Reset(1) | As Reset(0), but all cell, row, columns, headings, grid styles, types and colors are reset to their default values. Per column and row data aware information is also removed. |

##### Example:


     .gridControl.Reset(i)

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
