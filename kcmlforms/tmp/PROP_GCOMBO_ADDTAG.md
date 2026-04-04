Add (grid control method)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Add(string, string) Method

**Used to add strings with tags to the drop down portion of a DBEdit control**

|      |                 |
|------|-----------------|
| Str1 | Descriptive tag |
| Str2 | Text of item    |

The Add(tag\$, key\$) method is used to add entries into the KCML grid cell drop down list box supplying a descriptive tag string that identifies the entry to the user. This causes the dropdown list to work in an enhanced mode that limits input to the entries in the list. The descriptive text is displayed to the right of the entry in the cell as well as being displayed in the list box. The separation of the two columns in both parts of the control is controlled by the [.TabStop\$](PROP_KCMLEDIT_TABSTOP.htm) property.

For an example program (actually using edit controls but the principle is the same) see [Using tags and dropdown lists with edit controls](/ExampleDropDown.htm).

The Add() method can also be used without supplying a tag. This just populates the list. See [Add(str)](PROP_GCOMBO_ADD.htm). .gridControl1.Add(Desc\$, NewItem\$)

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
