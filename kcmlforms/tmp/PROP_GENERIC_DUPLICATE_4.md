Duplicate (generic control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Duplicate(int, int, string, int) Method

**Duplicate control with title and tab page**

|      |                                            |
|------|--------------------------------------------|
| Int1 | The horizontal position of the new control |
| Int2 | The vertical position of the new control   |
| Str  | The text label for the new control         |
| Int3 | The sym of a newly generated tab page      |

This method is used within the [*Create()* event handler to duplicate a control to a new location on a tab of the current form. As in the basic](PROP_FORM_CREATE.htm) [Duplicate(int, int)](PROP_GENERIC_DUPLICATE_2.htm) method, the first two parameters specify the new location of the control relative to the top left hand corner of the form. The optional string parameter allows the controls label to be changed. This is only relevant to controls that have text labels such as buttons and static text controls and can be blank if not applicable. The fourth parameter specifies the [sym](PROPNUM_SYM.htm) of a tab page. Tab pages can be created using the [Duplicate(str)](PROP_TABBED_DUPLICATE.htm) tab control method which returns such a sym.

The method returns a [sym](PROPNUM_SYM.htm) pointer to the newly created control to allow the program to later reference the controls properties and methods.

This method can also be used to create new tab pages and add controls to those pages, for example: newsym = .tabControl1.Tab1.Duplicate("New page") .btnControl2.Duplicate(5, 12, "New button", newsym)

Note that the source control must be available on the previously duplicated tab.

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
