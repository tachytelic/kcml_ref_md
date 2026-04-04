Working with Secure Sockets

Secure sockets, often called SSL or TLS, use public key encryption to secure a socket connection. They can verify the authenticity of the server using a server X509 certificate and they can optionally authenticate the client by using a client certificate. The encryption key is negotiated between the client and the server at the start of the conversation. There is a slight performance penalty for SSL conversations because of this CPU intensive negotiation, the less onerous stream encryption and the extra characters sent. For more details of the SSL/TLS protocol see the [RFC 2246](http://www.ietf.org/rfc/rfc2818.txt).

On [supported operating systems](SystemRequirements.htm) KCML supports SSL as either the client or the server using SSL v3 or TLS v1 protocols. It also supports the use of SSL on sockets that equire the initial connection to be plaintext and then switched into SSL following negotiation (e.g. the STARTTLS command in SSL enabled SMTP). This can be accomplished using the [KCML_Socket_SetSSL()](tmp/kintfld.htm#KCML_Socket_SetSSL) \$DECLARE.

Acting as a client

In the majority of cases all that is required is that the SSL=Y option is added. You need to add it after the IP address. Make sure the appropriate SSL enabled port is used. For instance the following program will read a page back from a secure website:


    DIM h,tx$0,rx$3000,nSent,nRead,nTimeout=5*1000,nPos,n
    h = OPEN "www.kcml.com:https,SSL=Y","@"
    IF (h > 0)
    REM opened OK
    REDIM tx$ = "GET / HTTP/1.1" & HEX(0D0A) & "Host: www.kcml.com" & HEX(0D0A) & "Accept: *" & HEX(0D0A) & "Connection: close" & HEX(0D0A 0D0A)
    nSent = WRITE #h,tx$
    IF (nSent > 0)
        REM test for reply
        nPos = 1
            WHILE TRUE DO
                n = $IF #h,nTimeout
                IF (n == 1)
                    nRead = READ #h,STR(rx$,nPos)
                    IF (nRead <= 0)
                        BREAK
                    END IF
                    nPos += nRead
                ELSE
                    BREAK
                END IF
            WEND
        END IF
        CLOSE #h
    END IF

Some connections require the client to identify itself using a certificate. The location of the certificate is specified by the **KSSL_CLIENT_CERT** enviroment variable.

Acting as a server

This is complicated by the fact that whereas certificates are optional for clients, they are required for servers. The location of the certificate is specified by the **KSSL_SERVER_CERT** enviroment variable.

When KCML acts as a server two sockets are involved. The first socket listens for connections which get accepted on the second socket. It is that second socket which needs the SSL=Y option set. So for example


    DIM hServer, n, h, nTimeout=60 * 1000
    hServer = OPEN ":9090,LCL=Y", "@"
    PRINT "waiting to connect"
    n = $IF #hServer, nTimeout
    IF (n == 1)
        PRINT "accept"
        h = OPEN $PRINTF("#%d,SSL=Y", hServer), "@"
    END IF
    n = WRITE #h, $PRINTF("Hello, I am your server today\r\n")

Certificates

On Unix systems the environment variables (**KSSL_CLIENT_CERT** or **KSSL_SERVER_CERT**) must point to the certificate file. The file must be in PEM format. The PEM format file must contain both the public key, the private key, and any certificates in the CA chain.

On Windows systems the environment variables can point to a PKCS12 (PFX) file containing certificates or into the windows system key store. Using the key store is very limited. The certificate must be in the *Current User* store and you can only search by the certificates SubjectString. To use the system store we must start the string with a '\*' followed by the certificate field to search for.


        ENV("KSSL_CLIENT_CERT") = "*SubjectString='GB, Berkshire, Hungerford, ADP DSI, KCML, MyCertificate'"

For more about how to obtain a suitable server certificate see this [page](SSLcert.htm).

Compatibility and System Requirements

SSL support was introduced with KCML version 6.20.

Operating as a client and server is supported on Windows 2000 and XP.

Client and server modes are supported on AIX5 and Linux provided [OpenSSL](http://www.openssl.org) is installed. Linux 2.6 versions of KCML 6.20+ will require OpenSSL 0.9.8, all other platforms, including Linux 2.4 & AIX5, require OpenSSL 0.9.7. The OpenSSL libraries are an optional component for AIX5. They can be installed from a set of RPMs on the **Linux Tools for PowerPC** disk.

See also:

[OPEN#](OPENhash.htm), [CLOSE#](CLOSEhash.htm), [READ#](READhash.htm), [WRITE#](WRITEhash.htm), [\$IF]($IF.htm), [\$OPTIONS#]($OPTIONShash.htm), [\$PRINTF(]($PRINTF.htm)\
[Programming sockets with KCML,](sockets.htm)\
[Creating SSL server certificates](SSLcert.htm)
