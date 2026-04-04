LIST R

------------------------------------------------------------------------

General Form:

LIST \[title\] R \[variable\]

Where:

title = alpha_variable or a literal string\
variable = record or field name

------------------------------------------------------------------------

The LIST R statement lists details of the DEFRECORDs in a program. If no variable is specified then it produces just a list of the records in the executing program together with the record size e.g.

: LIST R pstat_record 48 TestRec 409 :

Note that the program must be resolved before this statment will execute. If name of a particular record is specified then it will produce a list of the fields in the record. E.g.

: LIST R TestRec TestRec 409 a (1, "SY8") b\$24 (9, "CHAR(24") c\$\<\<9\>\>10 (33, "CHAR(10") d(2) (123,"UINT(3)")

The same detailed list is available if one of the field names in a record is specified (with the leading dot).

See also:

[DEFRECORD](DEFRECORD.htm)
