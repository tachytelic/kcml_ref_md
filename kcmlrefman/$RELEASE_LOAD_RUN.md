\$RELEASE LOAD RUN

------------------------------------------------------------------------

General Form:\
\
     \$RELEASE LOAD RUN \[#stream,\] \[prog_name\]\
\
Where:\
\
     prog_name           = a string expression\
\

------------------------------------------------------------------------

The \$RELEASE LOAD RUN statement starts an additional partition belonging to the calling terminal but running in background. The new child partition is created as a copy of the foreground partition and then the specified program is loaded into memory and executed. The parent foreground process continues with the next statement so both partitions are running together. The copying ensures that the background partition inherits any [\$DEVICEs]($DEVICE.htm), [\$SELECTs]($SELECT.htm), [\$RELEASE KEYs]($RELEASE_KEY.htm) etc. from the parent partition. The terminal however is detached from the background process and if the keyboard is read or a write is done to the screen then the partition will be suspended until the terminal is attached with a [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm). The partition number of the new partition is returned if \$RELEASE LOAD RUN is used as part of an expression. This statement is only available on Unix versions, under DOS an "A08 Statement not legal here" error will result if executed.

Executing a [\$END]($END.htm) in a child process when it is in the foreground will do an automatic [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm) but executing [\$END]($END.htm) in the parent process if it is in the foreground will log the user off leaving the background child process detached. When the same user logs on later on the same terminal a [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm) or a hot key (see [\$RELEASE KEY]($RELEASE_KEY.htm)) can be used to recover these partitions.

If no program name is specified, a default program name of START is used. The environment variable START may be set to change the default program name used by \$RELEASE LOAD RUN.

Syntax examples:

\$RELEASE LOAD RUN "BGJOB"\
new_part = \$RELEASE LOAD RUN

Compatibility notes:

This statement is only available on Unix versions.

See also:

[\$RELEASE KEY]($RELEASE_KEY.htm), [\$RELEASE]($RELEASE.htm), [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm)

 
