KCMLDdeLoad(module\$, program\$)

This checks to see if the server *module\$* is running, if not it launches the program *program\$*. Unless this call is made to load the appropriate DDE server, then any attempt to open a conversation will fail. If the program is not already loaded, then the function will attempt to find it, searching in the following places (in order):

1.  The current directory
2.  The Windows directory
3.  The Windows SYSTEM directory
4.  The directory containing the executable file for the current task
5.  The directories listed in the PATH environment variable
6.  Any directories mapped in a network

Syntax

\$DECLARE'KCMLDdeLoad(STR(), STR())

Returns

If successful, the function will return 0, else -1 is returned.

Notes

Kclient will attempt to load the program and display it as an icon. If you wish to load the program normally, or maximised (full screen) you can \$DECLARE the WinExec() API call.

Example

The following example will attempt to load Microsoft Excel:

\$DECLARE 'KCMLDdeLoad(STR(),STR()) ret = 'KCMLDdeLoad("excel", "excel.exe") IF ret == 0 THEN PRINT "Loaded OK" : ELSE PRINT "Cannot load"
