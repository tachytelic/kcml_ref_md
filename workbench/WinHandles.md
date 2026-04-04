## Handles Window

Displays all the current database handles open in the program.

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/WinHandles.png" data-border="0" width="546" height="173" alt="Handles Window" />

</div>

| Value | Description |
|----|----|
| Handle Number | This is the internal KCML handle number. |
| Type | This shows what type of database the handle is connected to. A type prefixed by '-' represents a temporary handle. |
| Connection Number | This is the internal KCML connection number. |
| Table Name | This is the name of the table to which the current handle is connected. |
| Mode | (W)rite, (R)ead, e(X)clusive, (U)tility. Utility mode means unrestricted access. |
| Record Length | Length of the record. |
| User Path | \- |
| WCount | The amount of users that have the file open in write mode. The database can only be opened in exclusive mode if this count is zero. |
| State | Closed, Opened, Prepared, Executed, Control, Failed |
