Enabled (group control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Enabled(int) Method

**Enables/disables controls in the group**

***Int***      A boolean value (***TRUE*** or ***FALSE***)

This method is used to enable and disable all controls within the group. Specifying a value of ***TRUE*** enables the controls while a value of ***FALSE*** disables the controls. Groups are set up and named at design time within the [Form Designer](/FormsDesignerGroupingControls.htm). For example the following would disable all the controls in the group *grpControl1*: .grpControl1.Enabled(FALSE)

##### See also:

Other [group](group.htm) properties, methods and events and [generic](generic.htm) properties and methods.
