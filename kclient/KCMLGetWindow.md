'KCMLGetWindow()

This function can be used to get the window handle for the active text window. Window handles can be used with WIN32 API \$DECLARE calls to size, hide or move the text window. They can also be used to chage the text in the title bar as in the example below. This call is backward compatible with WDW. Note that the WIN32 API call GetActiveWindow() may not return the right handle and should not be used.

Syntax

\$DECLARE 'KCMLGetWindow()

Returns

The function returns a window handle for the main WDW or Kclient window.

Example

\$DECLARE 'KCMLGetWindow() \$DECLARE 'SetWindowText(INT(),STR()) PRINT "This window should have a title saying Hello" 'SetWindowText('KCMLGetWindow(), "Hello") INPUT z\$
