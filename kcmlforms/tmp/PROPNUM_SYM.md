Sym (generic property)

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
<td>Advanced</td>
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> SYM property

**Returns a pointer value to the control**

This property is used to return the pointer value for the control. The value can be assigned to a variable and then later be used to reference the control. The control is referenced by replacing the controls name with an asterisk followed by the numeric variable containing the pointer value, for example to assign the pointer value of the control *btnControl1* to a variable the following would be used: Pointer = .btnControl1.sym

and to reference the control using the pointer the following would be used: .\*Pointer.Text\$ = "Some Text"

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
