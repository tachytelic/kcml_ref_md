Exit (form control server-side event)

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

**Called when the form is terminated**

This event is called when the form is terminated, i.e. when the Cancel or OK buttons are clicked or if the [*Terminate()* form method is executed. This event handler can be used to verify the user input before the form is closed.](PROP_DLG_TERMINATE.htm)

You cannot reference any controls, in particular any [OCX controls](/IntroOCX.htm), that were on the form as they will have been terminated before this event is raised.

Furthermore you must not open any new forms in the exit event handler as the client will not have a parent for them. This was permitted in KCMLs prior to KCML 6.00, and often worked, but will now give a P34 error.

##### Example:


     DEFEVENT Form1.Exit()

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
