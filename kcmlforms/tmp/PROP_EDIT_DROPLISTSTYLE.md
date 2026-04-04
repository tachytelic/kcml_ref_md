DropListStyle (kcmledit control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Tag, Simple)*

**Specifies the behaviour of the drop down list**

This property is used to determine the behaviour of the drop-down list in a dbedit control.

Default

Same as Tag.

Tag

The list box displays items including the tag (if given). The tag acts as the accelerator.

Simple

The behaviour is more like that of a standard ComboBox control. The tags are never displayed and the list is accelerated by cycling through all items with an initial letter the same as the accelerator character. This altered behaviour is transparent to how the control is programmed.

An equivalent property for grids is not currently available

##### Example:


     .editControl.DropListStyle = &.Default

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
