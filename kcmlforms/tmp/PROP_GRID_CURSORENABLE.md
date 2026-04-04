CursorEnable (grid control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Enable, Disable, DisableFixed, DisableFixedRow)*

**Specifies the behaviour of the cursor when the arrow keys are used**

\

|  |  |
|----|----|
| Default | Use [precedence](/GridCellPrecedence.htm) rules. If not set elsewhere then it acts the same as Enable. |
| Enable | Enables the cursor and allows the user to navigate it over all the cells of the grid. |
| Disable | No cursor is available. The user cannot interact with the grid. |
| DisableFixed | Enables the cursor but restricts navigation to those cells of the grid that are not fixed. |
| DisableFixedRow | Like DisableFixed except only fixed rows are out of bounds. |

This property determines how the user is allowed to interact with a grid. If disabled, no cursor is presented and no interaction is possible. If enabled the cursor will be visible and can be moved either with a mouse click or with the keyboard navigation keys.

##### Example:


     .gridControl.CursorEnable = &.Default

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
