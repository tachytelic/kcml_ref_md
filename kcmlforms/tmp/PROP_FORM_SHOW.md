Show (form control server-side event)

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
<img src="/bitmaps/browsetool52.png" data-border="0" width="16" height="15" alt="server-side event icon" /> Server-side Event

**Called once the form has been displayed**

This event is called as soon as the form has been displayed and before the user can access any of the controls on the form (including OCX controls which are instantiated only after the [Enter()](PROP_FORM_ENTER.htm) event has completed). This event handler is commonly used to display an information or warning message in the context of the form.

##### Example:


     DEFEVENT Form1.Show()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
