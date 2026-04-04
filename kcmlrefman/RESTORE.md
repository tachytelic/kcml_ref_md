RESTORE

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/restore.gif" data-align="BOTTOM" data-border="0" alt="restore.gif" />\
\
Where:\
\
     numeric_expression      = numeric expression \>=0 and \<=65535\
\

------------------------------------------------------------------------

The RESTORE statement is used to reset the pointer for [READ](READ.htm) and [DATA](DATA.htm) statements to allow the repetitive use of the data contained in [DATA](DATA.htm) statements. When a RESTORE statement is executed, the system resets the data pointer to the specified [DATA](DATA.htm) value, causing the next [READ](READ.htm) statement to read from the specified value.

If RESTORE is used without any parameters, it resets the data pointer to the first value on the first [DATA](DATA.htm) statement appearing in the program.

When the optional LINE clause is used, the data pointer is set to the first value of the specified line number. If a numeric expression follows the line number, the pointer is moved to the specified value on the line starting from one.

If the numeric expression is specified without a line number, the data pointer is set to the N'th data value in the program starting from one.

The data pointer is set to the first [DATA](DATA.htm) value in the program upon execution of a [RUN](RUN.htm), or [LOAD](LOAD.htm) statement.

Syntax examples:

RESTORE\
RESTORE 135\
RESTORE LINE 4000\
RESTORE LINE 5000, data_count

See also:

[DATA](DATA.htm), [READ](READ.htm)
