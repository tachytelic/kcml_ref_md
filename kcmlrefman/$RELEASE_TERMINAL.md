\$RELEASE TERMINAL

------------------------------------------------------------------------

General Form:\
<img src="bitmaps/releaseterminald.gif" data-align="BOTTOM" data-border="0" alt="releaseterminald.gif" />\
Where:\
\
     numeric expression      =      a valid partition number\
\

------------------------------------------------------------------------

The \$RELEASE TERMINAL is used to swap the current partition into a background partition, the statement will have no effect unless there is a partition in the background belonging to the terminal. Such a partition should have been previously created by a [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm) statement executed on the terminal. If such a partition exists then the current partition is detached from the screen and the background partition will be instructed to attach itself to the terminal instead. If there is more than one background partition then the lowest numbered partition will be selected unless an explicit partition number or name is specified. The partition name is declared with a [DEFFN@PART](DEFFN_@PART.htm) statement within the partition. This statement is only available on Unix versions, under DOS an "A08 Statement not legal here" error will result if executed.

A detached partition has a status of \`D' in its [\$PSTAT]($PSTAT.htm) entry. It continues to execute after the [\$RELEASE]($RELEASE.htm) but it will hang if it attempts to read from the keyboard. While hung the status will be \`W'. When re-attached processing will continue. Local printing can be done from a detached terminal provided that the local printer was locked by the partition executing a [\$OPEN /004]($OPEN.htm) before it was detached.

The optional TO clause will release to the terminal number specified, the number must be a terminal number previously created by the parent with the [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm) statement.

The optional [STOP](STOP.htm) clause makes the newly attached partition stop executing as soon as it gets control of the terminal with the usual colon prompt.

\$RELEASE TERMINAL works by detaching from the terminal and then setting a flag in the [PSTAT]($PSTAT.htm) entry of the terminal it wants to attach.

Syntax examples:

\$RELEASE TERMINAL\
IF test_variable \< 1 THEN \$RELEASE TERMINAL\
\$RELEASE TERMINAL TO back_part

Compatibility notes:

This statement is only available on Unix versions.

See also:

[\$RELEASE]($RELEASE.htm), [\$RELEASE KEY]($RELEASE_KEY.htm), [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm)
