CursorMove (grid control event)

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
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when the user moves the selection box to another cell**

Once the grid control is in focus the North, South, East and West arrow keys can be used to move the user cell selection rectangle (the cursor) around the grid control. This event is triggered when the cursor is moved to another cell. The location of the cursor can be determined with the [*CursorRow* and](PROP_GRID_CROW.htm) [*CursorCol* properties.](PROP_GRID_CCOL.htm)

For example, the following would update the current location of the cursor in the static text control *txtControl1*: - DEFEVENT Form1.GridControl1.CursorMove() LOCAL DIM Position\$100, row\$4, col\$4 CONVERT ..CursorRow TO row\$, (####) CONVERT ..CursorCol TO col\$, (####) Position\$ = "Row :" & row\$ & ", Col :" & col\$ .txtControl1.Text\$ = Position\$ END EVENT

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
