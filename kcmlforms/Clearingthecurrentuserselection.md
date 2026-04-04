Clearing the current user selection

------------------------------------------------------------------------

To remove the current user selection the

*MoveCursor()* method is called with a row and column position of 0, for example:

.GridControl1.MoveCursor(0,0)

Note that the user can only select cells that have the [*LeftAction* or](tmp/PROP_GRID_LEFTACTION.htm)

*RightAction* properties set accordingly.
