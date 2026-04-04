EndEdit (grid control event)

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

**Called when the user has finished editing a row**

This event handler is called when a grid editing session started with one of the [*EditCell()*,](PROP_GRID_EDITCELL.htm) [*EditGrid()*, or](PROP_GRID_EDITGRID.htm) [*EditRow()* methods is terminated.](PROP_GRID_EDITROW.htm)

- If the [*EditCell()* method is being used then this event handler will be called when the user attempts to move to another cell or to another control on the form.](PROP_GRID_EDITCELL.htm)
- If the [*EditRow()* method is being used then this event will be called when the user attempts to move to a cell out side of the current row, or when Shift Tab is pressed at the start of the row or if the Tab key is pressed at the end of the row. It will also be called if the user selects another control on the form.](PROP_GRID_EDITROW.htm)
- If the
  *EditGrid()* method is being used then this event will be called if the user selects another control on the form.

The [*EditReason* property is available within this event handler to determine the reason for the end of the edit session.](PROP_GRID_EDITREASON.htm)

Note that the [*EditValidate()* event handler will be called prior to *EndEdit()* if the](PROP_GRID_VALIDATE.htm) [*Validate* property for the cell is set to either ***EditWithValidate*** or ***EditAlwaysValidate***.](PROP_GRIDCELL_VALIDATE.htm)

**Note:** The EndEdit() event is used only with EditCell(), EditRow() and EditGrid(). It is not triggered when using the new [AutoEdit](PROP_GRID_AUTOEDIT.htm) grid editing technique introduced in KCML 6.00. This technique is recommended for all new coding of editable grids.

##### Example:


     DEFEVENT Form1.gridControl.EndEdit()

##### See also:

Other [grid](grid.htm) properties, methods and events, [gridcell](gridcell.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
