ValidateSelChange (kcmledit control property)

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

**Causes a validate event when the user changes the selected item in the drop down portion of the control.**

This boolean property can be used to tell an edit control that a [Validate()](PROP_KCMLEDIT_VALIDATE.htm) event should be triggered when the user changes the selection in the dropdown list. This triggers only in this specific case and avoids having to use the more general, but strongly deprecated, [SelChange()](PROP_EDIT_SELCHANGE.htm) event on the listbox. Unlike the **SelChange** event, only user actions (such as typing in the editbox until the description appears, or selecting an item with the mouse/keyboard) will generate the event. Programmatic changes to the [Text\$](PROPSTR_TITLE.htm) property will not force this event.

This property only applies to edit controls and not to grid cells. Form1.editControl1.ValidateSelChange = TRUE

##### See also:

Other [kcmledit](kcmledit.htm) properties, methods and events and [generic](generic.htm) properties and methods.
