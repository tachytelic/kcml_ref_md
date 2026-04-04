Flush (form control method)

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
<img src="/bitmaps/browsetool22.png" data-border="0" width="16" height="15" alt="method icon" /> Flush() Method

**Forces an update of any controls that the event handler has modified**

This method is used to force an update of any controls that the event handler has modified. Normally when the properties of a control are changed within an event handler the actual change is not made until the event handler has finished. This is not always desirable as the event may need to constantly update controls on the form while it is processing. For example: -DEFEVENT Form1.ProcessData() WHILE (Count++ \< 100) DO 'ProcessRecords() .gaugeControl1.Position = Count .form.Flush() WEND END EVENT

##### See also:

Other [form](form.htm) properties, methods and events and [generic](generic.htm) properties and methods.
