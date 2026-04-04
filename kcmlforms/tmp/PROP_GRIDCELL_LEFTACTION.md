LeftAction (gridcell control property)

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
<td>Write<br />
only</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Ignore, Down, Click, ClickAndDblClick)*

**Specifies the default mouse action for a left click**

This property is used to specify what action is to be taken if the left mouse button is held down, clicked or double clicked on a KCML grid cell. If the style for a cell is not Default, then this style will apply to the cell. If the style is Default, then the left mouse action will depend on any non-default LeftAction setting for the row or column, or the entire grid.

Available styles for *LeftAction* are as follows:

Default

Default behaviour. If applied to a cell, then any non-default style for the row or column or whole grid is used instead. If all these are Default, then the behaviour is the same as Ignore.

Ignore

Ignores all left button mouse action.

Down

A

*LeftClick()* event will be triggered when the left mouse button is pushed on a cell. The Down style is useful where the program action is immediate, such as changing the color of a cell or putting the cell into edit mode. Moving the mouse around a grid with the left button held down will also generate click events for cells with this LeftAction style set.

Click

A

*LeftClick()* event will be triggered when the left mouse button is clicked on a cell. A Click style is useful where less immediate action is taken such as bring up another form, as the bechaviour is similar to that of a push button.

ClickAndDblClick

A [*LeftClick()* event will be triggered when the left mouse button is clicked on a cell. A](PROP_GRID_LEFTCLICK.htm) [*LeftClick()*event and then a](PROP_GRID_LEFTCLICK.htm)

*LeftDblClk()* event will be triggered when the left mouse button is double clicked on a cell.

DisableCursor

Introduced with KCML 5.03. This is like Ignore except that the mouse cursor cannot be moved into the cell using the cursor keys either. It is typically set for fixed rows and columns where moving the cursor into these areas has no useful meaning.

This grid cell property is not stored on the server and therefore cannot be inspected by server code. If set on the server it will be passed down to the client but no record is kept on the server.

The **Default** behaviour of an enumerated gridcell property is to check for an overriding setting using the [prededence rules](../GridCellPrecedence.htm) and if not set elsewhere to use the next setting from the enumeration, in this case **Ignore**.

##### Example:


     .gridcell.LeftAction = &.Default

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
