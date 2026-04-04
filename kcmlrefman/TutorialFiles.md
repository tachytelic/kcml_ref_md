Data and program file access

Introduction

Normally in **KCML** both data and program files are created directly within the native operating systems file system. However, the platter image concept available in older versions of **KCML** is still available for compatibility reasons.

Maintenance of files held within the native file system is quite easy as normal operating system commands and utilities can be used with the files. However, care should be taken when naming files as there are several special characters that could cause problems if used. In both UNIX and Windows avoid using wildcard characters, especially asterisks (\*) and question marks (?). Other characters to avoid are shown below as these have a special meaning in the UNIX operating system.

\` \| " \$ ^ & ( ) \[ \]\
{ } \\ / \< \> ; \* ? !

Data files

There are two main methods available for data file access, K-ISAM (Kerridge Indexed Sequential Access Method) which is an efficient access method designed for large and complex data bases, and the standard file access method which is designed for much simpler file access. This section only describes the simpler standard file access method.

The standard file access method is designed to conform to the UNIX/DOS/ANSI model. The functions can all be used on standard UNIX/DOS/NTFS files, named pipes and character devices.

Opening and creating data files

Existing files are opened and new files are created with the [OPEN \#](OPENhash.htm) statement. The file is opened on the specified stream which can previously be selected to a native operating system directory with the [SELECT \#](SELECT_DISK.htm) statement. Alternatively the absolute or relative pathname of the file can be specified. The stream can later be freed with the [CLOSE \#](CLOSEhash.htm) statement.

The syntax for the [OPEN \#](OPENhash.htm) statement is as follows:

OPEN \#s,file\$\[,mode\$\] \[,permissions\$\] \[,buffersize\]

which would open the file *file\$* on stream *\#s*. Any file previously open on the stream is first closed.

The mode parameter specifies how the file is to be opened. For example:

OPEN \#10, "/user1/FILE1","r+"

would open the file "/user1/FILE1" in read and write mode. The statement would error if the file did not exists. To open the file for both read and write operation and create a new file each time the file is opened the following would be used:

OPEN \#10, "/user1/FILE1","w+"

The default permissions to be set on the file when it is created can also be set. These are specified using the format used to the UNIX *umask* command. They consist of a leading zero followed by three octal digits representing the user, group and public permissions for the file. For example:

OPEN \#10, "/user1/FILE1","w+", "0666"

would create the file with both read and write permissions set for the user, the members of the users group and all other users of the system. To close the file and free the stream the following would be used:

CLOSE \#10

Several different modes are available with the [OPEN \#](OPENhash.htm) statement, refer to the [OPEN \#](OPENhash.htm) statement in the statements manual for details of the valid modes and permissions.

Writing information to files

Once the file has been opened information can be written to the file. The modes used to open the file will effect the way in which information can be written. For example, if the file was opened with a mode of ‘a’ then information can only be appended to the file. Information already contained within the file cannot be modified. Whereas if the file were to be opened with a mode of ‘r+’ information can be written anywhere within the file.

Information is written using the WRITE \#writehash statement which writes the contents of an alpha variable to the file currently open on the specified stream. For example:

OPEN \#10, "/user1/FILE1","w+"\
offset = WRITE \#10, buffer\$

would create and open the file "/user1/FILE1" and write the contents of the variable *buffer\$*, including any trailing blanks, to the file. After the write the file pointer is automatically advanced by the number of bytes written. A second [WRITE \#](WRITEhash.htm) to the file would append the contents of the specified variable to the end of the file. The numeric receiver variable contains the number of bytes written.

If an error occurs WRITE \# returns a value of -1. The reason for the error can be found with the [ERR](ERR.htm) function. For example:

IF WRITE \#10, buffer\$ = -1 THEN DO\
PRINT "Last error code was ";ERR\
ENDDO

Reading information from files

The [READ \#](READhash.htm) statement is used to read data from the file currently open on the specified stream. After the read the number of bytes read is returned as the value of the function and the file pointer is advanced. If there are not enough bytes to fill the alpha variable then the numeric variable will be less than the size of the buffer variable and the END condition will be set. This can be tested with the [IF](IFTHEN.htm), [WHILE](WHILE.htm), or [UNTIL](REPEAT.htm) statements. Any further READ will return zero bytes. For example:

WHILE NOT END DO\
BytesRead = READ \#10,Buffer\$\
'Process(STR(Buffer\$,,BytesRead))\
WEND

Like [WRITE \#](WRITEhash.htm), if an error occurs [READ \#](READhash.htm) returns a value of -1. The reason for the error can be found with the [ERR](ERR.htm) and [\$OSERR]($OSERR.htm) functions.

[READ \#](READhash.htm) can be made to read a line at a time from a file again returning the number of characters copied to the buffer. The rest of the buffer is left unaltered. The count does not include the termination character and the terminating character is not copied to the buffer. A count of zero could indicate that either a blank line has been read or that there is nothing to read and the end of the file has been reached. If the termination character has been reached then HEX(04) bit is set in byte 4 of [\$OPTIONS \#]($OPTIONShash.htm) for the relevant stream. The line terminator is specified within [\$OPTIONS \#]($OPTIONShash.htm)d by ORing HEX(01) into byte 2, and setting byte 5. Reads are buffered and the buffer size can be specified by [OPEN \#](OPENhash.htm) when the file is opened. Opening the file in text mode for DOS files will automatically translate HEX(0D0A) sequences into HEX(0A) terminators. Under UNIX you can also translate HEX(0D0A) sequences into HEX(0A terminators by ORing HEX(02) bit of [\$OPTIONS \#]($OPTIONShash.htm) byte 2 for the relevant stream. If a HEX(0D) character is found then the HEX(02) bit of byte 3 is also set.

Changing the current file pointer

The file pointer can be positioned prior to a [READ \#](READhash.htm) or [WRITE \#](WRITEhash.htm). with the SEEK \#seekhash statement. [SEEK \#](SEEKhash.htm) can be used to seek to the beginning of the file by specifying the BEG parameter, the end of the file with END, or for an increment from the current position with the FOR parameter. The syntax for [SEEK \#](SEEKhash.htm) is as follows:

n = SEEK \#s,\[\[BEG\|END\|FOR\] \[,\]\] \[numexpr\]

For example:

new_pos = SEEK \#10, BEG

would instruct a subsequent [READ \#](READhash.htm) or [WRITE \#](WRITEhash.htm) operations to operate from the beginning of the file, while:

new_pos = SEEK \#10, END

would instruct the [READ \#](READhash.htm) or [WRITE \#](WRITEhash.htm) operations to operate at the end of the file, and:

new_pos = SEEK \#10, FOR 120

would instruct any subsequent [READ \#](READhash.htm) or [WRITE \#](WRITEhash.htm) operations to operate at 120 bytes forward from the previous pointer position.

An additional parameter can also be appended to the BEG and END parameters to instruct SEEK \# to move to the BEGinning or end + or - the specified value. For example:

new_pos = SEEK \#10, BEG, 120

would move the pointer to byte 120 in the file, and

new_pos = SEEK \#10, END, -120

would move the pointer 120 bytes back from the end of the file.

Seeking beyond the end of the file is allowed. Executing a [WRITE \#](WRITEhash.htm) after such a seek will automatically extend the file up to the new position.

Like [READ \#](READhash.htm), and [WRITE \#](WRITEhash.htm) if an error occurs [SEEK \#](SEEKhash.htm) returns -1 and the reason for the error can be found with the ERR function.

File locking

Advisory file locks are set with the [\$OPEN]($OPEN.htm) statement and are removed with the [\$CLOSE]($CLOSE.htm) statement or when the stream is freed with the [CLOSE \#](CLOSEhash.htm) statement. Advisory locking means that other partitions can read or write the \$OPENed file but they cannot \$OPEN it themselves.

If the specified stream has already been \$OPENed by another partition, the statement will hang until the device is freed, unless an optional line number is specified causing the program to branch to the specified line.

For example, the following would open and lock the file "NEWFILE".

OPEN \#10, "NEWFILE", "r+"\
\$OPEN \#10, 1000

An I92 "Time out error" will result if an attempt is made to lock a file that has not been opened with write access.

Miscellaneous file IO statements

Obtaining file details

The LIMITS statement can be used to return the start, end and current pointer position of the file currently open on the specified stream. For example:

LIMITS T#10, file_start, file_end, current_pos

Because this stream was opened with [OPEN \#](OPENhash.htm) the values are returned in bytes. The start value will always be 0.

Removing files

Files created with the [OPEN \#](OPENhash.htm) statement can be removed with the [REMOVE](REMOVE.htm) statement. For example:

REMOVE "NEWFILE"

would remove the file currently open on stream \#10.

Renaming files

The RENAME T statement can be used to rename files created with the [OPEN \#](OPENhash.htm) statement. For example:

RENAME T#10,"OLDFILE" TO "NEWFILE"

PRINT#, PRINTUSING#

Output from the [PRINT](PRINT.htm) and [PRINTUSING](PRINTUSING.htm) statements can be directed to files using streams. For example:

OPEN \#10,"/tmp/TESTFILE","w+"\
PRINTUSING \#10, "#####.##",total\
CLOSE \#10

The end of each line is terminated with a HEX(0A). This can be changed to HEX(0D0A) on DOS systems by appending the ‘t’ flag to the mode options when the file is opened.

Program files

Saving program files

Program files can be SAVEd directly into the file system with the [SAVE](SAVE.htm) or [RESAVE](RESAVE.htm) statements. If you are using the **KCML** Workbench then both SAVE and RESAVE can be performed with CTRL-S or from the File menu.

Both the [SAVE](SAVE.htm) and [RESAVE](RESAVE.htm) statements can be used to create a new program file in the specified directory. With the SAVE statement if the specified filename already exists a \`D83 Cannot save file' error will occur. For example, to save the program currently held in memory into the UNIX directory "/user1/PROGS", the following would be used:

SELECT DISK "/user1/PROGS"\
SAVE "M-MENU"

alternatively the absolute pathname of the file may be used or a stream could be selected to the relevant directory. The following would both save the program into the directory "/user1/PROGS":

SAVE "/user1/PROGS/M-MENU"\
\
SELECT \#27, "/user1/PROGS"\
SAVE "M-MENU"

To save a program into a program file that already exists the [RESAVE](RESAVE.htm) statement should be used.

Removing program files

KCML programs can be removed with the [REMOVE](REMOVE.htm) statement. This statement should be used with caution as many operating systems will not allow the file to be recovered. The REMOVE statement works within the current working directory but it also allows absolute path names to be specified. To work in the context of a stream and the current value of SELECT DISK you can use the now deprecated SCRATCH which works relative to the stream table. Thus both of the following could be used to remove the file created in the examples above:

REMOVE "/user1/PROGS/M-MENU"\
\
SELECT \#46 "/user1/PROGS"\
SCRATCH "M-MENU"

Loading program files

Programs are loaded from directories with the [LOAD](LOAD.htm) and [LOAD RUN](LOAD_RUN.htm) statements in the same way as if loading from a platter image. Programs can also be loaded directly from anywhere in the file system by specifying the full pathname of the file. For example:

LOAD "/user1/PROGS/TESTPROG"

or

LOAD RUN "/user1/PROGS/TESTPROG"

Alternatively the [SELECT DISK](SELECT_DISK.htm) statement could be used to select the default stream (#0) to the directory, e.g.

SELECT DISK "PROGS"\
LOAD "TESTPROG"

Scrambling program files

KCML allows programs to be protected by scrambling the program with a password. When **KCML** is executing a scrambled program, all LISTing, editing, and TRACEing is disabled. Pressing the [HALT](TextTermHalt.htm) key will stop the program, but the only actions available are [CLEAR](CLEAR.htm) and [LOAD RUN](LOAD_RUN.htm). However if the program is overlaid with lines from a normal program, then [LIST](LIST.htm) and the **KCML** Workbench will only show the program lines of the new program, stopping at the first protected line.

To scramble programs for all subsequent [SAVE\<!\>](SAVE.htm) or [RESAVE \<!\>](RESAVE.htm) statements, the [SELECT PASSWORD](SELECT_PASSWORD.htm) command is used. Once the command has been executed **KCML** will prompt twice for a password. Echoing of characters as they are entered is suppressed, so the password has to be entered identically twice to avoid mistakes. The password is SAVEd with the scrambled program.

The program may be revealed by specifying the original password with the [SELECT PASSWORD](SELECT_PASSWORD.htm) command immediately after the program has been [LOAD](LOAD.htm)ed.

As an aid to the support of scrambled programs, it is possible to temporarily reveal the executing program without giving away the master password. See [SELECT PASSWORD](SELECT_PASSWORD.htm) and [SAVE](SAVE.htm), and the *checknum* utility in the **KCML** utilities chapter.
