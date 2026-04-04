Indexing

By adding an index to a table a program can traverse the table sequentially in a different order to the natural order of rows. It also provides for direct access to a specific row based on a key or to a subset of the table based on a starting key value.

Adding an index to a table

This is done with the [CREATE INDEX](CREATE_INDEX.htm) SQL statement. Only UNIQUE indices where all the keys are different are supported.

With the original KCML storage formats prior to type 7, all the inices for a table had to be define when the table was created using [KI_CREATE](tmp/KI_CREATE.htm). Non unique indices were also supported where duplicate key values were permitted. This was a convenience for programmers but could often have a serious performance overhead.

Naming an index

In a KCML program an index is linked to a path number which is a integer counted from 1. When the index is created the name given to the index must be constructed from the table name and the path number e.g. for path 1 on table FOO the index would be called FOO_A1. The letter A distinguished the index from a word index.

Defining a key

A key can involve one or more columns up to a maximum of 8. To build a key from a row buffer use KI_BUILD. The key is then useable in [KI_READ](tmp/KI_READ.htm) to read randomly or in [KI_START](tmp/KI_START.htm) to define the start of a sequential rowset. This key string can have a maximum size of 128 bytes.

Sequential access

You can use [KI_START_BEG](tmp/KI_START_BEG.htm) to create an ordered rowset based on the given index which includes all the rows atring with the first one in the index. To limit the rowset to an open ended list of rows that start at a given key value the [KI_START](tmp/KI_START.htm) call is available. To limit the list further to just those rows that share a number of columns from the leading part of the key then [KI_START_ON](tmp/KI_START_ON.htm) is preferable as only those rows which have those particular column values will be included. To proceed backwards use a negative path number.

[KI_READ_NEXT](tmp/KI_READ_NEXT.htm) us used to traverse the sequential rowset established by a start operation. It is a requirement that the same path number is used in each call. Changing the sign of the path number will reverse the direction of traversal.

Random access

[KI_READ](tmp/KI_READ.htm) allows a program to pick a particular row from a table where the columns exactly match those of the supplied key. If no columns match the key then a KE_NOTFOUND [status](tmp/errorcodes.htm) code is returned.
