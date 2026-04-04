Deleting individual strings from a combo box list

To delete an item from a combo box the [*Delete(Int)* method is used. This method requires the index value of the string to be deleted. Index values are assigned to strings as they are added to the list box. To find the index value of a string use the](tmp/PROP_COMBO_DELETE.htm)

*GetIndex(Str)* method. For example, to delete the string "Graham" from the combo box *comboControl1* the following would be used:

.comboControl1.Delete(.comboControl1.GetIndex("Graham"))
