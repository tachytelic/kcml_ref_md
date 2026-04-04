## Database Browser

This displays the databases that have been defined in your **kconf.xml** file. This browser can display table, column, and index information. In debug mode it can also display the open handles connected to given data base.

<img src="bitmaps/dbbrowse.png" data-border="0" width="279" height="255" alt="Database Browser Tree" />

Above show an expanded browser tree for a sample database.

This browser also supports drag-and-drop and context-menu options for some tree nodes. Below is a table outlining this functionality.

| Node Type | Context-Menu Options | Drag&Drop Options | Description |
|----|----|----|----|
| Database | Create DEFOBJ Statement | Create DEFOBJ Statement | Creates a dummy DEFOBJ statement at current cursor position in editor code window. |
| Table | Create RowBuffer | Create RowBuffer | This will insert a DIM statement either in the current defsub or globally. The variable defined so that it can be used as a row buffer for this particular table, with its dimensions automatically assigned. The row buffers name is take from the table name |
| Field | Create FLD Statement | Create FLD Statement | This will create a FLD subroutine call. Using the table and field names as reference. |
