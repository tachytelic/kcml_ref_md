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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Add(string, string) Method

**Used to add tagged items to a list box**

|      |                          |
|------|--------------------------|
| Str1 | Text of item to be added |
| Str2 | User tag                 |

The Add(str1, str2) method is used to add entries into a list box supplying a tag string that identifies the entry to the program. The tag is supplied by the programmer to efficiently identify the entry and has no significance to the control. Entries are added in sequential order unless the [*Sort* property is set. As each item is added the system allocates a unique index number to the item which is can later be used to set the selection marker, or to delete the entry etc. The index value for an item can be returned with the](PROP_LISTBOX_SORT.htm) [*GetIndex()* method.](PROP_LISTBOX_FINDINDEX.htm)

Tags are used as an alternative way of searching for an item within the list, see [*GetTag\$()*.](PROP_LISTBOX_GETTAG.htm)

The Add() method can also be used without supplying a tag. See [Add(str)](PROP_LISTBOX_ADD.htm). .listControl1.Add(NewItem\$, Tag\$)

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
