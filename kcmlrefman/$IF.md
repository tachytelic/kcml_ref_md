\$IF

------------------------------------------------------------------------

General Form:

<img src="bitmaps/ifd.gif" data-align="BOTTOM" data-border="0" alt="ifd.gif" />

------------------------------------------------------------------------

The \$IF function allows a program to wait on input from multiple devices. \$IF does not actually read from the device(s) but returns with an index which indicates that data is available to be read. An optional timeout with millisecond granularity is also available. If no timeout is specified then \$IF will wait until there is information available to read from any of the devices in the list. \$IF is a function and is valid wherever a numeric function is legal.

There can be up to 32 devices tested by the function and they should be in a list separated by commas. Alternatively a single numeric array of streams can be used. The first zero or negative element in the array marks the end of the list. If no streams are specified then \$IF can be used as a simple break statement, delaying for the specified number of milliseconds, for example:

dummy = \$IF ,50

which would delay for five hundredths of a second.

If \$IF with the optional timeout is to be used within a numeric expression then it should be enclosed within parentheses to prevent parts of the numeric expression being used as the timeout.

\$IF returns the index, counted from one, of the first stream which has data available to be read but it will return zero if the timeout expires first. It can return -1 if an error occurs.

\$IF can also be used in a server to test for an incoming connection on a [listening socket](sockets.htm). This works for all Unix systems but is only supported for Windows with KCML 6.0 or later and only then on systems which support Winsock 2.

While \$IF is waiting, KCML will set byte 29 of [\$PSTAT]($PSTAT.htm) to HEX(FD).

Syntax examples:

Result = \$IF \#5, \#240, \#47, timeout\
IF (\$IF \#5, \#120, \#30 == 3)\
Ret = \$IF Streams(), 100\
testing = (\$IF \#1, \#2, \#3, 1000) + 1000\
process = \$IF, timeout
