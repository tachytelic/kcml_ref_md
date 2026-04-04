General configuration

Partitions and terminals

KCML is to a large extent self configuring. Partitions are created by running **KCML** and are thus equivalent to UNIX processes.

Each instance of **KCML** on a system is allocated a unique partition number as an integer in a contiguous range from 1 to a theoretical 32767. This partition number is displayed on the line below the copyright message when the [CLEAR](CLEAR.htm) command is entered or when the RESET key is pressed. The partition number can also be returned with the [\#PART](_PART.htm) function. A working limit of 1024 partitions is enfored by default on all UNIX versions of **KCNML** though the [bkstat](bkstat.htm) utility can be used to increase the maximum up to the theoretical maximum of 32767. On NT under KCML 5.03 the working limit is fixed at 512.

Each **KCML** running will also have a terminal number which is also a small integer in the range 0 to 32767 representing the physical terminal on which it is running. Again a working limit of 1024 is used under Unix and 512 under NT. The terminal number is returned by the [\#TERM](_TERM.htm) function. The terminal number can be zero if the program is running in the background disconnected from a physical terminal.

On Unix versions of **KCML** terminal numbers are stored in an ASCII file whose name and location is determined by the [TERMFILE](EnvVars.htm#TERMFILE) environment variable. On UNIX versions if [TERMFILE](EnvVars.htm#TERMFILE) is not set then the file '/tmp/TERMFILE' is used. If the file determined by [TERMFILE](EnvVars.htm#TERMFILE) does not exist, **KCML** will automatically create it and allocate terminal numbers, counting up from 1 as each new terminal logs in. The first column of this file contains the Client computer name (if Kclient), an IP address if WDW or the UNIX *tty* name if neither of those. The second column holds the terminal number that will be the [\#TERM](_TERM.htm) and [\#PART](_PART.htm) value for the first partition on that terminal. Any other numbers on the line will be allocated as [\#PART](_PART.htm) for subsequent **KCML** processes running concurrently on the terminal. All the **KCML**s share the same [\#TERM](_TERM.htm) value. If there are more **KCML**s than numbers on the line then the extra partitions will be allocated [\#PART](_PART.htm) values counting down from 512 (or the value set by the [BCDPART](EnvVars.htm#BCDPART) environment variable). A typical TERMFILE entry on a UNIX system might be:

/dev/term/45    50 51 52 53

For client server NT or for WKCML the same information is stored in the server registry.

This allows users running multiple sessions on the same terminal e.g. Windows **KCML**. This ensures that each time **KCML** is run from a particular terminal it will always get the same [\#TERM](_TERM.htm). See [TERMFILE](EnvVars.htm#TERMFILE) in the **KCML** Environment section.

If a second partition is created at a particular terminal using either [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm) or SHELL "kcml" on UNIX versions, or if an additional **KCML** is started up on the Windows version the new **KCML** keeps the same [\#TERM](_TERM.htm) terminal number but is given a new partition number allocated from the pool of available partitions, counting down from the value of the [BCDPART](EnvVars.htm#BCDPART) environment variable.

The [BCDPART](EnvVars.htm#BCDPART) environment variable may be used to restrict the range of partition numbers available to **KCML**. This can be set to the maximum allowable partition number e.g.

BCDPART=400 export BCDPART

Memory allocation

Memory allocation for a terminal is, for most implementations, automatic, with partitions being allocated space as required. **KCML** starts out with a certain memory allocation called a heap whose size is controlled by either the [HEAPINIT](EnvVars.htm#HEAPINIT) environment variable. If this variable has not been pre-set then the initial *heapsize* is automatic. The heap is used for all internal tables, program lines and variables. If the program requires more than the initial heap then it is automatically extended. Beware that space allocated is not automatically freed if the variables are cleared or a smaller program is LOADed. The [\$SPACE]($SPACE.htm) statement is used to force a memory compacting routine, and perhaps should be executed from within menu programs etc.

The [LIST SPACE](LIST_SPACE.htm) command can be used to display a breakdown of the memory usage for the current partition.

Configuring KCML devices

The Device Equivalence Table

The device equivalence table (DET) is an area of memory allocated to each partition to hold a list of available and currently selected devices. The device table is checked each time any I/O operation is performed.

Each device is accessed by referencing a unique three character device address. Each character must be a valid hexadecimal digit, (0-9, A-F).

Preallocated device addresses

The DET for each partition is defined with the [\$DEVICE]($DEVICE.htm) statement, which should be executed before the device is referenced. The [\$DEVICE]($DEVICE.htm) statement links the device address with a file. Certain devices are pre-allocated:

/000 /dev/null Null printer\
/001 stdin Standard input, usually the keyboard\
/005 stdout Standard output, usually the screen\
/215 /dev/lp Line printer\
/204 stdout Local Printer

The first three devices are not strictly part of the DET and cannot be redefined with [\$DEVICE]($DEVICE.htm). The printer devices can be redirected with explicit [\$DEVICE]($DEVICE.htm) statements. For example, to change the device used by the line printer (/215) you would issue a statement similar to the following:

\$DEVICE /215="/dev/term/27"

Adding or removing DET entries

New entries may be added, modified or removed from the DET using a similar statement. The optional keywords DISK and TC are allowed to specify that the device is a platter image or 2227B device respectively. Device addresses beginning with 3, B or D are always assumed to be disk platter images.

\$DEVICE /D10="G:\demo\accounts.bs2"\
\$DEVICE /920="/dev/rfd096ds15",DISK\
\$DEVICE(/01C)="COM1",TC

If a platter is to be defined without a 3, B or D as the first character of the address then the DISK clause must be specified after the [\$DEVICE]($DEVICE.htm) statement. The parentheses surrounding the device address are optional.

Entries may be removed by specifying a blank filename, e.g.

\$DEVICE /217 = " "

or

\$DEVICE /217

which both remove the /217 device from the DET. This can only be done if the device is not currently in use.

Platter images and native operating system files are configured in a similar way. If the full pathname of the file is not specified, the file is assumed to be in the current directory.

Using \$DEVICE as a function

The [\$DEVICE]($DEVICE.htm) statement may also be used as a function returning the name of the native operating system file underlying the device address, e.g.

prdev\$ = \$DEVICE /215

The internal Device Table (DT)

Default devices

The DT also contains certain default addresses reserved for specific I/O operations, such as line printer devices etc. These default addresses are:

|  |  |
|----|----|
| [CI](SELECT_CI.htm) | Used to specify the Console Input device address for immediate mode commands and program editing. The characters entered into the Console Input device are automatically echoed on the console output device. The default address of this device is /001 for the keyboard. |
| [CO](SELECT_CO.htm) | Used to specify the Console Output device address. Characters entered from the [CI](SELECT_CI.htm) device in immediate mode or during program editing are displayed on the console output device. All responses to [INPUT](INPUT.htm), [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), [LINPUT LIST](LINPUT_LIST.htm), [KEYIN](KEYIN.htm), [TRACE](TRACE.htm) etc. are echoed to the [CO](SELECT_CO.htm) device. The default address of this device is /005 for the screen. This value also holds the line width value for the screen, which defaults to 80. |
| [INPUT](SELECT_INPUT.htm) | Used to specify the device address to be used to enter data to the [INPUT](INPUT.htm), [KEYIN](KEYIN.htm), [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), and [LINPUT LIST](LINPUT_LIST.htm) statements. The default address of this device is /001 for the keyboard. |
| [LIST](SELECT_LIST.htm) | Used to specify the output device on which all [LIST](LIST.htm) output is to be displayed. The default address of this device is /005 for the screen. This parameter also holds the line width value for the device. The line width defaults to 80. |
| [LOG](SELECT_LOG.htm) | Used to specify the output device on which all keyboard input will be recorded. The default address of this device is /005 for the screen. |
| [PRINT](SELECT_PRINT.htm) | Used to specify the output device on which all output from the [PRINT](PRINT.htm) and [PRINTUSING](PRINTUSING.htm) statements is to be sent. The default address for this device is /005 for the screen. This parameter also holds the line width value for the device. The line width defaults to 80. |
| [TAPE](SELECT_TAPE.htm) | Used to specify the address to be used for any tape class operations that do not specify a device address or file number in the instruction itself, for example \$GIO, \$IF ON. The default address for this device is /005 for the screen. |
| [TRACE](SELECT_TRACE.htm) | Used to specify the address to which all output from the [TRACE](TRACE.htm) command and the [\$COMPILE]($COMPILE.htm) statement is to be sent. Usually /005 for the screen. |

The above devices can be modified with the [SELECT](SELECT.htm) statement followed by the name of the device, e.g.

SELECT INPUT /009

would change all input to the [KEYIN](KEYIN.htm), [LINPUT](LINPUT.htm), [LINPUT LINE](LINPUT_LINE.htm), [LINPUT LIST](LINPUT_LIST.htm) statements to read from the device /009.

The above devices can also be selected directly to a native file or even a pipe by specifying the filename or pipe as a literal string, e.g.

SELECT LIST "\|lpr"

would send the output from all [LIST](LIST.htm) commands to the UNIX print spooler \`lpr'. To re-select [LIST](LIST.htm) output to the screen the following would be used:

SELECT LIST /005

Selecting streams

The DT allows access to devices via a stream address, the actual device is selected to the stream with the [SELECT](SELECT.htm) statement. Data files can then be opened or programs loaded by specifying a stream instead of a device address. Streams are numbered from 0 to 255. Each stream can maintain one device address. Once a device address is selected to a stream, all subsequent I/O references made to that stream are directed to the corresponding device address. If no stream address is specified with I/O statements, then the default stream of \#0 is used. The [DISK](SELECT_DISK.htm) select parameter is used to specify an address to stream \#0.

Streams can also be selected to native operating system directories, making all subsequent I/O operations work in the selected directory. Directory names are specified as a literal string, e.g.

SELECT \#129 "/usr/PROGRAMS"

In the DOS and Windows version, **KCML** will automatically translate the forward slash to a backslash.

Deselecting streams

A certain amount of memory is required each time a new stream number is activated. When that stream number is no longer required the memory can be recovered with the DESELECT statement, e.g.

DESELECT \#129

would deselect the stream selected in the example above

Streams are automatically cleared upon execution of the [CLEAR](CLEAR.htm) command, [LOAD RUN](LOAD_RUN.htm) statement, pressing the RESET key, or if the \$SELECT "." statement is executed.

Using SELECT as a function

As with the [\$DEVICE]($DEVICE.htm) statement the [SELECT](SELECT.htm) statement can be used to return the device address or native file allocated to the specified stream, or select parameter, e.g.

PRINT SELECT PRINT, SELECT \#27\
\
005       /user1/PROGS

The [SELECT](SELECT.htm) function can be used wherever a alpha function is valid.

Changing the current working directory

The files or directories specified in the literals used by [\$DEVICE]($DEVICE.htm) and some select statements will expect to find the file in the current directory, unless the file name begins with a slash character (/ or \\. The \$[SELECT](SELECT.htm)d statement can be used to change the current working directory to a different position within the native operating system tree. When the statement is executed all currently selected streams are automatically closed, and the new directory selected. All DET entries remain intact, even entries to files held in the previous working directory. These files can be cleared with the [\$REWIND]($REWIND.htm) statement. Like all [SELECT](SELECT.htm) statements, \$[SELECT](SELECT.htm)d can be used as a function returning the current working directory. E.g.

\$SELECT "/user1/tmpdir"\
PRINT \$SELECT\
\
/user1/tmpdir

Displaying the DET and DT with LIST DT

The [LIST DT](LIST_DT.htm) statement displays the current contents of the Device Equivalence Table, along with the Device Table. The display is divided up into two main sections. The first lists the device table showing those stream numbers that have been allocated with the full filename, along with the start, end, used and free information for the file. The current lock status for the file is also shown.

The second section refers to the DET, under the heading \`Devices defined'. The default devices followed by any additional devices defined with the [\$DEVICE]($DEVICE.htm) statement are listed. The second section also contains the remaining [SELECT](SELECT.htm) devices, such as LIST, TRACE, CI, CO etc.
