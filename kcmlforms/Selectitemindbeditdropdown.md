Selecting an item in the Edit control drop down

------------------------------------------------------------------------

To select an item in the drop down area of a Edit control the

*SetSelection()* method is used. The index of the item is used to specify which item is to be selected, for example:

.EditControl1.SetSelection(5)

would select the fifth item in the drop down area. The [*GetIndex()* method can be used to return the index of an item. If no index value is specified with the](tmp/PROP_ECOMBO_FINDINDEX.htm)

*SetSelection()* method then any existing selection, if any, is cleared.
