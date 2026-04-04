AlwaysValidate (kcmledit control property)

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
<td>Appears in<br />
browser</td>
<td>Advanced</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Edit, EditWithValidate, NoEdit, EditAlwaysValidate)*

**Allows edits to be always validated**

This property is used to determine if the [*Validate()* event handler is to be called when the user moves focus out of the edit control. The following is a list of available settings for this property. Note that these values are taken from the same enumeration used for the](PROP_KCMLEDIT_VALIDATE.htm) [Validate](PROP_GRID_VALIDATEPROP.htm) property of grid cells and that some of the values do not apply to simple edit controls.

Setting EditAlwaysValidate will mimic the action of the deprecated LoseFocus() event but will correctly handle ellipsis and dropdown focus changes.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Default</td>
<td>Uses the current underlying setting for the grid. If this is set to default then the <em>EditWithValidate</em> setting is assumed.</td>
</tr>
<tr>
<td>EditWithValidate</td>
<td>If the user moves focus out of the control and the cells contents were modified then call the
<em>Validate()</em> event handler, if it exists.</td>
</tr>
<tr>
<td>EditAlwaysValidate</td>
<td>The
<em>Validate()</em> event is always called when the user moves focus out of the control, regardless of any changes made to the cell contents.</td>
</tr>
<tr>
<td>Edit</td>
<td>Reserved</td>
</tr>
<tr>
<td>NoEdit</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

##### Example:


     .editControl.AlwaysValidate = &.Default

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
