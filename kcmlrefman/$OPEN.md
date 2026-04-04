\$OPEN

------------------------------------------------------------------------

<div class="Generalform">

General Forms:

1.  \$OPEN \[line_number\] *devspec* \[, *devspec*\] ...
2.  status = \$OPEN *devspec* \[, *devspec*\] ... \[, timeout\]

where:\
\

<div class="indent">

*devspec* is \#*stream* or /*devaddr* or \<*strexpr*\>

</div>

</div>

------------------------------------------------------------------------

The \$OPEN statement provides advisory locking of a native file or device. Advisory locking means that other KCML processes can read or write the \$OPENed file or device but they cannot \$OPEN it themselves. Once a device has been \$OPENed the device remains locked until either a [\$CLOSE,]($CLOSE.htm) [CLEAR,](CLEAR.htm) [\$END]($END.htm) or [\$REWIND]($REWIND.htm) statement is executed. If a \$OPEN is executed for a device \$OPENED elsewhere then what happens depends on the form of the statement.

the \$OPEN statement will hang until the device is freed, unless an optional line number is specified in which case the program will branch immediately to the specified line.

\$OPEN can be used either as a statement with an optional label or as a function returning a value. The first form is supported only for backward compatibility. In this form if no line number of label is supplied the statement will block until the lock can be achieved. When the label is supplied then the statement will lock the device if not already locked elsewhere but if it can't get the lock then it will jump to the label.

The second form where \$OPEN is a function returning a status is the preferred form. There is an optional timeout value, expressed in milliseconds, which determines what happens if a lock is unavailable. If no timeout value has been supplied or if the value is a positive number then the statement will block until the lock can be obtained. The actual value of the positive timeout is immaterial in KCML 6.2. However a zero timeout value will cause the function to return immediately if a lock would block and the status value returned will be the ordinal of the problem device in the device list so in the following statement:

s = \$OPEN \#1,#9,0

the returned value will be 2 if the file open on \#9 was locked by another process. If all the devices can be locked then the status returned will be zero but if there is an operating system error then the returned value will be a negative number and [\$OSERR]($OSERR.htm) should be inspected to see the reason given by the operating system for refusing the lock.

More than one file or device can be specified in the list and \$OPEN will attempt to lock them in order. It will hang on the first one found to be already locked elsewhere. For a non blocking call with either a zero timeout or a label supplied, it will first unlock previously locked devices from the list before returning.

The operating system will generally detect a deadly embrace when files are being locked and will fail the statement with an I92 error so it may be prudent to add an [ERROR](ERROR.htm) clause.

KCML will ignore an attempt to lock a device already locked by the process on the same device address. On Unix systems it is possible to lock a file you already have locked yourself under a different device address as Unix will spot the duplication and ignore the request. On Windows NT you will block on a second attempt to lock the file just as if it were locked by another process.

Files, whether native file or file on a platter, are always locked using the operating systems file locking functions. A \$OPEN on a local printer, a pipe or LPD device (see [\$DEVICE]($DEVICE.htm)) will not block. The \$OPEN is still recommended for these devices because \$CLOSE has no effect unless the device was previously \$OPENed and \$CLOSE is used to close the pipe or network connection in order to allow spooling to take place. On Unix only, advisory locking is implemented for printers by creating a lock file in the /tmp temporary directory. The lock file name will be constructed from the major and minor device numbers of the tty device (e.g. /tmp/lck0A1F) and so will be unique to that printer irrespective of the KCML device name used in \$DEVICE. However if Unix does not supply a unique name then KCML will use the device address in the name (e.g. /tmp/lck_215) and it may be ambiguous with another On NT it is assumed that all printing is done though spooling and so \$OPEN does not block for character devices.

TC and GPD devices are initialized using the initialization string specified in the \$DEVICE when a \$OPEN is executed. On Unix such devices are advisory locked using lock files just like printers. On NT no locking is performed.

Mandatory locking

Advisory locking is the default for most implementations of KCML, however mandatory locking is optional with many implementations of UNIX based on System 5.4. A mandatory lock will not only block another \$OPEN but will also block any attempt to read or write from the file. Unix allows files to be marked by the chmod +l (l for lock) command as requiring a mandatory lock e.g. in the shell

chmod +l filename

To remove this mark use:

chmod -l filename

Advisory locks do not require lock checks on every file access thus using less system resources and so are to be preferred over mandatory locks if possible.

Syntax examples:

IF (\$OPEN 9000, \#3,0 \<\> 0) THEN 'locked()\
a=\$OPEN \#3\
\$OPEN 9000, /215, /01C, /211\

Compatibility notes:

Printer locking is always advisory except on certain systems such as AIX on the IBM RS6000 where the parallel printer device driver maintains its own mandatory lock when opened. Other users then cannot access this device in any way without a P48 error until the original owner frees the device with a [\$REWIND]($REWIND.htm) of that device. \$CLOSE can be made to perform a \$REWIND by setting a bit in byte 51 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE51). This is the default.

AIX on RS6000s does not support the chmod +l command to mark a file as requiring mandatory locks.

The functional form of \$OPEN was introduced for KCML 6.20. Non-zero timeouts are not fully implemented in 6.20.

See also:

[\$CLOSE]($CLOSE.htm), [LIST DT](LIST_DT.htm), [\$REWIND]($REWIND.htm)
