LIST T

------------------------------------------------------------------------

General Form:\
\
     \[@\]LIST \[title\] T\[\*\] strexpr\
\
Where:\
\
          title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST T statement searches for instances of text in the program. Embedded spaces are ignored in the text, but the match is not case sensitive. Only one text string is allowed per search. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

Text search operations are best performed from the search dialog box within the KCML Workbench.

If an asterisk immediately follows the T then all statements containing the search text will be LISTed in full. Leading colons (:) are inserted to show the exact position of the statement containing the text within the line, for example:

LIST T\* "FOR"\
00010 FOR count=1 TO length\
09000 :::FOR z=1 TO 50\
09000 ::::FOR y=2 TO 20 STEP 2

without the asterisk the output would be as follows:

LIST T "FOR"\
00010 09000 09000

Syntax examples:

LIST T "Fred"\
LIST T AARDVARK\$(1)\
@LIST T\*"Returning"

 
