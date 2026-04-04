Char (grid control event)

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

**Called when the user presses a key**

The **Char()** event is called when the user presses a key that is not used by the grid itself (e.g. the arrow keys are used by the grid for navigation). The properties [LastChar\$](PROP_GRID_LASTCHAR.htm) and [LastKey](PROP_GRID_LASTKEY.htm) are set to indicate which key was pressed.

If there is no Char() event handler, then the space key will generate a [LeftClick()](PROP_GRID_LEFTCLICK.htm) event on the current cell (whenever a single left-click would be accepted), and similarly the return key will generate a [LeftClick()](PROP_GRID_LEFTCLICK.htm) followed by a [LeftDblClk()](PROP_GRID_LEFTDBLCLK.htm) event (for the return key to be accepted, the [WantReturn](PROP_GRID_WANTRETURN.htm) property must be set).

Grid cells in edit mode do not generate char() events.

##### Example:


     DEFEVENT Form1.gridControl.Char()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
