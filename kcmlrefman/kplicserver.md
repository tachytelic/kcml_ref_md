Remote Licence Daemon

## Introduction

The **Remote Licence Daemon** manages licences for products such as **Kprint** and **Kmail 3.0**. This enables several machines running these products to use one central licence file instead of each machine having to be individually licenced.

The Remote Licence Daemon is usually installed on the main *Application Server*. The Remote Licence Daemon will look for \[KPrint\] and \[KMail\] sections in the licence file and then listen, on UDP port 1791, for *licence requests*. The entries in these sections are a *pool* of user counts. KPrint and KMail 3.0 can then send a *licence request* to the Remote Licence Daemon over the network. If there are enough spare licences left in the product's licence pool, then the Remote Licence Daemon will book out the requested number of licences against the IP address of the machine that is running KPrint or KMail 3.0. The Remote Licence Daemon will then send a reply back to KPrint or KMail 3.0. to acknowledge the request. If the Remote Licence Daemon was not able to grant the request, then the reply will contain a description of the error.

- [Installation](#installing)
- [Execution](#exec)
- [Command line flags](#cmdflags)
- [Inspecting the KPrint Licence table](#kplictbl)
- [Configuration](#config)

------------------------------------------------------------------------

## <span id="installing">Installing</span>

The Remote Licence Daemon is installed as part of KCML version 6 or is available separately for systems running earlier versions of KCML.

##### Windows

For Windows based systems, the [installer program](installers.htm) will automatically create a service for the Remote Licence Daemon.\
For Example:

| Name | Status | Port | Server Name | Server Path | Command Line |
|----|----|----|----|----|----|
| kplic | Running |  | Remote Licence Daemon | C:\Kerridge\KCML\kplicserver.exe |  |

This service can be controlled by the KCML Service Administrator, KServAdm, and the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm). Both of these applications will also display the KPrint Licence Table.

##### Unix systems

The Remote Licence Daemon is installed using the *kpinst* install script. Download this script and the *kplicserver* executable to a temporary directory, eg /tmp, on the Unix server. Make sure both files have *execute* permission by using the command


    chmod +x kpinst kplicserver

To execute the script use the command


    ./kpinst

You must be the **root** super-user to do this. As the Remote Licence Daemon must be started during system boot-up, the install script will create a *startup script*. If this script already exists it will be left unchanged. The install script will display the name of the startup script and the directory in which it is created. It will then prompt for the directory into which the Remote Licence Daemon is to be installed.


    # ./kpinst
    Info - Startup script will be S68Kerridge in /etc/rc2.d
    Please enter installation dir, or press return for '/usr/local/kcml'
    Installation directory :

This directory is usually the same one that KCML has been installed into. Either press return, to accept the default value of */usr/local/kcml*, or enter an alternative directory. The kpinst script will now install the Remote Licence Daemon


    Installing KPrint Licence Server into /usr/local/kcml

If you are running the script to upgrade an existing copy of the Remote Licence Daemon, the install script will stop any kplicserver process before upgrading. After the Remote Licence Daemon has been installed, the script will execute it. It will then display the KPrint Licence table using [bkstat -r](bkstat.htm)


    IP address      Queues  Editor  Fax    Template

    Totals:         Queues  Editor  Fax    Template
                    0       0       0      0

    Remain:         Queues  Editor  Fax    Template
                    23      5       7      4

    Licence:        Queues  Editor  Fax    Template
                    23      5       7      4

------------------------------------------------------------------------

## <span id="exec">Execution</span>

The install script configures the host system so that the Remote Licence daemon is automatically started when the machine boots up. For Windows systems, this is acheived by running the daemon as a service that can be controlled with **kservadm**.

On Unix systems the install script creates a boot script that is executed when the host machine starts up. This script is executed before the machine enters multi-user mode. The filename of the boot script is platform dependent:

| Platform | Filename / method |
|----|----|
| AIX | As the **root** user, execute *lsitab kcc* |
| Linux | Typically */etc/init.d/Kerridge* |
| HP-UX | */sbin/init.d/Kerridge*, with parameters stored in */etc/rc.config.d/Kerridge* |
| System 5.4, Unixware etc | */etc/rc2.d/S\*Kerridge* |

The filename of for System 5.4 hosts is chosen so that is is executed before the boot script for the **inetd** daemon. For example, if the system starts inetd with the script */etc/rc2.d/S69inet*, then the filename of the Remote Licence daemon's script will be */etc/rc2.d/S68Kerridge*

On AIX systems, the script is registered in */etc/inittab* with the name of **kcc**. The boot script is copied into the installation directory, typically */usr/local/kcml* or */usr/lib/kcml*. The */etc/inittab* file should not be edited directly, but can be maintained with the *lsitab*, *mkitab*, *chitab* and *rmitab* commands.\
For example:


    # lsitab kcc
    kcc:234:once:/usr/local/kcml/S98Kerridge

Linux systems have a master copy of the script in the */etc/init.d* directory. Each run-level has its own subdirectory, eg */etc/rc.d/rc2.d* or */etc/rc2.d*. The script is symbolically linked into each run-level directory, the filename of the symbolic link is chosen so that script is executed before the boot-script for the **inetd** or **xinetd** daemon.


    # cd /etc/rc.d/rc3.d
    # ls -l S*Kerridge
    lrwxrwxrwx    1 root     root           20 Jun 14 11:51 S49Kerridge -> /etc/init.d/Kerridge

The Remote Licence Daemon's boot script can also be used to launch other KCML products. A prime example of this would be to create a larger [\$PSTAT]($PSTAT.htm) area with the [bkstat -x/-y](bkstat.htm#config_pstat). The size of the \$PSTAT are must be set **before** users are allowed to logon, hence the need for the boot-script to be executed before the machine enters multi-user mode. The [Connection Broker](connectionbroker.htm) should also be started by this script. Other uses include the automatic starting of global libraries.

------------------------------------------------------------------------

## <span id="cmdflags">Command line switches</span>

General form:

kplicserver \[-r\] \[-s\] \[-p *port*\] \[-t *size*\] \[-R *attempts*\] \[-e *var=value*\]

The Remote Licence Daemon has the following command line switches

| Switch | Purpose |
|----|----|
| -r | Sends a **Refresh** packet on the local area network (LAN). |
| -s | Sends a **STOP** packet to the daemon running on *localhost*. |
| -e var=value | Set an environment variable *var* to the value of *value* |
| -t size | Specify the size of the KPrint licence table |
| -R attempts | Specify the number of attempts when trying to establish a network connection |
| -p port | Use an alternative UDP port |

The -r flag is used to force any remote licence daemons on the local area network to re-read their *lic.txt* licence files and *kconf.xml* configuration files. This is needed after a licence file has been upgraded with extra KPrint or KMail licences only for Unix versions of the Remote Licence Daemon. An alternative is to use the [Refresh](mk:@MSITStore:kwebserv.chm::/remotelic.htm) link on the Web-based Remote Administration tool. The Windows version of the Remote Licence Daemon can detect when the licence file has changed.

The -s flag can be used to stop a licence daemon running on *localhost*. This is done by sending a special **Stop** packet to the daemon. This is especially useful when running on an ASP server; the packet will be sent on to correct port, providing SYSTEMID has been set.

By default the Remote Licence Table will create a KPrint Licence table large enough for 256 KPrint servers. If there expected to be more than 256 machines running KPrint then the remote licence daemon should the *-t size* flag. For Unix systems, this will need to be done in the *startup script*\
For example:


    # Start the KPrint licence server
    /usr/local/kcml/kplicserver -t 1024 &

For Windows based systems this should be done by using **KServAdm** or the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm) to amend the *kplic* service.\
For example:

| Name | Status | Port | Server Name | Server Path | Command Line |
|----|----|----|----|----|----|
| kplic | Running |  | Remote Licence Daemon | C:\Kerridge\KCML\kplicserver.exe | -t 512 |

\
\
Under some versions of Unix, the underlying network sub-system may not be ready when the Remote Licence Daemon is started during system boot-up. Normally, the Remote Licence Daemon will do 20 attempts to create the network connection, with a 10 second pause between each attempt. For each attempt, the Remote Licence Daemon will also add an entry into the [system log](syslog.htm) of the form:


    KCML: WARNING /usr/local/kcml/kplicserver[root,245]: Socket: Network not yet up, retry 0 of 20

If, after these 20 attempts, the network connection has still not been made then the Remote Licence Daemon will exit. The number of attempts can be increased by adding the *-R retry* switch in the *startup script*\
For example


    # Start the KPrint licence server
    /usr/local/kcml/kplicserver -R 50 &

Will cause the Remote Licence Daemon to try to create the network connection 50 times.\
\
The *-p port* flag should only be used if UDP port number 1791 is already being used by another application. If it is used the any machines that are running KPrint or KMail 3.0 will have configured to used the new port number.

------------------------------------------------------------------------

## <span id="kplictbl">The Kprint Licence Table</span>

This is a table of all the machines that have obtained a KPrint licence from the Remote Licence Daemon. Each KPrint server can request a number of queues, a single editor licence and a single fax licence. If the KPrint licence pool does not have enough licence left for any these features the request will be refused. Once a KPrint server has obtained a licence it is kept permanently. The status of the KPrint licence table can be displayed using -r switch on the [bkstat](bkstat.htm) utility.\
Eg:


    IP address      Queues  Editor  Fax  Template
    172.31.251.22   4       1       1    0
    172.31.251.16   7       0       0    1
    172.31.251.11   2       0       1    1
    172.31.251.2    5       1       0    0

    Totals:         Queues  Editor  Fax  Template
                    18      2       2    2

    Remain:         Queues  Editor  Fax  Template
                    5       3       5    2

    Licence:        Queues  Editor  Fax  Template
                    23      5       7    4

    KPrint licence table has 256 slots, 4 used

The [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm) can also display the KPrint Licence Table.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th><strong><u>IP address</u></strong></th>
<th><strong><u>Queues</u></strong></th>
<th><strong><u>Editor</u></strong></th>
<th><strong><u>Fax</u></strong></th>
<th><strong><u>Template</u></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><em>172.31.251.22</em></td>
<td><em>4</em></td>
<td><em>1</em></td>
<td><em>1</em></td>
<td><em>0</em></td>
</tr>
<tr>
<td>172.31.251.16</td>
<td>7</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>172.31.251.11</td>
<td>2</td>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>172.31.251.2</td>
<td>5</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td><br />
</td>
<td><br />
</td>
<td><br />
</td>
<td><br />
</td>
<td><br />
</td>
</tr>
<tr>
<td>Totals</td>
<td>Queues</td>
<td>Editor</td>
<td>Fax</td>
<td>Template</td>
</tr>
<tr>
<td></td>
<td>18</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>Remainder</td>
<td>Queues</td>
<td>Editor</td>
<td>Fax</td>
<td>Template</td>
</tr>
<tr>
<td></td>
<td>5</td>
<td>3</td>
<td>5</td>
<td>2</td>
</tr>
<tr>
<td>Licence Details</td>
<td>Queues</td>
<td>Editor</td>
<td>Fax</td>
<td>Template</td>
</tr>
<tr>
<td></td>
<td>23</td>
<td>5</td>
<td>7</td>
<td>4</td>
</tr>
</tbody>
</table>

Other KPrint features, for example SMS, are licensed using a *generic licence table*. These tables cannot be inspected using *bkstat*, use the **Display a generic licence Table** link of the Connection Manager's [KPrint & KMail Remote Licensing](mk:@MSITStore:kwebserv.chm::/remotelic.htm) page.

------------------------------------------------------------------------

## <span id="kmailtbl">The KMail 3.0 Licence table</span>

The latest versions of KMail, 3.0 & 4.0, are licensed using a similar mechanism to KPrint. Unlike the KPrint Licence table the KMail Licence table has a dynamic size. The number of machines that can be licensed is determed by the user count in the \[KMail\] section of the licence file. Each machine that runs KMail 3.0 obtains a single user licence using a licence request on the same UDP port as KPrint. KMail sends a licence request before it connects to the POP3 mail server. A KMail 3 licence also has a finite, one hour, lifetime. If KMail has not done a request within this one hour lifetime, the licence can be issued to another machine. This will only occur when the KMail licence table is full. If the KMail licence table is full and all licences are less than one hour old then any extra licence requests will be refused. The KMail licence table can be displayed by the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm).\
For example:

**Maximum KMail users is 3.**\

| **IP address**  | Last Access               | **Age** | Expired |
|-----------------|---------------------------|---------|---------|
| *172.31.251.22* | *Fri Mar 9 16:55:33 2001* | *36s*   | *No*    |
| 172.31.251.16   | Fri Mar 9 16:55:41 2001   | 28s     | No      |
| 172.31.251.2    | Fri Mar 9 16:56:01 2001   | 8s      | No      |

------------------------------------------------------------------------

## <span id="config">Configuration</span>

When the Remote Licence Daemon is installed with KCML Version 6 it can be configured by settings in the *kconf.xml* configuration file via the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm). There are two important settings which the Remote Licence Daemon will use from the *kconf.xml* file

- [valid clients](mk:@MSITStore:kwebserv.chm::/systemconf.htm#validip) list.
- [SYSTEMID](EnvVars.htm#SYSTEMID) environment variable.

The [valid clients](mk:@MSITStore:kwebserv.chm::/systemconf.htm#validip) list can restrict access to the Remote Licence Daemon. Machines that send licence requests but are not in the [valid clients](mk:@MSITStore:kwebserv.chm::/systemconf.htm#validip) will be sent an error packet by the Remote Licence Daemon. Also the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm) uses an extension to the remote licence request protocol that is used by **KPrint** and **KMail 3.0** to communicate with the Remote Licence Daemon. Since both the Remote Licence Daemon and the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm) are running on the same machine this is done via the *localhost* network address. If the *localhost* entry is removed from the [valid clients](mk:@MSITStore:kwebserv.chm::/systemconf.htm#validip) list then this protocol with be broken and many of the [Webserver's](mk:@MSITStore:kwebserv.chm::/remotelic.htm) Remote Licensing pages will no longer be accessible.

The [SYSTEMID](EnvVars.htm#SYSTEMID) environment variable is used to determine the UDP port on [multiple environment ASP systems](asp.htm). **KPrint** and **Kmail 3.0** can be independently licenced by running multiple Remote Licence Daemons. Each Remote Licence Deamon will listen on a different UDP port. If the [SYSTEMID](EnvVars.htm#SYSTEMID) has been set both the Remote Licence Daemon and the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm) modify the default UDP port. This is simply done by adding the value of [SYSTEMID](EnvVars.htm#SYSTEMID) to the normal UDP port of 1791.\
For example, if [SYSTEMID](EnvVars.htm#SYSTEMID) has been set to 3, then the default UDP port will be 1791 + 3 = 1794. The [SYSTEMID](EnvVars.htm#SYSTEMID) can be set in the following ways.

- In the Unix *startup script*
- Using the *-e var=value* switch
- In *kconf.xml's* [general environment](mk:@MSITStore:kwebserv.chm::/systemconf.htm#genenv) section.
- In the environment section of a [service](mk:@MSITStore:kwebserv.chm::/systemconf.htm#services) section.

The first two methods are only really intended for use with KCML 5.02 systems. The [Unix startup script](#exec) can be modified to start all the Remote Licence Daemons


    # Start the KPrint licence servers

    SYSTEMID=1
    export SYSTEMID
    /user1/app1/kcml/kplicserver &

    SYSTEMID=2
    export SYSTEMID
    /user1/app2/kcml/kplicserver &

    SYSTEMID=3
    export SYSTEMID
    /user1/app3/kcml/kplicserver &

or using the -e swtich


    # Start the KPrint licence servers

    /user1/app1/kcml/kplicserver -e SYSTEMID=1 &

    /user1/app2/kcml/kplicserver -e SYSTEMID=2 &

    /user1/app3/kcml/kplicserver -e SYSTEMID=3 &

For KCML 6 systems it is preferable to set the [SYSTEMID](EnvVars.htm#SYSTEMID) environment variable in the *kconf.xml* configuration file. This has the advantage that both the Remote Licence Daemon and the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm) use the same setting.

For some [ASP](asp.htm) systems it may be preferable for each application to have its own, private, copy of KCML 6. In this case the [SYSTEMID](EnvVars.htm#SYSTEMID) can be set in the [general environment](mk:@MSITStore:kwebserv.chm::/systemconf.htm#genenv) of the *kconf.xml* configuration file. This configuration is only applicable on Unix servers.\
For example:


    # Start the KPrint licence servers

    /user1/app1/kcml/kplicserver &

    /user1/app2/kcml/kplicserver &

    /user1/app3/kcml/kplicserver &

Each application has its own copy of the Remote Licence Daemon with its own *kconf.xml* configuration file. The [SYSTEMID](EnvVars.htm#SYSTEMID) variable can be set in the [general section](mk:@MSITStore:kwebserv.chm::/systemconf.htm#genenv) of each *kconf.xml* configuration file.

Other [ASP](asp.htm) systems may use a common copy of KCML. Each application will therefore store the value of [SYSTEMID](EnvVars.htm#SYSTEMID) in a [service's](mk:@MSITStore:kwebserv.chm::/systemconf.htm#services) environment block within the *kconf.xml* file. In this case the Remote Licence Daemon needs to know which [service](mk:@MSITStore:kwebserv.chm::/systemconf.htm#services) to inspect. This is done by setting the **SERVICE** environment variable.\
This should be done in the [Unix startup script](#exec), for example:


    # Start the KPrint licence servers

    SERVICE=Marketing
    export SERVICE
    /usr/local/kcml/kplicserver &

    SERVICE=Accounts
    export SERVICE
    /usr/local/kcml/kplicserver &

Or, by using the -e command line switch


    # Start the KPrint licence servers

    /usr/local/kcml/kplicserver -e SERVICE=Marketing &

    /usr/local/kcml/kplicserver -e SERVICE=Accounts &

For Windows based systems is can be done by modifying the service using **KServAdm** or the [Web-based Remote Administration tool](mk:@MSITStore:kwebserv.chm::/systemconf.htm#inetserv).\
For example:

| Name | Status | Port | Server Name | Server Path | Command Line |
|----|----|----|----|----|----|
| kplic mktg | Running |  | Remote Licence Daemon | C:\Kerridge\KCML\kplicserver.exe | -e SERVICE=Marketing |
| kplic acc | Running |  | Remote Licence Daemon | C:\Kerridge\KCML\kplicserver.exe | -e SERVICE=Accounts |

\
In the first example, when the Remote Licence Daemon reads the *kconf.xml* configuration file it will load the environment block for the ***Marketing*** service. If this environment block contains a [SYSTEMID](EnvVars.htm#SYSTEMID) variable of value 5 then the Remote Licence Daemon, and the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm), will use a UDP port of 1791 + 5 = 1796. The ***Accounts*** service may have a [SYSTEMID](EnvVars.htm#SYSTEMID) of 6. This service would then use a UDP port of 1791 + 6 = 1797. As each application is idependently licensed, they must have their own licence file. KCML, the [Web-based Remote Administration Tool](mk:@MSITStore:kwebserv.chm::/remotelic.htm), and the Remote Licence Daemon will attempt to load a licence file with a name of the form [*lic.x.txt*](asp.htm), where *x* is the value of [SYSTEMID](EnvVars.htm#SYSTEMID). If a *lic.x.txt* licence file could not be found then the normal *lic.txt* filename will be used. Using the two examples from above the ***Marketing*** system will use a licence file called *lic.5.txt* while the ***Accounts*** service will use a *lic.6.txt* licence file.\
A service may also restrict access by setting its own [valid clients](mk:@MSITStore:kwebserv.chm::/systemconf.htm#validip) list.

When the **SERVICE** environment variable is set the kconf.xml configuration file must exist. If kconf.xml does not exist then the Remote Licence daemon will add an entry to the [system log](syslog.htm) of the form


    KCML: ERROR kplicserver[root,17841]: Failed to load kconf.xml for service 'Sales'.
    Try setting $KCML_SOURCES or invoke the Remote Licence daemon with an absolute pathname.

and then terminate.
