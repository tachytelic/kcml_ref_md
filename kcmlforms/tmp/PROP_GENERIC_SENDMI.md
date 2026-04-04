Message (generic control method)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Message(int, int, int) Method

**Used to send messages to forms and controls**

|      |            |
|------|------------|
| Int1 | Message ID |
| Int2 | wParam     |
| Int2 | lParam     |

Allows a knowledgeable programmer to send a message to the control to which the method is applied. It invokes the Windows **SendMessage()** API however no return value is available. The lParam parameter is sent as a DWORD. To send a string as the lParam use the [Message(int, int, str)](PROP_GENERIC_SENDMS.htm) method.

##### Example:


     .generic.Message(i, j, k)

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
