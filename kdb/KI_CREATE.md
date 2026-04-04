KI_CREATE

This call will size, create and open a new table. The size of the table is deduced from the number of rows and the row length. The *Type* specifier should be 6 unless backward compatibility is required. This call cannot be used for table formats later than 6 or for KDB tables which must be created by executing an SQL [CREATE TABLE](../CREATE_TABLE.htm) statement.

The index details are passed by symbol index sym of an array keyspec\$() which has up to eighteen 33 byte entries defining each of the eighteen possible indices. This symbol index should be zero for an unindexed consecutive table, otherwise at least one index must be defined. To define an index, the first byte of any entry, which defines whether a key path permits duplicate entries, must be 'Y' or 'N'. Any other value terminates the key definitions. The next 32 bytes of the definition is an array of 8 segment specifiers with the structure:

|                   |                                 |
|-------------------|---------------------------------|
| start of segment  | 2 bytes binary counted from 1   |
| length of segment | 1 byte binary                   |
| flag byte         | 1 byte, must be HEX(00) for now |

Any index may therefore be defined in terms of up to 8 segments, with the restriction that the total length may not exceed 128 bytes. The segments may appear anywhere in the row, need not exactly correspond to columns (though they ought to) and they may overlap. When less than the full complement of eight segments are required, then the spare specifiers must be set to HEX(00 00 00 00). At least one specifier is required.

To discover how big a table will be a call can be made to ['KI_SIZE_FILE](KI_SIZE_FILE.htm).

The *packing factor* parameter was not used in early versions of the database. It defines the expected average packing of index blocks expressed as a percentage. The index is divided up into blocks and in general there will be free space in each block. When a block fills the database will automatically split it into two blocks, each half full. Thus a volatile table will have its blocks on average half full and this needs to be taken into account when sizing the index. A packing factor of 100 would be appropriate for a non-volatile table and a factor of 50 would be suitable for a table in which rows are frequently created or deleted.

The *blocklen* parameter defines the size of an index block in allocation units of 256 bytes. Values less than 2 are rounded up to 2 corresponding to 512 bytes. This is the value used on version 4 and earlier. The maximum value supported in version 5 tables is 8 corresponding to 2048 bytes. Increasing the index blocksize increases the maximum number of rows that can be indexed. There is a point at which increasing the index block size becomes counter productive and KCML will ignore attempts to set the blocklen to a greater value than is sensible.

Temporary files

Temporary files can be created with KI_CREATE. For more information see [temporary files](mk:@MSITStore:kcmlrefman.chm::/temporary.htm).

Compatibility

Not available for the KDB database introduced in KCML6 which requires the use of SQL.

Prior to KCML5 only 9 indices and 4 segment per index were allowed. The *Type* flag was introduced in KCML5 to allow the new type 6 format to be specified. The *Type* flag can be zero to specify use of the older rules listed below for selecting table type.

Version 4 KISAM did not have the blocklen parameter. It was assumed to be 2. In version 3 K-ISAM there was also no packing parameter. Packing was assumed to be 50%.

The presence of the packing and blocklen parameters govern the type of index created and its maximum size. If packing is set to zero or is missing, the default in the original version 3 'KI_CREATE stub, then the table will be created in KISAM version 3 format and will be limited to a maximum index size of 16MB.

If the blocklen parameter is zero or missing, the default for the stub routines supplied with KISAM version 4 and earlier, then the table will be created as a type 4 table with an effective blocklen of 2.

Note that the contents were not initialised on versions prior to KCML 3.10 and a separate call to ['KI_INITIALISE](KI_INITIALISE.htm) was then required.
