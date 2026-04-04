Selecting an item in a combo box list

------------------------------------------------------------------------

To select an item in a combo box the

*SetSelection()* method is used. The index of the item is used to specify which item is to be selected, for example:

.comboControl1.SetSelection(5)

would select the fifth item in the list box. The [*GetIndex()* method can be used to return the index of an item. If no index value is specified with the](tmp/PROP_COMBO_FINDINDEX.htm)

*SetSelection()* method then any existing selection, if any, is cleared.
