ShowCancel (tabbed control property)

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
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Adds Cancel button to wizard style tabs**

Used to show or hide the "Cancel" button on tab controls with a Wizard appearance. The cancel button allows the user to discard any changes made in the wizard.

##### Example:


     IF (.tabControl.ShowCancel)
       ...
     END IF

##### See also:

Other [tabbed](tabbed.htm) properties, methods and events, [tabbeditem](tabbeditem.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
