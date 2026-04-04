ShowSelection (grid control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, None, NoColor, NoForceOnScroll, Outline)*

**Shows how selected cells are highlighted**

Used to show how selected cells on a grid are displayed. The available settings are ***Default***, ***None*** and ***NoColor***. The ***Default*** scheme is to always show the cells using the Windows highlight text and background colors. The ***None*** scheme is never to show selected cells in different colors. The ***NoColor*** scheme is to only show selected cells using the Windows highlight colors if the cell's coloring would otherwise be a system color (including KClient defined system colors such as EditReadOnlyColor). The NoColor scheme is compatible with 5.02 KClient. .GridControl1.ShowSelection = &.None

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
