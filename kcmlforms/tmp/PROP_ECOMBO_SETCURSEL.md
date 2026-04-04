SetSelection (kcmledit control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> SetSelection(int) Method

**Used to select and item in the drop down list**

|     |                              |
|-----|------------------------------|
| Int | Index of item to be selected |

Used by a KCML Edit control to select the dropdown item specified by the index value.

For example: .EditControl1.SetSelection(ItemNo)

If no index value is specified then the current selection, if any, is removed. See [.SelSelection()](PROP_ECOMBO_NOCURSEL.htm)

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
