Duplicate (tabbeditem control method)

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
<td>Advanced</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Duplicate(string) Method

**Duplicate tab page**

|     |                                 |
|-----|---------------------------------|
| Str | The text label for the new page |

This method is used within the [*Create()* event handler to add a new page to a tab control of the current form. Later calls to the generic](PROP_FORM_CREATE.htm) [Duplicate(int, int, str, int)](PROP_GENERIC_DUPLICATE_4.htm) method can duplicate other controls such as buttons and edit controls onto the new page. The method returns a [sym](PROPNUM_SYM.htm) pointer to the newly created control to permit this.

For example this creates a new page and adds a button: newsym = .tabControl1.Tab1.Duplicate("New page") .btnControl2.Duplicate(5, 12, "Click Me", newsym)

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
