<span id="auth"></span>

Authentication

To access the [Administration functions](adminfns.htm) or any of the [services](systemconf.htm#services) you will need to have provided a username and password. This is checked against the host system's password database.\
Unix versions will also check for the presence of a [.kcmlLogin](overview.htm#unixAccess) file in the user's home directory. Accounts which do not have this file are regarded a *e-mail only* accounts, and access to all of the connection manager's services will not be granted.\
To prevent anyone, except the **root** user, from logging in, eg during system maintenance, a text file called */etc/nologin* can be created. This file should contain a simple text message, for example:


    System locked for software upgrade.

The Connection Manager then checks that the user name is in the [Valid Users](systemconf.htm#validusr) list. The IP address of the client is also checked against the list of [Valid Clients](systemconf.htm#validip). If a client is requesting to connect to a specific [service](systemconf.htm#services), and that service defines its own access control lists, then these are checked as well. If all these checks pass access is granted.\
When [KClient](mk:@MSITStore:kclient.chm::/loginprocess.htm) has connected and authentication fails, then a suitable [error message](connerrors.htm) is displayed. In the case of a */etc/nologin* then contents of the file will be shown.

##### See Also:

[Account Properties](overview.htm#unixAccess)
