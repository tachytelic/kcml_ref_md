\$CLOSE

------------------------------------------------------------------------

General Form:\
\
     \$CLOSE \[*devspec*\] \[, *devspec*\] ...\
\
\
where *devspec* is \#*stream* or /*devaddr* or \<*strexpr*\>\
\

------------------------------------------------------------------------

The \$CLOSE statement releases the specified files or devices which were previously hogged with a [\$OPEN]($OPEN.htm) statement. If no devices or stream numbers are specified, as in \$CLOSE on its own, then \$CLOSE will release all of the devices being hogged by the current partition. Execution of [CLEAR](CLEAR.htm), [\$END]($END.htm), [LOAD RUN](LOAD_RUN.htm), or [\$REWIND]($REWIND.htm) will also release any devices being hogged by the current partition.

Execution of a \$CLOSE by default performs an explicit [\$REWIND]($REWIND.htm), therefore if the device is a pipe or a LPD network spooler then the pipe will be closed. This can be supressed if required using byte 51 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE51). \$CLOSE will also instruct a Kclient local printer to close the Windows print job and thus allow the Windows spooler to start printing.

If the device being closed had not been previously locked by a \$OPEN in this KCML process then it is silently ignored. Thus \$CLOSE will not be able to close a spool file and allow the spooler to print unless the device was \$OPENed first. \$REWIND will always close a pipe or network spooler.

Syntax examples:

\$CLOSE\
\$CLOSE /01D\
\$CLOSE /01A, /015\
\$CLOSE \#3, \#channel_1

See also:

[\$OPEN]($OPEN.htm), [\$REWIND]($REWIND.htm)
