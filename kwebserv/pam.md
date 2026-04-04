PAM Overview

From KCML 6.20 onwards Pluggable Authentication Modules, PAM, is used for authentication on the following operating systems

- Linux
- HP-UX 11
- Sun Solaris
- AIX 5.3

The use of PAM allows the system administrator to control the method of authentication. This is done using a PAM configuration file. Any program that uses PAM has to register itself using a *service name*. The Connection Manager will use a lower cased version of the internet service name, as defined in */etc/services*, i.e.


    KCC     790/tcp         # KCML Connection Manager

In this example, the Connection Manager will register itself with PAM using the **kcc** service name.

If PAM finds a **kcc** entry in its configuation file, it will authenticate using those rules. If there is no **kcc** entry, then PAM will attempt to authenticate using the rules from a default PAM service, called **other**.

Before making any manual changes to the default PAM configuration files it is strongly recommended that you familiarize yourself with the PAM documentation for your system.

<span id="pamOrig">PAM on Sun Solaris and HP-UX 11</span>

The implementations of PAM on these platforms use the original */etc/pam.conf* configuration file. The **other** PAM service allows access by default, so no changes need to be made. The username and password is validated against the local database, eg */etc/passwd* & */etc/shadow*.

<span id="pamLinux">Linux-PAM</span>

The Linux implementation of PAM is slightly different to the original Solaris version. Instead of a central */etc/pam.conf* configuration file, each PAM service has a plain text file in the */etc/pam.d* directory. The **other** PAM service, in */etc/pam.d/other*, is always set to **deny access**. Hence, a **kcc** PAM configuration file must be added to */etc/pam.d*.

When adding a new Connection Manager service to */etc/services* then a corresponding PAM configuration file will need to be added to */etc/pam.d*. For example:


    KCCDEV     791/tcp         # KCML WebServer, development and testing

would require a */etc/pam.d/kccdev* configuration file.

There are several versions of Linux-PAM configuration which depend on the Linux distribution and version. The *kcmlinst* install script will create a PAM configuration file suitable for the system.

| Type | Description | System |
|----|----|----|
| [common-auth](PAMcommon.htm) | Directly include system configuration files | Debian 5, Ubuntu 8, SuSE 11 |
| [system-auth](PAMsystem.htm) | Directly include central system configuration file | RedHat ES 5, CentOS 5, Fedora Core5 |
| [pam_stack.so](PAMstack.htm) | Use pam_stack.so module to include central system configuration file | RedHat ES 3 & 4, Fedora Core3 |
| [pam_unix.so](PAMbasic.htm) | Authenticate against the local password database |  |

<span id="pamAix">PAM on AIX 5.3</span>

PAM authentication is supported from version 06.20 of the Connection Manager when running on AIX 5.3, or later. For earlier releases of the Connection Manager and AIX, the native password database will be used for authentication.

The AIX5.3 implemention of PAM uses the original */etc/pam.conf* configuration file. However, the **OTHER** service is always configured to reject authetication by using a */usr/lib/security/pam_prohibit* module:


    #
    # Authentication
    #
    ftp     auth    required        /usr/lib/security/pam_aix
    ... ...
    OTHER   auth    required        /usr/lib/security/pam_prohibit

This requires the addition of specific entries in */etc/pam.conf* to allow the Connection Manager to authenticate using PAM. The standard PAM module that is used for all PAM methods is */usr/lib/security/pam_aix*, which is what the ftp server is using in the above example.

The entries for the Connection Manager will use a PAM service name that is a lower case version of the network service name from */etc/services*. The *kcmlinst* install script creates a network service on port 790 called **KCC**, so the PAM service name will be **kcc**.\
The following fragment of */etc/pam.conf* shows the entries for the *ftp*, *kcc* and *OTHER* PAM services.


    #
    # Authentication Management
    #
    ftp auth    required    /usr/lib/security/pam_aix
    ... ...
    kcc auth    required    /usr/lib/security/pam_aix
    OTHER   auth    required    /usr/lib/security/pam_prohibit

    #
    # Account Management
    #
    ftp account required    /usr/lib/security/pam_aix
    ... ...
    kcc account required    /usr/lib/security/pam_aix
    OTHER   account required    /usr/lib/security/pam_prohibit

    #
    # Password Management
    #
    ftp password    required    /usr/lib/security/pam_aix
    ... ...
    kcc password    required    /usr/lib/security/pam_aix
    OTHER   password    required    /usr/lib/security/pam_prohibit

    #
    # Session Management
    #
    ftp session required    /usr/lib/security/pam_aix
    ... ...
    kcc session required    /usr/lib/security/pam_aix
    OTHER   session required    /usr/lib/security/pam_prohibit

The install script will use the *addpam.ksh* script to add the **kcc** PAM service to */etc/pam.conf*.

Adding new PAM services

If you add another Connection Manager service, via */etc/services* and */etc/inetd.conf*, then you will need to add new rules to */etc/pam.conf*. This can be done by manually editing the file, however, you can use the *addpam.ksh* script that is installed into the KCML directory. The first argument for the addpam.ksh script is the name of the PAM service. The filename of the PAM module to use can be specified with an, optional, second parameter. If no PAM module is specified, the script will use the default PAM module, eg */usr/lib/security/pam_aix*.

For example, adding new Connection Manager service, called KCC-TEST, on port 791.\
The network service name would be defined in */etc/services*


    KCC-TEST     791/tcp         # KCML Connection Manager

The */etc/pam.conf* rules would then be created by executing *addpam.ksh* with a lower-cased service name:


    $ addpam.ksh kcc-test

The script creates a backup, called */etc/pam.conf.orig*, before the modifications are made.

Note: Many implementations of PAM will not allow authentication if */etc/pam.conf* can be modified by regular users. Only the **root** super-user should be able to write to */etc/pam.conf*.

See also:

[Authentication in the Connection Manager](auth.htm)\
Linux-PAM [web site](http://www.kernel.org/pub/linux/libs/pam/Linux-PAM-html)\
Sun Solaris PAM [web site](http://wwws.sun.com/software/solaris/pam)\
AIX PAM [web site](http://publib16.boulder.ibm.com/doc_link/en_US/a_doc_lib/aixbman/security/pam_overview.htm)\
man pam.conf\
man pam.d\
