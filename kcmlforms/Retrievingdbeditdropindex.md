Retrieving the index number of a string in a Edit control drop down

------------------------------------------------------------------------

To find the index value of a string in a Edit control drop down use the

*GetIndex(Str)* method. For example:

IndexValue = .EditControl1.GetIndex(String\$)

<span style="font-family: Courier New,monospace; "> </span>The

*GetIndex(Str)* method is particularly useful when used in conjunction with methods that require an index value, for example:

.EditControl1.Delete(GetIndex(String\$))
