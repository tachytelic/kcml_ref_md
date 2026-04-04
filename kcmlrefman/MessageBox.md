\$DECLARE 'MessageBox

------------------------------------------------------------------------

One of the most common \$DECLARE functions is 'MessageBox() which pops up a window with a message and a number of buttons (usually "OK" or "OK" and "Cancel" or "Yes" and "No"). This is a very easy to use function except for the first parameter which specifies a parent window. It is possible using other \$DECLARE calls to obtain a suitable window handle but this can be tricky in a forms based application. There is a risk that the message box appears behind other windows where it may not be noticed by a user.

In 6.0 KClient, the 'MessageBox call is intercepted by the client, and the given parent window is always replaced by the top most form of the application. This ensures there will be no problem with ownership, and it means that an application may simply pass 0 for this first parameter.

A second advantage of KClient intercepting the 'MessageBox call, is that the CTRL-BREAK sequence is recognised, allowing a user to break into the code (if enabled). Note that the workbench will not appear until the message box is dismissed and the result returned to KCML.

\$DECLARE 'MessageBox(INT(), STR(), STR(), INT()) DIM \_MB_OK = 16 'MessageBox(0, "This message box appears properly", "Application", \_MB_OK)
