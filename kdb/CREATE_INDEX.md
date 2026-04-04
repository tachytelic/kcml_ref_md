CREATE INDEX

CREATE \[UNIQUE\] INDEX indexname ON tablename ( colname \[ASC\|DESC\] \[, colname ...\] )

where the table name should match that in the preceding CREATE TABLE statement. The index name should be the same as the table name with a suffix of "\_Axx" where xx is the path number (01 to 18). The parentheses contain the columns (maximum of 8) defining the segments of the key.

Though UNIQUE is optional in ANSI SQL, KDB requires all indices to be unique so thsi keyword must be used.

The ASC and DESC modifiers are optional and if not present ASC is assumed. However DESC, for descending order, is not supported in KCML5.

Examples

CREATE UNIQUE INDEX SL00trans_A1 on SL00trans (fname, sname)

See also:

[DROP INDEX](DROP_INDEX.htm), [CREATE TABLE](CREATE_TABLE.htm)
