EditGrid (grid control method)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> EditGrid(int, int) Method

**Allows the user to modify the contents of the entire grid**

|  |  |
|----|----|
| Int1 | Row position of cell to be edited ([CursorRow](PROP_GRID_CROW.htm)) |
| Int2 | Column position of cell to be edited ([Cursorcol](PROP_GRID_CCOL.htm)) |

This method is used to allow the user to modify all cells within an entire Grid control as opposed to individual cells or rows which is the case with the [*EditCell()* and](PROP_GRID_EDITCELL.htm) [*EditRow()* methods. With *EditGrid()* in force the user is allowed to Tab from the end of a row onto the beginning of new row and Shift Tab at the beginning of a row to the end of the previous row. The mouse can also be used to move to any other cell in the grid. Cells where editing is allowed must first have the](PROP_GRID_EDITROW.htm) [*LeftAction* or](PROP_GRID_LEFTACTION.htm) [*RightAction* and](PROP_GRID_RIGHTACTION.htm) [*LeftSelect* or](PROP_GRID_LEFTSELECT.htm) [*RightSelect* properties set accordingly to allow the user to click on the cell. Ideally this method should be called from within a](PROP_GRID_RIGHTSELECT.htm) [*LeftClick()* or](PROP_GRID_LEFTCLICK.htm) [*RightClick()* event handler.](PROP_GRID_RIGHTCLICK.htm)

Example: ..EditGrid(..CursorRow, ..CursorCol)

The [*Validate* property is used to determine what type of validation is performed as the user moves from one cell to the next.](PROP_GRIDCELL_VALIDATE.htm)

If the user clicks on a control outside of the grid while *EditGrid()* is in force then the [*EndEdit()* event handler is called, if it exists.](PROP_GRID_ENDEDIT.htm)

**Note:** This method must not be applied to grids which have [AutoEdit](PROP_GRID_AUTOEDIT.htm) enabled. You may find that AutoEdit provides a simpler model for editing.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
