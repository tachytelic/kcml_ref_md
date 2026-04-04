LIST \<\<

------------------------------------------------------------------------

General Form:\
\
     \[@\]LIST \[title\] \<\< \[\*\]\
\
Where:\
\
     title           = alpha_variable or a literal string\
\

------------------------------------------------------------------------

The LIST \<\< statement will list multi-language string definitions. Multi-language strings are always enclosed within chevrons, "\<\<" and "\>\>".

If the optional @ sign precedes the reserved word LIST, then the listing will be taken from the currently selected global partition, if any.

If an asterisk immediately follows the (\<\<) then all references to the strings will be LISTed in full. Leading colons (:) are inserted before each statement to show the exact position within the line, for example:

LIST \<\<\*\
01010 :: lang\$ = \<\<"Total"\>\>\
09000 :: \$IMAGE = \<\<"\$######.##"\>\>

Without the asterisk the output would be as follows:

LIST \<\<\
01010 09000
