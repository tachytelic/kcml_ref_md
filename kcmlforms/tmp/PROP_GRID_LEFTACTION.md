LeftAction (grid control property)

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
*(Default, Ignore, Down, Click, ClickAndDblClick)*

**Specifies the default mouse action for a left click**

This property is used to specify what action is to be taken if the left mouse button is held down, clicked or double clicked on a KCML grid cell. It defines the behaviour for the whole grid, excpet where overrided by individual cell or row or column settings.

For a grid with a fixed row and column, to enable clicking on any cell except in the fixed area, use the Click style for the entire grid, and override this for the first row and column. .GridControl1.LeftAction = &.Click .GridControl1.Cell(1,0).LeftAction = &.DisableCursor .GridControl1.Cell(0,1).LeftAction=&.DisableCursor

Available settings for *LeftAction* are as follows:

***Default***\
Default behaviour.

***Ignore***\
Ignores all left button mouse action.

***Down***

A [*LeftClick()* event will be triggered when the left mouse button is pushed on a cell.](PROP_GRID_LEFTCLICK.htm)

The Down style is useful where the program action is immediate, such as changing the color of a cell or putting the cell into edit mode. Moving the mouse around a grid with the left button held down will also generate click events for cells with this LeftAction style set.

***Click***

A [*LeftClick()* event will be triggered when the left mouse button is clicked on a cell.](PROP_GRID_LEFTCLICK.htm)

A Click style is useful where less immediate action is taken such as bring up another form, as the bechaviour is similar to that of a push button.

***ClickAndDblClick***

A [*LeftClick()* event will be triggered when the left mouse button is clicked on a cell.](PROP_GRID_LEFTCLICK.htm)

A [*LeftClick()*event and then a](PROP_GRID_LEFTCLICK.htm) [*LeftDblClk()* event will be triggered when the left mouse button is clicked on a cell.](PROP_GRID_LEFTDBLCLK.htm)

***DisableCursor***

|      |
|------|
| 5.03 |

This is like Ignore except that the mouse cursor cannot be moved into the cell using the cursor keys either. It is typically set for fixed rows and columns where moving the cursor into these areas has no useful meaning.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
