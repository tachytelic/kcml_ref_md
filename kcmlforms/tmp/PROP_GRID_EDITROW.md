EditRow (grid control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> EditRow(int, int) Method

**Allows the user to modify the contents of the specified row**

|  |  |
|----|----|
| Int1 | Row position of cell to be edited ([CursorRow](PROP_GRID_CROW.htm)) |
| Int2 | Column position of cell to be edited ([Cursorcol](PROP_GRID_CCOL.htm)) |

This method is used to allow a row in a grid control to be edited. The cell must first have the [*LeftAction* or](PROP_GRID_LEFTACTION.htm) [*RightAction* and](PROP_GRID_RIGHTACTION.htm) [*LeftSelect* or](PROP_GRID_LEFTSELECT.htm) [*RightSelect* properties set accordingly to allow the user to click on the cell. Ideally this method should then be called from within a](PROP_GRID_RIGHTSELECT.htm) [*LeftClick()* or](PROP_GRID_LEFTCLICK.htm) [*RightClick()* event handler. Once the user exits the row being edited the](PROP_GRID_RIGHTCLICK.htm) [*EndEdit()* event handler is called, if it exists.](PROP_GRID_ENDEDIT.htm)

Example: ..EditRow(..CursorRow, ..CursorCol)

The [*Validate* property is used to determine what type of validation is performed as the user moves from one cell to the next.](PROP_GRIDCELL_VALIDATE.htm)

This method must not be applied to grids which have [AutoEdit](PROP_GRID_AUTOEDIT.htm) enabled. You may find that AutoEdit provides a simpler model for editing.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
