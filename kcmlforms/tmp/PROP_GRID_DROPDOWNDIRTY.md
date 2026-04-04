DropDownFilled (grid control property)

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
5.02+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Boolean property

**Determines whether the drop down portion of the control has been filled**

This property is used to determine whether the drop down portion of a grid cell has been filled. This property should be set to *TRUE* after the drop down portion of the control has been filled. If this property is set to *TRUE* then the [DropDown()](PROP_GCOMBO_DROPDOWN.htm) event handler will not be called again unless this property is set back to *FALSE* before the event occurs again. For example: -DEFEVENT Form1.gridControl1.DropDown() 'FillEditControl() .gridControl1.DropDownFilled = TRUE END EVENT

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
