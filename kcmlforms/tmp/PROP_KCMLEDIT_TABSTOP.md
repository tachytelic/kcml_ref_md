TabStop\$ (kcmledit control property)

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

A KCML edit control with a drop down list has the ability of displaying some secondary descriptive text, called a tag, to the right of the entry text. This text is taken from list box which must have been populated with the [.Add(desc\$, key\$)](PROp_ECOMBO_ADDTAG.htm) method associating a *desc\$* tag with each entry *key\$*. If the entry is changed, either by keying in a new value of picking from the list, the descriptibe text is updated.

By default columns are set in the two controls at 32 [Dialog Box Unit](/DialogBoxUnitsDLUs.htm) intervals. This string property can is used to set the tab expansion positions in both the edit box and any accompanying drop down listbox to a different value. The column values are expressed in Dialog Box Units as a comma separated string though only the first value is used e.g. .editControl1.TabStop\$ = "50"

This property should not be confused with the tab stops referred to in the Forms Designer when setting tab order on a form.

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
