kcmledit control

\
[Generic](generic.htm) <span id="kcmledit"></span>

|  |  |  |
|----|----|----|
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [Change()](PROP_DBEDIT_CHANGE.htm) | Called whenever the text in the DBEdit control is changed |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [Click()](PROP_KCMLEDIT_CLICK.htm) | Called when the Ellipsis button is clicked |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [DropDown()](PROP_KCMLEDIT_DROPEVENT.htm) | Called before the drop down portion of the control is displayed |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [MaxText()](PROP_DBEDIT_MAXTEXT.htm) | Called if the number of characters set by LimitText is reached |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [Return()](PROP_KCMLEDIT_RETURN.htm) | Called if the ReturnEvent property has been set to TRUE and the user has pressed the RETURN key |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [SelChange()](PROP_EDIT_SELCHANGE.htm) | Called when a new item is selected in the drop down portion of the control |
| <img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" />  | [Validate()](PROP_KCMLEDIT_VALIDATE.htm) | Called if the contents of the control were modified by the user |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Add(string)](PROP_ECOMBO_ADD.htm) | Used to add strings to the drop down portion of a DBEdit control |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Add(string, string)](PROP_ECOMBO_ADDTAG.htm) | Used to add strings with tags to the drop down portion of a DBEdit control |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Delete()](PROP_ECOMBO_RESET.htm) | Used to clear out the contents of a DBEdit drop down |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [Delete(int)](PROP_ECOMBO_DELETE.htm) | Used to remove individual items from a DBEdit dropdown |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetIndex(int)](PROP_ECOMBO_GETINDEX.htm) | Used to test drop down index numbers for validity |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetIndex(string)](PROP_ECOMBO_FINDINDEX.htm) | Used to return the index number associated with the specified string |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetString\$(int)](PROP_ECOMBO_GETSTRING.htm) | Returns the item from the specified index location |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [GetTag\$(int)](PROP_ECOMBO_GETTAG.htm) | Returns the tag from the specified index location |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetDataField(int, string)](PROP_SETDATAFIELD.htm) | Sets the datafield property to the specified numeric field information |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetDataField(string)](PROP_SETDATAFIELD2.htm) | Sets the datafield property to the specified FLD |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetSelection(int)](PROP_ECOMBO_SETCURSEL.htm) | Used to select and item in the drop down list |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [SetSelection()](PROP_ECOMBO_NOCURSEL.htm) | Removes any current selection from the drop down list |
| <img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" />  | [ShowDropDown()](PROP_KCMLEDIT_SHOWDROPDOWN.htm) | Forces the display of the DBEdit dropdown |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Alignment](PROP_KCMLEDIT_ALIGNMENT2.htm) | Specifies the alignment of text within the control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [AlwaysValidate](PROP_KCMLEDIT_VALIDATEPROP.htm) | Allows edits to be always validated |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [BackColor](PROP_GENERIC_BACKCOLOUR.htm) | Specifies the default background color |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [CanConvert](PROP_KCMLEDIT_CANCONVERT.htm) | Determines whether value can be converted to alternative currency |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Case](PROP_DBEDIT_CASE.htm) | Allows the character case entered into the control to be restricted |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataBind](PROP_DATABIND.htm) | Binds the control to a table object |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataField](PROP_DATAFIELD.htm) | Specifies the SYM of the column field name that is to be bound to the control. Deprecated. |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataField\$](PROP_GENERIC_DATAFIELD.htm) | Get or set the name of field to which the control is databound |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DataSource](PROP_DATASOURCE.htm) | Specifies that variable name that is bound to a database table |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DBEnabled](PROP_DBENABLED.htm) | Determines if the Database associated with the control is enabled |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Description](PROP_EDIT_DESCRIPTION.htm) | The control text can be given a tab-separated description |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DescText\$](PROP_EDIT_DESCTEXT.htm) | Text that will appears in edit's description field |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DropDown](PROP_EDIT_DROPDOWN.htm) | Used to set the DBEdit control to act as a regular edit control or as a drop down list box |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DropDownFilled](PROP_KCMLEDIT_DROPDOWNDIRTY.htm) | Determines whether the drop down portion of the control has been filled |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DropListStyle](PROP_EDIT_DROPLISTSTYLE.htm) | Specifies the behaviour of the drop down list |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [DropStyle](PROP_EDIT_DROPSTYLE.htm) | Determines whether the DBEdit control displays an down arrow or ellipses when acting as a dropdown control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [EditGroup](PROP_EDIT_EDITGROUP.htm) | Specifies the edit group the control belongs to |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [First](PROP_EDIT_LISTFIRST.htm) | Get first item object |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ImeMode](PROP_GRID_IME.htm) | Allow the default IME method to be defaulted |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Index](PROP_GENERIC_DATAPTR.htm) | Returns the index of the currently selected item in the drop down portion of the control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Label\$](PROP_EDIT_EDITLABEL.htm) | Label for the edit control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [LimitText](PROP_DBEDIT_LIMITTEXT.htm) | Used to restrict the amount of text entered into the control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ListCount](PROP_LISTBOX_COUNT.htm) | Returns the number of items in the list box |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [NoSelectOnEntry](PROP_EDIT_NOSEL.htm) | The text is not automatically selected on tabbing in to the listbox |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Password](PROP_EDIT_PASSWORD.htm) | All characters are displayed as the password char |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [PasswordChar\$](PROP_EDIT_PASSWORDCHAR2.htm) | Specifies the default echo character for passworded DBedit controls |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ReadOnly](PROP_DBEDIT_READONLY.htm) | Enables/disables readonly mode for the control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ReturnEvent](PROP_KCMLEDIT_RETURNEVENT.htm) | Enable/disable the Return() event handler |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [RightToLeft](PROP_GENERIC_RIGHTTOLEFT.htm) | Makes the control right-to-left or left-to-right (on systems that support this feature) |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [SortedListBox](PROP_EDIT_SORTLIST.htm) | Specifies if the listbox should be sorted |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [TabStop\$](PROP_KCMLEDIT_TABSTOP.htm) | Specifies the tab stop positions for the control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [TextColor](PROP_GENERIC_TEXTCOLOUR.htm) | Specifies the default text color |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [Type\$](PROPSTR_TYPE.htm) | Specifies the format that the user will use to enter information |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ValidateSelChange](PROP_KCMLEDIT_VALIDATESELCHANGE.htm) | Causes a validate event when the user changes the selected item in the drop down portion of the control. |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [ValidateText\$](PROP_KCMLEDIT_VALIDATETEXT.htm) | Contains the modified contents of the DBEdit control |
| <img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" />  | [WrapText](PROP_EDIT_WRAPTEXT.htm) | Enable word wrapping |
