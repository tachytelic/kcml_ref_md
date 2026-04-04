SymNext (generic property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> SYM property

**Returns the pointer value of the next control in the tab sequence**

This property is used to return the pointer value of the control next in the Tab Order for the referenced control. The value can be assigned to a variable and then later be used to reference the control. The control is referenced by replacing the controls name with an asterisk followed by the numeric variable containing the pointer value, for example to assign the pointer value of the control *btnControl1* to a variable the following would be used: Pointer = .btnControl1.SymNext

and to reference the control using the pointer the following would be used: .\*Pointer.Text\$ = "Some Text"

##### See also:

Other [group](group.htm) properties, methods and events and [generic](generic.htm) properties and methods.
