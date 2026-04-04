Secure Network Connections.

The Connection Manager, KCML and KClient are able to encrypt network traffic using the SSL/TLS protocols. <span id="secureconfig"></span>

Setting up a secure Connection Manager

Secure Connection Mode is supported in versions 6.20 and 6.90 of the Connection Manager for the Linux and AIX5 operating systems. AIX5 will require the OpenSSL Runtime package to be installed.

The default port for Secure Network Connections is 4790. This port number will need to be reserved in */etc/services*.\
For example:


    KCCSSL        4790/tcp         # KCML Connection Mgr with SSL

If the server is using [PAM](pam.htm) to authenticate, you will also need to register this network service. The PAM service name is a lower-case version of the network service name.\
\
Linux, just copy the PAM configuration file for the standard Connection Manager service:


    $ cd /etc/pam.d
    $ cp kcc kccssl

AIX5.3+, use the *addpam.ksh* script that is shipped with KCML:


    $ cd /usr/local/kcml
    $ ./addpam.ksh kccssl

Secure Connection mode is enabled by using the -x *SSLcert* flag in */etc/inetd.conf* or */etc/xinet.d/KCCSSL*\
\
Linux:


    # default: on
    # description: Kerridge Connection Manager
    service KCCSSL
    {
        flags           = REUSE NAMEINARGS
        socket_type     = stream
        wait            = no
        user            = root
        server          = /usr/local/kcml/kwebserv
        server_args     = /usr/local/kcml/kwebserv -x server.pem
        log_on_failure  += USERID
        disable         = no
        instances       = UNLIMITED
    }

AIX5:


    KCCSSL  stream  tcp     nowait  root    /usr/local/kcml/kwebserv  /usr/local/kcml/kwebserv -x server.pem

You will then need to refresh the *inetd* or *xinetd* daemon.

If the *SSLcert* argument for the -x flag is not an absolute pathname, as above, the Connection Manager will assume the SSL certificate is in the same directory as kwebserv. In this case, */usr/local/kcml/server.pem*. You can create an SSL certificate with the *openssl* utility, see [SSL Certificates](mk:@MSITStore:kcmlrefman.chm::/SSLcert.htm) for more information.

The SSL certificate should have read access for everyone:


    $ ls -l /usr/local/kcml/server.pem
    -rw-r--r--   1 root     system         2548 Nov 26 2009  /usr/local/kcml/server.pem

<span id="secureconnect"></span>

Using a Secure Connection Manager

KClient

To enable Secure Network Connections in KClient, choose the **Connect with encryption** option in the [Connection Page](mk:@MSITStore:kclient.chm::/connectionpage.htm), or use the **-l** command-line switch. When KClient is running in Secure Connection mode, it will use a default port number of 4790. This can be overidden, as always, by setting the **Service Port** on the [Options Page](mk:@MSITStore:kclient.chm::/optionspage.htm) or by using the **-V *port*** switch.

Web browser

The Connection Manager's built-in web browser and [Remote Adminstration Functions](adminfns.htm) can be accessed using a web browser that supports **https:**\
You would use a URL of the form:

https://myhost:4790

Applications that use the Connection Manager to serve documentation can make use of the [\$SERVER_HTTP_URI](webenvvar.htm) environment variable to constuct the \$HELPSERVER URL.\
For example:


    dim uri$16
    dim helpUrl$

    uri$=ENV("SERVER_HTTP_URI")
    IF (uri$ == " ")
      REM Not set, older version of kwebserv that did not support SSL, assume http:
      uri$="http:"
    ENDIF
    REDIM helpUrl$ = uri$ & "//" & ENV("SERVER_NAME") & ":" & ENV("SERVER_PORT") & "/" & ENV("SERVICE") & "/" & "Help"
    ENV("HELPSERVER") = helpUrl$

Applications can check if a secure connection is being used by inspecting the \$KSSL_SERVER_CERT environment variable.

If the Connection Manager is unable to negotiate a secure connection then a suitable error is reported to [syslog](mk:@MSITStore:kcmlrefman.chm::/syslog.htm).

##### See Also:

[Secure Sockets](mk:@MSITStore:kcmlrefman.chm::/SSL.htm) [SSL Certificates](mk:@MSITStore:kcmlrefman.chm::/SSLcert.htm) [SSL Error Codes](mk:@MSITStore:kcmlrefman.chm::/tmp/ksslerr.htm)
