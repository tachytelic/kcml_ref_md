DropDown (grid control event)

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
<img src="/bitmaps/browsetool20.png" data-border="0" width="16" height="15" alt="event icon" /> Event

**Called before the drop down portion of the control is displayed**

This event is called each time the drop down section of a grid cell drop down combo box is displayed.

Note that when an edit cell is created, it searches the cell, then the row, then the col and finally the grid for a listbox to use. Just setting the DropDown and DropStyle properties is not sufficient as it will not be known what lsit to use. Any action that affects the list may be used to instantiate the list, such as setting the DropDown property or adding items to the list using the Add() property.

REM Set up column 5 to have a drop down list .gridControl1.Cell(0, 5).DropDown = &.DropAlways .gridControl1.Cell(0, 5).DropStyle = &.DropDown REM Force a list to be created for the column .gridControl1.Cell(0, 5).DropDownFilled = FALSE REM The first time a drop down in this column is selected, the DropDown REM event will be triggered. CursorCol will be 5 and so we will REM be able to fill in the drop down contents.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
