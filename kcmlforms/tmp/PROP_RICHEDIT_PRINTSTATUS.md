PrintStatus (richedit control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Status of printing when a PrintStatus event occurs**

This property is used within the [*PrintStatus()* event handler to determine the status of the print operation that triggered the event. Possible values are](PROP_RICHEDIT_PRINTEVENT.htm)

|  |  |
|----|----|
| 0 | The print job was created successfully. Now OK to invoke the .Print() method to print the text. |
| 1 | The print job could not be created. |
| 2 | The control contents were printed successfully. |
| 3 | The control was unable to prints the contents. |
| 4 | The user cancelled the print setup or printer selection dialogs. |

Example - DEFEVENT Template.rtfcontrol1.PrintStatus() SELECT CASE (..PrintStatus) CASE 0 REM Print open successful .rtfControl1.Print() .rtfControl1.PrintClose() CASE 1 REM Print Open fail . . . CASE 2 REM Print document successful . . . CASE 3 REM Print document failed . . . CASE 4 REM user cancelled dialog . . . END SELECT END EVENT

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
