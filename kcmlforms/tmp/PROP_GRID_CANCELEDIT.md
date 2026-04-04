CancelEdit (grid control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Run<br />
time<br />
only</td>
<td>Read<br />
only</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
6.0+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Used in EditRowNotify to show taht the user cancelled the edit**

The CancelEdit property is defined in the [EditRowNotify](PROP_GRID_EDITROWNOTIFY.htm) event to indicate whether the row edit was terminated by a cancel action. Normally clicking on a Cancel button or hitting escape activate the Cancel button and terminates a form. However, the Cancel button may be disabled in which case hitting escape terminates the edit of an AutoEdit grid. This property is used to distinguish the cancel operation from any other means of provoking the event.

##### Example:


     n = .gridControl.CancelEdit

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
