# <span id="whatisabookmark."></span> What is a bookmark?

Bookmarking allows users to snapshot where they are in a program and have it saved to an icon file on their desktop. Later they can click on that icon and get reconnected back onto the same server at the same place. It exploits the ability in a kclient connection icon (.kcc file) to specify [command-line options](commandlineswitches.htm) for the application. They will typically be used to jump to a certain part of the system, such as particular menu option or by selecting a nominated account. How effective this is depends on the amount of support for the bookmarking concept that has been programmed into the application using [\$BOOKMARK](mk:@MSITStore:kcmlrefman.chm::/$BOOKMARK.htm). At worst, if the application has not been modified to support bookmarking at all, then all that can be recorded is the connection details and the program will always restart at the beginning.

See also:

[Saving bookmarks](savingabookmark.htm)\
[Support for bookmarking in applications](implbmarks.htm)
