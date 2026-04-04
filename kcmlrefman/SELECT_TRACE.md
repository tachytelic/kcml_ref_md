SELECT TRACE

------------------------------------------------------------------------

General Forms:\
\
1.\
<img src="bitmaps/selecttrace.gif" data-align="BOTTOM" data-border="0" alt="SELECT TRACE" />\
\
2.      SELECT TRACE\
\
\

------------------------------------------------------------------------

The TRACE select parameter allows the output from the [TRACE](TRACE.htm) command and the [\$COMPILE]($COMPILE.htm) statement to be written to a server file or device. By default in the workbench debugger this output would go to the [trace window](mk:@MSITStore:workbench.chm::/WinTrace.htm). If the terminal does not support the Workbench then output would be directed to the /005 device by default. This can be very confusing so redirection with SELECT TRACE is very helpful on such terminals. If SELECT TRACE is specified on its own then the output is device is reset to the default.

Example:

TRACE 1000,5000\
SELECT TRACE "/tmp/TRACEfile"

This would copy the output from the [TRACE](TRACE.htm) command into the file \`/tmp/tracefile', allowing the program to run without interfering with the screen display.

Syntax examples:

SELECT TRACE /204\
SELECT TRACE \<tracefile\$\>\
SELECT TRACE "/user1/tracefile"\
SELECT TRACE /204, PRINT /005

See also:

[TRACE](TRACE.htm), [\$COMPILE]($COMPILE.htm), [ON ... SELECT](ONSELECT.htm)
