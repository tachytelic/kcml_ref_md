<span id="remotelic"></span>

Kprint & KMail Remote Licensing

This page provides access to settings for the [Remote Licence Daemon](mk:@MSITStore:kcmlrefman.chm::/kplicserver.htm).\
Firstly, the WebServer will show the status of the Remote Licence Daemon. [Admin Users](systemconf.htm#admusr) will have links which enable them to stop, start and refresh the daemon. The **Refresh** link can be used after a licence file has been upgraded. Selecting this link will force the daemon to re-read the lic.txt licence file and kconf.xml configuration file. Next the version of the remote licence daemon is displayed along with the port number that it is listening on. Finally there are two links to display the licence tables for **KPrint** and **KMail 3**. The column headings on the tables are links which enable the order of the table to be changed.

Some of the links on this page use an extension to the Remote Licence Daemon's UDP protocol. So the **localhost** entry in the [validclients](systemconf.htm#validip) section should not be changed. The web server will wait for upto 5 seconds for a reply from the Remote Licence Daemon. This can be changed by setting an environment variable, called **KPLIC_DELAY** in the [general](systemconf.htm#genenv) section of kconf.xml.

**Multiple Environment [ASP](mk:@MSITStore:kcmlrefman.chm::/asp.htm) configurations**\
If the [SYSTEMID](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID) environment variable has been set, both the [Remote Licence Daemon](mk:@MSITStore:kcmlrefman.chm::/kplicserver.htm) and the WebServer will modify the network port that is used. By default this is port 1791. If [SYSTEMID](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID) has been set then the value of [SYSTEMID](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID) is added to this default port number. Eg SYSTEMID=3 then the port used by the WebServer and the remote licence daemon will be 1791 + 3 = 1794.

##### See Also:

[Remote Adminstration Functions](adminfns.htm)
