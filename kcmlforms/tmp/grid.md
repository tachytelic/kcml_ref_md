grid control

\
[Generic](generic.htm) <span id="grid"></span>

|  |  |  |
|----|----|----|
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [Char()](PROP_GRID_CHAR.htm) | Called when the user presses a key |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [CursorMove()](PROP_GRID_CURSORMOVE.htm) | Called when the user moves the selection box to another cell |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [DropDown()](PROP_GCOMBO_DROPDOWN.htm) | Called before the drop down portion of the control is displayed |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [EditRowNotify()](PROP_GRID_EDITROWNOTIFY.htm) | Called when editing a new row |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [EditValidate()](PROP_GRID_VALIDATE.htm) | Called when the user moves away from a cell that is being edited and has been modified |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [EllipsisClick()](PROP_GRID_CLICK.htm) | Called when the Ellipses button is clicked |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [EndEdit()](PROP_GRID_ENDEDIT.htm) | Called when the user has finished editing a row |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [Enter()](PROP_GRID_ENTER.htm) | Called when the user tabs into the grid control |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [LeftClick()](PROP_GRID_LEFTCLICK.htm) | Called when the user left clicks on a cell |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [LeftDblClk()](PROP_GRID_LEFTDBLCLK.htm) | Called when the user left double clicks on a cell |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [RightClick()](PROP_GRID_RIGHTCLICK.htm) | Called when the user right clicks on a cell |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [RightDblClk()](PROP_GRID_RIGHTDBLCLK.htm) | Called when the user right double clicks on a cell |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [RowRequest()](PROP_GRID_ROWREQUEST.htm) | Called when the user attempts to move beyond the last row if the DataPending property is set |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [SelChange()](PROP_GCOMBO_SELCHANGE.htm) | Called when a new item is selected in the drop down portion of the control |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [ServerEdit()](PROP_GRID_SERVEREDIT.htm) | Called when the grid cell gets focus (if AutoEdit set to ServerEdit) |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Add(string, string)](PROP_GCOMBO_ADDTAG.htm) | Used to add strings with tags to the drop down portion of a DBEdit control |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Add(string)](PROP_GCOMBO_ADD.htm) | Used to add strings to the drop down portion of a DBEdit control |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Cell(int, int)](PROP_GRID_CELLXY.htm) | Used with other grid properties to change the properties of individual cells, rows and columns |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [ChangeRowCol(int, int, int, int)](PROP_GRID_CHANGEROWCOL.htm) | Allows new rows and columns to be added to the grid |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Clear()](PROP_GRID_CLEAR.htm) | Clears the contents of the grid control |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [CopyToClipboard()](PROP_GRID_COPYTOCLIP.htm) | Copies current contents of grid to clipboard |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [DataAwareRow()](PROP_GRID_DATAAWAREROW.htm) | Used to fill the current row from the assigned database table |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [DataAwareRow(int, string)](PROP_GRID_DATAAWAREROW2.htm) | Used to fill the specified grid row with the contents of the data aware buffer |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Delete()](PROP_GCOMBO_RESET.htm) | Used to clear out the contents of a DBEdit drop down |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Delete(int)](PROP_GCOMBO_DELETE.htm) | Used to remove individual items from a DBEdit dropdown |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [EditCell(int, int)](PROP_GRID_EDITCELL.htm) | Allows the user to modify the contents of the specified cell |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [EditGrid(int, int)](PROP_GRID_EDITGRID.htm) | Allows the user to modify the contents of the entire grid |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [EditRow(int, int)](PROP_GRID_EDITROW.htm) | Allows the user to modify the contents of the specified row |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetIndex(string)](PROP_GCOMBO_FINDINDEX.htm) | Used to return the index number associated with the specified string |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetIndex(int)](PROP_GCOMBO_GETINDEX.htm) | Used to test drop down index numbers for validity |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetString\$(int)](PROP_GCOMBO_GETSTRING.htm) | Returns the item from the specified index location |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetTag\$(int)](PROP_GCOMBO_GETTAG.htm) | Returns the tag from the specified index location |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [MoveCell(int, int)](PROP_GRID_MOVECELL.htm) | Moves the programming cell to the specified cell |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [MoveCursor(int, int)](PROP_GRID_MOVECURSOR.htm) | Moves the user selection cell to the specified cell |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Reset(int)](PROP_GRID_RESET2.htm) | Resets the grid to its default design time configuration |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Reset()](PROP_GRID_RESET.htm) | Resets the grid to its default design time configuration |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetDataField(string)](PROP_SETDATAFIELD2.htm) | Sets the datafield property to the specified FLD |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetDataField(int, string)](PROP_SETDATAFIELD.htm) | Sets the datafield property to the specified numeric field information |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetSelection(int)](PROP_GCOMBO_SETCURSEL.htm) | Used to select and item in the drop down list |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetSelection()](PROP_GCOMBO_NOCURSEL.htm) | Removes any current selection from the drop down list |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [ShowDropDown()](PROP_GRID_SHOWDROPDOWN.htm) | Forces the display of the DBEdit dropdown |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Appearance](PROP_GRID_APPEARANCE.htm) | Specifies the appearance of the grid |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [AutoEdit](PROP_GRID_AUTOEDIT.htm) | Put cell into edit mode when it gets focus |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [BackColor](PROP_GENERIC_BACKCOLOUR.htm) | Specifies the default background color |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [CancelEdit](PROP_GRID_CANCELEDIT.htm) | Used in EditRowNotify to show taht the user cancelled the edit |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Cell](PROP_GRID_CURSOR.htm) | Used with other grid properties to change the properties of individual cells, rows and columns |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Cols](PROP_GRID_COLS.htm) | Specifies the number of columns |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ColSize](PROP_GRID_COLSIZE.htm) | Selects how column widths are determined |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ColWidth](PROP_GRID_COLWIDTH.htm) | Specifies the column width |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [CursorCol](PROP_GRID_CCOL.htm) | Returns the cursor column position to left/right click event handlers |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [CursorEnable](PROP_GRID_CURSORENABLE.htm) | Specifies the behaviour of the cursor when the arrow keys are used |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [CursorRow](PROP_GRID_CROW.htm) | Returns the cursor row position to left/right click event handlers |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataBind](PROP_DATABIND.htm) | Binds the control to a table object |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataField](PROP_DATAFIELD.htm) | Specifies the SYM of the column field name that is to be bound to the control. Deprecated. |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataField\$](PROP_GENERIC_DATAFIELD.htm) | Get or set the name of field to which the control is databound |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataPending](PROP_GRID_DATAPENDING2.htm) | Enables/disables the RowRequest() event handler |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataSource](PROP_DATASOURCE.htm) | Specifies that variable name that is bound to a database table |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DBEnabled](PROP_DBENABLED.htm) | Determines if the Database associated with the control is enabled |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DropDownFilled](PROP_GRID_DROPDOWNDIRTY.htm) | Determines whether the drop down portion of the control has been filled |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [EditCursor](PROP_GRID_EDITCURSOR.htm) | Changes the cursor to an edit/insertion carat |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [EditReason](PROP_GRID_EDITREASON.htm) | Returns the reason for the termination of EditRow() |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [FixedCols](PROP_GRID_FIXEDCOLS.htm) | Specifies the number of fixed column heading columns |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [FixedRows](PROP_GRID_FIXEDROWS.htm) | Specifies the number of fix row heading rows |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [HideSelection](PROP_GRID_HIDESELECTION.htm) | Hide any selected cells when grid does not have focus |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [HorizontalLines](PROP_GRID_HLINES.htm) | Enable/disable horizontal lines for the specified row |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ImeMode](PROP_GRID_IME.htm) | Allow the default IME method to be defaulted |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Index](PROP_GENERIC_DATAPTR.htm) | Returns the index of the currently selected item |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [LastChar\$](PROP_GRID_LASTCHAR.htm) | Returns the last key pressed by the user |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [LastKey](PROP_GRID_LASTKEY.htm) | Returns the last key and shift state |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [LeftAction](PROP_GRID_LEFTACTION.htm) | Specifies the default mouse action for a left click |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [LeftSelect](PROP_GRID_LEFTSELECT.htm) | Specifies the default selection for a left mouse click |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [LinesPerRow](PROP_GRID_LINESPERROW.htm) | Specifies the number of lines per row |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ListCol](PROP_GRID_LISTCOL.htm) | Returns the column used for the listbox during the current cell edit |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ListRow](PROP_GRID_LISTROW.htm) | Returns the row used for the listbox during the current cell edit |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [MouseX](PROP_GRID_MOUSEX.htm) | Returns the X coordinate of the last mouse click to left/right click event handlers |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [MouseY](PROP_GRID_MOUSEY.htm) | Returns the Y coordinate of the last mouse click to left/right click event handlers |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [NewCol](PROP_GRID_NEWCOL.htm) | Returns the column cursor will move to if current validate returns TRUE |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [NewRow](PROP_GRID_NEWROW.htm) | Returns the row cursor will move to if current validate returns TRUE |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [NoBorder](PROP_GRID_NOBORDER.htm) | Removes the 3D edging from a grid |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [NoIntegralheight](PROP_GRID_NOINTEGRALHEIGHT.htm) | Enables/disables size fixing |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [RightAction](PROP_GRID_RIGHTACTION.htm) | Specifies the default mouse action for a right click |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [RightSelect](PROP_GRID_RIGHTSELECT.htm) | Specifies the default selection for a right mouse click |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [RowHeight](PROP_GRID_ROWHEIGHT.htm) | Specifies the row height |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Rows](PROP_GRID_ROWS.htm) | Specifies the number of rows |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ServerText](PROP_GRID_SERVERTEXT.htm) | Enable server storage (and retrieval) of grid cell text |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ShowSelection](PROP_GRID_SHOWSELECTION.htm) | Shows how selected cells are highlighted |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [TabThrough](PROP_GRID_TABTHROUGH.htm) | When tabbing into grid, tabbing behaves as if each cell is a separate control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [TextColor](PROP_GENERIC_TEXTCOLOUR.htm) | Specifies the default text color |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Validate](PROP_GRID_VALIDATEPROP.htm) | Specifies the default cell validation action |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ValidateText\$](PROP_GRID_VALIDATETEXT.htm) | Passed into the EditValidate() event |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [VerticalLines](PROP_GRID_VLINES.htm) | Enable/disable vertical lines for the specified column |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [WantReturn](PROP_GRID_WANTRETURN.htm) | Return key should send char event |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [WholeDataAware](PROP_GRID_WHOLEDATAAWARE.htm) | The entire grid is data aware against a single data record |
