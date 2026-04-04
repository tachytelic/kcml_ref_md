TabStop\$ (listbox control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Array property

**Specifies the tab stop positions for the control**

This array property is used to set the [tab expansion positions](/settingthetabstopsinalistbox.htm) in a listbox. Provided the [*UseTabs* property is TRUE any HEX(09) characters in the listbox text will be expanded to position the following text at that point. The column values are expressed in](PROP_LISTBOX_USETABS.htm) [Dialog Box Units](/DialogBoxUnitsDLUs.htm) as a comma separated string e.g. .listControl1.TabStop\$ = "50, 100, 150, 200"

By default, if not changed at design time in the [forms designer](/FormsDesignerWorkingwithListboxes.htm), the columns are set at 32 DBU intervals.

This property should not be confused with the tab stops referred to in the Forms Designer when setting tab order on a form.

##### See also:

Other [listbox](listbox.htm) properties, methods and events, [listitem](listitem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
