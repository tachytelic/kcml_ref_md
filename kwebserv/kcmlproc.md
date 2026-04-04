<span id="kcmlproc"></span>

Current KCML Processes

This page deals with KCML specific features. The first set of links are [directory listings](dirlist.htm).

Link

Environment variable

Directory contents

KCML is installed in ...

\$KCMLDIR

KCML executable and configuration files

Show KCML panic files in ...

[\$PANICDIR](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#PANICDIR)

Snapshots of a KCML programs during an error

Show KCML screen dump file in ...

[\$SCREENDIR](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SCREENDIR)

Snapshots of screen memory from textmode applications

Show application files in ...

\$BASE or \$SYSADDR

Application program code and data

\
There is also a link to display the KCML Terminal table, **TERMFILE**. These values for these filenames are taken from the environment of the [Current Service](currentsrv.htm).

Next are two links to change your [current service](currentsrv.htm).\
\
The systems's broadcast message, [\$MSG](mk:@MSITStore:kcmlrefman.chm::/$MSG.htm) is shown, which can be changed using the **Reset broadcast message** link. A simple example would be to set [\$MSG](mk:@MSITStore:kcmlrefman.chm::/$MSG.htm) to something like Please log off at 1:30 This can be used with the **'Alert all partitions'** or the **'Send Broadcast message to all partitions'** links at the top of the KCML partition table page to send a system wide broadcast message to all KCML users. Using the *Broadcast* signal has the advantage that no application code changes are needed. KCML will force **KClient** to display the broadcast message on the terminal.\
If additional action is required then the [\$ALERT](mk:@MSITStore:kcmlrefman.chm::/$ALERT.htm) signal can be used. An application can then trap the [\$ALERT](mk:@MSITStore:kcmlrefman.chm::/$ALERT.htm) signal and then display the broadcast [message](mk:@MSITStore:kcmlrefman.chm::/$MSG.htm). DIM a\$ SELECT ON ALERT 'show_broadcast() PRINT "Waiting for input ..." KEYIN a\$ END DEFSUB 'show_broadcast() PRINT \$MSG END SUB There are two sets of three links to view the **KCML Partition Table**.

- Standard display
- Alternative display
- Full display

The **Standard** and **Alternative** display have been modelled on the [bkstat](mk:@MSITStore:kcmlrefman.chm::/bkstat.htm) utility. The **Full** display will display every property of a KCML Partition.\
The first group of links will display all KCML partitions that are using the same [TERMFILE](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#TERMFILE) as the default service. This is the normal behaviour of [bkstat](mk:@MSITStore:kcmlrefman.chm::/bkstat.htm) and [\$PSTAT](mk:@MSITStore:kcmlrefman.chm::/$PSTAT.htm) The second group of links which will display all KCML partitions. This is similar to the behaviour of [bkstat -g](mk:@MSITStore:kcmlrefman.chm::/bkstat.htm).

The column headings in KCML Partition table are links which can be used to alter the order in which the table is displayed. The default order is by partition number.\
View an example [partition table](examples/partitions.htm).

The entries in the first column, partition number, are links to display more detailed information on that partition.\
See example [partition information](examples/partinfo.htm).\
The resulting page can also be used to send signals to the KCML process using the following options.

| Option | Purpose |
|----|----|
| Clear | Clears a dead KCML partition |
| Alert | Sends a [\$ALERT](mk:@MSITStore:kcmlrefman.chm::/$ALERT.htm) to the process. |
| Screen | Forces the process to generate a screen dump file provided the process is attached to a terminal. See [\$ALERT SCREEN](mk:@MSITStore:kcmlrefman.chm::/$ALERT_SCREEN.htm) for more information. |
| Panic | Causes the target process to generate a [PANIC](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm) file. The process continues to run. |
| Panic+ | Causes the target process to generate a [PANIC](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm) file and to terminate. |
| Broadcast | Send the *Broadcast* signal to the partition. If the terminal is using **KClient** or then a dialog box displaying the current value of [\$MSG]($MSG.htm) is displayed. This is useful alternative to the Unix *wall* command |
| Terminate | Requests the target process to terminate gracefully as if executing a [\$END](mk:@MSITStore:kcmlrefman.chm::/$END.htm) at the point it next requires input from the client. If already waiting on a form event or on keyboard input it will terminate immediately. If executing a transaction it will note the request and terminate when it next reads the keyboard which ought to be outside the transaction. |
| Halt | Force the program to [halt](mk:@MSITStore:kcmlrefman.chm::/TextTermHalt.htm) and enter the debugger. This is only possible if programming is enabled and the process is attached to a terminal otherwise it will be ignored. |
| Reset | Force the program to [reset](mk:@MSITStore:kcmlrefman.chm::/TextTermHalt.htm) and enter the debugger in the console window. This is only possible if programming is enabled and the process is attached to a terminal otherwise it will be ignored. |
| Dump | Unix only. This causes the process to terminate immediately producing a core dump file. It may interrupt a transaction. |
| Murder | NT only. This causes the process to terminate immediately producing an internal stack trace using the *murder* utility program. It may interrupt a transaction. |
| Kill | This also causes the process to terminate immediately but without a core file. It may interrupt a transaction and should only be used if *Terminate* was ineffective. |
| Refresh | Redraws the page. |

\
When signalling a KCML processes with the [Panic](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm), [Panic+](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm) or the [Screen](mk:@MSITStore:kcmlrefman.chm::/$ALERT_SCREEN.htm) options it is advisable that the [current service](currentsrv.htm) should be the same service that the KCML process is running. This is so that environment variables, such as [PANICDIR](EnvVars.htm#PANICDIR), [SCREENDIR](EnvVars.htm#SCREENDIR) and [SYSTEMID](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID), have the correct values. After a [Panic](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm) or [Panic+](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm) signal has been sent to a partition the WebServer will list any panic files, in the [Panic directory](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#PANICDIR), the KCML partition has produced. This [table](dirlist.htm) lists the newest panic files first. Selecting the filename will display the panic file.\
If a [Screen](mk:@MSITStore:kcmlrefman.chm::/$ALERT_SCREEN.htm) signal has been sent to a KCML partition, the WebServer will display the resulting screen dump from the [Screen dump](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SCREENDIR) directory. Note that this option only applies to text-mode applications.

##### See Also:

[Connection Manager](connmgr.htm), [Connecting to a Service](connserv.htm), [Kerridge System Configuration](systemconf.htm), [bkstat](mk:@MSITStore:kcmlrefman.chm::/bkstat.htm)
