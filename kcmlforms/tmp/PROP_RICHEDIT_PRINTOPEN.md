PrintOpen (richedit control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> PrintOpen(string, int) Method

**Opens the printer**

***Str***      The name of the document\
***Int***      ***TRUE*** if the Windows default printer is to be used

This method is called prior to the [*Print()* method to open a connection to a printer. If the second parameter is ***TRUE*** then the default Windows printer is used otherwise the standard Printer Setup dialog is displayed allowing the user to manually select a printer.](PROP_RICHEDIT_PRINT.htm)

Upon completion, i.e. when the user has selected a printer or if the connection fails, the [*PrintStatus()* event handler is called. This gives the program an opportunity to display an appropriate error, or if successful the](PROP_RICHEDIT_PRINTEVENT.htm) [*Print()* method can be called to physically print the information.](PROP_RICHEDIT_PRINT.htm)

Note that nothing is sent to the printer until the [*PrintClose()* method is executed. This allows several documents to be printed together, for example as part of a mail merge.](PROP_RICHEDIT_PRINTCLOSE.htm)

Example: .rtfControl1.PrintOpen("Mail Merge", FALSE)

##### See also:

Other [richedit](richedit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
