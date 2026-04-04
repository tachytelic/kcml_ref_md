Selecting an item or items in a list box

------------------------------------------------------------------------

To select an item in a list box the

*SetSelection()* method is used. The index of the item is used to specify which item is to be selected, for example:

.listControl1.SetSelection(5)

would select the fifth item in the list box. The

*GetIndex()* method can be used to return the index of an item therefore to select a specific string within a list box the following could be used:

.listControl1.SetSelection(.listControl1.GetIndex(String\$))

If no index value is specified with the *SetSelection()* method then any existing selection, if any, is cleared.

If the list box is a multiple or extended selection list box (See [*Selection*) then the](tmp/PROP_LISTBOX_SELECTION.htm)

*AddSelection()* method is used to select additional items, for example:

.listControl1.AddSelection(Item)
