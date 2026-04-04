EditRowNotify (grid control event)

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
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when editing a new row**

The **EditRowNotify()** event can be used to implement efficient editing of a grid for the very common case where each row of the grid corresponds to a row in a database. The [TabThrough](PROP_GRID_TABTHROUGH.htm) property must be set, and will control tab navigation through the grid. Cells to be edited will use the [AutoEdit](PROP_GRID_AUTOEDIT.htm) properties.

The following properties are always set when the **EditRowNotify()** event is entered:

|  |  |
|----|----|
| [CursorRow](PROP_GRID_CROW.htm) | Cursor row of cell currently being edited (or 0) |
| [CursorCol](PROP_GRID_CCOL.htm) | Cursor column of cell currently being edited (or 0) |
| [NewRow](PROP_GRID_NEWROW.htm) | Cursor row of cell about to be edited (or 0) |
| [NewCol](PROP_GRID_NEWCOL.htm) | Cursor column of cell about to be edited (or 0) |
| [CancelEdit](PROP_GRID_CANCELEDIT.htm) | TRUE iff the edit was terminated by hitting Escape / clicking Cancel |

Notes:

- The **EditRowNotify()** event is called whenever the user starts or ends editing a row. If the user ends editing a row and starts editing a new row, then a single EditRowNotify() event is generated. The last cell being edited is specified by the [CursorRow](PROP_GRID_CROW.htm) and [CursorCol](PROP_GRID_CCOL.htm) properties. If there is no current edit cell then these properties will be 0. If a new edit cell will be started, its position will be found in [NewRow](PROP_GRID_NEWROW.htm) and [NewCol](PROP_GRID_NEWCOL.htm). If there is no new edit being started, then these properties will be 0.

- The [CursorRow](PROP_GRID_CROW.htm) and [NewRow](PROP_GRID_NEWROW.htm) properties can be used to control the locking of rows in a database. If a row is starting to be edited then the row will be locked (and maybe refreshed) and when the row edit is ending it will be written and unlocked. The [NewRow](PROP_GRID_NEWROW.htm) of one call to **EditRowNotify()** will always become the [CursorRow](PROP_GRID_CROW.htm) of the next call (provided the event handler does not cancel the edit).

- Operations that terminate a row edit include tabbing to another row on the grid, tabbing off the grid, clicking on another row of the grid or another control altogether. If the form terminates then an **EditRowNotify()** event is generated. If the user tabs to a cell on the grid that is not AutoEdit, then an **EditRowNotify()** event is generated even if cell is on the same row as the last edit.

- The [EditValidate()](PROP_GRID_VALIDATE.htm) event may be used to validate cell edits and will always be generated first. If the validate fails then the cursor will remain in the current edit cell, and so no **EditRowNotify()** is generated at this point.

- It is possible to modify the layout of a grid inside a **EditRowNotify()** event and provoke a further event (or several). For instance, if editing a grid, the user tabs out of editing the very last cell of a grid. The **EditRowNotify()** handler could add another line to the grid and make it editable. On return from the event handler, the tab operation will be tried again from the edit cell, and this time will move onto the new row for the grid. In this second call, [CursorRow](PROP_GRID_CROW.htm) will be 0 as the previous edit ending had already been notified.

- The grid's [MoveCursor()](PROP_GRID_MOVECURSOR.htm) method and the general [SetFocus()](PROP_GENERIC_FOCUS.htm) methods may be used inside an **EditRowNotify()** event handler. Both these methods stop the new edit from starting; there will be no subsequent **EditRowNotify()** event to say this edit has ended. If the [MoveCursor()](PROP_GRID_MOVECURSOR.htm) method is used, a subsequent **EditRowNotify()** event will be generated if the new cell is itself AutoEdit. It is also possible to use MoveCell(0, 0) to take focus off any particular cell. The next use of the tab key will place the cursor on the first permiited cell on the grid.

- It is possible to return FALSE to the **EditRowNotify()** event to indicate failure. This cancels the effect of the notification and returns editing to the previous edit row. This is useful when validation is done on a per row basis, rather than a per cell basis with [EditValidate()](PROP_GRID_VALIDATE.htm). The effect of the EditRowNotify is forgotten, so that the next time editing leaves the row, an **EditRowNotify()** is generated with [CursorRow](PROP_GRID_CROW.htm) set to the cell being edited. If the **EditRowNotify()** event is used to control locking and unlocking of database rows, then the application should return FALSE from this event if locking fails. This is because any previous edit would have been validated and the edit complete. Instead the application must choose an alternative course of action using either [MoveCursor()](PROP_GRID_MOVECURSOR.htm) or [SetFocus()](PROP_GENERIC_FOCUS.htm).

- If there is a right click event handler, then the right click will terminate the edit, generating an **EditRowNotify()** event followed by the [RightClick](PROP_GRID_RIGHTCLICK.htm) event.

- There are three circumstances where the edit may be terminated by a cancelling action. In all three cases the [CancelEdit](PROP_GRID_CANCELEDIT.htm) property will be TRUE. In all other cases it will be FALSE. These circumstances are:

  - The user clicks Cancel. The **EditRowNotify()** event will be generated before the Cancel [Click](PROP_BUTTON_CLICK.htm) event.
  - The user hits the Escape key and there is a Cancel button. The **EditRowNotify()** event will be generated before the Cancel button [Click](PROP_BUTTON_CLICK.htm) event.
  - The user hits the Escape key, but there is no Cancel (or it is not visble or enabled) button on the form. The **EditRowNotify()** is generated but the form will not be terminated.

  In all cases any changes to a cell being edited will be lost, and no validate events will occur.

|  |  |
|----|----|
| **Note:** | The **EditRowNotify()** event was introduced in 6.00 along with the [AutoEdit](PROP_GRID_AUTOEDIT.htm) and [TabThrough](PROP_GRID_TABTHROUGH.htm) properties as an easier and more efficient means of editing grids and is recommended for all new coding. However, it does not work with the older [EditCell()](PROP_GRID_EDITCELL.htm) , [EditRow()](PROP_GRID_EDITROW.htm) and [EditGrid()](PROP_GRID_EDITGRID.htm) methods. |

##### Example:


     DEFEVENT Form1.gridControl.EditRowNotify()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
