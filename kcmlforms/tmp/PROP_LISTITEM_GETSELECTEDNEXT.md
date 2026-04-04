SelectedNext (listitem control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Object property

**Get next selected item object**

This property returns an object reference for the next selected entry in a listbox. It will be NULL if there are no further items. The first selected item can be found by using the [SelectedFirst](PROP_LISTBOX_GETSELECTEDFIRST.htm) object on the listbox control e.g.


     count = 0
     OBJECT c = .listControl1.SelectedFirst
     WHILE OBJECT c <> NULL DO
        count++
        OBJECT c = c.SelectedNext
     WEND

##### See also:

Other [listitem](listitem.htm) properties, methods and events, [listbox](listbox.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
