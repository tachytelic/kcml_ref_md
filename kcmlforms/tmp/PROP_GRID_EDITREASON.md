EditReason (grid control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Returns the reason for the termination of EditRow()**

This property is used within the [*EndEdit()* event handler to determine the reason for the termination of a grid editing session. The codes returned by this property are as follows:](PROP_GRID_ENDEDIT.htm)

|     |                                                              |
|-----|--------------------------------------------------------------|
| 0   | Unknown                                                      |
| 1   | Tab at end of row                                            |
| 2   | Shift-Tab at beginning of row                                |
| 3   | Return key pressed                                           |
| 4   | Escape key pressed                                           |
| 5   | Mouse click on another part of the grid                      |
| 6   | Mouse click or focus moved to another control or application |

##### Example:


     n = .gridControl.EditReason

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
