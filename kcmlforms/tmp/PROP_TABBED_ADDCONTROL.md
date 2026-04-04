AddControl (tabbeditem control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> AddControl(OBJECT) Method

**Add the control to this tab page**

This method is used to add controls to a tab page. The single argument is an objecct reference to an existing or newly created control on a form that is not currently on a tab page. This method can only be used in the Create() event. See [CreateControl()](/tmp/PROP_FORM_CREATECONTROL.htm) for more details and examples.

##### Example:


     .tabbeditem.AddControl(OBJECT a)

##### See also:

Other [tabbeditem](tabbeditem.htm) properties, methods and events, [tabbed](tabbed.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
