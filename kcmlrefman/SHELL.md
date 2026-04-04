SHELL

------------------------------------------------------------------------

General Forms:

1.  SHELL alpha_expression
2.  numrecvr = SHELL alpha_expression

------------------------------------------------------------------------

The SHELL statement is used to execute native operating system commands, program or shell script from within KCM programs. If the string is blank then an interactive shell will be run.

The SHELL statement can also be used as a numeric function returning the completion code of the Unix command, program, or script. For both Unix and NT it is returned in the standard Unix format of a 16 bit integer where the least significant byte contains the status of the shell operation and the most significant byte is the return code from the command. If Unix cannot start the child process then a negative return code indicates the reason as a standard Unix *errno*.

The return code is probably not useful in Windows environments as the default command processor COMMAND.COM does not return this information to the caller.

Windows commands are always executed by a %COMSPEC% command processor subshell unless the HEX(02) bit is set in byte 37 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE37). There is a problem on Windows 95 and Windows 98 with commands that invoke COMMAND.COM, such as interactive sessions or batch files, hanging on exit. To avoid this KCML will run such commands using a helper function CONSPAWN.EXE which is installed into the KCML directory and must be available.

When searching for a command to run on Win9x and NT KCML will first look to see if it is registered with the Windows shell under the [AppPaths](javascript:TextPopup(hhctrl,%20APP_PATHS)) key and if so use the full filename found there to open it. If not it follows the same rule as WinExec(), namely

1.  The KCML directory.
2.  The current working directory.
3.  The Windows system directory.
4.  The Windows directory.
5.  The directories listed in the PATH environment variable.

On all platforms KCML will honour the standard Unix redirection operators in the command line, viz.

| Operator | Purpose |
|----|----|
| \< | Take standard input from a file |
| \> | Send standard output to a file |
| \>\> | Append standard output to a file |
| & | Run command as an asynchronous process. KCML will not wait for it to complete and the return code will not reflect the commands status, only the shell status. |
| ! | WKCML only. Run command in a separate visible window. This can also be achieved by setting the HEX(04) bit in byte 37 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE37). Use this if you will need to interact with the command e.g the DOS EDIT command. |

There is also support for treating the Unix null device */dev/null* as the equivalent *NUL* device in Windows.

The Unix environment variable [SHELL](EnvVars.htm#SHELL) may be used to determine the command shell used by the SHELL statement. Also for Unix KCML will switch the terminal back to the original terminal state to run the command unless it has detected the redirection operator '\>' in the command. This is necessary because KCML puts a terminal into a raw binary mode while executing interactively.

While the SHELL statement is being executed, byte 29 (DEVice awaited) of [\$PSTAT]($PSTAT.htm) will be set to HEX(FC).

Pseudo-tty support has been added to Unix versions so that interactive commands, such as **vi**, **passwd** or **man**, can be executed when connected via the [Connection Manager](mk:@MSITStore:kwebserv.chm::/connmgr.htm). This pseudo-tty support is only enabled when the [PSEUDOTTY](EnvVars.htm#PSEUDOTTY) environment variable has been set to **TRUE** in *kconf.xml* The pseudo-tty support can be disabled by clearing bit 8 of byte 37 of [\$OPTIONS RUN]($OPTIONS_RUN.htm#BYTE37). Setting this bit will only have an effect if [\$PSEUDOTTY](EnvVars.htm#PSEUDOTTY) has been set to **TRUE**.

Example:

test\$ = "date"\
result = SHELL test\$

Syntax examples:

SHELL "backupprog"\
result(1) = SHELL testport\$(1)
