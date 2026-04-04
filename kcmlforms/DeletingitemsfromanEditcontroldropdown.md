Deleting items from an Edit control drop down

To delete an item from a Edit control drop down the [*Delete(Int)* method is used. This method requires the index value of the string to be deleted. Index values are assigned to strings as they are added to the list box. To find the index value of a string use the](tmp/PROP_ECOMBO_DELETE.htm)

*GetIndex(Str)* method. For example, to delete the string "Graham" from the drop down portion of the control *EditControl1* the following would be used:

.EditControl1.Delete(.EditControl1.GetIndex("Graham"))
