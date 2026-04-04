Reset (grid control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Reset() Method

**Resets the grid to its default design time configuration**

The Reset() method clears the text from the grid and resets the number of rows and columns back to their design time sizes. It does not remove any programmed styles or headings.

In KCML 6.00, [Reset(int)](PROP_GRID_RESET2.htm) was introduced to allow resetting of styles and other cell attributes. Reset() is equivalent to Reset(0).

##### Example:


     .gridControl.Reset()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
