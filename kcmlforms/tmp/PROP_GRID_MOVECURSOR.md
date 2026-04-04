MoveCursor (grid control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> MoveCursor(int, int) Method

**Moves the user selection cell to the specified cell**

***Int1***      Row value\
***Int2***      Column value

This method is used to move the user selection rectangle to the specified row and column within a Grid control. For example, the following would move the selection rectangle to row 5, column 6: .GridControl1.MoveCursor(5, 6)

<span style="font-family: Courier New,monospace; "> </span>Note that the [*CursorRow* and](PROP_GRID_CROW.htm) [*CursorCol* properties can be used to retrieve the current location of the user selection rectangle.](PROP_GRID_CCOL.htm)

Specifying a row and column position of zero will remove the current user selection.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
