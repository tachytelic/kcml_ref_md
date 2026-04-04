bkstat (UNIX)

General Form:\
\
bkstat \[-agkrsCTSPDBF\] \[-c *part*\] \[-p *pid* \] \[-u \[*sem_id*\]\] \[-t *term_no*\] \[-P *part*\]\

------------------------------------------------------------------------

The *bkstat* utility reports on the status of KCML partitions and gives some system information about the KCML processes. The meaning of the information in a *bkstat* listing is shown in [table 1](#table1).

Each page contains typically up to 16 partitions. At the bottom of the screen is a menu bar. To see more partitions or to refresh the screen if there are less than a screenfull select *Next* with the space bar or by pressing the letter \`N' and press RETURN.

To leave the utility position the reverse video block at the *Quit* option with the space-bar or by pressing the letter \`Q'. Then press RETURN.

To see more detail on one particular partition choose the *Detail* option. This allows the cursor to be aligned with one particular partition and when RETURN is pressed a *ps -l* for that process is displayed at the bottom of the screen. See ps(1) in your UNIX documentation for more details.

If any partition is not in use, then the PID field for that partition will be highlighted. These entries may be cleared with the *Clear* option on the menu which allows the cursor to select the partition to be cleared. Examples of unused partitions are KCML processes that be been abnormally terminated, pehaps due to a 'kill -9', or a memory mapped file global that is not mapped in by another partition. Below is an example of a *bkstat* listing:

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/bkstat.gif" data-border="1" alt="Screen dump of bkstat -g" />

</div>

The parameters available with the *bkstat* utility are as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Switch</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>-a</td>
<td>Display alternate page (see <a href="#table2">table 2</a>)</td>
</tr>
<tr>
<td>-c <em>part</em></td>
<td>Clear the entry for the specified usused partition.</td>
</tr>
<tr>
<td>-C</td>
<td>Clear entries for all unused partitions.</td>
</tr>
<tr>
<td>-D <em>part</em></td>
<td>Display process information for the specified partition</td>
</tr>
<tr>
<td>-g</td>
<td>If specified, information for all partitions on the machine is displayed irrespective of <em>TERMFILE</em> use. Normally <em>bkstat</em> only shows those partitions whose owners share the same <em>TERMFILE</em>.</td>
</tr>
<tr>
<td>-k</td>
<td>If specified, <em>bkstat</em> returns the shared memory partition identifier. This information can also be obtained with the UNIX <em>ipcs</em> command. The partition can be removed with the <em>ipcrm</em> command, both the shared memory and the semaphore must be removed.</td>
</tr>
<tr>
<td>-p <em>pid</em></td>
<td>If specified, <em>bkstat</em> displays all the normal information for the specified process only.</td>
</tr>
<tr>
<td>-P <em>part</em></td>
<td>If specified, <em>bkstat</em> displays all the normal information for the specified partition only.</td>
</tr>
<tr>
<td>-M</td>
<td>List all the partitions together with the memory used for data.</td>
</tr>
<tr>
<td>-s</td>
<td>Allows access to the <em>Signal</em> option on the <em>bkstat</em> ring menu. Options in the signal menu are shown in <a href="#table3">table 3</a> below. The option to <em>Terminate</em> a process should always be used in preference to the option to <em>Kill</em>. Killing processes can be dangerous as not all locks may be removed, and/or shared memory space cleared. <strong>The <em>Kill</em> option should only be used as a last resort.</strong></td>
</tr>
<tr>
<td>-S</td>
<td>Displays the status information about each <a href="$PSTAT.htm">$PSTAT</a> semaphore. Semaphores that are shown as LOCKED are locked with the @LOCK statement. If the process executing an <a href="@LOCK.htm">@LOCK</a> dies then it is possible that the global will remain locked. Use <em>bkstat -u</em> to unlock the global.</td>
</tr>
<tr>
<td>-t <em>term_no</em></td>
<td>If specified, display the information for the specified terminal. If the terminal is not in use then nothing is returned.</td>
</tr>
<tr>
<td>-T</td>
<td>If specified, displays the $PSTAT, terminal id number. This is a unique number taken from the UNIX inode number of the <em>TERMFILE</em> file (see the <a href="TutorialConfig.htm">KCML Environment configuration</a> section). This number is used to attach KCML processes to Global partitions.</td>
</tr>
<tr>
<td>-u [semid]</td>
<td>Unlock <a href="$PSTAT.htm">$PSTAT</a> semaphore previously locked with the <a href="@LOCK.htm">@LOCK</a> statement, see the -S option.</td>
</tr>
<tr>
<td>-w</td>
<td>Wide display page. Shows all attributes of a partition. Note that this is only suitable for wide screens of 128 characters or more.</td>
</tr>
<tr>
<td>-r</td>
<td>Displays the KPrint Licence Table that is managed by the <a href="kplicserver.htm">Remote Licence Daemon</a>.</td>
</tr>
<tr>
<td>-x <em>size</em></td>
<td>Set the size of the <a href="$PSTAT.htm">$PSTAT</a> partition array to allow <strong>size</strong> partitions. See <a href="#config_pstat">Configuring $PSTAT</a></td>
</tr>
<tr>
<td>-y <em>size</em></td>
<td>Set the size of the <a href="$PSTAT.htm">$PSTAT</a> terminal array to allow <strong>size</strong> terminals. See <a href="#config_pstat">Configuring $PSTAT</a></td>
</tr>
<tr>
<td>-R <em>size</em></td>
<td>Set the size of the <a href="kplicserver.htm">KPrint Licence</a> table to allow <strong>size</strong> KPrint servers. See <a href="#config_pstat">Configuring $PSTAT</a></td>
</tr>
<tr>
<td>-B <em>part_no</em></td>
<td>Sends the <em>Broadcast</em> signal a KCML partition that is using the current TERMFILE.<br />
<em>part_no</em> = 0 : Send broadcast to all partitions<br />
<em>part_no</em> &gt; 0 : Send broadcast to partition <em>part_no</em><br />
<em>part_no</em> &lt; 0 : Send broadcast to all partitions execpt <em>part_no</em><br />
To send the broadcast signal to every KCML process in the partition table add <strong>-g</strong> flag.</td>
</tr>
<tr>
<td>-K <em>part_no</em>:<em>sig</em>[:<em>action</em>]</td>
<td>General purpose signalling flag. This will send the signal <em>sig</em> to the specified partition. The optional <em>action</em> field is used with the SIGUSR2 signal. It has the following values:<br />
<strong>Snoop:</strong> causes the KCML process to genereate a screen dump file. See <a href="$ALERT_SCREEN.htm">$ALERT SCREEN</a>.<br />
<strong>Panic Continue:</strong> causes the KCML process to genereate a PANIC file, program execution continues. See <a href="PANIC.htm">PANIC</a>.<br />
<strong>Panic+:</strong> causes the KCML process to genereate a screen dump file, the KCML process then aborts. See <a href="PANIC.htm">PANIC</a>.<br />
<strong>Broadcast:</strong> causes the KCML process to display the current value of <a href="$MSG.htm">$MSG</a> on the terminal.<br />
If <em>part_no</em> is zero then bkstat will attempt to signal all partitions.</td>
</tr>
<tr>
<td>-F</td>
<td>Lists all foreground KCML partitions that are attached to a terminal. When executed by user <strong>root</strong> bkstat will display all foreground partitions for all possible values of <a href="EnvVars.htm#SYSTEMID">$SYSTEMID</a>. This is a replacement for the Unix <em>who</em> and <em>finger</em> commands which would not show KCML sessions invoked by the <a href="mk:@MSITStore:kwebserv.chm::/connmgr.htm">Connection Manager</a></td>
</tr>
</tbody>
</table>

The *bkstat* utility uses the KCML TERMINFO database and the value of the environment variable [KTERM](EnvVars.htm#KTERM) to discover how to control the screen. It supports dynamic screen sizing for screen depth. Output can also be redirected as in

bkstat -M \>mem.txt

<table id="table1">
<caption>Table 1, Details contained within a <em>bkstat</em> listing</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Column</th>
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>PART</td>
<td>Partition number.</td>
</tr>
<tr>
<td>2</td>
<td>TERM</td>
<td>The terminal number.</td>
</tr>
<tr>
<td>3</td>
<td>USERMSG</td>
<td>Any <a href="$PSTAT.htm">$PSTAT</a> message set by program.</td>
</tr>
<tr>
<td>4</td>
<td>USERID</td>
<td>The name of the user running KCML.</td>
</tr>
<tr>
<td>5</td>
<td>@NAME</td>
<td><a href="DEFFN_@PART.htm">DEFFN @PART</a> name if global.</td>
</tr>
<tr>
<td>6</td>
<td>VER</td>
<td><strong>KCML</strong> version number, 30 for versions &lt;3.10.00, 31 for versions &gt;3.00.00 and &lt;3.20.00, etc.</td>
</tr>
<tr>
<td>7</td>
<td>ERR</td>
<td>The number of the last error recorded in the partition, including the minor error code.</td>
</tr>
<tr>
<td>8</td>
<td>DEV</td>
<td>Device number or event code if blocked.</td>
</tr>
<tr>
<td>9</td>
<td>PID</td>
<td>Process id number.</td>
</tr>
<tr>
<td>10</td>
<td>GLOB</td>
<td>Current global partition selected.</td>
</tr>
<tr>
<td>11</td>
<td>TEXT</td>
<td>Partition number of text being executed.</td>
</tr>
<tr>
<td>12</td>
<td>DATA</td>
<td>Partition number of <a href="RESTORE.htm">RESTORE</a> pointer.</td>
</tr>
<tr>
<td>13</td>
<td>S</td>
<td>Terminal status (A/D/W).</td>
</tr>
<tr>
<td>14</td>
<td>P</td>
<td>Programmability - `P' if the partition is programmable.</td>
</tr>
<tr>
<td>15</td>
<td>T</td>
<td>On simple systems with only one TERMFILE this column should be '0' for all partitions. On complex sites with more than one TERMFILE, bkstat -g shows all partitions, grouping them by TERMFILE, '0', '1'</td>
</tr>
<tr>
<td>16</td>
<td>F</td>
<td>Terminal type. Possible values, in bold, are:<br />
<em><strong>F</strong></em>orms (KClient)<br />
<em><strong>T</strong></em>ext (WDW)<br />
<em><strong>B</strong></em>atch program, executed with the <a href="kcml.htm">-p</a> switch<br />
<em><strong>S</strong></em>upport<br />
<em><strong>N</strong></em>one, eg vt100 terminal<br />
For memory mapped partition files the value is <em><strong>G</strong></em></td>
</tr>
</tbody>
</table>

| Column | Heading | Description |
|----|----|----|
| 1 | PART | Partition number |
| 2 | TERM | The terminal number |
| 3 | USERID | Logged on userid |
| 4 | DEV | Device number or event code if blocked see [\$PSTAT]($PSTAT.htm) for a list |
| 5 | PID | The process ID |
| 6 | CHILD | Partition number of [\$RELEASE]($RELEASE.htm)d child |
| 7 | CHAIN |  |
| 8 | Mem | The size of the dynamic data segment in 1024 byte pages (see [LIST SPACE](LIST_SPACE.htm)) |
| 9 | LastAcc | Time since last access (key press, mouse click etc). |
| 10 | IPADDR | IP address or computer name of client |
| 11 | SERIAL | WDW serial number |

Table 2, Details contained within a *bkstat* alternate listing {#table2}

| Option | Purpose |
|----|----|
| Halt | Force the program to [halt](TextTermHalt.htm) and enter the debugger. This is only possible if programming is enabled and the process is attached to a terminal otherwise it will be ignored. |
| Reset | Force the program to [reset](TextTermHalt.htm) and enter the debugger in the console window. This is only possible if programming is enabled and the process is attached to a terminal otherwise it will be ignored. |
| Alert | Sends a [\$ALERT]($ALERT.htm) to the process. |
| Screen | Forces the process to generate a screen dump file provided the process is attached to a terminal. See [\$ALERT SCREEN]($ALERT_SCREEN.htm) for more information. |
| Panic | Causes the target process to generate a [PANIC](PANIC.htm) file. The process continues to run. |
| Panic+ | Causes the target process to generate a [PANIC](PANIC.htm) file and to terminate. |
| Broadcast | Send the *Broadcast* signal to the partition. If the terminal is using **KClient** or **WDW** then a dialog box displaying the current value of [\$MSG]($MSG.htm) is displayed. This is useful alternative to the Unix *wall* command |
| Terminate | Requests the target process to terminate gracefully as if executing a [\$END]($END.htm) at the point it next requires input from the client. If already waiting on a form event or on keyboard input it will terminate immediately. If executing a transaction it will note the request and terminate when it next reads the keyboard which ought to be outside the transaction. |
| Dump | This causes the process to terminate immediately producing a core dump file. It may interrupt a transaction. |
| Kill | This also causes the process to terminate immediately but without a core file. It may interrupt a transaction and should only be used if *Terminate* was ineffective. |

Table 3, Options available on the signal menu {#table3}

<span id="config_pstat"></span>

##### Configuring \$PSTAT using bkstat

The KCML partition, terminal and [KPrint Licence](kplicserver.htm) tables all have the following fixed sizes.

| Table           | Default Size | Command flag   |
|-----------------|--------------|----------------|
| Partition       | 1024         | -x *max_parts* |
| Terminal        | 1024         | -y *max_terms* |
| KPrint Licences | 256          | -R *max_lic*   |

The *max_parts* & *max_terms* values for the -x & -y flags must have the same value.

These tables are created when the first KCML product is executed after system start-up. Once these tables have been created their sized cannot be changed. If alternative sizes are required then the first KCML product to start should be the bkstat utility with the appropriate command-line flags. This can be done in a *start-up script*. These are command shell scripts which are executed when the server boots up. A typical example of this is the start-up script for the [Remote Licence Daemon](kplicserver.htm). The install script for the [Remote Licence Daemon](kplicserver.htm) ensures that either bkstat or the Licence Daemon itself is the first KCML product to start by deriving the file name of the start-up from that of the start-up script for the internet services daemon, *inetd*. The start-up script for the [Remote Licence Daemon](kplicserver.htm) is executed just before *inetd* is started ensuring that no-one can log-in, and start a KCML process, before bkstat has created the correctly sized [\$PSTAT]($PSTAT.htm) tables.\
For example:

\# Add /usr/lib/kcml to PATH PATH=/sbin:/usr/sbin:/usr/bin:/etc:/usr/ccs/bin:/usr/lib/kcml export PATH \# Use this script to set up PSTAT and to start KCML deamons \# Change size of partition, terminal and KPrint licence tables /usr/lib/kcml/bkstat -x 4096 -y 4096 -R 1024 \# Start the KPrint licence server /usr/lib/kcml/kplicserver & would allow a maximum of 4096 KCML partitions to run from a maximum of 4096 terminals. The [Remote Licence Daemon](kplicserver.htm) would also be able to manage licences for 1024 **KPrint** servers, provided the licence file has enough queues.
