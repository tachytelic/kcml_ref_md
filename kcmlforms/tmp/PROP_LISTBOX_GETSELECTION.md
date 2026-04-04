GetSelection (listbox control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> GetSelection(int) Method

**Used to return the index of a selected item within the list**

***Int***      The ordinal value of the item

Used to return the index of a selected item in a list. The specified value corresponds to the ordinal number of the selected item, i.e. passing a value of 1 would return the index of the first selected item. This method can only be used with list boxes that have the multiple selection or extended selection properties set. For example, the following would retrieve the text of the first selected item in the list box: SelString\$ = .listControl1.GetString(.listControl1.GetSelection(1))

If the specified item is not currently selected then a value of -1 is returned.

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
