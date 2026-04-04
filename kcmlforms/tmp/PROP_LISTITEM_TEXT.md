Text\$ (listitem control property)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Get text of a list item**

This property refers to the text which appears in the listbox for an item. The listbox [Add(str)](PROP_LISTBOX_ADD.htm) method can be used to set the text for a listitem at the time the item was being added to the list.

The **Text\$** property is often used with object references to listbox item as in OBJECT c = .listControl1.First WHILE OBJECT c \<\> NULL DO IF (STR(c.Text\$,,1) == "x") STR(c.Text\$,,1) = "X" END IF OBJECT c = c.Next WEND

##### See also:

Other [listitem](listitem.htm) properties, methods and events, [listbox](listbox.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
