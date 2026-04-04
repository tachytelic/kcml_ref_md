Replacing text within an RTF control

------------------------------------------------------------------------

A special feature of the RTF control is the ability for the program to search and replace text within the control. This feature is specifically designed for operations such as a mail merge where names and addresses are read in from a database, merged in with a default document which is then printed.

The [*Replace()* method is used to perform the search and replace operation. Replaceable text in the body of the document must be surrounded with two pairs of braces, i.e. "{{FIRSTNAME}}". The](tmp/PROP_RICHEDIT_REPLACE.htm)

*Replace()* method could then be called as follows:

.rtfControl1.Replace("FIRSTNAME", dbFirstName\$)

This would replace all occurances of "{{FIRSTNAME}}" with the contents of *dbDirstName\$*.

To actually perform a mail merge operation you would need to perform the replace operation for each required record print the document and then reload the original template before perfoming another replacement. Note that after each document is printer with the [*Print()* method all documents are not actually sent to the printer until a call](tmp/PROP_RICHEDIT_PRINT.htm)

*PrintClose()* is made.

 
