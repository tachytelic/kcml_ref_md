\$TRAN device translation

------------------------------------------------------------------------

General Form:\

\$TRAN /devaddr

------------------------------------------------------------------------

This form of the \$TRAN statement is used to retrieve and modify the translation table associated with a specific device. The table consists of 256 elements. Each element is mapped by using its ASCII value as an offset into the table to get the replacement character. This form of \$TRAN is valid wherever an alpha variable is valid.

To retrieve the translation table for the device /215 the following command would be entered:

table215\$ = \$TRAN /215

After the table has been changed is can be saved back with the following command:

\$TRAN /215 = table215\$

For example, to change the printing of a hash \`#' to a pound sign on the terminal, the following program would be executed.

DIM screen_table\$256\
screen_table\$ = \$TRAN /005\
STR(screen_table\$,VAL("#")+1,1) = HEX(7C)\
\$TRAN /005 = screen_table\$

Syntax examples:

table\$(2) = \$TRAN /217\
FLD(table\$.main_printer\$) = \$TRAN /215\
\$TRAN /214 = printer\$\
STR(\$TRAN /005,49,1) = HEX(2A)
