# <span id="commandlineswitches"></span> Command line switches

Note that switch characters are case sensitive.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th width="85">Switch</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>-A <em>app</em></td>
<td>Run application <em>app</em>. This implies -d, see below. The application to be run is defined a string named <em>app</em> in the registry under the key
HKEY_LOCAL_MACHINE/SOFTWARE/Kerridge/Apps
The string value of the key <em>app</em> will be interpreted as a program. In the examples above V8profile had the value d:\rev8\profile.src</td>
</tr>
<tr>
<td>-a <em>ans</em></td>
<td>Define a VT100 answerback string. When Kclient starts up in client server mode it is initially in a vt100 terminal emulation mode until such time as it is able to get authenticated and start the server process which will then switch the client into its proper KCML mode. During logon the Unix .profile may well interrogate the client with and ascii ENQ character to get the answerback as a simple form of security. This switch allows you to define the string to be sent in response to this query.</td>
</tr>
<tr>
<td>-b</td>
<td>This will suppress the splash bitmap that the kclient issues during initialization. It will only do this if another client is already running and if it has enough information to logon to the server without input from the user.</td>
</tr>
<tr>
<td>-C <em>args</em></td>
<td>Application command line. The possibly quoted argument that follows the -C will be passed to the kcml server as found. The server program can gain access to this via the $DECLARE function defined thus:
$DECLARE 'KCMLCommandLine(RETURN STR())
and can use this string to determine how to run. This mechanism is how bookmarking is implemented.</td>
</tr>
<tr>
<td>-d</td>
<td>Direct mode with both client and server on the same machine. This requires the kserver.dll DLL to be in the same directory as the client. This is the mode that WKCML uses.</td>
</tr>
<tr>
<td>-h <em>host</em></td>
<td>Defines the host computer as either a hostname (defined by a DNS or by an entry in a hosts file) or a dotted IP address e.g. 10.0.0.10. By default kclient uses port 23 but another port may be specified by adding a comma or colon and the port number, Eg: -h myhost,45 or -h myhost:45</td>
</tr>
<tr>
<td>-i <em>file,index</em></td>
<td>Defines the icon to be used in terms of an index number in the icon resource of the file file (which may be an exe or a dll)</td>
</tr>
<tr>
<td>-L</td>
<td>Connect to an NT server without a logon process</td>
</tr>
<tr>
<td>-m</td>
<td>Client to start minimized</td>
</tr>
<tr>
<td>-N</td>
<td>Use NT LanMan authentication to automatically log into the server with the credentials used to log into the client. Not available for Unix servers. Requires NT server and both client and server to be in an NT domain.</td>
</tr>
<tr>
<td>-o <em>userid</em></td>
<td>Login with this <em>userid</em>. Do not update the stored 'last user'.</td>
</tr>
<tr>
<td>-P <em>x,y</em></td>
<td>Set position of the initial form using pixel co-ordinates based on top left corner of screen.</td>
</tr>
<tr>
<td>-q</td>
<td>Quit immediately if unable to connect. Without this switch the login dialog will remain allowing the host to be changed.</td>
</tr>
<tr>
<td>-R</td>
<td>Cache the users password in an encrypted form in the registry after a successful log in and use this password when subsequently connecting to that server under the same userid. This is only available if the user is explicitly logged into the client.</td>
</tr>
<tr>
<td>-r</td>
<td>Force a request for the userid and password despite any other prevailing setting.</td>
</tr>
<tr>
<td>-S <em>dir</em></td>
<td>Set the current working directory for a direct login. Not applicable for remote connections.</td>
</tr>
<tr>
<td>-s</td>
<td>Disable dynamic screen resizing in the KCML workbench</td>
</tr>
<tr>
<td>-T</td>
<td>Display a text window after connection thus revealing the login process.</td>
</tr>
<tr>
<td>-t</td>
<td>Display text window after login process is completed.</td>
</tr>
<tr>
<td>-u <em>userid</em></td>
<td>Login with this <em>userid</em></td>
</tr>
<tr>
<td>-V <em>Port</em></td>
<td>Specify the port to connect to. The default port is 23, as used by the Telnet service</td>
</tr>
<tr>
<td>-v <em>Service</em></td>
<td>Specify the service when connecting through the Connection Manager</td>
</tr>
<tr>
<td>-w <em>file</em></td>
<td>Load command line options from the specified file</td>
</tr>
<tr>
<td>-X <em>pwd</em></td>
<td>Supply a password to go with the userid in -u</td>
</tr>
<tr>
<td>-Y</td>
<td>Disable access to the prefences menu. Useful on Citrix managed environments.</td>
</tr>
<tr>
<td>-z</td>
<td>On KCML 6.0 systems use the original KCML 5 editor rather than the Workbench</td>
</tr>
<tr>
<td>User@Host:Port</td>
<td>Short hand for connecting as <em>'User'</em> to the server <em>'Host'</em> on port <em>'Port'</em></td>
</tr>
</tbody>
</table>

The following switches can also be used on a direct connection only as they will be passed on to KCML

| KCML switch | Purpose                              |
|-------------|--------------------------------------|
| -g          | defines a global process             |
| -p *prog*   | explicitly defines a program to load |
| -e *env*    | defines an environment variable      |
| -n          | NPL compatibility                    |
| -x *lib*    | specify dynamic library to load      |
