TabStop (generic control property)

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
<td>Advanced</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Style property (boolean property)

**Include in the forms tab sequence**

This generic Boolean property is used to include or exclude the control in the tabbing order of the form. This order is established at design time using the [tab order feature](/FormsDesignerSettingthetaborder.htm) of the forms designer. When the user presses the TAB key at runtime the focus will shift to the next control in the tab order. By setting this property to FALSE either at design time or at run time a control can be skipped in this sequence. However it is not possible to reorder the sequence at runtime in a program.

Note that a picture button that has the .TabStop property set FALSE will not take focus, even when clicked on, although the event will still be generated

This property should not be confused with the listbox property [.TabStop\$](PROP_LISTBOX_TABSTOP.htm) which is used to set tab expansion columns in a listbox.

##### See also:

Other [generic](generic.htm) properties, methods and events and [generic](generic.htm) properties and methods.
