Print (richedit control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Print() Method

**Print to an open printer**

This method is called after a successfull call to the [*PrintOpen()* method to print the contents of the control to the select printer.](PROP_RICHEDIT_PRINTOPEN.htm)

Upon completion, i.e. once all text has been sent to the printer or if print fails, the [*PrintStatus()* event handler is called. This gives the program an opportunity to display an appropriate error.](PROP_RICHEDIT_PRINTEVENT.htm)

##### Example:


     .rtfControl.Print()

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
