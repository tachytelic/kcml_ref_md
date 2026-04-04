<span id="connmgr"></span>

Connection Manager

When a network connection is made to the Connection Manager it determines what type of client is attempting to connect and it will then [authenticate](auth.htm) the user's name and password before invoking the appropriate server. The type of server is determined by looking down the table of [Web Services](websrv.htm). The exceptions to this are when a connection is made from a HTTP client such as a Web Browser. The HTTP request is either treated as a [SOAP](websoap.htm) request, or is passed onto the internal web-server.

The connection manager can support multiple applications. Each application is described by a [service](systemconf.htm#services), which defines the application's environment block, database catalogue and optional access control lists. The location of the KCML program file to be executed when connecting with **KClient** is held in the [START](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#START) environment variable.

Client programs need to [inform](connserv.htm) the Connection Manager which [service](systemconf.htm#services) they wish to connect to. This is so the Connection Manager knowns which [service's](systemconf.htm#services) environment block to load before invoking the server program.

For Unix systems, if the environment variable **UMASK** has been set in the [General](systemconf.htm#genenv), [ValidUser](systemconf.htm#validusr) or [ValidService](systemconf.htm#services) sections of kconf.xml, then the connection manager will set the file creation mask before invoking the server program. This is replacement for the execution of a **umask** command in a *.profile* script via a Unix Telnet connection.

##### See Also:

[Connecting to a Service](connserv.htm), [Authenication](auth.htm), [Connection Manager Errors](connerrors.htm)
