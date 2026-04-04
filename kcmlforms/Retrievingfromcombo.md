Retrieving the currently selected item from a combo box list

------------------------------------------------------------------------

To retrieve the currently selected item from a combo box use the [Index](tmp/PROP_GENERIC_DATAPTR.htm) property. For example:


     CurSelectedItem = .comboControl1.Index

To retrieve the string associated with the index value the [GetString()](tmp/PROP_COMBO_GETSTRING.htm) method is used, for example:


     CurSelectedItem$ = .comboControl1.GetString$(.comboControl1.Index)

See also the listbox documentation [here.](Retrieveitemfromlistbox.htm)
