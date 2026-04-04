Association (editgroup control property)

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
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Indexed property

**Associates two or more edit groups**

EditGroups can be linked into associations using the Forms Designer. All editgroups in an assiciation will use the same alignment for their controls. Alignment is calculated in coordinates relative to the editgroup so provided the editgroups themselves are aligned, all the controls within will be aligned.

This feature is useful if the alignment of controls needs to span tabs or frames. Simply place one editgroup in each tab or frane and make them all part of the same association.

##### Example:


     .editgroup.Association

##### See also:

Other [editgroup](editgroup.htm) properties, methods and events and [generic](generic.htm) properties and methods.
