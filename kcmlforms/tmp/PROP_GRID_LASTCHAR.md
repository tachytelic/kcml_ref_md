LastChar\$ (grid control property)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Returns the last key pressed by the user**

This property returns the last character pressed by the user while the Grid control was in focus. This property can be used in conjunction with the [*Char()* event handler to allow the keyboard to be used to select cells as well as the mouse.](PROP_GRID_CHAR.htm)

##### Example:


     a$ = .gridControl.LastChar$

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
