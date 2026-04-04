\$MACHINE

------------------------------------------------------------------------

<div class="Generalform">

General Form:

- \$MACHINE

</div>

------------------------------------------------------------------------

The \$MACHINE system variable contains a value based on the hardware and system software currently being used. \$MACHINE may legally be used anywhere an alpha variable would be used except on the left hand side of an assignment statement. See below for a list of the \$MACHINE byte settings.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Byte(s)</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr id="BYTE1">
<td>1</td>
<td>Operating system type,<br />
U for UNIX,<br />
N for MS Windows,</td>
</tr>
<tr id="BYTE2">
<td>2</td>
<td>Bit field for the terminal capabilities (see also byte 53):<br />
HEX(01)     Windows drawn with <a href="WINDOW.htm">WINDOW OPEN</a> are done by the terminal.<br />
HEX(04)     Screen saving (HEX(0000)) is done locally<br />
HEX(08)     Support <a href="$DECLARE.htm">$DECLARE</a><br />
HEX(10)     Support for 32 bit <a href="$DECLARE.htm">$DECLARE</a><br />
HEX(20)     Client uses an 8 bit character set<br />
HEX(40)     Client supports KCML forms<br />
HEX(80)     Client running on Windows CE</td>
</tr>
<tr id="BYTE3">
<td>3</td>
<td>Monitor type,<br />
" " (Blank) dumb terminal, "W" Kclient, DW or WDW</td>
</tr>
<tr id="BYTE4">
<td>4</td>
<td>Text mode box graphics enabled:<br />
"G" enabled or " " no graphics available</td>
</tr>
<tr id="BYTE5">
<td>5</td>
<td>Not used, HEX(00)</td>
</tr>
<tr id="BYTE6">
<td>6</td>
<td>Current number of users at start up, not counting the current process.</td>
</tr>
<tr id="BYTE7">
<td>7</td>
<td>KCML version, "I" for the interpretive version, "P" for the non-interpretive run time only version.</td>
</tr>
<tr id="BYTE8">
<td>8</td>
<td>Screen width in binary, taken from the Columns clause in terminals TERMINFO definition, HEX(50) by default</td>
</tr>
<tr id="BYTE9">
<td>9</td>
<td>Terminal type, taken from the TermCode clause in the terminals TERMINFO definition.</td>
</tr>
<tr id="BYTE10">
<td>10</td>
<td>Math coprocessor present, always HEX(01) on UNIX versions. On DOS versions HEX(01) if the coprocessor is present, otherwise HEX(00).</td>
</tr>
<tr id="BYTE11">
<td>11</td>
<td>Not used, always HEX(02)</td>
</tr>
<tr id="BYTE12">
<td>12</td>
<td>Number of colors available,<br />
HEX(02) monochrome screen,<br />
HEX(10) color PC or Color Magna</td>
</tr>
<tr id="BYTE13">
<td>13</td>
<td>Maximum number of users allowed, if greater than 255 then this field is set to HEX(FF).</td>
</tr>
<tr id="BYTE14">
<td>14-15</td>
<td>Not used, HEX(00)</td>
</tr>
<tr id="BYTE16">
<td>16</td>
<td>Maximum number of device table entries available, always 255 HEX(FF))</td>
</tr>
<tr id="BYTE17">
<td>17</td>
<td>Number of device table entries in use, in binary.</td>
</tr>
<tr id="BYTE18">
<td>18</td>
<td>Indicates whether or not the current partition in use was started in a background partition.<br />
HEX(00) if started in foreground<br />
HEX(01) if started in background</td>
</tr>
<tr id="BYTE19">
<td>19</td>
<td>Keyboard redirection and logging status.<br />
HEX(00) normal keyboard input</td>
</tr>
<tr id="BYTE20">
<td>20-22</td>
<td>Not used, HEX(00)</td>
</tr>
<tr id="BYTE23">
<td>23</td>
<td>Last mouse row position, set to HEX(FF) if no mouse found.</td>
</tr>
<tr id="BYTE24">
<td>24</td>
<td>Last mouse column position, set to HEX(FF) if no mouse found.</td>
</tr>
<tr id="BYTE25">
<td>25</td>
<td>Most significant bit of the current user count</td>
</tr>
<tr id="BYTE26">
<td>26</td>
<td>Least significant bit of the current user count</td>
</tr>
<tr id="BYTE27">
<td>27</td>
<td>Most significant bit of the maximum users allowed.</td>
</tr>
<tr id="BYTE28">
<td>28</td>
<td>Least significant bit of the maximum users allowed.</td>
</tr>
<tr id="BYTE29">
<td>29</td>
<td>The keyboard shift state during a mouse event:<br />
HEX(00)     No mouse present<br />
HEX(01)     Mouse present<br />
HEX(02)     Shift down<br />
HEX(04)     Ctrl down<br />
HEX(08)     Alt down<br />
HEX(10)     Drag in progress<br />
HEX(40)     Non-client area drag event</td>
</tr>
<tr id="BYTE30">
<td>30-32</td>
<td>Not used</td>
</tr>
<tr id="BYTE33">
<td>33</td>
<td>Terminal <a href="LanguageCodes.htm">language code</a> as deduced by KClient from NT/Win9x</td>
</tr>
<tr id="BYTE34">
<td>34-35</td>
<td>Maximum value of <a href="_TERM.htm">#TERM</a></td>
</tr>
<tr id="BYTE36">
<td>36-37</td>
<td>Maximum value of <a href="_PART.htm">#PART</a></td>
</tr>
<tr id="BYTE38">
<td>38-39</td>
<td>Number of kclient users at startup</td>
</tr>
<tr id="BYTE40">
<td>40-41</td>
<td>Maximum kclient users allowed by license</td>
</tr>
<tr id="BYTE42">
<td>42</td>
<td>Type of license<br />
HEX(01) Client server<br />
HEX(02) Peer-to-Peer WKCML LAN with license server<br />
HEX(04) Single user</td>
</tr>
<tr id="BYTE43">
<td>43-44</td>
<td>Local <a href="timezone.htm">timezone</a> offset from GMT in minutes.</td>
</tr>
<tr id="BYTE45">
<td>45-48</td>
<td>Server IP address. Zero if direct connect (WKCML).</td>
</tr>
<tr id="BYTE49">
<td>49-52</td>
<td>Client IP address. Zero if direct connect (WKCML).</td>
</tr>
<tr id="BYTE53">
<td>53</td>
<td>Second bitfield for terminal capabilities (see also byte 2):<br />
HEX(01) Client is running on a Netier NT terminal<br />
HEX(02) Client is running on a Citrix or WTS thin client<br />
HEX(04) Client is connected directly (i.e. client and server are running as one process and not in client server mode). This is the mode in which the WKCML product always runs.<br />
HEX(08) Client is a Unicode version.<br />
HEX(10) Reserved.<br />
HEX(20) Client is running on a Wyse NT terminal.<br />
HEX(80) Reserved.<br />
</td>
</tr>
<tr id="BYTE54">
<td>54</td>
<td>A bit field indicating optional features set during connection or compiled into KCML<br />
HEX(01) Can access files up to 4 Terabytes else up to 2 Gigabytes<br />
HEX(02) Pseudo-tty support is enabled for <a href="SHELL.htm">SHELL</a>, always true for telnet connections<br />
HEX(04) Client was authenticated and $LOGNAME is reliable<br />
HEX(08) A service has been selected and an appropriate environment set up. $SERVICE is reliable. This could have been done by either the connection manager or KCML executing CALL KI_CONNECT.<br />
HEX(10) A process global started as kcml -g and using shared memory.<br />
HEX(20) The server supports server-side $DECLARE<br />
HEX(40) Non-telnetd connection. Either connect to inetd using <a href="kcml.htm#switch">kcml -l</a> or started via the <a href="mk:@MSITStore:kwebserv.chm::/connmgr.htm">Connection Manager</a><br />
HEX(80) KCML started via the <a href="mk:@MSITStore:kwebserv.chm::/connmgr.htm">Connection Manager</a> only.<br />
</td>
</tr>
<tr id="BYTE55">
<td>55-56</td>
<td>A two byte field holding the number of distinct users logged on when KCML started. This is the count used by KCML to compare against maximum in the license file.</td>
</tr>
<tr id="BYTE57">
<td>57</td>
<td>$COMPLIANCE language support. 1 means the code must comply with stricter rules, which currently are that all DEFSUB must be matched by an ENDSUB and all variables must be dimmed. See <a href="$COMPLIANCE.htm">$COMPLIANCE</a>.</td>
</tr>
<tr id="BYTE58">
<td>58</td>
<td>Bitfield for server mode:<br />
HEX(01) KCML is running as a SOAP server<br />
HEX(02) KCML will render forms as XML<br />
HEX(04) KCML is a persistent application or SOAP server<br />
</td>
</tr>
<tr id="BYTE59">
<td>59</td>
<td>Bitfield indicating the encoding used by the server when interpteting data to be printed or sent to the client.<br />
HEX(00) Server using the locale of the client (the default unless the environment variable USING_UTF8 is set).<br />
HEX(01) Server expects all data to be UTF-8 encoded.<br />
</td>
</tr>
<tr id="BYTE60">
<td>60</td>
<td>Bitfield indicating the development functionallity permitted by the license file.<br />
HEX(01) Reserved<br />
HEX(02) Programmable - code can be viewed, variables inspected, read only mode.<br />
HEX(04) Limited debugging - program flow can be changed, variables modified, read/write mode.<br />
HEX(08) Full Workbench support for writing/modifying programs and debugging.<br />
</td>
</tr>
</tbody>
</table>

The defined size of \$MACHINE is currently 64 bytes.

\$MACHINE as a record

KCML defines a [KCML_MACHINE](tmp/kintfld.htm#KCML_MACHINE) built in [DEFRECORD](DEFRECORD.htm) that can be used to access the fields in \$MACHINE e.g.


    maxpart = FLD($MACHINE.MACHINE_MaxPart)

Syntax examples:

Os\$ = FLD(\$MACHINE.OS_Type\$)\
IF (STR(\$MACHINE,18,1) == HEX(00))

See also:

[Internal structures](tmp/kintfld.htm)
