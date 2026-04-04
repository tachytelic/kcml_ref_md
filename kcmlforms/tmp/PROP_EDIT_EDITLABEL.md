Label\$ (kcmledit control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Label for the edit control**

The **Label\$** property is used to label a KCML edit control. The label appears on the left-hand side of the control with the editable region occupying the remainder of the space. If necessary, the label is truncated to prevent the editable area becoming too small. In appearance, using the Label\$ property is equivalent to having a static text control to the left of an edit control.

The real benefit of the Label\$ is found when the KCML edit is part of an [EditGroup](../FormsDesignerWorkingWithEditGroups.htm). Within such a group, the editable portions of the KCML edit controls are automatically aligned, based on the longest label. If there is room, the editable area can be extend beyond the notional area of the control although it will always be bound by the group container. This makes it much easier to allow for language translations that produce much longer labels, without having to leave large amounts of space between the label and the editable area for the worst case.


    .EditControl1.label$ = "&Name:"

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
