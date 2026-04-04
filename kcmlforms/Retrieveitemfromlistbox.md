Retrieving the currently selected item(s) from a list box

------------------------------------------------------------------------

To retrieve the currently selected item from a list box use the [Index](tmp/PROP_GENERIC_DATAPTR.htm) property. For example, the following could be used to return the index number of the currently selected item:


     CurSelectedItem = .listControl1.Index

To return the currently selected string the [Index](tmp/PROP_GENERIC_DATAPTR.htm) property is used in conjunction with the [GetString\$()](tmp/PROP_LISTBOX_GETSTRING.htm) method, for example:


     Selected$ = .listControl1.GetString$(.listControl1.Index)

If the list box is a multiple or extended selection list box, as set by the [Selection](tmp/PROP_LISTBOX_SELECTION.htm) property, then the index numbers of the selected items can be returned with the [GetSelection()](tmp/PROP_LISTBOX_GETSELECTION.htm) method. The specified value corresponds to the ordinal number of the selected item, i.e. passing a value of 1 would return the index of the first selected item in the list, for example:


     SelectedItem1 = .listControl1.GetSelection(1)

Note that if the specified item is not selected then the [GetSelection()](tmp/PROP_LISTBOX_GETSELECTION.htm) method returns a value of -1.

To return the text of selected items in a multiple or extended selection list box the [GetSelection()](tmp/PROP_LISTBOX_GETSELECTION.htm) method can be used in conjunction with the [GetString()](tmp/PROP_LISTBOX_GETSTRING.htm) method, for example:


     Selected$ = .listControl1.GetString$(.listControl1.GetSelection(Number))

There is also an object notation for iterating over a multi-selection using the [SelectedFirst](tmp/PROP_LISTBOX_GETSELECTEDFIRST.htm) and [SelectedNext](tmp/PROP_LISTITEM_GETSELECTEDNEXT.htm) object properties.
