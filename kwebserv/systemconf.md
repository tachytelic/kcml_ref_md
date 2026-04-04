<span id="kccsys"></span>

Kerridge System Configuration

This page is used to configure Kerridge Software by changing the settings in the *kconf.xml* configuration file. Although many of the links are available to any [Valid User](#validusr), only [Admin Users](#admusr) can make any changes.

The first two links are [directory listings](dirlist.htm) for the KCML directory and the WebServer's root directory. Next are a table of links for inspecting and changing settings in the various sections of the *kconf.xml* configuration file.

| Link | Purpose |
|----|----|
| [General Environment](#genenv) | Environment variables common to all services |
| [Services](#services) and their environments | Add/Remove a service or change a service's environment variables |
| [Valid users](#validusr) and their environments | List of users who are allowed to access the WebServer |
| [Admin users](#admusr) | List of users who are allowed to make changes using the WebServer |
| [Valid clients](#validip) and their environments | List of IP addresses and machine names who are allowed to access the WebServer |
| [Web Aliases](aliases.htm) | Look-up table for aliasing URL's to filenames and directories |
| Web Services | Look-up table for matching a client to a server |
| Table spaces | Default directory for a service's database files |
| Update kconf.xml | Directly edit kconf.xml |

<span id="genenv"></span>

### General Environment Variables

This section stores a table of environment variables which are common to all [services](#services), [valid clients](#validip) and [valid users](#validusr).\
Typical examples of environment variables that are stored in this section are:

| Variable | Default value | Purpose |
|----|----|----|
| WEBSERVER | true | Enables/disables access to the WebServer's from a Web Browser, the [Connection Manager](connmgr.htm) is still enabled |
| WEBADMIN | true | Enables/disables the WebServer's [Administration functions](adminfns.htm) |
| PATH | Machine dependent | List of directories to search when executing a command. |

Setting variables in this section has a global effect. However, values can be overridden by resetting variables to different values in the environment blocks of the [Valid User](#validusr), [Valid Clients](#validip), or [Services](#services) sections.\
**Important Note:** Care must be taken when setting the **PATH** variable, especially on Unix systems. As **KWebServ** is started via the network daemon, *inetd*, then it will not inherit any environment variables that are set via */etc/profile* for a *telnet* login. This means that **PATH** must be initialised in *kconf.xml*, it cannot self-reference.\
For example: *PATH=\$PATH:/myapp/bin* would result on a **PATH** value of *:/myapp/bin*\
When *kconf.xml* is installed the **PATH** environment variable is taken from the shell.

<span id="services"></span>

### Services

This section describes the various applications the connection manager can provide. A service has the following properties

- Name
- Type
- Connection
- Catalogue
- Description
- Default tablespace
- Table space list
- Global ID
- KCML type
- SOAP service list
- Environment block
- Startup script

The **Name** is the name of the service. It is a common reference used by the WebServer, KClient and the Kerridge ODBC Server.\
The **Type** property describes what type of database files the service will use.\
The **Connection** property allows/disallows KClient to connect.\
The **Catalogue** is the name of the ODBC catalogue file which is also used by the Kerridge ODBC Server.\
A brief description can be entered into the **Description** field.\
The **Default tablespace** property is default directory where the application stores its database files.\
The list of directories the service will store its database tables can be specified in the **Table Space list**\
The **Global ID** property is used to identify the service. If it is unset the inode number of the KCML's TERMFILE is used.\
The **KCML type** property is used identify the KCML type. This is currently 6.\
The **SOAP Services** link allows a list of appplication [SOAP interfaces](websoap.htm) to be configured.\
A **Startup script** can be defined for use with [kwebserv -i](webasp.htm) in a boot script.\
The **Catalogue** is a database table containing the list of data files that the service uses.\
The service can have an **Environment block**. This should contain application specific environment variables.\
Typical examples are:

| Variable | Purpose |
|----|----|
| BASE | The location of the application |
| START | Filename of the [KCML program to execute](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#START) when connecting with KClient. |
| PANICDIR | Directory containing KCML [Panic](mk:@MSITStore:kcmlrefman.chm::/PANIC.htm) files |
| SCREENDIR | Directory containing KCML [Screen dump](mk:@MSITStore:kcmlrefman.chm::/$ALERT_SCREEN.htm) files |
| SYSTEMID | Multiple [ASP](mk:@MSITStore:kcmlrefman.chm::/asp.htm) environment [identifier](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SYSTEMID) |
| TERMFILE | The location of the KCML terminal [table](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#TERMFILE). |
| UMASK | **Unix only.** File creation mask, eg 022. |

In addition to the names of environment variables, files can be included by using the **get_include**, **try_include** or **include** directives. The **include** will load environment variables from an XML document. The **get_include** and **try_include** directives will load the environment from a plain text format file:


    [UNB]"VAR","value"

The first character of a line in this file determines what platform the variable applies to.\
It can take the following values.

| Character | Meaning                                 |
|-----------|-----------------------------------------|
| U         | Set variable on Unix platforms only     |
| N         | Set variable on NT platforms only       |
| B         | Set variable on both types of platforms |

Note: From 6.20 onwards environment variables can be used in the pathnames for the location of table spaces, database catalogues, and the include directives.

Each service can define it own private [valid user](#validusr), [valid client](#validip) and [admin user](#admusr) access control lists. These per-service access control lists are checked in addition to the lists that are defined at the top level. This is particularly useful when using the Connection Manager in an [ASP](mk:@MSITStore:kcmlrefman.chm::/asp.htm) environment as access to a service can be restricted to a specific set of users or network addresses.\
If a service doesn't define any of its own access control lists, then access is only restricted by the top-level [valid user](#validusr), [valid client](#validip) and [admin user](#admusr) access control lists.

<span id="validusr"></span>

### Valid Users

This is an access control list of user names, or patterns such as *fred\**. When a user is [authenticated](auth.htm) they are checked against this list after being verified against the system's password database. On Unix system's the account's home directory is also checked for the existence of a [.kcmlLogin](auth.htm) file. If their username is in this list, or it matches a pattern, the access is granted. Each valid user can have their own environment block. The [Current service](currentsrv.htm) is stored in this block as the **SERVICE** variable.

<span id="admusr"></span>

### Admin Users

This is a list of user names, or patterns, of users who can make changes to the settings stored in the *kconf.xml* configuration file using the WebServer's [administration functions](adminfns.htm).

<span id="validip"></span>

### Valid Clients

This is a list of machine names, IP addresses or IP address patterns. When a connection is made to the WebServer it will check the address of the client. If the address is in this list, or it matches one of the IP address patterns then access is granted. The default entries are **localhost** and a pattern which allows access to all machines on the host server's subnet. For example if the host server has an IP address of 1.12.23.34, then the pattern will be 1.12.23.\* . Machine name patterns, such as *fred\** are not supported.\
A valid client can also have an **Environment block**. For example, setting the *WEBADMIN* environment variable can enable or disable the WebServer's [Administration functions](adminfns.htm) for that machine-name, IP address or IP address pattern. Setting the *WEBSERVER* environment variable can enable or disable access to Web-Browser for specific **valid clients**.

From 6.20 onwards, the access control lists can be defined in an *include file*. Add a username or IP address of **include** followed by the pathname of the include file. This file is an XML document, and is has similar layout to *kconf.xml*.

**Important Note:**The *localhost* entry should not be removed at it is used by the [Remote licence daemon](mk:@MSITStore:kcmlrefman.chm::/kplicserver.htm). If this entry is removed, the licence daemon will refuse connections from the WebServer and many of the links on the [KPrint & KMail Remote Licensing](remotelic.htm) page will fail to work.

When configuring *kconf.xml* for the first time, when large number of new users may be being added to the system, it may be useful to use the [kconf](mk:@MSITStore:kcmlrefman.chm::/kconf.htm) utility to import access control list data from a text file.

##### See Also:

[Connection Manager](connmgr.htm), [Connecting to a Service](connserv.htm), [Remote Adminstration Functions](adminfns.htm)
