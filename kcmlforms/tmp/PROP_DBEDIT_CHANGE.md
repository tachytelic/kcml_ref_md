Change (kcmledit control event)

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
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called whenever the text in the DBEdit control is changed**

This event is called when the user attempts to change the text in a DBEdit. It will still be called even if the user makes an invalid input and the text remains unchanged.

##### Example:


     DEFEVENT Form1.editControl.Change()

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
