Binary large objects in KCML databases

Binary Large Objects or **BLOB**s are streams of binary data of arbitrary size. They can be stored in KCML databases where they are not held inline in the rows directly but instead are referenced via a BLOB Identifier or **BID** which is stored in the column. A BID is a 6 byte token which can be passed on a subsequent call to retrieve the actual data. Thus the column width is 6. The BID represents where the data is stored in the table and may change if the data is incresed in size during an UPDATE operation. There can be more than one BLOB column per row but one BLOB cannot be associated with more than one row or more than one column in a row. BLOBs were introduced with type 7 tables.

When creating the table use a datatype of BLOB as in:

CREATE TABLE Movies (FILM VARCHAR(30), RELDATE DATE, STAR VARCHAR(30), TRAILER BLOB)

The database is unaware of what the BLOB actually represents and the database designer may need other columns to store that information. In the example above the BLOB might have been MPEG data but the database just sees binary bytes and if passed to an application by the data binding, it is up to the programmer to invoke an appropriate media player.

The column can be referenced in a program as the BID.

KCML provides an API to retrieve BLOBs by BID ([KI_BLOB_GET](tmp/KI_BLOB_GET.htm)) and to insert or update them ([KI_BLOB_SET](tmp/KI_BLOB_SET.htm)). The database will take care of space allocation within the table and will recover the space of deleted BLOBs. If a row is deleted the database will delete associated BLOBs automatically.

A row can be INSERTed into a table using [KI_WRITE](tmp/KI_WRITE.htm) with a NULL or zero BID. Setting a BLOB column to zero and UPDATEing the row with [KI_REWRITE](tmp/KI_REWRITE.htm) will automatically delete the BLOB that was previously associated with the column.

An application which loads a row containing a BLOB column will need to extract the BID from the column and use it in a call to KI_BLOB_GET to retrieve the data. If necessary this call will redimension the buffer to be large enough to hold the BLOB. In all cases it returns the size.

If the application wants to add a row containing a BLOB it should INSERT the row with a NULL column first. This can be done with KI_WRITE's option to write and lock. Then KI_BLOB_SET can be used to pass the row buffer and block buffer to the database which will save the BLOB, allocate a BID and insert it in the column and internally update the row in the table. The lock remains set and the application may then do nothing, may add another BLOB column the same way or update other columns. In any case it should finally unlock the row with a KI_UNLOCK or KI_REWRITE.

The database tracks the BLOBs it knows are associated with a row so attempting to UPDATE a row with a BLOB column which has been changed outside of this protocol will result in an error.

Data binding for forms will transmit a BLOB to a control automatically. Currently only pictures are supported and the control is responsible for determining the format of the BLOB and presenting it as a JPG, PNG or whatever.
