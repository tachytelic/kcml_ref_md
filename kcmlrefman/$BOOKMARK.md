\$BOOKMARK

------------------------------------------------------------------------

General Forms:\
\
1.      \$BOOKMARK=alpha_expression\
\
2.      receiver_variable = \$BOOKMARK\
\

------------------------------------------------------------------------

Bookmarking exploits the ability in a KClient connection icon (.kcc file) to specify command-line options for the application. They will typically be used to jump to a certain part of the system, such as particular menu option or by selecting a nominated account. Bookmarking extends these facilities by allowing the application to record its current state, allowing the user to easily create new icons to start the application again at this point.

The user creates a bookmark icon by choosing the bookmark option from the system menu on the current form. This brings up a dialog box with a suggested name for the new connection and an icon which can be dragged with the mouse and dropped onto the desktop.

There are two components to bookmarking for the programmer. One is the setting of the current bookmark, done at strategic points in an application such as menus. This is done so that the client is always aware of the application in use. The second is to retrieve any bookmark associated with the icon from the client during application initialisation. This string can then be used to return the application to the position of the bookmark. The value of bookmarks and how they are used to navigate within the application is left entirely to the application programmer.

The \$BOOKMARK statement allows the setting of the bookmark at any time.

\$BOOKMARK="DisplayAccount012345"

Any string expression may be specified as the value. It can also be used as a function to inspect its current value.

PRINT \$BOOKMARK

Retrieving the bookmark from the client during startup is harder as it involves \$DECLARE, but will probably only ever be done once in an application.


    $DECLARE 'KCMLCommandLine(RETURN STR())
    DIM a$0
    DIM len
    REM By passing 0 for the string, we just get its length
    len = 'KCMLCommandLine(0)
    IF (len > 0)
        REM Knowing the length we can MAT REDIM to exactly the size we need
        MAT REDIM a$len
        REM This time fetch the string into a$
        'KCMLCommandLine(STR(a$))
        PRINT "Command line is ",a$
    END IF
