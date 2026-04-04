Id (generic control property)

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
<td>Read<br />
only</td>
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**The ID of the control as used in the Windows API**

This is a read only property that returns the unique identifier assigned by KCML to a control to identify it to Windows. The ID can be used to interact with the form directly from another program.

Certain Id values are predefined by Windows for special buttons, for example

|     |               |
|-----|---------------|
| 1   | OK button     |
| 2   | Cancel button |
| 6   | Yes button    |
| 7   | No button     |
| 8   | Close button  |
| 9   | Help button   |

This property is used internally by KCML and cannot be changed.

##### Example:


     n = .generic.Id

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
