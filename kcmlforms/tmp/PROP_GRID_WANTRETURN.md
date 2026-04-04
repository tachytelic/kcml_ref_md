WantReturn (grid control property)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Return key should send char event**

If set to *TRUE* the edit control in a grid cell will treat a RETURN as a normal carriage return character. It can also allow RETURN to be returned by a [Char()](PROP_GRID_CHAR.htm) event.

If the cell is not editable, but has focus, and *.WantReturn* is TRUE then a click and a double click event will be generated if RETURN is pressed. A single click event will be generated for SPACE. This permits a keyboard only simulation of a mouse.

This is a design time only property that has no effect if changed under program control. It applies to the whole grid and cannot be applied to individual cells in isolation.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
