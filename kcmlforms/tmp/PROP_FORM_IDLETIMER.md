IdleTimer (form control property)

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
<td>Appears in<br />
browser</td>
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the interval in which the Idle() event handler is called in milliseconds**

This property is used to specify the interval at which the [*Idle()* event handler is to be called, if it exists. By default this property is set to -1 which means that the *Idle()* event handler is disabled. To enable the *Idle()* event this property should be set to a positive integer specifying the interval in milliseconds. For example, the following would set the interval to 5 seconds:](PROP_FORM_IDLE.htm)


    .form.IdleTimer = 5000

Don't set this property unless you have an event handler otherwise the server will be waking up unnecessarily. Also though the timeout is measured in milliseconds you would not want to have the server woken repeatedly at sub one second intervals because of the consequent degredation of performance for other users.

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
