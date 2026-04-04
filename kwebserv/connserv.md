<span id="connserv"></span>

Connecting to a service

To connect a Web browser to the Connection Manager's built-in WebServer use a URL of the form

<http://localhost:790>

The WebServer will then display the [Welcome](webwelcome.htm) page.\
This has links of the form **Connect to service ...**.\
Selecting one of these links will invoke **KClient**, if installed, so that it connects to Connection Manager. This is done by specifying a set of command line arguments which include the [service name](systemconf.htm#services) and the network port number.

When creating a [KClient connection](mk:@MSITStore:kclient.chm::/remoteconnection.htm), the [service name](systemconf.htm#services) can be specified in the *Connect to Service* edit box on the *Properies* tab page. KClient will then use a default network port of 790, an alternative port can be specified on the [Options](mk:@MSITStore:kclient.chm::/optionspage.htm) tab page if the WebServer has been configured to listen on a different port.

The connection manager will also accept connections from the Kerridge ODBC Driver. When creating an [ODBC Data Source](mk:@MSITStore:drvkisam.chm::/Manage_DSN.htm), use a hostname of the form

myhost,790

##### See Also:

[Connection Manager](connmgr.htm), [Authentication](auth.htm)
