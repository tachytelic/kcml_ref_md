\$REWIND

------------------------------------------------------------------------

General Form:\
\
     \$REWIND \[#stream\] ...\
\

------------------------------------------------------------------------

The \$REWIND statement is used to force a close of the native file underlying a specified device address. If no explicit devices are specified then \$REWIND closes all the native files and devices in the device table. This should have no effect on most application programs but telecomms lines will drop DTR and pipes will be closed.

Syntax examples:

\$REWIND\
\$REWIND \#46, \#45, \#stream
