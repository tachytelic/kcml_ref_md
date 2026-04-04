TabThrough (grid control property)

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
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**When tabbing into grid, tabbing behaves as if each cell is a separate control**

The TabThrough style applies to the whole grid and affects the behaviour of the Tab and Shift-Tab keys. Normally tabbing steps through every control that has the TabStop style set (usually everything except static labels). A grid is a single control so tabbing onto a grid will cause the current cell to show its focus rectangle, and the next use of Tab will move onto the next control. If the TabThrough style is set, then the grid behaves as if each cell is a single control. In this case, tabbing on the grid will cause the first selectable cell to be selected and subsequent use of the Tab key will cycle through the selectable cells on the grid. After the last selectable cell on the grid, Tab will move to the next control on the form.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
