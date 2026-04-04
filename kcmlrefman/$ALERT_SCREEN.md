\$ALERT SCREEN

------------------------------------------------------------------------

General Form:

\$ALERT SCREEN partition_number

Where:

partition_number = a numeric expression yielding a valid partition number.

------------------------------------------------------------------------

\$ALERT SCREEN generates a signal which causes the target process to generate a screen dump file in the current directory. It is ignored by processes that have no screen and have a \#TERM of zero. As with [\$ALERT]($ALERT.htm) the target process must be blocked waiting for an external event.

The file will be generated in a directory specified by the [SCREENDIR](EnvVars.htm#SCREENDIR) environment variable, if it exists, otherwise they will be created in the current directory. Text mode clients will generate a file with the name 'scrnd' followed by the target partition number. Forms client use the 'form' prefix.

A text mode screen file is in the format of a [INPUT SCREEN](INPUT_SCREEN.htm) buffer. An application that wishes to decode the screen can read the first 80 bytes to get the header and extract the number of sections and number of rows and columns in each section. Alternatively it can just read the while file into a buffer to use in a [PRINT SCREEN](PRINT_SCREEN.htm) statement redispling the captured screen.

A forms screen file is in format that can be understood and displayed by the [DisplayScreen()](mk:@MSITStore:kcmlforms.chm::/tmp/KClient_DisplayScreen.htm) client COM method. The file should be read into a buffer and passed to the method as the argument.

Unix implementation

The effective user id (UID) of both foreground and global processes must be the same. This may cause problems on versions of Unix that prevent users from having the same effective UID number, i.e. SCO Unix and Unix 5.4 machines such as the IBM RS6000 and the ICL DRS6000. This can be done by setting the SUID bit on the KCML file, usually with something like

chmod u+s /usr/lib/kcml/kcml

Refer to your Unix documentation for more information about effective user ids.

Syntax examples:

\$ALERT SCREEN 254\
\$ALERT SCREEN partition

See also:

[\$ALERT]($ALERT.htm)\
[Bkstat utility](bkstat.htm)\
[WebServer](mk:@MSITStore:kwebserv.chm::/adminfns.htm). [DisplayScreen()](mk:@MSITStore:kcmlforms.chm::/tmp/KClient_DisplayScreen.htm)
