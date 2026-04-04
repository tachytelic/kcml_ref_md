Terminate (form control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Terminate(int) Method

**Used to terminate the form**

|     |                                                            |
|-----|------------------------------------------------------------|
| Int | Value returned to the [Open()](/OpenFormmethod.htm) method |

This method is used to terminate the current form under program control from within an event handler. The specified integer value is returned by the form [Open()](/OpenFormmethod.htm) method. For example: .form.Terminate(5)

**Note:** Currently the integer value returned by this method is limited to be an unsigned 16 bit integer between 0 and 65535. Numbers greater than this will be reduced modulo 65536. In a future version of KCML this may be relaxed.

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
