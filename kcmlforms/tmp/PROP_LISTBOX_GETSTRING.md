GetString\$ (listbox control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> GetString\$(int) Method

**Used to return the item associated with the specified index value**

***Int***     The index of the required item

Used to return the item from the specified index location. For example, the following would return the item text from the fifth item added to the list box: Item\$ = .listControl1.GetString\$(5)

To return the currently selected item this method can be combined with the [Index](PROP_GENERIC_ODATAPTR.htm) property, for example: Selected\$ = .listControl1.GetString\$(.listControl1.index)

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
