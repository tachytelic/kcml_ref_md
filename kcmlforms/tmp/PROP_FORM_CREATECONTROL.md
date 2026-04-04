CreateControl (form control method)

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
<td>Advanced</td>
<td>KCML<br />
6.20+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> CreateControl(int, int, OBJECT) Method

**Create control in the Create event**

The CreateControl() method allows controls to be created dynamically during the [Create()](/tmp/PROP_FORM_CREATE.htm) event. This method has been superceded by a new [CreateControl()](/tmp/PROP_FORM_CREATECONTROL2.htm) method with a fourth parameter.

##### Example:


     .Form.CreateControl(i, j, OBJECT a)

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
