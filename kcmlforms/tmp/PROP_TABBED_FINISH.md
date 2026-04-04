Finish (tabbed control event)

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
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called when Finish button on Wizard style tabs is clicked**

The Finish() event is called when the Finish button is clicked on a tab control. The Finish button is displayed in place of the Next button on the last page of a tab control that has Appearance set to *Wizard*. The event handler gives the application a chance to perform the operation that the Wizard has led the user through.

##### Example:


     DEFEVENT Form1.tabControl.Finish()

##### See also:

Other [tabbed](tabbed.htm) properties, methods and events, [tabbeditem](tabbeditem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
