AddSelection (listbox control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> AddSelection(int) Method

**Used to select all items in a multiple or extended selection list box**

\
***Int***      Index of item to be selected

In a multiple selection or extended selection list box, this method will select the item specified by the index value. For example: .listControl1.AddSelection(5) If no value is specified then all items are selected.

To remove all current selections use the [*SetSelection()* method without any parameters.](PROP_LISTBOX_NOCURSEL.htm)

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
