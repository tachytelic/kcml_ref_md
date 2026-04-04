PANIC

------------------------------------------------------------------------

General Form:\

1.  PANIC
2.  PANIC CONTINUE

------------------------------------------------------------------------

The first form of the **PANIC** statement takes a snapshot of the current program state into a file. If programming is enabled then the KCML editor is displayed, otherwise, if programming is disabled, a message is displayed and the KCML session is terminated. Note that programming is disabled by setting byte 36 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE36). An immediate mode PANIC prints the message specifying the filename used but does not terminate.

In the second form, **PANIC CONTINUE**, the program continues executing and does not terminate. It does not print a message to the CO device. This allows a program which has detected an error condition to dump ist state and recover. Note that the LIST device is used and will be reset to /005 by this statement.

The [bkstat](bkstat.htm) utility under Unix, kservadm on Windows or the [Web Administration Tool](mk:@MSITStore:kwebserv.chm::/kcmlproc.htm) can be used to force a KCML process to generate a dump. There are two options on the signal menu: the **Panic+** option generates the dump and terminates the process whereas the **Panic** option only generates the dump and it allows the process to continue to run.

PANIC should be used in place of [STOP](STOP.htm) statements in parts of programs that can only be executed as a result of a program bug or data corruption. It will terminate the session but give a postmortem dump of the program state allowing support personel to analyse the cause of the bug. The [STOP PANIC](STOP_PANIC.htm) statement can be used to force all STOP statements to act like PANIC.

The dump is placed in a native file whose name starts with the word 'panic' ('pan' on Windows versions) followed by a unique number corresponding to the process id of the KCML task. The panic event, together with the file name used, is logged in the operating system event log. The file contains the following information:

- The date and time.
- Contents of the text output screen (if any)
- UNIX login name
- UNIX terminal number
- The KCML version number.
- The KCML software license number.
- The contents of the [\$MACHINE]($MACHINE.htm), [\$OPTIONS]($OPTIONS.htm), [\$OPTIONS RUN]($OPTIONS_RUN.htm), [\$OPTIONS LIST]($OPTIONS_LIST.htm) and [\$PSTAT]($PSTAT.htm) system variables.
- The operating system type and version number (if available.)
- A list of operating system environment variables.
- The value of the [\#TERM](_TERM.htm) and [\#PART](_PART.htm) functions.
- The value of the [ERR](ERR.htm) function.
- The value of the [\#LINE](_LINE.htm) and [\#STAT](_STAT.htm) functions.
- The output from the [LIST RETURN](LIST_RETURN.htm), [LIST DT](LIST_DT.htm) and [LIST DIM](LIST_DIM.htm) commands.

In versions of KCML prior to 6.0 the format of the dump was unstructured ascii text with LIST DIM and LIST RETURN in exactly the same format as their console mode equivalents. If KCML 6.0+ the format is XML and there is a .xml extension to the filename. This can be viewed as a structured tree in an XML aware browser like IE5 or Netscape 6. To format the file a XSLT stylesheet pan.xsl is installed in the kcml directory and copied to the panic directory with the first panic.

The PANIC file is created by default in the current working durectory. On Windows 9x and Windows NT, if the the registry key HKEY_LOCAL_MACHINE/SOFTWARE/Kerridge/PanicDir exists then it can provide the default directory. This key can be set using the *kservadm* utility which also has a facility to browse the panic directory and display any panics. Setting the environment variable [PANICDIR](EnvVars.htm#PANICDIR) to a native directory name using the [ENV()](ENV(.htm) function will cause all future PANIC files to be created in the specified directory. This takes priority over the registry setting.

If KCML detects an unrecoverable internal fault, a PANIC file is automatically created along with a core file if the [DUMP](EnvVars.htm#DUMP) environment variable is set.

If the HEX(02) bit of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE53) byte 53 is set, programming is enabled, HALT is enabled and the user has previously interrupted the program displaying the debugger, then a PANIC executed within the program will not not produce a panic file and terminate the session but will drop back into the editor with an error A00.28. The behaviour of PANIC in immediate mode is not affected so you can then manually force one if you need it. This bit in \$OPTIONS is set by default so to revert to the behaviour prior to KCML 5.0 unset this bit in your program.

See also:

[STOP PANIC](STOP_PANIC.htm) [Web Administration Tool](mk:@MSITStore:kwebserv.chm::/adminfns.htm) [bkstat](bkstat.htm)
