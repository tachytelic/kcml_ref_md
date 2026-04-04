EditValidate (grid control event)

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

**Called when the user moves away from a cell that is being edited and has been modified**

This event handler is called when a user modifies the contents of a grid cell*.* This event handler is only called for cells that have the [*Validate* property set to ***EditWithValidate*** or ***EditAlwaysValidate***.](PROP_GRIDCELL_VALIDATE.htm)

Once called the current contents of the grid cell are stored in the [*ValidateText\$* property while the original contents are stored in the](PROP_KCMLEDIT_VALIDATETEXT.htm) [*Text\$* property. To return the user back to the cell if the required validation failed, the RETURN FALSE statement is executed, for example: -DEFEVENT Form1.GridControl1.EditValidate() IF (..ValidateText\$ \< Check\$) 'ProcessEntry(..Text\$, ..ValidateText\$) ELSE RETURN FALSE END IF END EVENT](PROPSTR_TITLE.htm)

If the validation is triggered by an attempt to move to another cell then the row and column of that cell will be available in the [NewRow](PROP_GRID_NEWROW.htm) and [NewCol](PROP_GRID_NEWCOL.htm) properties.

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
