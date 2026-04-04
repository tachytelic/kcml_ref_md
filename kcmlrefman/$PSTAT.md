\$PSTAT

------------------------------------------------------------------------

<div class="Generalform">

General Forms:\

1.  \$PSTAT = alpha_expression
2.  alpha_receiver = \$PSTAT \[(numeric_expression)\]

</div>

------------------------------------------------------------------------

The \$PSTAT statement is used to return status information for the specified partition. The first 8 bytes of \$PSTAT may be changed with the first form.

Specifying no numeric expression for the second form of \$PSTAT is the same as entering STR(\$PSTAT(#PART),,8).

<table>
<caption>Bytes used by $PSTAT</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="8%">Byte</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>1-8</td>
<td>User specified status as set by the <a href="$PSTAT.htm">$PSTAT</a> statement.</td>
</tr>
<tr>
<td>9</td>
<td>Always 'K' for KCML.</td>
</tr>
<tr>
<td>10</td>
<td>KCML release, HEX(30) for release 3.0, HEX(31) for release 3.1, HEX(32) for release 3.2 etc.</td>
</tr>
<tr>
<td>11</td>
<td>Not used, always HEX(30).</td>
</tr>
<tr>
<td>12-13</td>
<td>Partition size, current value of the <a href="EnvVars.htm#SPACEK">SPACEK</a> environment variable or HEX(9999) if not set.</td>
</tr>
<tr>
<td>14</td>
<td>Programmability, 'P' if programmable (the default), ' ' if <a href="EnvVars.htm#NOPROG">NOPROG</a> environment variable is set.</td>
</tr>
<tr>
<td>15</td>
<td>BCD terminal number, Always BCD HEX(99) for terminal 99 and above. See bytes 41-42 for true terminal number.</td>
</tr>
<tr>
<td>16</td>
<td>Terminal status `A' if attached, 'D' if detached, 'W' if waiting to attach, 'F' if a suspended <a href="$RELEASE.htm">$RELEASE</a> parent.</td>
</tr>
<tr>
<td>17-24</td>
<td>Global name, all HEX(00) if no <a href="DEFFN_@PART.htm">DEFFN @PART</a> is executed.</td>
</tr>
<tr>
<td>25</td>
<td><a href="ERR.htm">ERR</a> function value, numeric code from last error whether trapped or not, else HEX(00). The subscript error code is stored in byte 49.</td>
</tr>
<tr>
<td>26</td>
<td>BCD text partition number. The partition number of the text currently being executed. Always BCD, HEX(99) for partition 99 and above. See bytes 43-44 for true text partition. For KCML 6.0+ this is always set to #PART.</td>
</tr>
<tr>
<td>27</td>
<td>BCD global partition number of the text currently selected in a <a href="SELECT_@PART.htm">SELECT @PART</a>. Always BCD, HEX(99) for partition 99 and above. See bytes 45-46 for the true global partition number.</td>
</tr>
<tr>
<td>28</td>
<td>BCD DATA partition number. Partition number containing the current <a href="RESTORE.htm">RESTORE</a> pointer. This will only be different from <a href="_PART.htm">#PART</a> if a <a href="RESTORE.htm">RESTORE</a> was executed in global text. Always BCD, HEX(99) for partition 99 and above. See bytes 47-48 for the true DATA partition number.</td>
</tr>
<tr>
<td>29</td>
<td>Device awaited:<br />
HEX(00) while executing.<br />
HEX(01) if awaiting a keystroke.<br />
HEX(FF) if blocked on <a href="$OPEN.htm">$OPEN</a> of a native file.<br />
HEX(FD) if waiting on a <a href="$IF.htm">$IF</a>.<br />
HEX(FC) if executing a <a href="SHELL.htm">SHELL</a> statement.<br />
HEX(FB) if executing a <a href="$BREAK.htm">$BREAK</a> statement.<br />
HEX(FA) if waiting for a request when acting as a <a href="soapserver.htm">SOAP server</a>.<br />
Any other value should be interpreted as a device address from <a href="$DEVICE.htm">$DEVICE</a></td>
</tr>
<tr>
<td>30-36</td>
<td>User's login name. Truncated if longer than 7 bytes. Full usernames are displayed by the <a href="mk:@MSITStore:kwebserv.chm::/kcmlproc.htm">WebServer</a> .</td>
</tr>
<tr>
<td>37-40</td>
<td>Process id, four byte binary.</td>
</tr>
<tr>
<td>41-42</td>
<td><a href="_TERM.htm">#TERM</a> in binary (supersedes byte 15).</td>
</tr>
<tr>
<td>43-44</td>
<td>Executing partition in binary (supersedes byte 26). For KCML 6.0+ this is always set to #PART.</td>
</tr>
<tr>
<td>45-46</td>
<td>Selected global partition in binary (supersedes byte 27).</td>
</tr>
<tr>
<td>47-48</td>
<td>DATA partition in binary (supersedes byte 28).</td>
</tr>
<tr>
<td>49</td>
<td>The subscript code for the last error (See byte 25.)</td>
</tr>
<tr>
<td>50-68</td>
<td>Reserved</td>
</tr>
<tr>
<td>69-72</td>
<td>IP address of client, if supplied by client program</td>
</tr>
<tr>
<td>73-74</td>
<td>dynamic heap size in kb</td>
</tr>
<tr>
<td>75</td>
<td>client category,<br />
'T' licensed for text only<br />
'F' licenced for forms<br />
'N' not applicable<br />
'G' memory mapped global pseudo partition<br />
'B' batch program, executed with the <a href="kcml.htm">-p</a> switch</td>
</tr>
<tr>
<td>76-91</td>
<td>Client computer name, if supplied by client program (null terminated string)</td>
</tr>
<tr>
<td>92</td>
<td>Reserved</td>
</tr>
<tr>
<td>93-96</td>
<td><a href="$TIME.htm">$TIME</a> format timestamp of last keyboard activity or, for a SOAP server, the last request.</td>
</tr>
<tr>
<td>97-104</td>
<td>Reserved</td>
</tr>
<tr>
<td>105-110</td>
<td>Client PC's MAC/Ethernet card address, 6-byte binary value</td>
</tr>
<tr>
<td>111-128</td>
<td>Reserved</td>
</tr>
</tbody>
</table>

\$PSTAT as a record

KCML defines a [KCML_PSTAT](tmp/kintfld.htm#KCML_PSTAT) built in [DEFRECORD](DEFRECORD.htm) that can be used to access the fields in \$PSTAT e.g.


    pid = FLD($PSTAT.PSTAT_ProcessId)

Compatibility notes

The extra fields from byte 50 onwards were introduced with KCML 6.0. Because of support for memory mapped globals and for libraries KCML 6.0+ no longer tracks the executing partition in bytes 43 and 44. If a SELECT@PART for a process global is in effect then bytes 45-46 will be set to the global's partition number but if the SELECT @PART referred to a memory mapped global then this field will be set to \#PART. Similarly the DATA partition will only be set for a process global. These fields should be considered obsolete and should not be used.

Syntax examples:

\$PSTAT = user_message\$\
partition\$ = \$PSTAT\
pt\$ = STR(\$PSTAT,,3)

See also:

[SYSTEMID](EnvVars.htm#SYSTEMID), [bkstat](bkstat.htm), [Web Administration Tool](mk:@MSITStore:kwebserv.chm::/adminfns.htm), [Internal structures](tmp/kintfld.htm)
