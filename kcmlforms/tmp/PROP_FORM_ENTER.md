Enter (form control server-side event)

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

**Called before the form is displayed**

This event is called before the form is actually displayed. This event handler is usually used to initialize form controls before the form is actually displayed. Because the form has not actually been created within Windows at this time, any OCX controls it contains have yet to be instantiated and so cannot be referenced here. However the standard KCML controls do exist and can be inspected or modified at this time.

##### Example:


     DEFEVENT Form1.Enter()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
