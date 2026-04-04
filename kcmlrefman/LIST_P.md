LIST P

------------------------------------------------------------------------

General Form:\
\
<img src="bitmaps/listp.gif" data-align="BOTTOM" data-border="0" alt="listp.gif" />\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST P statement searches for instances of text in the program corresponding to the regular expression specified in the string. It is case sensitive and spaces are significant. If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

Text search operations can also be performed from the search dialog box within the KCML Workbench.

If an asterisk immediately follows the P then all statements containing the search text will be LISTed in full. Leading colons (:) are inserted to show the exact position of the statement containing the text within the line, for example:

LIST P\* "F\*R"\
00010 FOR count=1 TO length\
09000 :::FOR z=1 TO 50\
09000 ::::FOR y=2 TO 20 STEP 2

without the asterisk the output would be as follows:

LIST P "F\*R"\
00010 09000

LIST P uses the same pattern matching routine as is used by many Unix commands, for example ed, sed, vi etc. Therefore this statement is not supported on the DOS version. Characters such as \`.' and \`\$' may be escaped with a backslash.

Syntax examples:

LIST P "Fred?"\
LIST P\* AARDVARK\$(1)\
@LIST P "NAME\[23\]"

 
