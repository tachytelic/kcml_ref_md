LIST !

------------------------------------------------------------------------

General Form:\
\
     LIST \[title\] ! \[\*\]\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST ! statement will list the line numbers of lines containing syntax errors, if any. Programs can be saved even if they contain syntax errors but in the resolve phase prior to execution, any errors will stop execution. The line can be edited and the program resaved or just executed. When a program is LISTed any lines in error will not be structured and will have a \`!' before the line number.

If an asterisk is immediately follows the (!) then the erroneous line will be listed in full, for example:

LIST !\*\
00010 PRINT"TESTING

without the asterisk the output would be as follows:

LIST !\
00010

 
