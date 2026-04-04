Retrieving the currently selected string from a Edit control drop down

------------------------------------------------------------------------

To retrieve the currently selected item from a Edit control drop down the

*Index* property is used. For example:

CurSelectedItem = .EditControl1.Index

To retrieve the string associated with the index value the

*GetString()* method is used, for example:

CurSelectedItem\$ = .EditControl1.GetString\$(.EditControl1.Index)
