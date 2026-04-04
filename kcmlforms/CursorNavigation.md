The cursor and grid navigation

The grid cursor defines the grid cell that has focus within a grid control. When the grid has focus the cursor cell will display the focus stippled rectangle. It is also marked by being selected, that is it takes on the select background color, often blue. This color persists even when focus leaves the grid and passes to another control.

The cursor is sometimes called, more descriptively, the user selection rectangle. When editing in a grid with, say, the [EditGrid()](tmp/PROP_GRID_EDITGRID.htm) method, the cursor can be changed to an Insertion caret using the [EditCursor](tmp/PROP_GRID_EDITCURSOR.htm) property. This is done automatically if [AutoEdit](tmp/PROP_GRID_AUTOEDIT.htm) is used.

If a cursor is enabled for the grid the user can move it around using standard keyboard navigation keys:

|  |  |
|----|----|
| Up arrow | Move selection up one row. If already in the first visible, non-fixed row then vertically scroll the grid if permitted. |
| Down arrow | Move selection down one row. If in the last visible row then vertically scroll the grid if permitted. |
| Left arrow | Move selection left one column. If already in the first visible, non-fixed column then horizontally scroll the grid if permitted. |
| Right arrow | Move selection right one column. If in the last visible column then horizontally scroll the grid if permitted. |
| Home | Move selection to first non-fixed column of the current row, scrolling if necessary to keep it in view. |
| CTRL-Home | Move selection to first non-fixed column of the first non-fixed row, scrolling if necessary to keep it in view. |
| End | Move selection to last column of the current row, scrolling if necessary to keep it in view. |
| CTRL-End | Move selection to last column of the last row, scrolling if necessary to bring it into view. |

The mouse is not used to move the cursor. Clicking on the cell array of the grid may trigger one of the click events if so enabled but it will not shift the cursor. It will not even shift focus unless the scrollbars are clicked. If the scrollbars are used to scroll the visible part of the grid the cursor will always stay visible and therefore may move as a consequence.

By default a grid does not have a cursor. It has to be enabled with the [CursorEnable](tmp/PROP_GRID_CURSORENABLE.htm) property which also determines whether the cursor can enter the fixed heading row(s) and column(s).

The program can be notified if the cursor position changes by defining a [CursorMove()](tmp/PROP_GRID_CURSORMOVE.htm) event handler. This event will be triggered by the selection changing to another cell. The [CursorRow](tmp/PROP_GRID_CROW.htm) and [CursorCol](tmp/PROP_GRID_CCOL.htm) properties can be inspected to find the new cursor position.
