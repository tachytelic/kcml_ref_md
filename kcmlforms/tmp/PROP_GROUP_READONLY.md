ReadOnly (group control method)

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
<td>Appears in<br />
browser</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> ReadOnly(int) Method

**Makes the controls in the group read only**

***Int***      A boolean value (***TRUE*** or ***FALSE***

This method is used to make all controls within the group read only. A read only control allows the user to enter the field but they are not able to make any changes. Specifying a value of ***TRUE*** makes the controls in the group read only while a value of ***FALSE*** returns the controls back to the default edit mode. Groups are set up and named at design time within the [Form Designer](/FormsDesignerGroupingControls.htm). For example the following would make the controls in the group *grpControl1* read only: .grpControl1.ReadOnly(TRUE)

##### See also:

Other [group](group.htm) properties, methods and events and [generic](generic.htm) properties and methods.
