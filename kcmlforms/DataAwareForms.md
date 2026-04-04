Data aware forms

Edit controls, grids and static text on forms can be made data aware to simplify programming database applications. Data aware controls have their values synchronised with the originating data buffers on the server. If the user alters the value in a bound control that new value is sent to the server and the bound row buffer or strcuture is updated when the next form event fires. Similarly any changes to bound row buffers on the server will be automatically sent to the form at the end of the event.

The binding links a field in a buffer using its field definition.

##### Traditional approach

A control is linked to a specific row buffer using the [DataSource](tmp/PROP_DATASOURCE.htm) property and then to a column in the row via the [DataField](tmp/PROP_DATAFIELD.htm) property. A row buffer with the same name as the DataSource must exist in the program and a [field](mk:@MSITStore:kcmlrefman.chm::/TutorialFields.htm) must exist with the name of each of the DataField properties.

This linkage can be established by editing these properties directly in the Forms Designer or by using drag and drop from the Forms Designers table view. See [Working with database tables in the Forms Designer](FormsDesignerWorkingwithTables.htm). To use the Forms Designer you must be using the native KCML database but you can set these properties manually and therefore use data awareness with any database as described [elsewhere](BespokeDataAwareness.htm).

##### The modern approach

Starting with KCML 6.10 a new [DataBind](tmp/DataBind.htm) control has been introduced which is bound to a KCML variable and which specifies a [DEFRECORD](mk:@MSITStore:kcmlrefman.chm::/DEFRECORD.htm) name defining it. This allows binding to both database rows and structures that can be described by DEFRECORD. For more on the DataBind control see [here](DataBinding.htm).

##### Events

When the form is presented the controls will be populated from the columns of the bound database row buffer after the forms [Enter()](tmp/PROP_FORM_ENTER.htm) event and prior to the [Show()](tmp/PROP_FORM_SHOW.htm) event. This allows the application to load an initial row buffer during the Enter() event. If the row buffer is changed in the application the form will be updated at the time of the next form method or event. If one of the columns is edited on the form then the new value of that column will be sent back to the server and the row buffer updated with the next form event. Only changed columns are sent in either direction.

If a grid is data aware the binding is done per cell in a column so each row of the grid will correspond to a row in the bound row buffer. To do this the DataSource property is set for the whole grid and the DataField property is set per column. The grid can be explicitly filled using the [DataAwareRow()](tmp/PROP_GRID_DATAAWAREROW.htm) method or it can be filled on demand by raising a [RowRequest()](PROP_GRID_ROWREQUEST.htm) event to ask for more data if the grid's [DataPending](tmp/PROP_GRID_DATAPENDING2.htm) property is TRUE and the user attempts to move past the last row of the grid, e.g. by pressing the down arrow or page down key or by moving the vertical scroll bar down as far as it will go. The event handler can then make the grid bigger and fetch a fresh row buffer from the database. At the end of the event the new row will be populated automatically.
