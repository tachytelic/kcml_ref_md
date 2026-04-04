DataPending (Grid control property)

When this property has been set TRUE the [RowRequest()](PROP_GRID_ROWREQUEST.htm) event handler is called when the user attempts to move past the last row of the grid, i.e. by pressing the down arrow or page down key or by moving the vertical scroll bar down as far as it will go. The [RowRequest()](PROP_GRID_ROWREQUEST.htm) event handler can then be used to extend the grid and add additional rows.

To add new rows of information the grid must first be extended by modifying the [Rows](PROP_GRID_ROWS.htm) property before new data can be inserted. Once the last row has been added DataPending must again be set to TRUE to enable this feature. If there are no more rows to add to the grid then this property should not be set as it is reset to FALSE automatically when the event triggers.

**Note:** When DataPending is set an empty row is created at the end of the grid. When KClient attempts to display this row the [RowRequest()](PROP_GRID_ROWREQUEST.htm) event will be called. Once set both DataPending and the empty row will persist until the RowRequest event handler is called. Manually resetting DataPending is not supported.

**Note:** If DataPending is set before [Rows](PROP_GRID_ROWS.htm) the [RowRequest()](PROP_GRID_ROWREQUEST.htm) event will be thrown when the grid is scrolled to the row that was the bottom of the grid at the time DataPending was set. Not at the actual bottom of the grid which has been modified by setting [Rows](PROP_GRID_ROWS.htm). This behaviour is provided to maintain backward compatibility with legacy applications. New applications should be careful not to modify [Rows](PROP_GRID_ROWS.htm) after setting Datapending until the [RowRequest()](PROP_GRID_ROWREQUEST.htm) event has been called.

See this [example program](../examplefillinggrid.htm) for a demonstration of filling a grid using this method.
