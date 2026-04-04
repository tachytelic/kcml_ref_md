EventPending (form control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> EventPending() Method

**Tests to see if the user has triggered another event**

Normally an event handler will continue processing until complete. Executing the *EventPending()* method allows the event to test to see if another event has been triggered and optionally exit the current event handler prematurely.

**Note:** In KCML versions prior to 6.10 build 8120 the EventPending() method checks to see if there is anything in the input stream from the client. It cannot distinguish between property values being returned from the client and events being triggered and so may return TRUE even though no event has has been triggered. The intention of EventPending() is to use it as a cancel option when processing may take some considerable time. It is recommended then to bring up a child form with just a cancel button (and, ideally, a progress bar), so that the result of EventPending() is unambiguous. IF (.form.EventPending()) RETURN FALSE END IF

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
