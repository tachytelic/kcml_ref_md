Return (kcmledit control event)

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
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called if the ReturnEvent property has been set to TRUE and the user has pressed the RETURN key**

This event handler is only called if the [*ReturnEvent* property has been set to TRUE, and the user has pressed the RETURN key within an Edit control. It replaces the normal behaviour of RETURN which is to action any default button.](PROP_KCMLEDIT_RETURNEVENT.htm)

If a [validate](PROP_KCMLEDIT_VALIDATE.htm) event handler also exists for the control then it will be called instead if the text has been modified since the text was last valid. Focus will stay on the control.

##### Example:


     DEFEVENT Form1.editControl.Return()

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
