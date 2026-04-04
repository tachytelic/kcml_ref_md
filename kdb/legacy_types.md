Legacy database table formats

The current database storage scheme was introduced with KCML 6.00 and like earlier versions it is based on native operating system files. Such files are sometimes called type 7 files and they are quite different internally compared to earlier storage layouts. Note however that all versions of KCML can read and write the file formats of previous versions.

| File type | KCML version | Details |
|----|----|----|
| 1 | 2.0 | Obsolete |
| 2 | 2.0 | Obsolete |
| 3 | 3.0 | Effectively obsolete as it will be converted to type 4 if referenced by a later KCML |
| 4 | 3.1 | Fixed size. Limited index size. |
| 5 | 3.2 | Fixed size. Larger index size. |
| 6 | 5.0 | Support for extents. Unlimited index and data size. Word search indexing. |
| 7 | 6.0 | Page structured. Embedded schema. BLOB support. Requires KDB connection. |

Type 7 tables are based on 8kb blocks called pages which can contain either data or index blocks. There are no extents and tables will grow as required. The non-unique index feature of previous versions has been dropped on the grounds of performance and all indices must now be unique. Word search index block are now in the same file rather than held in parallel files. Arbitrary sized binary data called [BLOBs](BLOBsupport.htm) are areso stored in the same file.

Up to KCML 6.00 and the type 7 file format, tables could be accessed outside of a database schema using the default connection. The current table format can only be used in the context of an overall database schema on a specific database connection. Furthermore they can only be created using DDL statements in SQL and the KI_CREATE API is not available.

File types up to and including type 6 can be converted to a type 6 file in place using the [krebuild](krebuild.htm) utility. To convert to the current type 7 format file the [kconvert](kconvert.htm) utility must be used and it will create a new file rather than convert in place.
