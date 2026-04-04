GetString\$ (gridcell control method)

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

**Returns the item from the specified index location**

***Int***     The index of the required item

Used to return the item from the specified index location. For example, the following would return the item text from the fifth item added to the Edit control: Selected\$ = .EditControl1.GetString\$(5)

To return the currently selected item this method can be combined with the [Index](PROP_GENERIC_DATAPTR.htm) property, for example: Selected\$ = .EditControl1.GetString\$(.EditControl1.Index)

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
