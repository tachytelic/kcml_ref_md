DataField\$ (generic property)

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
<td>KCML<br />
6.10+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> String property

**Get or set the name of field to which the control is databound**

This property of a data aware control specifies the name of the field bound to a control. It is different from the now deprecated [DataField](PROP_DATAFIELD.htm) property which refers to symbol indices and is usually set at design time.

This field will normally be set in the forms editor by dragging from the table list onto the control.


        .txtDesc.DataField$ = "Name"

This property was introduced in KCML 6.10 to allow the programmer to inspect or change the binding of a control to a field in a record buffer. It replaces the obsolete technique of setting the [DataField](PROP_DATAFIELD.htm) indexed property using SYM as this mechanism will not be supported in future versions of KCML.

This property also replaces the experimental SetDataField() method which was withdrawn in KCML 6.11

##### See also:

Other [edit](edit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
