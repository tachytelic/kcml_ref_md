Working with large grid controls

------------------------------------------------------------------------

When working with large grids it is not desirable to fill every row as the user will be forced to wait while the grid is filled. Filling a grid with a large number of rows will not necessarily effect the user but it does mean that a large of amount information is being passed from the server to the client. In most cases the user may not want to view all the information anyway.

To cut down on the user delay and on network traffic a more preferable method of filling the grid is to add new rows to the grid when the user demands it. For example, when the grid is first displayed only 50 items are added. Adding 50 items to a grid is almost instant and generally will not cause a great deal of network traffic. As the user moves down through the grid you can then add additional blocks of rows to the grid automatically.

This functionality is achieved with the use of the [*DataPending* property and the](PROP_GRID_DATAPENDING2.htm) [*RowRequest()* event handler. Once the first block of data has been sent to the grid you then set the](tmp/PROP_GRID_ROWREQUEST.htm) [*DataPending* property to *TRUE*. With this property set, if the last line of the grid would be made visible to the user, i.e. if the user drags down the scroll bar, then the](PROP_GRID_DATAPENDING2.htm) [*RowRequest()* event handler is called. Within this event handler you could then send the next block of data to the grid. After a new block of data has been sent you must again set](tmp/PROP_GRID_ROWREQUEST.htm) [*DataPending* to re-enable the action. Once there is no more information to add to the grid then](PROP_GRID_DATAPENDING2.htm)

*DataPending* should be set to *FALSE*.

[Click Here](Examplefillinggrid.htm) for an example program.

 
