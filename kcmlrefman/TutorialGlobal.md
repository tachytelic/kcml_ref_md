Global and background partitions

Introduction

KCML allows a foreground partition to attach additional (background) partitions to itself to allow several tasks to be performed from one terminal. THis switching between partitions is only supported under Unix. All versions of **KCML** allow one or more partitions to be declared as **Global Partitions** which share code, giving other partitions access to common routines and variables. Also available on all version of KCML is the [\$RELEASE]($RELEASE.htm) function, which allows the temporary cloning of a partition, and the capability of running a partition permanently in the background disconnected from the user.

Switchable background partitions

Switchable background partitions are only available on UNIX versions of **KCML**. The [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm), [\$RELEASE KEY]($RELEASE_KEY.htm), [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm) statements will give an 'A08 Statement not legal here' error if executed under NT.

Starting and stopping background partitions

Background partitions are created with the [\$RELEASE LOAD RUN]($RELEASE_LOAD_RUN.htm) statement, which starts an additional partition belonging to the calling terminal but running in background. The new child partition is created as a copy of the foreground partition, then the specified program is loaded and executed. The terminal however is detached from the background process and therefore any keyboard reads will suspend program execution until the terminal is re-attached. To start the program *BACK1* running in background the following would be used:

\$RELEASE LOAD RUN "BACK1"

Each background task started by the parent will remain available until the [\$END]($END.htm) statement is executed. If a **KCML** partition executes a \$END, **KCML** will automatically \$RELEASE TERMINAL into the next waiting background partition, if any. Subsequent \$END will keep releasing into the next waiting background partition until there are no more partitions to release to, only then will the user be returned to the operating system.

Accessing background partitions

KCML allows background partitions to be attached to the terminal under program control with the [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm) statement, or by user control by programming a function key as a hot key.

When the \$RELEASE TERMINAL statement is executed the current foreground partition is detached from the terminal, and the next available background partition is then attached to the terminal. The old foreground task will continue executing until it reaches a keyboard I/O statement. If several child processes have been started by the parent, the \$RELEASE TERMINAL statement allows the partition number to be specified, the partition number must be a valid number for a partition attached to the parent, otherwise a \`X77 Invalid partition reference' error will occur. E.g.

\$RELEASE TERMINAL TO 253

The [\$RELEASE KEY]($RELEASE_KEY.htm) statement is used to define the specified function key as a hot key, which when pressed will automatically \$RELEASE TERMINAL to the next available partition waiting to attach. The text screen is saved and is restored when the partition regains control, for example:

\$RELEASE KEY=20

would instruct **KCML** to perform a \$RELEASE TERMINAL if function key 20 is pressed.

The \$PSTAT function

The [\$PSTAT]($PSTAT.htm) function is used to return status information about the specified partition, when using background partitions it can be useful to determine which background partitions are currently waiting for I/O and which partitions are currently detached but are still processing.

The \$PSTAT function holds 48 bytes of information. Byte 16 holds information about the terminal status, if set to \`A' the partition is attached to the terminal, if set to \`D' the partition is detached from the terminal and if set to \`W' the partition is detached and is waiting on I/O. For example:

IF STR(\$PSTAT(#PART),16,1)=="D" THEN 9000

would jump to line 9000 if the executing partition was detached from the terminal, this example may be used to prevent background tasks from executing any screen or keyboard statements.

The \$RELEASE function

The [\$RELEASE]($RELEASE.htm) function is used to clone the existing program and run it as a child process. It is available on both Unix and NT. The parent process will wait until the child dies by executing the \$END statement. This function allows other programs to be executed that might destroy the contents of common variables or overwrite program lines.

Global Partitions

Global partitions provide the capability for **KCML** partitions to share subroutines and data. This allows common subroutines to be combined into one program making the original programs smaller, therefore making them load quicker. The number of global partitions available at any one time is hardware dependent, although software is far easier to maintain if all common subroutines and global variables are combined into one program.

Global partitions were largely obsoleted by the the more general [library](TutorialModules.htm) concept introduced with KCML 6.0. KCML Libraries should be used in all new applications.

Defining a partition as global

Global partitions are started by executing **KCML** with the \`-g' switch. The name of the global partition (used by the [SELECT @PART](SELECT_@PART.htm) statement) is specified by the [DEFFN @PART](DEFFN_@PART.htm) statement.

KCML will generally automatically allocate the right amount of memory for a global partition however if it has to be specified then the [HEAPINIT](EnvVars.htm#HEAPINIT) environment variable should be set before the global partition is started. The [HEAPINIT](EnvVars.htm#HEAPINIT) environment variable is used to specify the size of the global partition in Kb, for example:

HEAPINIT=512 export ; HEAPINIT\
kcml -g GLOBAL1 &

would reserve 512K of shared memory, and start the program *GLOBAL1* executing in that area. The ampersand \`&' instructs the UNIX operating system to run the process in background, otherwise the terminal would \`go into' the global partition as if it were a normal **KCML** task.

To start global partitions in the Unix Korn shell, which supports job control, the standard input should be redirected from the device '/dev/null' as the Korn shell handles background jobs in a different way to other shells, e.g.

kcml -g GLOBAL1 \</dev/null &

Normally a global partition would be started during the machines boot up process, by creating a script to start the global(s) and adding an entry into the machines */etc/inittab* file to call the start-up script, for example:

\# Script to start KCML global partition\
KCMLDIR=/usr/lib/kcml\
PATH=\$PATH:\$KCMLDIR\
TERMFILE=\$KCMLDIR/TERMFILE\
HEAPINIT=512\
KTERM=dumb\
\
export PATH PATH TERMFILE HEAPINIT KTERM\
\
( cd /user1 ; kcml -g PROGS/GLOBAL1 \>/tmp/gblog1 )\
\
HEAPINIT=50 ; export HEAPINIT\
\
( cd /user2 ; kcml -g PROGS/GLOBAL2 \>/tmp/gblog2 )

would start the programs *GLOBAL1* and *GLOBAL2* running as global partitions, the second program required less space than the first, therefore the value of the [HEAPINIT](EnvVars.htm#HEAPINIT) environment variable is changed before the second global partition is started. This script may be created in any directory, but it is suggested that it is created in the **KCML** utilities directory (normally /usr/lib/**KCML**). The two lines that contain the

*KCML -g* commands are enclosed in parentheses so that the current working directory can be set to that specified by the *cd* command, therefore any [\$DEVICE]($DEVICE.htm), [SELECT](SELECT.htm) etc. statement that do not specify absolute path names will work correctly. Any errors generated during the start up process and while the global partitions are running will be recorded into the files specified after the greater than sign \`\>'.

Once the above script has been created, the execute permissions must be set to allow the operating system to execute it. E.g.

chmod +x /usr/lib/kcml/kcmlsetup

The above script would be called from the \`/etc/inittab' file on most UNIX implementations, e.g.

gb:2345:boot:/usr/lib/kcml/kcmlsetup 1\>/dev/syscon 2\>&1

would execute the script \`/usr/lib/**KCML**/**KCML**setup' only if the machine was booted into any of the multiuser run levels (1-5), at this stage any errors would go directly to the system console.

When **KCML** is executed from the shell you cannot execute a program directly from a platter image, therefore a program held within a UNIX directory is required to first [\$DEVICE]($DEVICE.htm) any platter images into the device table, and then [LOAD](LOAD.htm) and execute the global program, this program would be called from the script described on the previous page, e.g.

REM Program to load and execute the global\
\$DEVICE /D10="/user1/D10.bin"\
\$DEVICE /D11="/user1/D11.bin"\
\$DEVICE /D12="/user1/D12.bin"\
SELECT DISK D10\
LOAD RUN "MAINGLOB"

Defining a partition as global (*kcmladmin* installed systems)

On most systems installed with the

*KCMLadmin* program the

*KCMLsetup* script is created automatically. Also the /*etc/inittab* file is modified to call the

*KCMLsetup* program.

To add global partitions to systems installed with the

*KCMLadmin* script, you must first create a program that contains all of the Device Table entries required by the global and save this program into the **KCML** utilities directory (usually /usr/lib/kcml). The last line of this program should select the disk containing the global program and execute it. The program should be SAVEd with a name made up as follows:

GLOBAL*n1.n2*

Where *n1* is a unique number given to each global partition counting upwards from 1, and *n2* is the size of the global partition in Kb (See [HEAPINIT](EnvVars.htm#HEAPINIT).

The program would be similar to the following:

\$DEVICE /D10="/usr/kcml/D10.bin"\
\$DEVICE /D11="/usr/lib/kcml/D11.bin"\
SELECT DISK D10\
LOAD RUN"GBLPRG"

The above program must be SAVEdsave into the **KCML** utilities directory, this can be done as follows:

SAVE "/usr/lib/kcml/GLOBAL1.100"

which would be the first global partition to be started, and would have 100Kb of memory allocated for the global. To start-up the Global partitions the machine must be re-booted.

Naming the global program

The program that is placed into shared memory, must contain a [DEFFN@PART](DEFFN_@PART.htm) statement. This statement defines the unique name of the global partition which will be used by other partitions to identify the global partition. E.g.

DEFFN @PART"GBMAIN1"

If the global partition is going to contain only shared text, that is several routines defined with the DEFFN' statement that will be used by partitions accessing the global, then only the DEFFN@PART and variable declaration statements need to be executed, once these have been executed the global can then be put to sleep. This is done with the [\$BREAK !]($BREAK.htm) statement, for example:

COM @junk\$1000, @lockvar=99\
INIT(HEX(FF)) @junk\$\
DEFFN @PART"TESTGBL"\
\$BREAK !\
DEFFN 'one\
. . .\
. . .\
RETURN

which would first declare and initialize the variables *@junk\$* and *@lockvar* and declare the name of the global, then it would sleep for ever. Therefore, the subroutine *'one* would never be executed by the global partition.

Accessing a global partition

Once the global partition is resident in the memory of the machine, other partitions can access its variables and subroutines simultaneously. The global partition is selected with the [SELECT @PART](SELECT_@PART.htm) statement, once selected all global variables and subroutines can then be accessed from the executing partition.

When a subroutine call is made with the [GOSUB'](GOSUBquote.htm) statement, the calling partition is searched first for the routine. If it is not found then the global partition is searched. If the subroutine is not found in either the executing or the global partition, then a "P37 Undefined marked subroutine" error will result. E.g.

<div align="CENTER">

<img src="bitmaps/GlobAccess.gif" data-border="0" width="462" height="218" />

</div>

In the diagram above the executing partition selects the global partition *GLOB1* the first GOSUB'test statement would have first looked for the routine *'test* in the executing partition, as it did not find the routine it then looked into the global partition, having found the routine, the lines were executed. When the RETURN statement was executed in the global partition, the program then went on to the next statement. The second GOSUB'local statement immediately executes the subroutine *'local* as it is resident in the currently executing partition.

A global partition is not de selected until either a new program is loaded, another global partition is selected, or a blank name is specified with the [SELECT @PART](SELECT_@PART.htm) statement. E.g.

SELECT @PART " "

The *KEEPSHARED* environment variable

Normally, if a [LOAD](LOAD.htm) statement is executed the currently selected global partition is de-selected. This can be prevented by setting the [KEEPSHARED](EnvVars.htm#KEEPSHARED) environment variable to any value.

Local and global variables

Global variables are declared from within a global partition, but can be referenced from any partition that selects the global with the [SELECT @PART](SELECT_@PART.htm) statement. Global variables exist as a completely different range of variables, and are identified by prefixing the variable name with the \`@' sign, therefore the variables *abc\$* and *@abc\$* are two completely different variables.

Global variables must be declared explicitly with a [COM](COM.htm) or [DIM](DIM.htm) statement, whereas local variables may be declared implicitly by reference. Once a global variable is modified, the modification becomes instantly available to all other partitions that have the global selected.

When global variables are used as a locking mechanism, the statements that modify the variable must be surrounded with the [@LOCK](@LOCK.htm) and [@UNLOCK](@UNLOCK.htm) statements. These statements implement advisory locking of the currently selected global partition. Advisory locking means that after an [@LOCK](@LOCK.htm) statement other partitions can still read and modify global variables but if they execute an [@LOCK](@LOCK.htm) statement themselves they will sleep until the global is unlocked.

In the example below, partition 2 executes the [@LOCK](@LOCK.htm) statement, and proceeds with the global subroutine *'updte,* meanwhile partition 50 will hang at the [@LOCK](@LOCK.htm) statement until partition 2 executes the [@UNLOCK](@UNLOCK.htm).

<div align="CENTER">

<img src="bitmaps/GlobLock.gif" data-border="0" width="472" height="211" alt="Illustrates use of @LOCK" />

</div>

Global variables may also be declared as local variables in a non-global partition. Such variables are not true global variables. All references to global variables after a global partition is selected will be directed to the global partition. This is a hangover from BASIC-2 dialects where variable names are restricted to 1 alpha character or one alpha character followed by a number, thus by adding the \`@' sign before the variable name allows a new range of variable names to these dialects.

Listing global program text

Most of the [LIST](LIST.htm) statements detailed in the statements and commands manual can be preceded with the \`@' sign to instruct them to list the currently selected global partition. For example:

@LIST 1000,

would list all program lines after line 1000 in the currently selected global partition,

@LIST T"ABC"

would search the currently selected global for the letters *ABC* and *abc*, and

@LIST '

would list all subroutines and subroutine references within the currently selected global partition.

The CALL, FROM', P, V, and \# [LIST](LIST.htm) options can also be performed on the currently selected global partition. Lines listed from the global partition or any lines displayed when an error is detected, are identified by the \`@' sign before the line number.
