EditGroup (kcmledit control property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Specifies the edit group the control belongs to**

This read-only design time property defines the Edit Group name for any [Edit Group](../IntroEditGroup.htm) to which the control may belong. A control can only be a member of a single group. Edit groups, in conjunction with the [.Label\$](PROP_EDIT_EDITLABEL.htm) property, facilitate the alignment of edit controls and their labels.

For more details about setting up an edit group see [EditGroups in the Forms Designer](../FormsDesignerWorkingWithEditGroups.htm).

##### Example:


     .editControl.EditGroup

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
