Invoking Unix and NT command

Accessing UNIX and NT commands from within KCML

KCML allows access to UNIX or Windows operating system commands and utilities directly from the immediate mode prompt with the ‘!’ command, or under program control with the [SHELL](SHELL.htm) statement.

The ‘!’ command entered in immediate mode on the Workbench console will drop straight into the UNIX shell or Windows command processor, displaying the normal operating system prompt; entering \`exit' at the shell prompt will return back to the **KCML** immediate mode prompt. Alternatively individual operating system commands can be executed from immediate mode by entering the command after the \`!' command, for example:

!ls -l

for UNIX systems or

!DIR

on Windows systems would list the contents of the current working directory. Any UNIX or Windows command available to the user including piping and redirection, can be executed with the ‘!’ command.

On the UNIX version the type of shell used by **KCML** defaults to the Bourne shell, this can be changed by setting the *SHELL* environment variable in the users *.profile*.

The statement is used to execute operating system commands from within **KCML** programs. can be used anywhere a numeric expression is valid as on UNIX versions it returns the error status of the command. For example:

SHELL "ls -l \| pg"\
SHELL "DIR \p"

would list the contents of the current directory in a text window and (on the UNIX version) pipe the results to the \`pg' command. Most UNIX commands will return 0 if they worked correctly and any other number if they fail. On the Windows version the return value is always zero. For example:

IF SHELL"ubackup"==0 THEN PRINT "Backup completed O.K."\
ELSE PRINT "Backup Failed"

would display any output from the UNIX program *ubackup* at the current cursor position on a text window. A message depending on the return status of the program would be displayed upon completion.

On UNIX versions care should be taken when removing, renaming or changing the status of **KCML** files or platter images that any other **KCML** tasks do not have the file or platter open, as the change will not come into effect until the task closes and re-opens the file. Platters and files are only opened when a request is made to read information from the platter or file.

When using the Windows version of **KCML** a Windows DOS box needs to be started up for each execution of a DOS command. This may cause screen flicker and effect performance if DOS commands need to be executed repeatedly. Setting byte 37 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE37) to HEX(01) forces **KCML** to run DOS boxes minimised therefore hiding the output of the command from the user.

Redirecting input and output

KCML allows the Console Input, Standard Input, Console Output, List and Print devices to be redirected to and from UNIX/DOS files with the [CI](SELECT_CI.htm), [INPUT](SELECT_INPUT.htm), [CO](SELECT_CO.htm), [LIST](SELECT_LIST.htm), [LOG](SELECT_LOG.htm), [TRACE](SELECT_TRACE.htm) and [PRINT](SELECT_PRINT.htm) **SELECT** parameters respectively. Instead of specifying a device address a literal string or an alpha variable containing the native filename may be specified, for example:

SELECT LIST "G:\TMP/LISTFILE.TXT"\
LIST\
SELECT LIST /005

would send the output of the [LIST](LIST.htm) statement into the file 'G:\TMP\LISTFILE"'. Another useful example of redirection is the use of the CI select parameter to read in immediate mode commands from an ASCII file. For example, if the file *ren1* contained the following lines:

RENAME a\$ TO junk\$\
RENAME b\$ TO test\$

By selecting the Console input device (CI) to this file, all occurrences of *a\$* would be renamed to *junk\$* for the program currently held in memory. Once finished CI should be re-selected back to the keyboard /001, e.g.

LOAD "OLDPROG"\
SELECT CI "ren"\
SELECT CI /001\
SAVE "NEWPROG"

KCML also provides the ability for applications to open pipes for reading or writing, via the [\$DEVICE]($DEVICE.htm) and [SELECT](SELECT.htm) statements, for example:

\$DEVICE /290="\|lpr"\
SELECT LIST /290\
LIST\
SELECT LIST /005\
\$DEVICE /290=" "

would define the device /290 so that any output to that device would be piped to the UNIX print spooler. The last [\$DEVICE]($DEVICE.htm) statement is used to close the pipe, alternatively [\$REWIND]($REWIND.htm) /290 could be used. The same effect can be obtained by specifying the pipe directly with the [SELECT](SELECT.htm) statement, e.g.

SELECT LIST "\|lpr"\
LIST\
SELECT LIST /005

Under Windows it should be noted that **KCML** emulates the pipe by creating a temporary file in the '\\ directory of the current drive to hold all of the information required before the pipe is read, therefore piping large amounts of data requires corresponding amounts of space on the PC disk.

Information may also be read in via a pipe, either character by character with the KEYIN statement, or groups of characters may be read in with [INPUT](INPUT.htm) or [LINPUT](LINPUT.htm) statements, for example:

DIM abc\$30\
\$DEVICE /01F="date\|"\
SELECT INPUT /01F\
LINPUT abc\$\
SELECT INPUT /001

would read the result of the UNIX *date* command into the variable *abc\$*. Before the information can be re-read from the pipe the device must be closed and re-opened again either by removing and re \$DEVICEing the device or executing the [\$REWIND]($REWIND.htm) statement for the device. If the device is not closed an 'X70 Insufficient data error’ will be generated. The same program could be re-written without the \$DEVICE statements, thus

DIM abc\$\
SELECT INPUT "date\|"\
LINPUT abc\$\
SELECT INPUT /001

Changing the scheduling priority (UNIX only)

The [\$NICE]($NICE(.htm) function allows programs to reduce their scheduling priority by increasing the UNIX nice factor. This is a useful function allowing the programmer to reduce the scheduling priority of users that do not require immediate responses or tasks that are long and mundane and require vast amounts of CPU time.

The \$NICE function can be used anywhere a numeric expression is valid. The specified numeric expression will be added to the current nice factor which is then returned by the function. Specifying a nice factor of zero returns the current nice factor, for example:

PRINT \$NICE(0)\
PRINT \$NICE(5)

would first display the current nice factor followed by the original nice factor + 5.

The normal nice factor is 20 and can be increased to a maximum of 40, corresponding to the lowest priority. Only the super user can decrease the nice factor. If the \$NICE function fails, -1 is returned. Child processes inherit the current nice factor.

The current nice factor for a specified terminal on most UNIX versions can be found with the UNIX ‘ps -lt’ command, under the column headed NI.

Using environment variables

Operating system environment variables may be read into **KCML** or can be set locally with the [ENV(](ENV(.htm) function. All environmental variables that have been set and exported either by the users login script (.profile in the UNIX Bourne shell, or AUTOEXEC.BAT on DOS systems), or automatically by the system can be examined, e.g.

PRINT ENV("TERM")

would return the contents of the *TERM* environment variable. Environment variables can also be set locally with the [ENV(](ENV(.htm) function, e.g.

ENV("TERM") = "vt100"

would change the contents of the *TERM* variable, the new value is included into any new background partitions started for the terminal, any existing background partitions would still have the original value.

The [LIST E](LIST_E.htm) statement can be used to list all locally set environment variables and their contents.

See also:

[ENV(](ENV(.htm)
