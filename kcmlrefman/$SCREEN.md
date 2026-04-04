\$SCREEN

------------------------------------------------------------------------

General Forms:\
\
1.      \$SCREEN=alpha_expression\
\
2.      receiver_variable = \$SCREEN\
\

------------------------------------------------------------------------

The \$SCREEN statement is used to retrieve and modify the translation table associated with the standard text mode output device (/005). The table consists of 256 elements. Each element is mapped by using its ASCII value as an offset into the table to get the replacement character. The \$SCREEN function is valid wherever an alpha variable is valid. The [\$TRAN]($TRAN.htm) device translation statement supersedes \$SCREEN as it allows the translation table for any device to be modified.

For example, to change the printing of a hash \`#' to a pound sign on the terminal, the following program would be executed.

STR(\$SCREEN,VAL("#")+1,1) = HEX(7C)

Syntax examples:

table\$(2) = \$SCREEN\
FLD(table\$.main_printer\$) = \$SCREEN\
\$SCREEN = screen1\$\
STR(\$SCREEN /005,49,1) = HEX(2A)

See also:

[\$TRAN]($TRAN.htm)
