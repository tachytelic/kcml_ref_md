DATA

------------------------------------------------------------------------

General Form:\
\
     DATA data-element \[, data-element\]...\
\
Where:\
<img src="bitmaps/data.gif" data-align="BOTTOM" data-border="0" alt="data.gif" />\
\

------------------------------------------------------------------------

The DATA statement is used to supply alpha or numeric values that can be read into variables with the [READ](READ.htm) or [MAT READ](MAT_READ.htm) statements.

When a [READ](READ.htm) statement is executed from within a program, the next sequential item held in the DATA statements will be assigned to the variable(s) in the [READ](READ.htm) statement, the DATA pointer is then moved to the next item in the DATA statements. Initially the data pointer is pointing at the first data statement in the program. The [RESTORE](RESTORE.htm) command can be used to reset the data pointer back to the beginning of a specific DATA statement. If there is insufficient data for the [READ](READ.htm) statement then an error will occur.

The [DATA](DATA.htm) statement can also be used to define fields for use with the [FLD(](FLD(.htm) function. A field definition consists of a pair of start and length expressions enclosed in parentheses. The first expression defining the start may be left blank and the [READ](READ.htm) statement will calculate the start from the length of the previous field.

The parser does not remove redundant spaces in DATA statements, this allows several data statements to line up correctly. E.g.

DATA 9876.89, 67281.7, 1324.8\
DATA 48.02, 8971.2, 1.9

Syntax examples:

DATA 3.141\
DATA HEX(020402), HEX(020400)\
DATA 2, 4, 6, HEX(7C), "Red", 3E05\
DATA 0x0123, 0x9078, 0x1452

See also:

[MAT READ](MAT_READ.htm), [READ](READ.htm), [RESTORE](RESTORE.htm)

 
