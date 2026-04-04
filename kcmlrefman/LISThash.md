LIST \#

------------------------------------------------------------------------

General Form:\
\
     \[@\]LIST \[title\] \# \[\*\]\[ \[start_line\] \[, end_line\] \]\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST \# statement, lists all references to all line numbers or a specific line number. The output first displays the line referenced followed by a list of lines that reference it. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any. If a line does not exist, then it is enclosed in parentheses. For example:

 LIST \#\
 2020 - 04000 05000 07000 09020\
 5000 - 00010 00050\
(6000)- 00090 00010 00050

Line number search operations are best performed from the search dialog box in the KCML Workbench.

If an asterisk follows the \# then the line referenced followed by a list of the statements that reference it are listed in full. Leading colons (:) are inserted before each statement show the exact position within the line, for example:

LIST \# \* 1000\
01000 REM Main routine\
        - 00040 IF count==new_count THEN GOSUB 1000\
        - 00100 ON test GOSUB 1000,2000,3000

without the asterisk the output would be as follows:

LIST \# 1000\
01000 - 00040 00100

The optional line numbers perform the following:

- If only one line number is specified then all lines that reference that line number will be listed.
- If the start line is followed by a comma, then all lines after the start line will be cross referenced.
- If only one line number is entered and it is preceded with a comma then all lines up to and including that line will be cross referenced.
- If two line numbers are used separated by a comma, then all lines between and including the two lines will be cross referenced.
- If no line numbers are used then all lines in the program will be cross referenced.

Syntax examples:

LIST \#\
LIST \# 310\
@LIST \# ,200\
@LIST \# 300,400
