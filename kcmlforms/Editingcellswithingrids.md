Editing cells within grids

------------------------------------------------------------------------

Automatic editing with AutoEdit

KCML 6.00 introduced an easy and efficient technique to edit grids on a row by row basis. It is particularly useful for data aware grids where grid rows correspond to rows in a database table. If the [AutoEdit](tmp/PROP_GRID_AUTOEDIT.htm) property is enabled for a grid then clicking in a row will allow editing of the cells in that row. This can be set at design time. Switching to edit mode for teh target cell will be automatic when focus moves into the grid. If the [TabThrough](tmp/PROP_GRID_TABTHROUGH.htm) property is also set then the user can move left and right through the row with TAB and BACK-TAB without triggering any unnecessary events. The [EditRowNotify()](tmp/PROP_GRID_EDITROWNOTIFY.htm) event handler will be called only when the user moves between rows or when focus enter or leaves the grid to allow the server to lock and refresh the new rows and update and unlock the previous ones. The grid stays in edit mode while focus remains in the grid.

ServerText design time property

Prior to KCML 6.00 the programmer had some control over whether the server tracked changes in editable grids. If the [ServerText](tmp/PROP_GRID_SERVERTEXT.htm) design time property was set to FALSE for the grid control, editing was a local action within the client and no data was sent back to the server when the cell was updated. This was only useful if the grid was data aware and the data aware mechanism was to be used to retrieve the changes. If the property was set to TRUE then KCML maintained a copy of the grid in memory on the server. This may require a lot of space and the default was FALSE. This was a design time property that had to be set in the [Forms Designer](FormsDesignerWorkingwithGridControls.htm).

As of KCML 6.00 ServerText is fixed at TRUE by default. Any attempt to change it is ignored.

The EditCell(), EditGrid(), and EditRow() methods

These methods were the original editing mechanism for KCML5. They give more control in some circumstances but are more difficult to use than AutoEdit. In particular the program needs to switch the grid into editing mode whereas with AutoEdit the grid can switch on its own. The use of AutoEdit in preference to these legacy methods is strong recommended.

To allow the user to edit the contents of a grid cell one of the [*EditCell()*,](tmp/PROP_GRID_EDITCELL.htm) [*EditGrid()* and](tmp/PROP_GRID_EDITGRID.htm) [*EditRow()* methods should be called from within a mouse activated event handlers for the grid, e.g.](tmp/PROP_GRID_EDITROW.htm) [*LeftClick()*, or *[RightClick()](tmp/PROP_GRID_RIGHTCLICK.htm)*. Once the user clicks on a cell the](tmp/PROP_GRID_LEFTCLICK.htm) [*EditCell()*,](tmp/PROP_GRID_EDITCELL.htm) [*EditGrid() or*](tmp/PROP_GRID_EDITGRID.htm) [*EditRow()* method is then called specifying the row and column that the user selected. The](tmp/PROP_GRID_EDITROW.htm) [*CursorRow* and](tmp/PROP_GRID_CROW.htm)

*CursorCol* properties are used to return the location of the mouse click within the grid. For example:

-DEFEVENT Form1.GridControl1.LeftClick() ..EditGrid(..CursorRow, ..CursorCol) END EVENT

- If
  *EditCell()* is used then the user is able to click on a cell and change its contents. Pressing Tab or Shift Tab will then move to the next or previous control in the forms tab order.
- Using
  *EditGrid()* allows the user to click on any cell within the grid and use Tab and Shift Tab to move to the next or previous cell.
- Using the
  *EditRow()* method allows a whole row to be edited, Tab and Shift Tab are used to move to the next or previous cells within the row. If Tab is pressed at the end of a row or if Shift Tab is pressed at the beginning of a row then focus moves away from the grid.

These methods work on all versions of KCML5 but they must not be used on a grid with the AutoEdit property enabled as the event mechanisms are multually incompatible.

Note that the mouse activated event handlers such as [*LeftClick()* and](tmp/PROP_GRID_LEFTCLICK.htm) [*RightClick()* are only enabled for cells that have the](tmp/PROP_GRID_RIGHTCLICK.htm) [*LeftAction*,](tmp/PROP_GRID_LEFTACTION.htm) [*RightAction* and the](tmp/PROP_GRID_RIGHTACTION.htm) [*LeftSelect* and](tmp/PROP_GRID_LEFTSELECT.htm)

*RightSelect* properties set accordingly.

Validating user entry - The Validate property and the EditValidate() event handler

When a user leaves a cell it is possible to call the [*EditValidate()* event handler when the user leaves a cell. To enable the](tmp/PROP_GRID_VALIDATE.htm) [*EditValidate()* event the](tmp/PROP_GRID_VALIDATE.htm)

*Validate* property must be set to either ***EditWithValidate*** or ***EditAlwaysValidate*** for example:

.GridControl1.cell.Validate = &.EditWithValidate

In this example, the the [*EditValidate()* event handler will only get called if the user changes the contents of the cell. To force execution of the](tmp/PROP_GRID_VALIDATE.htm)

*EditValidate()* event, the validate event should be set to ***EditAlwaysValidate***.

Once the [*EditValidate()* event has been called, the](tmp/PROP_GRID_VALIDATE.htm) [*ValidateText\$* property contains the current contents of the cell, while the](tmp/PROP_KCMLEDIT_VALIDATETEXT.htm)

*Text\$* property contains the contents of the cell prior to any changes. If the users entry is invalid executing a RETURN FALSE statement will return focus back to the cell, for example

-DEFEVENT Form1.GridControl1.EditValidate() IF (..ValidateText\$ \< Check\$) 'ProcessEntry(..Text\$, ..ValidateText\$) ELSE RETURN FALSE END IF END EVENT

When editing and entire grid with the [*EditGrid()* method or individual rows with the](tmp/PROP_GRID_EDITGRID.htm) [*EditRow()* method you can force cells within the row to be skipped when the user attempts to Tab or Shift Tab into the row. This is done by setting the](tmp/PROP_GRID_EDITROW.htm) [*Validate* property for the cell to ***NoEdit***. Setting ***NoEdit*** for a cell will only skip the cell upon a Tab or Shift Tab, it does not prevent the user from simply clicking on the cell. To completely disable editing for a cell you should set the](tmp/PROP_GRIDCELL_VALIDATE.htm)

*LeftAction* property to ***Ignore***.

The ***Default*** setting for the [*Validate* property allows editing but will not call the](tmp/PROP_GRIDCELL_VALIDATE.htm)

*EditValidate()* event handler when the user leaves the cell.

Validating user entry - The EndEdit() event handler

When an editing session is completed by the user the

*EndEdit()* event handler is called.

- If the [*EditCell()* method is used then](tmp/PROP_GRID_EDITCELL.htm)
  *EndEdit() event* is called each time the user leaves a cell. The user can move by pressing Tab, Shift Tab or Escape or by clicking on another cell or on another control.
- If the [*EditGrid()* method is used then the](tmp/PROP_GRID_EDITGRID.htm)
  *EndEdit()* event is only called when the user selects another control on the form, or if the Escape key is pressed.
- If the [*EditRow()* method is used then the](tmp/PROP_GRID_EDITROW.htm)
  *EndEdit()* event is only called when the user attempts to Tab or Shift Tab off of the current row. It is also called if the user clicks on another cell or on another control, or if the Escape key is pressed.

The exact reason for the end of the current editing session can be determined within the [*EndEdit()* event handler with the](tmp/PROP_GRID_ENDEDIT.htm)

*EditReason* property.

**Note:** The *EndEdit()* event is not triggered for grids in [AutoEdit](tmp/PROP_GRID_AUTOEDIT.htm) mode.
