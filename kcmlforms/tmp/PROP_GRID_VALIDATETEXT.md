ValidateText\$ (grid control property)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Passed into the EditValidate() event**

This property is used by the grid controls [EditValidate()](PROP_GRID_VALIDATE.htm) and the Edit controls [Validate()](PROP_KCMLEDIT_VALIDATE.htm) event handlers. If the text in a grid control cell or edit control is modified the appropriate event handler is called, if it exists. When the event handler is called this property is set to contain the current text in the control. The original text is stored in the [Text\$](PROPSTR_TITLE.htm) property.

This property is set by KCML and should generally only be inspected by the event handler code. If set and the validate event handler returns FALSE then the new value will be sent back to the client which will consider the control modified thus firing another validate event. In the special case of a grid cell [ServerEdit()](PROP_GRID_SERVEREDIT.htm) event handler in AutoEdit mode, a program is expected to set the property to the new value.

##### Example:


     a$ = .gridControl.ValidateText$

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
