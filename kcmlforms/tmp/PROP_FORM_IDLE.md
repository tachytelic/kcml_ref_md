Idle (form control server-side event)

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
<img src="/bitmaps/browsetool52.png" data-border="0" width="16" height="15" alt="server-side event icon" /> Server-side Event

**Called when no other event handlers are in operation**

When a form is dispalyed the server will be in an idle state awaiting notification of an event from the client. Only when actually executing an event handler after such a notification is the server busy and consuming CPU or otehr server resources. It is possible to set a timer going on the server which will interrupt the waiting and execute a .Idle() event handler, if one is defined for the form. This event will not be triggered if there are unprocessed real client side events queued and the timer is restarted on return from an event handler.

This event handler is only called if the [*IdleTimer* property is set to a positive integer value for the timeout in milliseconds and will continue to be scheduled until *IdleTimer* property is reset back to its default value of -1 which disables the feature.](PROP_FORM_IDLETIMER.htm)

The Idle() event can be used for polling server status changes such as mail being available. You are cautioned against too frequent polling as this can put an unnecessary load on the server. Also you will want to minimise the amount of work done in the handler in order to keep the client responsive as the server can execute only one event at a time. In particular the handler should be careful not to block waiting for a database lock or some other unavailable resource as this will leave the client in a busy state and confuse the user.


    -DEFEVENT Form.Idle()
       REM do some incremental stuff
       ...
       IF (Completed)
          .form.IdleTimer = -1
       END IF
    END EVENT

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
