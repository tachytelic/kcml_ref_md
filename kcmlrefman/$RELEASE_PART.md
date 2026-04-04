\$RELEASE PART

------------------------------------------------------------------------

General Form:\
\
     \$RELEASE PART\
\

------------------------------------------------------------------------

The \$RELEASE PART statement is used to create background daemon processes. It is available only in partitions created with the [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm) statement which are at status 'D' at the time of execution (See [\$PSTAT]($PSTAT.htm)), otherwise this statement is ignored. This statement is only available in Unix versions of KCML.

Once executed the [\#TERM](_TERM.htm) value is set to zero and screen output is redirected to the device /dev/null. It is not possible to reconnect to such a partition at a later stage. Errors or any attempts to read from the keyboard will force the partition to [PANIC](PANIC.htm) and will terminate the process.

Compatibility notes:

This statement is only available on Unix versions.

See also:

[\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm)
