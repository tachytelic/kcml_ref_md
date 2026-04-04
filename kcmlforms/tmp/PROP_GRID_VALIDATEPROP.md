Validate (grid control property)

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
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Enumerated property\
*(Default, Edit, EditWithValidate, NoEdit, EditAlwaysValidate)*

**Specifies the default cell validation action**

This property is used to determine if the [*EditValidate()* event handler is to be called when the user moves out of the cell. The following is a list of available settings for this property:](PROP_GRID_VALIDATE.htm)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Default</td>
<td>Uses the current underlying setting for the grid. If this is set to default then the <em>Edit</em> setting is assumed.</td>
</tr>
<tr>
<td>Edit</td>
<td>Editing is enabled for the cell but the
<em>EditValidate()</em> routine will not be called when the user leaves the cell.</td>
</tr>
<tr>
<td>EditWithValidate</td>
<td>If the user moves out of the cell and the cells contents were modified then call the
<em>EditValidate()</em> event handler, if it exists.</td>
</tr>
<tr>
<td>EditAlwaysValidate</td>
<td>The
<em>EditValidate()</em> event is always called when the user moves between cells, regardless of any changes made to the cell contents.</td>
</tr>
<tr>
<td>NoEdit</td>
<td>Used to skip to the Next or Previous cell when the user attempts to Tab or Shift Tab into the cell. Only relevant when the <a href="PROP_GRID_EDITROW.htm"><em>EditRow()</em> or</a>
<em>EditGrid()</em> methods are being used. Note that this property does not prevent the user from clicking on the cell directly. To completely disable a cell you should set the <em>LeftAction</em> or <em>RightAction</em> property to <em>Ignore</em> so as to disable the click event handler.</td>
</tr>
</tbody>
</table>

##### Example:


     .gridControl.Validate = &.Default

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
