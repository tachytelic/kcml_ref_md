RowRequest() (Grid control event handler)

This event handler is used to add rows to the grid control when the user has attempted to move past the last row in the grid, i.e. by pressing the down arrow or the page down key or if the vertical scroll bar is moved to the very bottom. This event handler is only called when the [DataPending](PROP_GRID_DATAPENDING2.htm) property is set to *TRUE*. To add rows the event handler must first extend the grid by modifying the [Rows](PROP_GRID_ROWS.htm) property, then new data can then be placed into the rows. Once the new rows have been added the [DataPending](PROP_GRID_DATAPENDING2.htm) property must then be set again to make sure that the event handler is called again if necessary. To disable the event handler the [DataPending](PROP_GRID_DATAPENDING2.htm) property must be *FALSE*, which is the default setting.

See this [example program](../examplefillinggrid.htm) for a demonstration of filling a grid using this method.
