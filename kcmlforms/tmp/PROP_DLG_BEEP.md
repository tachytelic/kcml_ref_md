Beep (form control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Beep(int) Method

**Makes the corresponding Windows sound**

|     |                                                                  |
|-----|------------------------------------------------------------------|
| Int | Value ranging from 0-5 corresponding to the sound type required. |

This method is used to sound a warning beep based on the standard sounds set in the Windows control panel. A value ranging from 0 - 5 is used to specify the sound, these values correspond to the following Windows sound types:

KCML constant

Value

Sound

\_BEEP_NONE

0

Default sound

\_BEEP_CRITICALSTOP

1

Critical stop

\_BEEP_QUESTION

2

Question

\_BEEP_EXCLAMATION

3

Exclamation

\_BEEP_ASTERISK

4

Asterisk

\_BEEP_DEFAULT

5

Default beep

For example, the following would play the Exclamation sound: .Form.Beep(\_BEEP_EXCLAMATION)

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
