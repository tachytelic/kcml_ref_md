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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Message(int, int, string) Method

**Used to send messages to forms and controls**

|      |            |
|------|------------|
| Int1 | Message ID |
| Int2 | wParam     |
| Str  | lParam     |

Allows a knowledgeable programmer to send a message to the control to which the method is applied. It invokes the Windows **SendMessage()** API however no return value is available. The lParam parameter is assumed to be a string and is sent as a char \* pointer. To send an integer as the lParam use the [Message(int, int, int)](PROP_GENERIC_SENDMI.htm) method.

This method should only be used for functionality that is not available through the standard KCML methods. For example, both of the following could be used to add an item to a list box. .listControl1.Message(0x180, 0, "Hello World") .listControl1.Add = ("Hello World")

The second example illustrates the preferred method. The former method hardwires a magic constant that may change in future versions of Windows (it did change in the transition from 16 to 32 bits).

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
