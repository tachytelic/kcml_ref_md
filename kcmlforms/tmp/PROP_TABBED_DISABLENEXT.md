DisableNext (tabbed control property)

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
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Disable the Next button on wizard style tabs**

Used to disable or enable the "Next" / "Finish" buttons on tab controls with a Wizard appearance. A Wizard application might want to do that until the user has entered valid data on the currently selected page. When all the data has been collected and validated the button can be re-enabled.

##### Example:


     IF (.tabControl.DisableNext)
       ...
     END IF

##### See also:

Other [tabbed](tabbed.htm) properties, methods and events, [tabbeditem](tabbeditem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
