NT Core Files

Definition

A core dump file is a snapshot of the memory in a process. They are created when something serious happens within KCML or the application causing the program to terminate abruptly. Core files are similar to KCML Panic files, and can sometimes help the application or KCML department fix problems that would otherwise be difficult or impossible or solve. A good analogy would that of the black box data recorder fitted to aircraft.

A local core file is saved onto the filesystem of the system that generated it be it the server or client. A network core file can be copied from the system that generated it to a central repository using FTP. Network core files are very useful for debugging client problems.

Enabling local core files

By default core files are never created. The core dump options are enabled by setting values in the registry. An example KCML program is presented below to alter the registry for you. This may be built into an application as an administrative option and allows the settings to be altered on the host machine while connected from a remote client.

The program allows you to specify the directory to place core files, and whether core files should be generated on crashes or on crashes and panics. All core files are generated to this directory and have names clearly indicating the date and time the file is created. Core files are created through a compression process to keep the size small.

Enabling network core files

To enable network core files an environment variable **KCML_CORE_FTP** must be set in the connection manager. This enables cores for both the server and any connected clients while connected. The value of this variable specifies the location of the FTP repository and any authentication necessary in a comma separated list.


    KCML_CORE_FTP="directory,server,userid,password"

for example


    KCML_CORE_FTP="/cores,callisto,pjc,secret"

If anonymous FTP is supported on the server the userid and password can be omitted. The server can be either an IP address or a resolvable DNS domain name. The directory will either be relative to the FTP directory root for anonymous FTP or should be a qualified filename for authenticated FTP. The directory must exist and be writable otherwise the core dumping operation will silently fail.

If a system is configured for network core files this will take precedence over any local core file settings.

Using core files

Core files were originally designed to enable the KCML support investigate intractable problems on remote sites but they can have uses for the application developer as well (in KCML 6.x). In particular a developer can recover the text of the program being edited following a crash.

**The version of KCML used to analyse a core must be exactly the same version as the KCML that generated the core file.**

Recovering Code

If KCML crashes during application development then it is possible to lose developed code if it has not recently been saved. The core file is a dump of memory and so contains the program. The -corelist option is used from KCML (even if the session is started from kclient -d).


     kcml -corelist <corefile>

This lists to standard output the program in memory. Normally this will be redirected to a file:


     kcml -corelist core1999-11-12_172311 > myprog.src

Using the workbench

This option starts up KCML and places the programmer in the workbench at the point at which the core dump (which will probably be a panic) occured. It will appear exactly as if programming was enabled and the program executed a PANIC statement taking the programmer into the workbench. In this mode it is possible to view variables, code and other debugging options. However it is not possible to execute any code as none of the originally open files will be open.


     kcml -coreeditor core1999-11-12_172311

Limitations

- Core dumps are experimental and are an on-going area of development. They are documented here because in certain cases they have been extremely useful.
- Core dumps are only supported on NT and not UNIX or other versions of Windows (Windows 95 and Windows 98).
- Loading core files into the workbench will identify where in the application the problem occured. No subsequent debugging operation can be guaranteed.

KCML program to set registry values to enable local core files

<a href="#nowhere" onclick="CopyTextToClipboard(&#39;EXAMPLE1&#39;)">Copy example to clipboard</a>


    REM Note that the registry API uniquely expects the sizes of buffers to be passed in bytes
    REM and not characters so on calls with such parameters we must ensure we call the ANSI version
    REM and not the Unicode version (the default for the Unicode Kclient)
    $DECLARE 'RegOpenKeyEx(INT(),STR(),INT(),INT(),RETURN INT())
    $DECLARE 'RegQueryValueEx(INT(),STR(),INT(),RETURN INT(),RETURN DIM(),TO RETURN INT())=".RegQueryValueExA"
    $DECLARE 'RegQueryValueStr(INT(),STR(),INT(),RETURN INT(),RETURN STR(),TO RETURN INT())=".RegQueryValueExA"
    $DECLARE 'RegCreateKeyEx(INT(),STR(),INT(),INT(),INT(),INT(),INT(),RETURN INT(),RETURN INT())
    $DECLARE 'RegSetValueEx(INT(),STR(),INT(),INT(),STR(),INT())=".RegSetValueExA"
    $DECLARE 'RegDeleteValue(INT(),STR())
    $DECLARE 'RegDeleteKey(INT(),STR())
    $DECLARE 'RegCloseKey(INT())
    $DECLARE 'RegEnumKeyEx(INT(),INT(),RETURN STR(),TO RETURN INT(),INT(),INT(),INT(),INT())
    $DECLARE 'CreateDirectory(STR(),STR())
    $DECLARE 'GetFileAttributes(STR())
    DIM _FILE_ATTRIBUTE_DIRECTORY=0x10
    DIM REG_BINARY=0, REG_SZ=1, REG_DWORD=4, REG_EXPAND_SZ=2
    DIM KEY_READ=0x00020019, KEY_SET_VALUE=0x02
    DIM hkey
    DIM filename$256, dword$4
    - DEFFORM Form1()={.form,.form$,.Style=0x50c000c\
    4,.Width=350,.Height=105,.Text$="Form",.Id=1024}\
    ,{.ok,.button$,.Style=0x50010001,.Left=\
    295,.Top=6,.Width=50,.Height=14,.Text$="OK",.__A\
    nchor=5,.Id=1},{.cancel,.button$,.Style=0x500100\
    00,.Left=295,.Top=23,.Width=50,.Height=\
    14,.Text$="Cancel",.__Anchor=5,.Id=2},{.Help,.bu\
    tton$,.Style=0x50010000,.Left=295,.Top=44,.Width\
    =50,.Height=14,.Text$="&Help",.__Anchor\
    =5,.Id=9},{.CoreDumps,.checkbox$,.Style=0x500100\
    02,.Left=5,.Top=6,.Width=88,.Height=10,.Text$="E\
    nable NT Core Dumps",.Id=1000},{.filena\
    me,.kcmldbedit$,.Style=0x50810080,.Left=24,.Top=\
    44,.Width=170,.Height=13,.Id=1001},{.Panic,.chec\
    kbox$,.Style=0x50010002,.Left=24,.Top=7\
    1,.Width=80,.Height=10,.Text$="Core dump on &Panic",\
    .Id=1002},{.filenametext,.static$,.Style=0x\
    50000000,.Left=24,.Top=33,.Width=69,.He\
    ight=8,.Text$="Core &dump path:",.Id=1003},{.grp\
    Control1,.groupbox$,.Style=0x50000007,.Left=6,.T\
    op=22,.Width=248,.Height=66,.Text$="Det\
    ails",.Id=1004}
    + DEFEVENT Form1.Enter()
    LOCAL DIM rc, filenamelen, dwordlen, type, paniccore
    REM Open key on HKEY_LOCAL_MACHINE
    rc = 'RegOpenKeyEx(0x80000002, "SOFTWARE\Kerridge\KCML", 0, KEY_READ + KEY_SET_VALUE, SYM(hkey))
    IF (rc == 0)
    REM get directory name
    filenamelen = LEN(STR(filename$))
    rc = 'RegQueryValueStr(hkey, "Core", 0, SYM(type), filename$, SYM(filenamelen))
    IF (rc == 0 AND type == REG_SZ AND filenamelen > 0)
    .CoreDumps.State = 1
    ELSE
    rc = 'RegQueryValueStr(hkey, "CoreDisabled", 0, SYM(type), filename$, SYM(filenamelen))
    .CoreDumps.State = 0
    END IF
    .filename.Text$ = filename$
    REM set if core on panic is enabled
    dwordlen = 4
    rc = 'RegQueryValueEx(hkey, "PanicCore", 0, SYM(type), STR(dword$), SYM(dwordlen))
    $UNPACK(F=HEX(D004)) dword$ TO paniccore
    .Panic.State = paniccore
    REM enable or disable controls appropriately
    Form1.CoreDumps.Click()
    END IF
    END EVENT
    + DEFEVENT Form1.Exit()
    REM close reg key
    IF (hkey <> 0)
    'RegCloseKey(hkey)
    END IF
    END EVENT
    + DEFEVENT Form1.CoreDumps.Click()
    REM enable according to checkbox state
    .filename.Enabled = Form1.CoreDumps.State
    .filenametext.Enabled = Form1.CoreDumps.State
    .Panic.Enabled = Form1.CoreDumps.State
    END EVENT
    + DEFEVENT Form1.ok.Click()
    LOCAL DIM a, a$4, b$4
    IF (.CoreDumps.State == 1)
    REM want cores, try to ensure dir exists
    a = 'GetFileAttributes(.filename.Text$)
    a$ = BIN(a, 4)
    IF (a$ == HEX(FFFF FFFF))
    REM need to create
    'CreateDirectory(.filename.Text$, 0)
    ELSE
    REM exists but is it a directory?
    b$ = a$ AND BIN(_FILE_ATTRIBUTE_DIRECTORY, 4)
    IF (b$ == HEX(0000 0000))
    REM no
    .form.Beep(_BEEP_DEFAULT)
    RETURN FALSE
    END IF
    END IF
    REM log directory name name in registry
    'RegSetValueEx(hkey, "Core", 0, REG_SZ, .filename.Text$, LEN(.filename.Text$))
    ELSE
    REM disable cores
    'RegDeleteValue(hkey, "Core")
    REM remember previous dir in case we re-enable later
    'RegSetValueEx(hkey, "CoreDisabled", 0, REG_SZ, .filename.Text$, LEN(.filename.Text$))
    END IF
    REM extra flag for panic cores
    $PACK(F=HEX(D004)) b$ FROM .Panic.State
    'RegSetValueEx(hkey, "PanicCore", 0, REG_DWORD, b$, 4)
    END EVENT
    FORM END Form1
    Form1.Open()
