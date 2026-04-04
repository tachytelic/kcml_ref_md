Add (kcmledit control method)

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

**Used to add strings to the drop down portion of a DBEdit control**

|     |                          |
|-----|--------------------------|
| Str | Text of item to be added |

This method is used to add entries into the drop down portion of an Edit control . As each item is added the system allocates a unique index (See [Index](PROP_GENERIC_DATAPTR.htm)) number to the item which can later be used to set the selection marker, or to delete the entry etc. The index value for an item can be returned with the [GetIndex()](PROP_ECOMBO_FINDINDEX.htm) method.

See also the [.Add(str1, str2)](PROP_ECOMBO_ADDTAG.htm) method which can be used to add an item and flag it with a user supplied tag string to facilitate identification If tags are used as an alternative way of searching for an item in the list, they are then displayed in the first column of the drop down list when it is displayed. .EditControl1.Add(NewItem\$)

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
