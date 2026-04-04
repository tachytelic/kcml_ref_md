Tag\$ (listitem control property)

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

**Tag of a list item**

This property is a free text field which can be referenced and modified by the program without affecting the appearance of the control. It is commonly used to associate keys with items in the list. The listbox [Add(str, str)](PROP_LISTBOX_ADDTAG.htm) method can be used to associate a tag with a listitem at the time the item was being added to the list.

The **Tag\$** property is often used with object references to listbox item as in count = 0 OBJECT c = .listControl1.First WHILE OBJECT c \<\> NULL DO IF (c.tag\$ == "X") count++ END IF OBJECT c = c.Next WEND

##### See also:

Other [listitem](listitem.htm) properties, methods and events, [listbox](listbox.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
