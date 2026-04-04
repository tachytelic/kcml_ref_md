KCMLReadClipboard(buffer\$, len)

This function will read a string of text from the clipboard into the *buffer\$* parameter. The maximum length of the data to receive is passed in the *bufsize* parameter. It expects the clipboard to contain text in CF_TEXT clipboard format.

Syntax

\$DECLARE 'KCMLReadClipboard(RETURN STR(), INT())

Returns

This function returns the number of characters transferred to buffer\$ or -1 if it failed. An empty clipboard will return 0.

Example

The following program will obtain the length of the data in the clipboard using the [KCMLGetClipboardLength](KCMLGetClipboardLength.htm) function, and then read it into a buffer using this function. \$DECLARE 'KCMLReadClipboard(RETURN STR(),INT()) \$DECLARE 'KCMLGetClipboardLength DIM a\$0 clipsize = 'KCMLGetClipboardLength() MAT REDIM a\$clipsize + 1 'KCMLReadClipboard(a\$, clipsize)
