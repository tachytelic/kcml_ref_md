kcml

General Form:\
\
kcml \[-gcdfnprwzv\] \[*program*\] \[*param*...\]

This command invokes the KCML interpreter from the shared library *kserver.dll* (NT), *kserver.sl* (HP-UX) or *kserver.so*. It will read commands from the standard input, and will be interactive if this is a terminal. End of file will cause the system to exit and return to the operating system unless interactive, in which case the [\$END]($END.htm) statement must be used. Refer to the [appendix](tmp/ExitCodes.htm) for a list of the values returned to the operating system when KCML is closed.

If the optional program argument is given, it should be the name of a file containing either a compiled KCML program, or a sequence of immediate statements in ASCII. In the former case, the program will be run before any commands read from the standard input. In the latter case, the commands and statements will be executed.

If the optional program argument is not given, but the environment variable *START* exists, and holds the name of a file, this file will be used as the start-up program in the same way.

Any other optional parameters after the start program are not used by KCML and are available for the application to inspect using the [\$ARG()]($ARG(.htm) function.

Any or all of the standard input, standard output, or error output may be redirected. The usage of these files is as follows:

|        |                    |
|--------|--------------------|
| stdin  | CI and INPUT       |
| stdout | CO, PRINT and LIST |
| stderr | TRACE              |

The switches are case sensitive.

<span id="switch"></span>

| Switch | Purpose |
|----|----|
| -b | Act as a [SOAP server](soapserver.htm) listening out for web service requests. |
| -c | Forces KCML to run in a batch compiling mode with the same functionality as [compile](compile.htm). *compile* is not available as a separate program under DOS. This must be the first switch on the command line. Subsequent switches can be taken from the list of switches in the *compile* documentation. |
| -d | Dongle test. Only relevant on versions of KCML that are supported by dongles. Executing a CML -d returns information about the dongle, i.e. the maximum number of supported users, the KCML software license number, the [\#GOLDKEY](_GOLDKEY.htm) value etc. |
| -e *envvar* | Sets an environment variable. This can be used for those variables that need to be set before KCML has started running, e.g. [HEAPINIT](EnvVars.htm#HEAPINIT) or [BCDPART](EnvVars.htm#BCDPART). A value can be set using an = sign or if no value is given the environment variable is set to TRUE |
| -g | KCML will load the specified program into a shared memory area and execute it as a global partition. See [Background and Global partitions](TutorialGlobal.htm) chapter. |
| -k *lowPort,hiPort \[,timeout\]* | KCML will run persistently having reconnected to a port between loPort and hiPort. Timeout in seconds can optionally be set. This can be used in connection with Apache's mod_kcml to start persistent KCML SOAP servers. |
| -l | [Direct telnet](dircon.htm) support |
| -n | Enables NPL compatibility mode at runtime. It disables the special treatment of global variables with an ‘@’ prefix, forces 24 lines for [INPUT SCREEN](INPUT_SCREEN.htm) on terminals with more than 24 lines and disables scrolling in [PRINT AT()](PRINT_AT(.htm). This functionality can also be enabled and disabled with byte 33 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE33). |
| -p *prog* | Start KCML server and run the nominated program as a non-interactive [kcml script](script.htm). |
| -q | Start KCML and connect to a [Corba](comintro.htm) ORB, usually to act as a [Corba server](corbaserver.htm). ORB specific switches should follow this. If this instance is to act as a Corba server you must specify a program to run and that program should invoke the server. |
| -s | Switch to the directory of the command line directory program argument before starting execution. The default is to stay in the current directory. |
| -S service | Load the environment associated with the specified service using kconf.xml. This is performed automatically by the connection manager but can also be specified this way for direct connections. |
| -v | Display the build version |
| -x *lib.so* | Unix only. Specified a [KCML shared library](ufn.htm) to be loaded for use in [CALL](CALL.htm). Multiple libraries are allowed by repeating this switch. |
| -y | Use C runtime memory allocator. This has the same effect as setting the [USEMALLOC](EnvVars.htm#USEMALLOC) environment variable. |
| -corelist *core* | NT only. Specifies a [core file](NTCoreFiles.htm) to be loaded and listed. |
| -coreeditor *core* | NT only. Specifies a [core file](NTCoreFiles.htm) to be loaded. The workbench will then be loaded displaying the program state at the time of the crash. |

The parameters available with the *kcml* utility are as follows

Examples:


     kcml -g -e BCDPART=99

and


     kcml -v

Could display


     kcml release version 06.00.00.7114, 64-bit disk access

For a KCML that as been compiled with large (\>2Gb) file support.

See also:

[compile](compile.htm), [START](EnvVars.htm#START) environment variable
