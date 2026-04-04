First (gridcell control property)

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
6.20+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Object property

**Get first item object**

This property returns a listitem object reference for the first entry in the edits listbox. It will be NULL if the listbox is empty. The next item can then be found by using the [Next](PROP_LISTITEM_GETNEXT.htm) property on this object e.g. count = 0 OBJECT c = .editControl1.First WHILE OBJECT c \<\> NULL DO count++ OBJECT c = c.Next WEND

##### See also:

Other [gridcell](gridcell.htm) properties, methods and events, [grid](grid.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
