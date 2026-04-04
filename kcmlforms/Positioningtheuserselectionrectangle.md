Positioning the user selection rectangle

------------------------------------------------------------------------

The user selection rectangle is positioned by with the

*MoveCursor()* method. For example, the following positions the focus rectangle at row 5, column 6:

.GridControl1.MoveCursor(5, 6)

<span style="font-family: Courier New,monospace; "> </span>Once the selection cell rectangle has been positioned the [*SetFocus()* method can be used to make the grid control the current control in focus. Once the grid control is in focus the arrow keys can be used to move the cell selection rectangle around the grid. Note that the](tmp/PROP_GENERIC_FOCUS.htm)

*CursorMove()* event handler can be used to trap cursor movements.
