KCML environment variables

Each environment variable is displayed along with the description, if the variable can also be changed with one of the [\$OPTIONS]($OPTIONS.htm), [\$OPTIONS LIST]($OPTIONS_LIST.htm) or [\$OPTIONS RUN]($OPTIONS_RUN.htm) system variables then the variable and byte numbers are also shown.

Unless specified all of the following variables are available on all KCML versions. Some of the variables listed here are general UNIX environment variables that have an effect on UNIX versions of KCML only.

<span id="_answerback"></span>

\_ANSWERBACK

This variable and [\_KTERM](#_KTERM) will be set by kclient on login to a server using a Unix feature that allows the setting of environment variables passed on the login line. The [selfid](mk:@MSITStore:kcmlrefman.chm::/selfid.htm) utility will then use them to avoid querying the terminal directly making it more efficient. If no answerback is defined in the client the variable will exist but will be blank.

<span id="_kterm"></span>

\_KTERM

Set automatically by the client on logging into the server. See [\_ANSWERBACK](#_ANSWERBACK) above. The version number of the client is passed after the KTERM value e.g. KClient_46.

<span id="atreplace"></span>

ATREPLACE

Replacement characters for the ‘@’ sign at the beginning of variables when compiling ASCII source when importing from environments where the ‘@’ prefix does not denote a global variable. Byte 28 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE28) specifies the character to be used, normally an ‘@’ sign, if set to HEX(00) the value of this environment variable is used.

> ATREPLACE=Glob\_ export ATREPLACE

<span id="bcdpart"></span>

BCDPART

By default KCML supports up to 1024 partitions and allocates the partition numbers for background partitions from 1024 downwards. On NT for KCML5.03 these limits are 512 and 254 respectively. If your applications would fail if given a \#PART value of this size you can use this environment variable to limit the maximum value KCML can allocate. If you require more than 1024 terminals or partitions on Unix then refer to the [bkstat utility documentation](bkstat.htm). If the variable can be interpreted as a number then that will be the maximum partition number and if just set to TRUE then 99 will be assumed as the maximum.

> BCDPART=1024 export BCDPART

It is also possible, in unusual circumstances, to start allocating both terminals and partitions from other than 1 by supplying both a minimum and a maximum value e.g.

> BCDPART="100,255" export BCDPART

<span id="break30"></span>

BREAK30\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 8

On versions of KCML previous to the 3.20 version a [\$BREAK]($BREAK.htm) specifying no time would delay for 50 clock ticks (about 1 second), on KCML 3.20 and later the delay was reduced to 1 clock tick. This variable was added to provide compatibility with older versions. It must be set before KCML is started.

> BREAK30=true export BREAK30

<span id="compat2200"></span>

COMPAT2200\
[\$OPTIONS LIST]($OPTIONS_LIST.htm) byte 1\
<span id="compatniakwa"></span>COMPATNIAKWA\
[\$OPTIONS LIST]($OPTIONS_LIST.htm) byte 2

These variables control the LIST’ing of programs. They must be set before KCML is started. Unless this variable is set to anything, KCML will automatically recreate certain statements to the KCML form. For example:

> MAT a = b

would be recreated as:

> a() = b()

The following statements are affected

> |             |      |          |
> |-------------|------|----------|
> | \$FORMAT    | INIT | SELECT D |
> | \$TRAN      | LIST | SELECT G |
> | ALL         | LOAD | SELECT P |
> | HEXPRINT    | REM  | SELECT R |
> | IF ... THEN | SAVE |          |

Most MAT statements are also effected.

> COMPAT2200=true export COMPAT2200

<span id="compat30"></span>

COMPAT30\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 1

This variable should be set if you are developing software in KCML versions later than 3.10 and you would like the software to be used on version 3.0. If set, KCML will give a warning for each line containing a statement introduced in versions after 3.0 that is not supported by version 3.0. E.g. [\$DISCONNECT]($DISCONNECT.htm), [\$IF]($IF.htm) etc.

> COMPAT30=true export COMPAT30

<span id="compat32"></span>

COMPAT32\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 16

This variable should be set if you are developing software in KCML versions 4.0 and above and you would like the software to be used on version 3.2x. If set, KCML will generate backward compatible code and SAVEsave will give a warning for each line containing a statement introduced in versions 4.0 and later that is not supported by version 3.2x. E.g. [OPEN#](OPENhash.htm), [LINPUT +](LINPUTplus.htm) etc.

> COMPAT32=true export COMPAT32

<span id="compat40"></span>

COMPAT40\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 38

This variable should be set if you are developing software in KCML versions 5.00 and above and you would like the software to be used on versions \< 5.00.

> COMPAT40=true export COMPAT40

<span id="curchar"></span>

CURCHAR\
[\$OPTIONS]($OPTIONS.htm) byte 4

If set to a string of up to two characters, that string will replace the dollar sign as the currency symbol when [PRINTUSING](PRINTUSING.htm) is printing numbers. The dollar is still required in the [PRINTUSING](PRINTUSING.htm) image. Only one character can be specified if [\$OPTIONS]($OPTIONS.htm) is used to change the currency symbol.

> CURCHAR='FF' export CURCHAR\
> STR(\$OPTIONS,4,1)=HEX(7C)

<span id="cwd"></span>

CWD

This variable can be used to determine the initial working directory for KCML. If it is not supplied then KCML will assume the current working directory.

> CWD=/user1/test/progs export CWD\
> CWD=\$NEWDIR export CWD

<span id="dcinternal"></span>

DCINTERNAL\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 10

Workaround for problem with multisector DATA LOAD/SAVE DC of string of 251+n\*254 bytes overflowing the sector.

<span id="doselect"></span>

DOSELECT\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 7

Unix only. Setting this variable to anything turns on the use of the select system call prior to reading from file descriptor zero and writing to file descriptor one. This can help with problems encountered with terminals connected via TCP/IP terminal server connections, especially on RS6000's.

> DOSELECT=true export DOSELECT

<span id="dotchar"></span>

DOTCHAR\
\$OPTIONS byte 6

If set to a single character, that character will replace the '.' as the decimal point character when [PRINTUSING](PRINTUSING.htm) is printing numbers. The period is still required in the image. The continental European usage of a comma as the decimal character is shown in the example below.

> DOTCHAR=',' export DOTCHAR\
> STR(\$OPTIONS,6,1)=","

<span id="dumpcore"></span>

DUMPCORE\

If set, will cause KCML to create a memory core file if KCML abnormally terminates. Only relevant on UNIX versions.

> DUMPCORE=true export DUMPCORE

<span id="editor"></span>

EDITOR

Unix only. This variable is used to select the native operating system text editor that is to be used upon invoking the EDIT command within the **KCML** immediate mode. This variable has no effect on the Workbench. If *EDITOR* is not set then KCML assumes the *ed* editor.

> EDITOR=vi export EDITOR

<span id="forceterm"></span>

FORCETERM

If set to a numeric integer within the range 1 - 512, KCML will then set the value returned by the [\#TERM](_TERM.htm) function to the value specified by *FORCETERM*. Particularly useful for BASIC-2 ports where some programs have terminal numbers hardwired within certain statements, i.e. [\$ALERT]($ALERT.htm), [\$RELEASE TERMINAL]($RELEASE_TERMINAL.htm) etc.

> FORCETERM=500 export FORCETERM

<span id="forcewindows"></span>

FORCEWINDOWS

If set, KCML will force the generation of the special KCML windowing sequences for intelligent terminals (DW, WDW, Kclient, Magna, Spx701 etc) irrespective of actual terminal type. Only relevant on UNIX versions and probably obsolete. See [WINDOW](WINDOW.htm) statement.

> FORCEWINDOWS=true export FORCEWINDOWS

<span id="haltchar"></span>

HALTCHAR

Unix only and now obsolete. The key to be used for the [HALT](TextTermHalt.htm) keyboard command is normally taken from the UNIX interrupt key. This can be overridden by setting this environment variable to the ASCII hex representation of the required character. The example below defines Ctrl+Z as a HALT key.

> HALTCHAR=1A export HALTCHAR

<span id="heapinit"></span>

HEAPINIT

Generally KCML will manage memory automatically both for foreground partitions and also shared memory partitions and it should be allowed to do so as this will minimize the memory required. However if memory mapped global partitions are required then it may be necessary to tell KCML before it starts up how much memory will be needed as it cannot grow such memory. By setting the environment variable *HEAPINIT* to number of kilobytes the size of the initial allocation may be controlled. If a global partition fails to run because of memory problems try a bigger *HEAPINIT* value. The value is in kilobytes.

> HEAPINIT=2048 export HEAPINIT

<span id="helpextension"></span>

HELPEXTENSION

Used by the [\$HELP]($HELP.htm) statement and Help buttons on forms when using a client browser to view HTML. Used to determine the extenson to append to a URL filename if no explicit extension is supplied. If not set the '.html' will be assumed.

<span id="helpserver"></span>

HELPSERVER

Used by the [\$HELP]($HELP.htm) statement and Help buttons on forms. If set to the name of a Windows Help file, and the HEX(10) bit of byte 41 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE41) is set then \$HELP will call the specified Windows Help file. This requires that either Windows KCML or UNIX KCML connected via kclient or the Windows DW terminal emulator is being used. For example:

> ENV("HELPSERVER")="C:\KCMLHelp\KCMLMAN.HLP"\
> \$HELP("\$DECLARE’")

*HELPSERVER* can also be used to point to a directory on the PC containing HTML files. With this set both Windows KCML and Windows DW can be forced to load the files with a Windows browser by setting byte 41 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE41) to HEX(0C), for example:

> STR(\$OPTIONS RUN,41,1)=HEX(0C)\
> ENV("HELPSERVER")="C:\HelpFiles"\
> \$HELP("Main.htm")

*HELPSERVER* can also be used to instruct \$HELP to go to a Web Server for its help files, again this requires that byte 41 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE41) is set to HEX(0C) and that you are running under Windows. For example:

> STR(\$OPTIONS RUN,41,1)=HEX(0C)\
> ENV("HELPSERVER")="http://www.kerridge.com"\
> \$HELP("index.htm")

This can be particularly useful for applications that use the [Connection Manager](mk:@MSITStore:kwebserv.chm::/connmgr.htm), as this will define environment variables that can be used to construct a portable URL:

> HELPSERVER=http://\$SERVER_NAME:\$SERVER_PORT/\$SERVICE/Help

Where **Help** is a directory alias defined in the service's section of kconf.xml. The Connection Manager will then serve the help pages.

<span id="home"></span>

HOME

Used to specify the initial directory for the [Workbench file browser](mk:@MSITStore:workbench.chm::/wbbrowsefiles.htm).

<span id="http_proxy"></span>

HTTP_PROXY

Used to specify the location of a HTTP proxy server through which [SOAP](ObjSoap.htm) requests will be sent. It can be overridden by the proxy keyword in [CREATE](CREATE.htm). The general format is \[user\[:password\]@\]proxyserver\[:port\] though not all proxy servers require a user and password.

> HTTP_PROXY=proxy.bigco.com:8080 export HTTP_PROXY

<span id="KCML_HEAP_SIZE"></span>

KCML_HEAP_SIZE

Linux, HP-UX11, Solaris and AIX 5 versions of KCML allocate memory from a virtual memory mapped file. The default size of this file, and therefore the maximum amount of memory a KCML process can allocate, is 64Mb. This size can be changed by setting the KCML_HEAP_SIZE variable.

> \# Set max size of KCML heap to 128 Mb\
> KCML_HEAP_SIZE=128\
> export KCML_HEAP_SIZE

KCML_ID

Used to change the value returned by the [\#ID](_ID.htm) function. By default \#IDid is set to the same value as is returned by the [\#GOLDKEY](_GOLDKEY.htm) function which is set in the KCML license file.

> KCML_ID= 9426 export KCML_ID

<span id="kcmlini"></span>

KCMLINI

Obsolete on KCML 6.0. If using the original KCML4 editor and not the KCML Workbench then it can be used to indicate the location of the file that holds the users editor preferences. In KCML 6.0 and later the Workbench stores these in the clients registry.

> KCMLINI=/usr/lib/kcml/kcml.ini export KCMLINI

<span id="kcmlpath"></span>

KCMLPATH

The text of all error messages is held in the file *berror.d* which must be in a directory on the current path (see *[PATH](#PATH)* below). Other important files such as the *TERMINFO* directory and default translation tables are also expected to be found in that directory. A fatal error will be given if KCML cannot find *berror.d* or *TERMINFO* when it starts up. If the file cannot appear on the path then the directory containing the file may be explicitly specified as the environment variable *KCMLPATH*.

> KCMLPATH=/user1/progs/errordir\
> export KCMLPATH

<span id="keepshared"></span>

KEEPSHARED\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 11

Selected global partitions are normally automatically de-selected by a [LOAD](LOAD.htm) of a program or overlay. If the new program requires access to the global then it needs to issue its own [SELECT @PART](SELECT_@PART.htm). This can be avoided by setting the environment variable *KEEPSHARED*. Also controlled by this environment variable is a change to the search algorithm for defined functions. In the BASIC-2 dialect, subroutines were first looked for in the executing partition and then in any selected global, if different from the currently executing partition. With this change the original home partition is always searched first before the currently executing partition. These changes are to support shared text as a library of useful routines and to allow the caller to override the default routines with special versions of his own.

> KEEPSHARED=true export KEEPSHARED

<span id="kindent"></span>

KINDENT\
[\$OPTIONS LIST]($OPTIONS_LIST.htm) byte 20

This variable is used to specify the number of spaces used to indent the body of loops etc. when programs are LISTed. The default for this variable is 4.

> KINDENT=2 export KINDENT\
> STR(\$OPTIONS LIST,20,1)=BIN(2)

<span id="klang"></span>

KLANG\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 20

This variable is used to select the default language string that is to be used when multilingual strings are referenced. Refer to the [Multilanguage support chapter](TutorialLangs.htm) in this volume for more information. A list of the available language codes may be found under byte 20 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE20)

> KLANG=2 export KLANG\
> STR(\$OPTIONS RUN,20,1)=BIN(2)

<span id="klogkey"></span>

KLOGKEY\

For development it may be desirable to have several different KCML database journal systems. The KLOGKEY environment parameter can be used to keep these systems separate. It must be exactly 4 characters long. It's value is used as the key for the shared memory and semaphore that control the journal system. It's default value is "KLOG", 0x424C4F47. For more information see [Transactions](mk:@MSITStore:kdb.chm::/transact.htm)

> KLOGKEY=TEST export KLOGKEY

<span id="kterm"></span>

KTERM

The *KTERM* variable is used in preference to the *TERM* variable to allow greater flexibility when using other UNIX packages that use the *TERM* variable. If *KTERM* has not been set, the value of *TERM* is used.

> KTERM=wy160 export KTERM

<span id="linelen"></span>

LINELEN

Because the Workbench editor can edit any size of program line but the old [line editor](mk:@MSITStore:workbench.chm::/LineEditor.htm) used in KCML3 and on the console window of KCML4 and KCML5 was limited to 1900 characters, the various compatibility flags set bt COMPAT30 etc will set an internal maximum line length of 1900 and you will be warned if you exceed that length. This environment variable can be used to set the maximum to any arbirary size. By default the limit is set to zero which disables the checking mechanism.

> LINELEN=512 export LINELEN

<span id="mallocspace"></span>

MALLOCSPACE

Unix specific. By default KCML allows a 128kb space at the beginning of the data segment to allow space for the C runtime library function malloc(). In general this is enough for the library functions called by KCML itself. If you are using [external functions](ufn.htm) you may need more and this space can be set to any given value by setting the MALLOCSPACE environment variable to the number of kilobytes required. This must be done before KCML is executed.

> MALLOCSPACE=1000 export MALLOCSPACE

<span id="noenddoerror"></span>

NOENDDOERROR\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 6

At resolve time KCML checks the program to make sure that it can execute correctly, for example it make sure that there are no syntax errors, and that all [FOR](FOR.htm) statements have a corresponding NEXT statement etc. On all versions from 3.20 on, KCML checks for unmatched [DO](DO.htm) and END DO statements, therefore, programs that ran perfectly on earlier versions will error on all version from 3.20 on if they contain unmatched DO ... END DO statements. This should only be used as a temporary fix, the programs should really be fixed as soon as possible.

> NOENDDOERROR=true export NOENDDOERROR

<span id="nohalt"></span>

NOHALT\
\$OPTIONS, 13

If this environment is set to any value, then the [HALT](TextTermHalt.htm) key will be disabled preventing users from interrupting programs.

> NOHALT=true export NOHALT\
> STR(\$OPTIONS,13,1)=BIN(1)

<span id="noglobmap"></span>

NOGLOBMAP

This applies to Unix only and should be set before KCML is started. On a system with multiple active shared memory global partitions, KCML will map in all existing partitions before creating and mapping in a new partition in order to guarantee a unique starting address. Setting this environemnt variable to TRUE will disable this and the new partition will be created at the next available address. Do not use unless requested to by KCML support.

<span id="noprog"></span>

NOPROG

If this environment variable exists at startup, i.e. is set to any value, then the user will be prevented from entering any programming commands or editing programs. If *NOPROG* is set and a program returns to the immediate mode prompt for any reason, i.e. if [HALT](TextTermHalt.htm) or [RESET](TextTermHalt.htm) is pressed, if either of the STOPstop or [END](END.htm) statements are executed or if the program errors then KCML will automatically execute the [PANIC](PANIC.htm) statement.

> NOPROG=true export NOPROG

<span id="noreset"></span>

NORESET\
\$OPTIONS byte 12

If this environment variable exists at startup, i.e. is set to any value, then the [RESET](TextTermHalt.htm) key will be disabled preventing users from interrupting programs.

> NORESET=true export NORESET\
> STR(\$OPTIONS,12,1)=BIN(1)

<span id="options"></span>

OPTIONS_nn

If this environment variable exists at startup then the corresponding byte *nn* in the [\$OPTIONS]($OPTIONS.htm) system variable will be preset to the value which must be interpretable as a two digit hexidecimal value. Thus to always force KCML to error unDIMed variables you could set [byte 38]($OPTIONS.htm#BYTE38) to HEX(01) in advance like so

> OPTIONS_38="01" export OPTIONS_38\

<span id="options_list"></span>

OPTIONS_LIST_nn

If this environment variable exists at startup then the corresponding byte *nn* in the [\$OPTIONS LIST]($OPTIONS_LIST.htm) system variable will be preset to the value which must be interpretable as a two digit hexidecimal value. Thus to always force KCML to indent loops with two spaces you could set [byte 20]($OPTIONS_LIST.htm#BYTE20) to HEX(02) in advance like so

> OPTIONS_LIST_20="02" export OPTIONS_LIST_20\

<span id="options_run"></span>

OPTIONS_RUN_nn

If this environment variable exists at startup then the corresponding byte *nn* in the [\$OPTIONS RUN]($OPTIONS_RUN.htm) system variable will be preset to the value which must be interpretable as a two digit hexidecimal value. Thus to always force KCML to LOAD and save programs in ascii with a .src extension you could set [byte 40]($OPTIONS_RUN.htm#BYTE40) to HEX(06) in advance like so

> OPTIONS_RUN_40="06" export OPTIONS_RUN_40\

<span id="panicdir"></span>

PANICDIR

The [PANIC](PANIC.htm) statement dumps to disk a snapshot of the state of the program at that time before terminating KCML. The report is placed in a file *panicxxxx,* where *xxxx* is the process number, in the current working directory. If you want these files to be created in another directory then specify the directory name as the value of the *PANICDIR* environment variable. On Windows a registry key set in **kservadm** can be used to set this directory but PANICDIR overrides that setting.

> PANICDIR=/usr/panics export PANICDIR

<span id="path"></span>

PATH

This variable is used by KCML, as it is in the native shell, in locating native operating system commands and programs when such commands or programs are called by KCML with the [SHELL](SHELL.htm) statement, or from the immediate mode prompt following the ‘!’shell command. Note that a different syntax is used under DOS to append to the current PATH.

> PATH=\$PATH:/usr/lib/kcml export PATH

<span id="pseudotty"></span>

PSEUDOTTY

Setting this environment variable to "TRUE" or "true", in *kconf.xml*, will enable the pseudo-tty support for interactive shell commands, such as *vi*, *ftp*, *passwd* and *man* when connected via the [Connection Manager](mk:@MSITStore:kwebserv.chm::/intro.htm) on Unix systems.

<span id="r7fix"></span>

R7FIX

This is a compatibility fix for some old versions of Kerridge Rev7 written for KCML 2.0. Changes introduced in KCML3 impacted some Rev7 programs and this switch will restore the KCML2 behaviour in certain areas if enabled.

- \$IF /xxx returns a P48 error if the device is not \$DEVICE'ed
- LINPUT issues a HEX(09) after the prompt rather than HEX(20)
- PRINT will break long strings which would extend beyond the end of the line but are not longer than the line widthrather than move the whole string to the new line

<span id="screendir"></span>

SCREENDIR

If a text mode program receives a SIGUSR2 signal from bkstat it dumps to disk a snapshot of the screen in [INPUT SCREEN](INPUT_SCREEN.htm) format. The report is placed in a file scrn*xxxx*, where *xxxx* is the [\#PART](_PART.htm) partition number, in the current working directory. If you want these files to be created in another directory then specify the directory name as the value of the *SCREENDIR* environment variable.

> SCREENDIR=/usr/screens export SCREENDIR

<span id="shell"></span>

SHELL

On Unix this environment variable can be used to override the shell to be used to execute a command in the [SHELL](SHELL.htm) statment. By default the shell used is the Bourne shell.

<span id="sepchar"></span>

SEPCHAR\
\$OPTIONS byte 5

If set to a single character, that character will replace the comma as the digit separator when [PRINTUSING](PRINTUSING.htm) is printing numbers. The comma is still required in the image. The continental European usage of a period as the digit separator requires the following to be used:

> SEPCHAR='.' export SEPCHAR\
> STR(\$OPTIONS,5,1)="."

<span id="soapstart"></span>

SOAPSTART

This environment variable will be checked before the [START](#START) environment variable when KCML is acting as a [SOAP server](soapserver.htm) and interpreted as the name of the program to be run. It will generally be set in kconf.xml for a service which can also be used interactively.

> SEPCHAR='.' export SEPCHAR\
> STR(\$OPTIONS,5,1)="."

<span id="space"></span>

SPACE

If this variable is set to a numeric value, it determines the value that will be returned by the [SPACE](SPACE.htm), [SPACEF](SPACE.htm), [SPACEP](SPACE.htm), [SPACEV](SPACE.htm) and [SPACEW](SPACE.htm) functions in **KCML**. This is made available as some BASIC-2 software tested the result of the SPACE function before certain operations could take place.

> SPACE=56 export SPACE

<span id="spacek"></span>

SPACEK

If this variable is set, it determines the value that will be returned by the [SPACEK](SPACE.htm) function in KCML. This is available as some BASIC-2 software tested the result of the [SPACEK](SPACE.htm) function before certain operations could take place.

> SPACEK=56 export SPACEK

<span id="spool"></span>

SPOOL

The variable is used to specify the lock file used by any UNIX spooler for the main system printer so that KCML can also lock using that file. It can only be used if there is only one system printer on device /015. If not supplied KCML will generate the lock file name from the prefix '*/tmp/lck*' and the devices major and minor device numbers. For example, device /215 might be locked by file '*/tmp/lck28(17)*'. Only relevant on the UNIX version.

> SPOOL=215lock export SPOOL

<span id="start"></span>

START

If this variable is set to a KCML program name KCML will attempt to [LOAD RUN](LOAD_RUN.htm) the program when KCML is first started. The program should reside in the current directory.

> START=DEVICES export DEVICES

<span id="systemid"></span>

SYSTEMID

This was introduced in KCML 5.02, for Unix, and in KCML 6.00 for Windows NT. Provided this is enabled in the license file with the SYSTEMID= keyword, you can set this environment variable before starting KCML to specify an instance number (a small integer counted from 0 to 65535) for the KCML environment you wish to use. The number you specify must agree with the license file number.\
\
Normally only one instance of KCML is installed on a particular server. Multiple instances permit independent environments which can reuse \#PART and \#TERM values without any conflict. This is particularly useful for [ASP](asp.htm) systems. Each instance requires its own license file and has its own shared memory [\$PSTAT]($PSTAT.htm) table and globals.

> SYSTEMID=2 export SYSTEMID

If this variable has been set KCML version 6.00, and later, will first look for a license file called *lic.n.txt*, where *n* is the value of SYSTEMID. Eg, using the above example lic.2.txt . If this licence file was not found then KCML 6.00 will use the normal filename of *lic.txt*

<span id="term"></span>

TERM

This is a UNIX specific environmental variable that is set to the type of the terminal being used in the current login session per standard UNIX conventions. KCML uses *TERM* for the same reason as UNIX, the TERMINFO sub directory, which should exist on the current *PATH*, is searched for a file matching the value of *TERM*. If the environment variable *KTERM* is set *TERM* will be ignored. If the value of *TERM* matches the suffix on any [\$KEYBOARD]($KEYBOARD.htm) or [\$SCREEN]($SCREEN.htm) files, KCML will automatically use these files.

> TERM=vt320 export TERM

<span id="termfile"></span>

TERMFILE

KCML remembers which partition a given terminal was allocated in a terminal file which is automatically created the first time KCML is run. On UNIX versions if *TERMFILE* is not set then KCML will create a file called *TERMFILE* in the directory ‘/tmp’. On DOS and Windows versions if *TERMFILE* is not set then the file is created in the current directory. It is very important that all users use the same value for this variable so this environment variable ought to be set in ‘*/etc/profile*’. The file *TERMFILE* should not be edited with users using KCML, especially under UNIX as UNIX editors remove and recreate the file which will change the inode number of the file, this will not only change the value of the \#ID function on some versions of KCML but will prevent any new users accessing any currently running global partitions.

> TERMFILE=/usr/lib/kcml/TERMFILE\
> export TERMFILE

TOMDIR, TOMFILE\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) bytes 4 and 5

If this variable is set and the third character of the filename is a space then KCML will change this for a forward slash '/', thus creating a separate directory, also any spaces after the third character are then replaced with an underscore character. For example, the program "AB C D E" would be saved as "AB/C_D_E". Since 'AB' is now a directory, if a program called 'AB' is now saved an error will occur. Setting the *TOMDIR* variable to anything enables the filename change to lower case if a directory of the same name already exists thus preventing the error. This is only relevant if programs and data files are to be saved as native operating system files.

> TOMFILE=true TOMDIR=true\
> export TOMFILE TOMDIR

<span id="unixprogs"></span>

UNIXPROGS\
[\$OPTIONS RUN]($OPTIONS_RUN.htm) byte 2

If set to anything KCML will expect to load programs from a native operating system directory and not from a platter image. This variable effects the following statements and commands:

> LOAD, SAVE, SCRATCH, LIMITS, LOAD DA, SAVE DA

> UNIXPROGS=true export UNIXPROGS

<span id="USEMALLOC"></span>

USEMALLOC

Setting this environment variable before KCML is run will cause it to use the standard memory allocation scheme rather than its own private mechanism. It has the same effect as using the -y [command line switch](kcml.htm#switch). This may be necessary if the KCML is sharing its address space with components compiled by third parties e.g. [dynamic objects](DynObj.htm), [user functions](ufn.htm) or complex library functions invoked by [\$DECLARE]($DECLARE.htm). As a consequence of this it will not be possible to release unused memory on [CLEAR](CLEAR.htm) or on [\$SPACE]($SPACE.htm). This is only necessary on Unix platforms that do not support a [memory mapped heap](#KCML_HEAP_SIZE).

> USEMALLOC=true export USEMALLOC

<span id="USING-UTF8"></span>

USING-UTF8

Setting this environment variable before KCML is run tells KCML that all strings and database columns are to be presumed encoded in UTF-8. In particular strings sent to the client will be in UTF-8. Byte 59 of [\$MACHINE]($MACHINE.htm) will be set to HEX(01) to indicate the server is running in this mode.

> USING-UTF8=true export USING-UTF8

<span id="workspace"></span>

WORKSPACE

This variable is used by the [FSORT](FSORT_BU.htm) statement to determine which directory is to be used to hold temporary work files during sorting. If this variable is not defined the directory '*/tmp*' is used.

> WORKSPACE=/user1/tmpdir export WORKSPACE

<span id="KCML_CLEAR_LOCALS"></span>

KCML_CLEAR_LOCALS

Setting this environment variable will force KCML to recover local symbol space more aggressively. This should only be enabled if symbol space consumption is an issue.

> KCML_CLEAR_LOCALS=true export KCML_CLEAR_LOCALS
