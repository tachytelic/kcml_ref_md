SSL certificates

X509 certificates are used in SSL to identify the server and optionally the client and to provide a mechanism to exchange encryption keys securely. KCML is currently not supporting the use of certificates to identify the client but a KCML server using SSL will need a server certificate. The certificate has a public component and a private key. The latter is encrypted using a pass phrase and should not be revealed.

Certificates are digitally signed using the certificate of a Certificate Authority (CA) which guarantees their authenticity. This can be done in a chain through intermediate authorities. Provided all the certificates in the chain are provided in the exchange, the remote peer will be able to authenticate your certificate.

If you need to make your server public then you will probably want to pay to get your certificate signed by one of the root Cerrtificate Authorities such as [Thawte](http://www.thawte.com) or [Verisign](http://www.verisign.com). The public keys of these CAs are well known and already embeded in many SSL enabled applications such as web browsers. Visit their web site and follw their instructions for generating a request and submitting it. Once you have the signed server certificate skip forward to the section on deployment [here](#deploy). Note that these signed certificates expire, usually after a year, and will need to be renewed.

On the other hand, if your KCML server application only needs to authenticate to other KCML clients, and both are under your control, you could act as your own Certificate Authority and generate your own CA root certificate to sign the server certificate. You may well want to do this when testing. Because you are then not authenticating the certificate against a reliable third party CA there is the possibility that your server could be spoofed by a hacker but this may not matter. You do however get secure encryption of the traffic. Many applications, such as web browsers, will warn that the server cannot be securely identified but will allow you to continue the conversation.

OpenSSL

KCML uses the OpenSSL package on Unix and Linux platforms to provide encryption support. Most Linux distributions come with the OpenSSL cryptographic package. It is also available for other platforms including Microsoft Windows. If you don't already have OpenSSL, you can download it from [www.openssl.org](htpp://www.openssl.org). OpenSSL also provides the useful command line tool *openssl* which can be used to generate and sign certificates.

Certificate formats

Certificates are usually in one of three formats, PEM format, DER format and PKCS12 format. PEM format is usual with OpenSSL and in the Unix world. DER format is used in Java signing and PKS12 is used in the Microsoft world.

PEM format files contain blocks of base64 encoded text between start and end markers that are enclosed in dashes. Text outside the markers is ignored and is often used to provide a readable version of the certificate. Because the markers identify their contents one file can contain more than one certificate and/or key.

These examples use PEM format

Generating a CA root certificate with OpenSSL

A CA root certificate is a self-signed certificate that can be used to sign other certificates for your organization. It provides no guarantee of authenticity to your clients unless they they themselves have access to the root key and trust it. However it is sufficient for private networks and for testing.

We will first create the root CA certificate by generating a request file then signing it using the same commonName as the request. The server certificate is generated the same way but then signed with the root certificate. Finally we bundle both certificates into a PEM file.

When generating a request the program will ask for a pass phrase and will prompt for information about the certificate using defaults taken from the OpenSSL configuration file */usr/share/ssl/openssl.cnf*. As this is the root CA certificate we must use something like 'Root CA' for the commonName or CN field. You won't need the email or the 'extra' attributes.


    $ openssl req -newkey rsa:1024 -sha1 -keyout rootkey.pem -out rootreq.pem
    Generating a 1024 bit RSA private key
    ...............................++++++
    ................................................................++++++
    writing new private key to 'rootkey.pem'
    Enter PEM pass phrase:
    Verifying - Enter PEM pass phrase:
    -----
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [GB]:
    State or Province Name (full name) [Berkshire]:
    Locality Name (eg, city) [Newbury]:Hungerford
    Organization Name (eg, company) [My Company Ltd]:Kerridge Computers
    Organizational Unit Name (eg, section) []:KCML
    Common Name (eg, your name or your server's hostname) []:Root CA
    Email Address []:
     
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:
    $

We now need to sign the certificate. You need to enter the pass phrase you entered when you generated the root key in step 1. This certificate is set to expire in 1460 days or 4 years.


    $ openssl x509 -req -in rootreq.pem -sha1 -extensions v3_ca -signkey rootkey.pem -out rootcert.pem -days 1460
     Signature ok
     subject=/C=GB/ST=Berkshire/L=Hungerford/O=Kerridge Computers/OU=KCML/CN=Root CA
     Getting Private key
     Enter pass phrase for rootkey.pem:
    $

We can now consolidate the root certificate and its private key into one file for convenience.


    $ cat rootcert.pem rootkey.pem >root.pem

Generating the server certificate

Again we first create a request then we sign it. It is vital that you use the server's DNS name as the commonName field. The other address and company details should be the same as you used for the root. Once more we will need a new pass phrase for this key.


    $ openssl req -newkey rsa:1024 -sha1 -keyout serverkey.pem -out serverreq.pem
    Generating a 1024 bit RSA private key
    ...++++++
    ....++++++
    writing new private key to 'serverkey.pem'
    Enter PEM pass phrase:
    Verifying - Enter PEM pass phrase:
    -----
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [GB]:
    State or Province Name (full name) [Berkshire]:
    Locality Name (eg, city) [Newbury]:Hungerford
    Organization Name (eg, company) [My Company Ltd]:Kerridge Computers
    Organizational Unit Name (eg, section) []:KCML
    Common Name (eg, your name or your server's hostname) []:testserver.kerridge.com
    Email Address []:
     
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:
    $

To sign the request we type


    $ openssl x509 -req -in serverreq.pem -sha1 -extensions usr_cert -CA root.pem -CAkey root.pem -CAcreateserial -out servercert.pem -days 1460
     Signature ok
     subject=/C=GB/ST=Berkshire/L=Hungerford/O=Kerridge Computers/OU=KCML/CN=testserver.kerridge.com
     Getting CA Private Key
     Enter pass phrase for root.pem:
    $

The pass phrase asked for it the first one used to create the root key. We now have our server certificate.

The server certificate pass phrase

The request process requires you to associate a pass phrase with the request to encrypt the private key. However with unattended servers it is not always possible to apply this pass phrase. You can drop the pass phrase by copying the file and typing


    # cp serverkey.pem serverkey.pem.org
    # openssl rsa -in serverkey.pem.org -out serverkey.pem

You need to know the pass phrase on the request for this. The only protection for the key is now the normal Unix security on the file so it should be chmoded to be readable only by the KCML user under which the server executes.

Deploying signed certificates

To use a certificate on the server KCML expects a file containing both the certificate part of the public signed certificate and the private key we generated with the request. If this is a locally signed certificate you will want to add the chain of CA certificate(s) used to sign it. We then need to put the combined file into a secure location pointed to by the **KSSL_SERVER_CERT** environment variable. This environment variable should be set in the appropriate section of the kconf.xml KCML configuration file.


    $ cat servercert.pem serverkey.pem rootcert.pem >server.pem

See also:

[Secure sockets with SSL](SSL.htm)\
[Programming sockets with KCML](sockets.htm)
