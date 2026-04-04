ALTER TABLE

ALTER TABLE tablename *col_action* ( *col_description*, \[*col_description*, ......\])

This statement allows columns to be added, modified, removed or renamed from/to an existing **Type 7** table. The allowed *col_action* actions are

ADD\
DROP\
MODIFY\
RENAME\

The **ADD** action allows columns to be added at the end of the row. In this case *col_description* takes the same format as the column description used in [CREATE TABLE](CREATE_TABLE.htm), with the exception that a STARTBYTE cannot be specified. Columns created in this manner will be initialised to all zeroes, except for VARCHAR's which will be initialised to 0x20's.

The **DROP** action is used to remove columns from the table. Columns following the column to be dropped are shuffled down to fill the space vacated by the dropped column so that free space is left at the end of the row. In this case *col_description* is simply a column name. Columns cannot be dropped if they are a **SERIALIZED** column, if they are a **BLOB_ID** column or if they form part of an index or word search index.

The **MODIFY** action alters columns which already exist in the table. Once again *col_description* take the same form as the column description in [CREATE TABLE](CREATE_TABLE.htm) with the exception that a STARTBYTE cannot be specified. There are several restriction that apply to the **MODIFY** action :

- The column may not be part of an index or word search index.
- The type of a column may not be altered.
- A column may not be decreased in size.
- A multiply occurring column may not have it's number of occurrences reduced.
- The width of individual columns within an OCCURS may not be changed.

When a column size is increased the data in rows that already existed is accordingly adjusted - VARCHAR's are space padded at the end, leading zeroes are added to INTEGER and HEX columns and NUMERICS are re-evaluated to fit into the new column size. It should be noted that information in the schema regarding the column will be exactly that which is specified in the *col_description*, any information from the previous definition of the column which needs to be retained must be specified in the *col_description*.

The **RENAME** action is used to rename columns in the table. In this case *col_description* is simply a pair of column names :

*old_column_name* *new_column_name*

The only restrictions are that *old_column_name* must not be the name of a serialized column and *new_column_name* should not already exist.

Examples

ALTER TABLE XX00test ADD (newcol VARCHAR(10)) ALTER TABLE XX00test MODIFY (newcol VARCHAR(20) NAME 'New column') ALTER TABLE XX00test RENAME (newcol oldcol) ALTER TABLE XX00test DROP (oldcol)

See also:

[CREATE TABLE](CREATE_TABLE.htm)
