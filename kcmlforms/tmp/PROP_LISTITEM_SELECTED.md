Selected (listitem control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Select this listbox item**

This Boolean object property can be used to select (TRUE) or deselect (FALSE) the listbox item object to which it is applied e.g. this program deselects the selected items in a listbox.


     LOCAL DIM OBJECT c, OBJECT n
     OBJECT c = .listControl1.SelectedFirst
     WHILE OBJECT c <> NULL DO
        c.Selected = FALSE
        OBJECT c = c.SelectedNext
      WEND

##### See also:

Other [listitem](listitem.htm) properties, methods and events, [listbox](listbox.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
