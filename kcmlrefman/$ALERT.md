\$ALERT

------------------------------------------------------------------------

General Form:

\$ALERT partition_number

Where:

partition_number = a numeric expression yielding a valid partition number.

------------------------------------------------------------------------

The \$ALERT statement is used to generate a signal to the specified partition. It is implemented differently on Windows compared to Unix systems and both implementations are more restrictive than the original 2200 one as they require the target process to be blocked waiting on an event.

\$ALERT will interrupt a blocked process provided a [SELECT ON ALERT](SELECT_ON_ALERT.htm) handler is present in the current program and that it has not been disabled with [SELECT OFF ALERT](SELECT_ON_ALERT.htm). It will be ignored by a running process that is not waitiong on a external event. A process may block while accessing the keyboard, waiting on an event from a form, reading or writing a socket, pipe or TC device, delaying on a \$BREAK or \$IF or waiting for a \$OPEN or @LOCK to complete. It will not block accessing a file.

If a [KEYIN](KEYIN.htm) or a [\$BREAK](BREAK.htm)! are interrupted by \$ALERT then program flow will continue at the next statement. With the [KEYIN](KEYIN.htm) statement the variable is left unchanged allowing the \$ALERT handler to be called. If a [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), [LINPUT +](LINPUTplus.htm) or [LINPUT LIST](LINPUT_LIST.htm) is interrupted it will drop through to the next statement as if the RETURN key had been pressed. [\$OPEN]($OPEN.htm) is not affected. If an ALERT handler has not been defined or is temporarily disabled then input statements will ignore the \$ALERT.

Unix

\$ALERT should be used with caution as some versions of Unix do not resume system calls interrupted by a signal such as an ALERT. The system calls likely to be a problem are those that write to tty devices such as printers or TC lines which may lose some characters if interrupted in the middle of a large write. Disk devices will not be effected as they write to a cache. To avoid these problems programs receiving \$ALERT should be altered to do the work in a child process if possible.

The effective user id (UID) of both foreground and global processes must be the same. This may cause problems on versions of Unix that prevent users from having the same effective UID number, i.e. SCO Unix and Unix 5.4 machines such as the IBM RS6000 and the ICL DRS6000. This can be done by setting the SUID bit on the KCML file, usually with something like

chmod u+s /usr/lib/kcml/kcml

Refer to your Unix documentation for more information about effective user ids.

Windows

Prior to KCML 6.0 the target process must be blocked waiting in a \$BREAK! otherwise an X77 error will occur. In KCML 6.0 and later the Windows implementation is the same as the Unix implementation and any blocked I/O statment can be interrupted.

Syntax examples:

\$ALERT 254\
\$ALERT partition

See also:

[]($ALERT_SCREEN.htm)\
[SELECT ON ALERT](SELECT_ON_ALERT.htm) [\$DISCONNECT]($DISCONNECT.htm),\
