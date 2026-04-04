Add (listbox control method)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Add(string) Method

**Used to add items to a list box**

***Str1***      Text of item to be added\

Used to add entries into a list box. Entries are added in sequential order unless the [Sort](PROP_LISTBOX_SORT.htm) property is set. As each item is added the system allocates a unique index number to the item which is can later be used to set the selection marker, or to delete the entry etc. The index value for an item can be returned with the [GetIndex()](PROP_LISTBOX_FINDINDEX.htm) method.

An optional second parameter can be used to add an tag which is to be associated with the string. Tags are used as an alternative way of searching for an item within the list, see [Add(str, str)](PROP_LISTBOX_ADDTAG.htm). .listControl1.Add(NewItem\$)

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
