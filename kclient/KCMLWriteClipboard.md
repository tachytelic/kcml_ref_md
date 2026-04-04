KCMLWriteClipboard(buffer\$)

This function will write a string of text, passed in the buffer\$ parameter, to the Windows clipboard. It will use the CF_TEXT clipboard format.

Syntax

\$DECLARE 'KCMLWriteClipboard(STR())

Returns

This function returns TRUE on success, or FALSE on failure.

Example

The following KCML program will write a string to the Windows clipboard: \$DECLARE 'KCMLWriteClipboard(STR()) 'KCMLWriteClipboard("This is a test string!")
