Deleting strings from a list box

To delete an item from a list box the [*Delete()* method is used. This method requires the index value of the string to be deleted. Index values are assigned to strings as they are added to the list box. To find the index value of a string use the](tmp/PROP_LISTBOX_DELETE.htm)

*GetIndex()* method. For example, to delete the string "Graham" from the list box *listControl1* the following would be used:

.listControl1.Delete(.listControl1.GetIndex("Graham"))
