Installation

The KCML installation script (on Unix), or the [KCML Server setup program](mk:@MSITStore:kcmlrefman.chm::/installers.htm) (for Windows) will automatically install the necessary files for the **Connection Manager**. This involves configuring the *kconf.xml* file, and the creation of the **WebServer's** home directory, *kwroot*. These files are shipped with a *.example* suffix. If *kconf.xml*, *kconf.dtd* or *kwroot* do not exist then they are copied from *kconf.xml.example*, *kconf.dtd.example* or *kwroot.example* respectively. If these files do exist then any further upgrades will not modify them.

A network service is also created to listen on port 790.\
On Windows NT/2000/XP systems this is done using a **Kservadm** service.

| Name | Status | Port | Server Name | Server Path | Command Line |
|----|----|----|----|----|----|
| kwebadmin | Listening | 790 | Web Server | C:\Kerridge\KCML\kwebserv.exe |   |

\
while on Unix systems this is done using **/etc/services**


    KCC     790/tcp         # Kerridge WebServer

and the Internet Service Daemon, *inetd*, via **/etc/inetd.conf**


    KCC     stream  tcp     nowait  root    /usr/local/kcml/kwebserv  /usr/local/kcml/kwebserv

One some Linux systems, the **inetd** daemon has been superceded by **xinetd**. Each network service has its own configuation file in the */etc/xinetd.d* directory. The name of the file is, by convention, the name of the network service as defined in */etc/services*. So for the Connection Manager, the configuration file will be */etc/xinetd.d/KCC*. For example:


    # default: on
    # description: Kerridge Connection Manager
    service KCC
    {
        flags       = REUSE NAMEINARGS
        socket_type = stream
        wait        = no
        user        = root
        server      = /usr/local/kcml/kwebserv
        server_args = /usr/local/kcml/kwebserv
        log_on_failure  += USERID
        disable     = no
        instances   = UNLIMITED
    }

Where available, the Connection Manager will use [Pluggable Authentication Modules](pam.htm), PAM, to authenticate a user's passsword.\
Under Linux, the install script will create the required PAM configuration files

- /etc/pam.d/kcc
- /etc/pam.d/kcml
- /etc/pam.d/kisam

The [.kcmlLogin](auth.htm) files, required for Unix versions of the connection manager, will also be created for those accounts which match the list of [Admin Users](systemconf.htm#admusr) in *kconf.xml.example*. This will allow users such as *root* or *kcc* to use the [Look up user name](overview.htm#unixAccess) link to create the .kcmlLogin files for other users.

See also:

[Connection Manager](connmgr.htm), [Remote Administration Functions](adminfns.htm), [kconf](mk:@MSITStore:kcmlrefman.chm::/kconf.htm) - batch processing of kconf.xml access control lists.
