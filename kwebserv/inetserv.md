<span id="inetserv"></span>

Internet Services Configuration

This page is only available to super users such as **root** on Unix systems or **Administrator** on Windows NT/2000/XP. Great care must be excercised when making changes to network settings as a mistake can cause future network connections to fail.

**Unix Systems**\
This page allows various internet settings to be displayed and changed. The following files can be displayed and changed

| File             | Purpose                                  |
|------------------|------------------------------------------|
| /etc/hosts       | Host name look-up table                  |
| /etc/services    | List of registered network ports         |
| /etc/resolv.conf | Network domain and address of DNS server |
| /etc/inetd.conf  | Internet service list                    |

\
After */etc/services* or */etc/inetd.conf* have been changed the the internet service daemon, *inetd*, will need to be notified before the new changes take effect. This is done by sending the SIGHUP signal to the inetd daemon. Select the **Send SIGHUP to inetd** link to do this.

**Window NT/2000/XP Systems**

Like Unix systems, Windows NT/2000/XP has a *etc/hosts* file which is a look-up table of commonly used host names. It is usually located within the Windows system directory, eg *C:\Winnt\System32\drivers\etc\hosts*. Selecting the **Display/Update /etc/hosts** link will allow you to edit this file.\
The WebServer is able to control Kerridge NT Services, just like the *Kerridge Service Administrator*, KServAdm. A table of Kerridge Services is displayed, in a similar style to KServAdm. The service name is a link to a page which allows you to start or stop the service. When a service has been **Uninstalled** its properties, such as command line arguments, can also be changed.\
View an example table of [KServAdm services](examples/ipconfig.htm).

**Caution: Do not stop or un-install the service that the WebServer is using as you will no longer be able to access the Web Admin pages!!**

##### See Also:

[Remote Administation Functions](adminfns.htm), [Installation](install.htm)
