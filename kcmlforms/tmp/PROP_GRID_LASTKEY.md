LastKey (grid control property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the last key and shift state**

This property returns the last character pressed by the user while the Grid control was in focus. This property can be used in conjunction with the [Char()](PROP_GRID_CHAR.htm) event handler to allow the keyboard as well as the mouse to be used to select cells.

Unlike [LastChar\$](PROP_GRID_LASTCHAR.htm) this property can be used with non-character based keys such as the function keys. The value is a combination of the VK character code and the shift status of the key. See [Key\$](PROP_MENU_KEY.htm) for a table of codes.

##### Example:


     n = .gridControl.LastKey

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
