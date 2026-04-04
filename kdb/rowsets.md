What are rowsets?

Rowsets are a collection of rows from a table. They can be accessed sequentially or randomly using the KCML database API. Initially a table needs to be opened using [KI_OPEN](tmp/KI_OPEN.htm) on a [handle](handle.htm) which can then be used in later functions to specify the rowset involved. Eventually when the rowset is no longer required, the handle should be closed with a [KI_CLOSE](tmp/KI_CLOSE.htm).

Rows can be accessed in sequential order using an index, if one exists, by using [KI_START](tmp/KI_START.htm) or [KI_START_BEG](tmp/KI_START_BEG.htm) to establish an initial position and [KI_READ_NEXT](tmp/KI_READ_NEXT.htm) to access one row at a time. The rowset can be traversed in its natural order without an index using the [KI_READ_RAW](tmp/KI_READ_RAW.htm) call which permits array fetching of rows.

When a row is read from a rowset it populates a row buffer which can be decomposed into columns using [FLD()](mk:@MSITStore:kcmlrefman.chm::/FLD(.htm) operators. The fields representing columns in a table can be instantiated using the [KI_FLD](tmp/KI_FLD.htm) call. Each row has an associated [rowid](rowid.htm) which identifies it and which can later be used to reload or update the row randomly.

The results of an SQL query can also be considered to be a rowset though in this case random access and indexed access is not possible.
