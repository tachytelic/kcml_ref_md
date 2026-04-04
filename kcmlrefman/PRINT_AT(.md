PRINT AT(

------------------------------------------------------------------------

General Form:     \
\
     AT(row, column \[, \[erase_length\] \] )\
\
Where:\
\
     row, column, erase_length           = numeric expressions\
\

------------------------------------------------------------------------

The AT( function is used to position the cursor at a specified row and column on the screen and optionally erase a specified number of characters from that point onwards. This statement is only relevant when developing text based applications. The AT( function can only be used in conjunction with the [PRINT](PRINT.htm) statement. Multiple [PRINT](PRINT.htm) functions (AT(, [BOX(](PRINT_BOX(.htm), [HEXOF(](PRINT_HEXOF(.htm), [TAB(](PRINT_TAB(.htm) ) can be incorporated anywhere in the [PRINT](PRINT.htm) statement, separated with semi-colons or commas.

The location of the cursor after the AT( function defines the position to which subsequent text will be displayed. The new cursor position is specified by giving the row and column number of the required location. The row is numbered from 0 to 23, and columns are numbered from 0 to 79 on standard screens. The Lines and Columns clauses in TERMINFO can override these maxima.

For example, the following line prints the word hello at the top right hand corner of the screen:

PRINT AT(0,74);"hello"

The erase length parameter specifies the number of characters to be erased immediately after the new cursor position. If a comma follows the column parameter and no erase length parameter is specified, then all lines from the current cursor to the bottom of the screen are erased.

Syntax examples:

PRINT AT(0,0);title\$(2)\
PRINT AT(row, col, erase); text\$\
PRINT AT(4 + down, 10,); "Total = "; total; "Grand Total = "; grand_total

See also:

[PRINT](PRINT.htm), [PRINT BOX(](PRINT_BOX(.htm), [PRINT HEXOF(](PRINT_HEXOF(.htm), [PRINT TAB(](PRINT_TAB(.htm)

 
