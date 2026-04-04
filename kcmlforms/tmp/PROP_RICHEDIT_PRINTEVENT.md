PrintStatus (richedit control event)

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
<td>KCML<br />
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called whenever a PrintOpen() or Print() method is completed, with result in PrintStatus property**

This event handler is called immediately after a [*PrintOpen()* or *Print()* method has been invoked. Once called the *PrintStatus* property can be used to determine the status of the print operation, see](PROP_RICHEDIT_PRINTOPEN.htm) [*PrintStatus* for a list of return values. For example, - DEFEVENT Template.rtfControl1.PrintStatus() SELECT CASE (..PrintStatus) CASE 0 REM Print open successful .rtfControl1.Print() .rtfControl1.PrintClose() CASE 1 REM Print Open fail . . . CASE 2 REM Print document successful . . . CASE 3 REM Print document failed . . . CASE 4 REM user cancelled dialog . . . END SELECT END EVENT](PROP_RICHEDIT_PRINTSTATUS.htm)

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
