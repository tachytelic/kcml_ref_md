Persist (group control property)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time<br />
only</td>
<td>Read<br />
only</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (design time only boolean property)

**Group need not have any controls in DEFFORM to persist and not be removed by KForm as redundant**

Normally a group which does not contain any controls will be silently dropped by the forms designer when it returns the form to the workbench. However in applications where forms are being dynamically constructed it may be desirable to have an empty group and this can be achieved by setting this boolean property to TRUE at design time in the forms editor.

##### See also:

Other [group](group.htm) properties, methods and events and [generic](generic.htm) properties and methods.
