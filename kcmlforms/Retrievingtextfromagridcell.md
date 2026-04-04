Retrieving text from a grid cell

------------------------------------------------------------------------

To retrieve text from a Grid cell, you must have the [*ServerText* property set to ***TRUE.*** Note that](tmp/PROP_GRID_SERVERTEXT.htm) [*ServerText* is a design time only property and can therefore only be set within the forms designer, setting](tmp/PROP_GRID_SERVERTEXT.htm)

*ServerText* within a program will have no effect.

With

*ServerText* set you can retrieve the contents of a cell with the text property, for example the following would retrieve the contents of the last cell that the user clicked on.

CellContents\$ = .gridControl1.Cell(..CursorRow, ..CursorCol).Text\$

 
