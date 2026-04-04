Resize (form control property)

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
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Form is resizable**

A form can only be resized by the user if the **Resize** property is TRUE. The default is FALSE. This is a design time property that has no effect if set at runtime.

When a form is resized a [Resize()](PROP_FORM_RESIZE.htm) event will result. Control sizes and positions only change if anchoring is used. If not, controls can be moved manually by changing these properties within the [Resize()](PROP_FORM_RESIZE.htm) event.

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
