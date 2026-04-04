## Internet Services Configuration

\

------------------------------------------------------------------------

Internet Services Configuration **<u>Help</u>**\
Kerridge Web Administration Tool **<u>Help</u>**

------------------------------------------------------------------------

## WARNING: Changing internet services configuration.

This page allows you to modify the settings used by internet services on this server. If your changes contain mistakes, you may no longer be able to access this server.

------------------------------------------------------------------------

Display/update **<u>/etc/hosts</u>**\
Display/update **<u>/etc/services</u>**\
Display/update **<u>/etc/lmhosts</u>**\
Update **<u>NBT cache</u>**\

****<u>Add</u>** a new service**

**Current KServadm services:**\

| Name | Status | Pid | Port | Server Name | Server Path | Command Line |
|----|----|----|----|----|----|----|
| web2 | Listening | <u>215</u> | 792 | Web Server Version 06.20 | C:\Kerridge\KCML620\kwebserv.exe |   |
| **<u>kisam</u>** | Listening | <u>153</u> | 747 | ODBC Server | C:\Kerridge\KCML\kiodbc.exe |   |
| **<u>std</u>** | Listening | <u>1274</u> | 23 | KCML Remote Server | C:\Kerridge\KCML\kcml.exe | C:/Kerridge/Kcml/startprog.src |
| **<u>kwebadmin</u>** | Listening | <u>538</u> | 790 | Web Server | C:\Kerridge\KCML\kwebserv.exe |   |
| **<u>kplic</u>** | Running | <u>827</u> |   | Remote Licence Daemon | C:\Kerridge\KCML\kplicserver.exe |   |

Display/update KWebServ configured **<u>web services</u>**\
\
As a last resort the internet services configured through KWebServ can be changed directly by,\
Display/update **<u>C:/Kerride/KCML620/kconf.xml</u>**\
\
KWebServ tracing is controlled by environment variables in the kconf.xml **<u>general</u>** section\
KWebServ tracing is disabled.

------------------------------------------------------------------------
