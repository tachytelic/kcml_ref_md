Retrieving the index number of a string in a combo box list

------------------------------------------------------------------------

To find the index value of a string in a combo box use the

*GetIndex(Str)* method. For example:

IndexValue = .comboControl1.GetIndex(String\$)

The

*GetIndex(Str)* method is particularly useful when used in conjunction with methods that require an index value, for example:

.comboControl1.Delete(.comboControl1.GetIndex(String\$))
