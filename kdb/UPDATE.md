UPDATE

UPDATE tablename SET column=expression \[, column=expression\]... \[ WHERE condition\]

This statement will update the specified columns in all the rows that meet the conditions set in the optional WHERE clause. If there is no WHERE clause then all rows are updated.

Examples

UPDATE SL00test SET quantity=0 WHERE color='red' UPDATE SL00test SET batchdate = '1999-10-31'

See also:

[SELECT](SELECT.htm), [INSERT](INSERT.htm), [DELETE](DELETE.htm)
