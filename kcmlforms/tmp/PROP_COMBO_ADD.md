Add (combobox control method)

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

**Used to add items to a combo box**

***Str1***      Text of item to be added\
***Str2***      Optional tag

Used to add entries into a combo box. Entries are added in sequential order unless the [Sort](PROP_COMBO_SORT.htm) property is set. As each item is added the system allocates a unique index number to the item which can later be used to set the selection marker, or to delete the entry etc. The index value for an item can be returned with the [GetIndex()](PROP_COMBO_FINDINDEX.htm) method. The second parameter is used to add an optional tag which is to be associated with the string. Tags are used as an alternative way of searching for an item within the list, see [GetTag\$()](PROP_COMBO_GETTAG.htm). .comboControl1.Add(NewItem\$, Tag\$)

##### See also:

Other [combobox](combobox.htm) properties, methods and events and [generic](generic.htm) properties and methods.
