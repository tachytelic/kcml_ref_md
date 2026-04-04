# <span id="optionspage"></span> Options page

The second property page defines some less important options

<div id="ClickDiv">

<u>Click here to view an example dialog</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/wizoptions.gif" data-border="0" alt="Options property sheet" />

</div>

The options on this page are described in the following table.

<span id="broker"></span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Option</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>Answerback</td>
<td>This will be disabled for direct connections. When Kclient starts up in client server mode it is initially in a vt100 terminal emulation mode until such time as it is able to get authenticated and start the server process which will then switch the client into its proper KCML mode. During logon the Unix .profile may well interrogate the client with an ASCII ENQ character to get the answerback as a simple form of security. This field allows you to define the string to be sent in response to this query. Some systems may use this to set terminal numbers and the form of the string will be mandated by your system administrator who should be consulted. This has no effect when connecting via the <a href="mk:@MSITStore:kwebserv.chm::/connmgr.htm">Connection Manager</a>.</td>
</tr>
<tr>
<td>Computer name</td>
<td>This is the string that the client will send to the server so that it can identify the client PC. It is defaulted to the name used by Microsoft Windows Networking (the netbios name).</td>
</tr>
<tr>
<td>Service Port</td>
<td>If the connection has specified a service in the <em>Connect to service</em> edit box, then KClient will use a default port number of 790. You can specify an alternative port number in this field if the <a href="mk:@MSITStore:kwebserv.chm::/connmgr.htm">Connection Manager</a> is listening on a different port.</td>
</tr>
<tr>
<td>Connect Directly</td>
<td>KClient will connect directly to the server. This is the default mode of connection.</td>
</tr>
<tr>
<td>Connect via a <a href="mk:@MSITStore:kcmlrefman.chm::/connectionbroker.htm">connection broker</a></td>
<td>KClient will connect via a <a href="mk:@MSITStore:kcmlrefman.chm::/connectionbroker.htm">connection broker</a> which will maintain the connection over an unreliable link. This option enables the following fields.</td>
</tr>
<tr>
<td></td>
<td><table>
<tbody>
<tr>
<td>This connection uses a dial-up/ISDN line</td>
<td>Set this option if the line incurs billing for time connected. Pings from the connection broker will keep the line up if this option is not set.</td>
</tr>
<tr>
<td>Broker</td>
<td>The name of the connection broker through which to connect.</td>
</tr>
<tr>
<td>Broker Port</td>
<td>The port on which the broker listens. If this field is blank the default port is 14600</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Connect via a proxy server</td>
<td>KClient will connect to the server via a proxy server. This option enables the following fields</td>
</tr>
<tr>
<td></td>
<td><table>
<tbody>
<tr>
<td>Proxy Server</td>
<td>The name of a proxy server through which to connect to the KCML server.</td>
</tr>
<tr>
<td>Proxy Port</td>
<td>The port on which the proxy server listens. If this field is blank the default port is 8080.</td>
</tr>
<tr>
<td>Proxy User</td>
<td>Username required to authenticate against the proxy server. Normally this will be the same username required to log into KCML and may be left blank</td>
</tr>
<tr>
<td>Proxy Password</td>
<td>If a proxy user must be specified the corresponding password may be entered here. If left blank KClient will display a login prompt when connecting if the proxy user and password are different to the KCML ones.</td>
</tr>
</tbody>
</table></td>
</tr>
<tr>
<td>Change icon…</td>
<td>This button allows you to choose an alternative icon to be used by this connection file. Click the button to browse a built in list of icons. External icons embedded in DLL or EXE files can also be browsed using a further Browse Icon button. ICO and BMP format files are also usable.</td>
</tr>
<tr>
<td>Dynamic screen sizing</td>
<td>Check this checkbox to allow the editor window to be resized. The default is on and generally you will want to enable this.</td>
</tr>
</tbody>
</table>
