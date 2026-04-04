<span id="adminfns"></span>

Administration Functions

To access these pages a user must first be [authenticated](auth.htm). Access to these pages can be further restricted by only setting the **WEBADMIN** variable to **true** in the environment section of a [validclient](systemconf.htm#validip), [validuser](systemconf.htm#validusr) or [adminuser](systemconf.htm#admusr). Setting this variable in the [general](systemconf.htm#genenv) section will allow access to any [validuser](systemconf.htm#validuser).

There are three levels of user privileges when using the Administration functions:

- Valid User
- Admin User
- Super User

A [Valid User](systemconf.htm#validusr) may be able to view various pages of the WebServer, but will never be allowed to make any changes.\
An [Admin User](systemconf.htm#admusr) can make changes to Kerridge Software using pages such as the [Kerridge System Configuration](systemconf.htm) page.\
**Super Users**, such as *root* on Unix and *Administrator* on Windows NT/2000/XP, are allowed to make changes to the host's operating system settings.\
**Note:** that under Windows NT/2000/XP an [Admin user](systemconf.htm#admusr) must have an account with **Administrative rights**.

The first page the WebServer will display after [authentication](auth.htm) will be the [Machine Type and Overview](overview.htm) page. The top of the Webserver's page will also change. Next to an image of the KCML logo will be a table of the Webserver's administration pages

| Link | Purpose |
|----|----|
| [Machine Type](overview.htm) and Overview | Description of server, system logs, disk space and process list |
| [Internet Services](inetserv.htm) Configuration | Listening services |
| [Kerridge System](systemconf.htm) Configuration | Display and change settings in kconf.xml |
| Current [KCML Processes](kcmlproc.htm) | Display the KCML Partition table and panics files |
| Interrogate [Services](interr.htm) | Display information on database files and connect to services |
| Current [user](username.htm) | Change your user ID |
| KPrint & KMail [Remote Licensing](remotelic.htm) | Displays the [Remote Licence Daemon's](mk:@MSITStore:kcmlrefman.chm::/kplicserver.htm) licence tables for KPrint and KMail 3 |
| KWebServ [Documentation](webdoc.htm) | Online documentation for Webserver |
| System [Commands](syscomm.htm) | Execute non-interactive shell commands |
| Add/Change Current [service](currentsrv.htm) | Change your default service |

##### See also:

[Connection Manager](connmgr.htm)
