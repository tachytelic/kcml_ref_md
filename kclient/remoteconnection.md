# <span id="remoteconnection"></span> Remote connection (Client server)

<div id="ClickDiv">

<u>Click here to see the main property page for a typical remote connection</u>

</div>

<div id="PicDiv" style="Display:none">

<u>Click here to hide the example dialog</u>

<img src="bitmaps/RemoteConn.gif" data-border="0" width="370" height="443" alt="Remote connection property page" />

</div>

Control

Purpose

Connection Type

'Connect to remote server'

Server

Defines the host computer as either a hostname (defined by a DNS or by an entry in a hosts file) or a dotted IP address e.g. 10.0.0.10. By default kclient uses port 23 but another port may be specified by adding a comma and the required port number.\
\
The drop down list contains the host names of hosts that have been successfully connected to in the past.

Login Type

This is a listbox defining the authentication to be used. See the section on [server authentication](authenticationoptions.htm) for more details

Login

The login to be used. This may be left blank and then supplied at the connection is used. It may be disabled if NTLM authentication is specified.

Password

The password to be used. Only supply this here if the password caching authentication option is chosen.

Application command line

This is a string to be made available to the server via a special 'KCMLCommandLine() \$DECLARE. The server can use it as a bookmark to determine an initial menu setting. See the -C flag in the [command line switches](commandlineswitches.htm) appendix and also the section on [bookmarking](implbmarks.htm).\
\
The string can also be parsed and made available as environment variables by the -c option in [selfid](mk:@MSITStore:kcmlrefman.chm::/selfid.htm). This could be invoked in the .profile.

Connect to Service

The name of a service provided by the [Connection Manager](mk:@MSITStore:kwebserv.chm::/connmgr.htm). This will cause KClient to open a connection on port 790 to the Kerridge Connection manager and pass the service name. The connection manager will then load the service's settings, such as environment variables, and invoke KCML.

Text Window

If checked this will bring up a text window immediately after login. Check this for applications that do not use forms. If you have a forms based application then it should be left unchecked.

Disable Workbench

If checked this will make KCML use the original KCML4 editor rather than the KCML 5.03 Workbench. The default is to use the Workbench.
