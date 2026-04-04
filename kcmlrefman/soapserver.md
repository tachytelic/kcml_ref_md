### Acting as a SOAP Server

- [Exporting the interface](#export)
- [WSDL conventions](#wsdlconv)
- [Error messages](#error)
- [Access to HTTP header lines](#http)
- [Running the KCML server from Connection Manager](#cm)
- [Running the KCML server as a Unix daemon](#unixdaemon)
- [Running the KCML server as an NT service](#ntservice)
- [Invoking KCML from Apache Server](#apache)
- [KCML session variables](#sessionvariables)
- [Developing KCML SOAP server programs](#development)
- [Security implications](#security)

KCML can act as a server for methods exposed through the [SOAP protocol](ObjSoap.htm). This is in addition to client support available through the [CREATE](CREATE.htm#soap) statement. A KCML SOAP server can either run as a standalone daemon or be invoked by a web server such as [Apache](http://www.apache.org).

In both cases it is given a program to run on the command line and, once started, the KCML instance loads the program, executes any initialization code and runs until it reaches a [\$BREAK!]($BREAK.htm) whereupon it will block awaiting a request. During the initialization the program can open files, overlay, attach to a global library or load libraries as necessary. It must execute a ['KCMLObjectExport()](tmp/kintfld.htm#KCMLObjectExport) [\$DECLARE]($DECLARE.htm) call during this initialization or the \$BREAK will error. When it blocks on the \$BREAK! the [DEFSUB](DEFSUB.htm)s that will be exposed as methods must be visible in the foreground program. When the client object is destroyed the TCP/IP connection to the server will be broken and KCML will exit the \$BREAK! allowing a tidy closedown of the server.

The current implementation for [DEFSUB](DEFSUB.htm) expects all parameters to be passed as strings or numerics and it can return a string or a numeric result. BYREF and REDIM parameters are supported, as are optional string and numeric parameters. However BYREF strings should be scalars and not arrays as SOAP provides no dimensioning information. Any returned string is limited to about 64kb.

##### <span id="export">Exporting the interface</span>

After any initialization code has been executed call the internally defined ['KCMLObjectExport()](tmp/kintfld.htm#KCMLObjectExport) \$DECLARE to specify the prefix used on the public methods. All the methods published by the server will have corresponding DEFSUBs in the program with the method name prefixed by some common prefix. This prefix is called the **interface**. By convention the interface also forms part of the endpoint URL. So for a method called gettime() we might have server code like


    ...
    DIM interface$="pjcsoaptest"
    DIM endpoint$0, wsdl$0
    REDIM endpoint$="http://www.pjcserver.com/" & interface$
    REDIM wsdl$="htdocs/" & interface$ & ".wsdl"
    'KCMLObjectExport("SOAP", interface$, wsdl$, endpoint$)
    ...
    $BREAK!
    $END

    DEFSUB 'pjcsoaptest_gettime$()
        REM return local time as a HHMMSSCC string
        RETURN TIME
    END SUB

The first argument to 'KCMLObjectExports must be "SOAP" for a SOAP server and there can be up to four arguments in total.

| Arg# | Purpose |
|----|----|
| 1 | Must be "SOAP" |
| 2 | The interface name. Only subroutines whose name is prefixed by the interface name and an underscore can be exposed through SOAP. This prevents access to private routines in the program. |
| 3 | WSDL local filename. If this is nonblank then KCML will scan the program for DEFSUBs that start with the interface name and will create a WSDL file with this name describing the calling interface. As this is an expensive operation it is suggested that this is not done on every invocation but only when a WSDL file must be regenerated due to changes in the program. If a filename is given the program should then terminate rather than go on to execute a \$BREAK. If blank then no WSDL is created and the program can go on to \$BREAK! and to listen out for the incoming SOAP requests. |
| 4 | The actual endpoint URL for the SOAP server e.g. http://localhost:800/soaptest. This is only needed to create the WSDL file. If the WSDL file is created dynamically in response to a GET request it is inferred from the URL of the GET (see below). |

The KCML SOAP server can create the WSDL on the fly, in response to a HTTP GET request to the endpoint, with a parameter of WSDL. For this to work the end point directory name should be the same as the interface. This example might be accessed by some client code of the form


    OBJECT s = CREATE "SOAP", "http://pjcserver.com/pjcsoaptest?WSDL"
    PRINT "The time is ";s.gettime$()
    OBJECT s = NULL

A GET request to the end point, by a browser for instance, will return an HTML page describing the web services exposed at the site.

##### <span id="wsdlconv">WSDL conventions</span>

When generating the WSDL file KCML follows certain conventions:

- Every method has an associated [soapAction](http://www.w3.org/TR/SOAP/#_Toc478383528) which is checked at runtime. The action string is formed from the concatenation of the interface name, a \# sign and the method name.
- The method namespace has the form "urn:kcml-" followed by the interface name.
- The parameter names are the argument symbol names from the DEFSUB line with any \$ suffix dropped.
- All methods are presumed to have a return value which is named "Result"
- All parameters are typed as either string or double as appropriate.

##### Implementation specifics

- The maximum size of a response must be 64kb or less
- If a string contains any characters between HEX(00) and HEX(1F) it will be typed as xsd:base64Binary not xsd:string
- There can be at most 16 BYREF parameters
- BYREF string arrays are not supported. Use scalar strings instead.
- There is limited support for default parameters provided the defaults are simple literal numbers and strings.

##### <span id="error">Error messages</span>

All the SOAP \$DECLARE calls will return TRUE if they are sucsessful and FALSE if they fail. It is good programming practice to check the return codes from all subroutines, however in the interests of brevity none are checked in the examples on this page.

In the event of a problem there are three \$DECLARES implemented for error reporting. These are available at both the client and server ends of a SOAP interaction.


    $DECLARE 'KCMLObjectGetLastError(STR(), RETURN INT())="*"
    $DECLARE 'KCMLObjectGetLastErrorString(STR(), RETURN STR())="*"
    $DECLARE 'KCMLObjectGetErrorString(STR(), INT(), RETURN STR())="*"
    ...
    'KCMLObjectGetLastError("SOAP", error_number)

Returns the last SOAP error number.


    'KCMLObjectGetLastErrorString("SOAP", error_text$)

Returns the last SOAP error text.


    'KCMLObjectGetErrorString("SOAP", error_number, error_text$)

Returns the error text for a given error number.

##### <span id="http">Access to HTTP header lines</span>

The HTTP header lines that accompany the envelope in a SOAP request can be accessed via the 'KCMLObjectGetHttpLine() \$DECLARE. The HTTP header lines sent with the SOAP response can be changed via the 'KCMLObjectSetHttpLine() \$DECLARE. New lines can also be added to the response with this call. The [Apache Server](#apache)'s [mod_kcml](mod_kcml.html) passes the HTTP lines to/from browsers unchanged, so these calls can be used to communicate with browsers connected to the KCML SOAP server. This could be used, as in the example below, to create a cookie on the browser.


    $DECLARE 'KCMLObjectGetHttpLine(STR(), STR(), RETURN STR())="*"
    $DECLARE 'KCMLObjectSetHttpLine(STR(), STR(), STR())="*"
    ...
    'KCMLObjectGetHttpLine("SOAP", "Accept-Language", language_text$)
    REM I now know the browser's language
    ...
    'KCMLObjectSetHttpLine("SOAP", "Set-Cookie", "temporary_test_cookie=test")

##### <span id="cm">Running the KCML server from the Connection Manager</span>

Running from the [Connection Manager](mk:@MSITStore:kwebserv.chm::/websoap.htm) has the advantage of being operating system independent and providing a common environment shared with interactive sessions. An existing service can be reused for starting a number of different SOAP servers in the same environment by defining a list of **\<soapservice\>** directives in kconf.xml under the **\<service\>** node. Each soapservice has a base **\<url\>** tag that is used to identify the SOAP interface. The value of the **\<start\>** tag is used to define the name of the program to be run for SOAP requests. The environment variable [SOAPSTART](EnvVars.htm#SOAPSTART) will be set to this value. The regular [START](EnvVars.htm#START) environment variable will be disregarded. The CM service name should be encoded in the SOAP endpoint URL as the first component. The second component of the URL will be the value of the SOAP service's base \<url\> tag.\
For example, if the SOAP service *KCMLSOAPService* was added to the CM service *myApp*, then you would connect to the SOAP service using the URL **http://pjcserver.com:790/myApp/KCMLSOAPService**

##### <span id="unixdaemon">Running the KCML server as a Unix daemon</span>

You first need to allocate a port number to use. This should not be used by any other service and should probably be greater than 1024 as on Unix systems these ports are reserved for the superuser. The server should be started with the -b command line switch indicating that it is a SOAP server and the -p switch specifying the program to run. STR([\$MACHINE]($MACHINE.htm), 58,1) is set by the -b switch indicating to application programs that they are running as a SOAP server.

On Unix add a line to /etc/services for the port, say on 8081,


    kcmlsoap    8081/tcp

and add the following to /etc/inetd.conf


    kcmlsoap    stream  tcp     nowait  soapuser    /usr/lib/kcml/kcml      /usr/lib/kcml/kcml -b -p /home/pjc/SOAPSVR.kcml

This example shows the server being run as the user soapuser rather than root. The KCML process persists, serving only requests from the client that caused inetd to create it, until that client terminates it by code of the form,


    OBJECT s = NULL

At which point the SOAP server program continues execution with the statement after its [\$BREAK!]($BREAK.htm)

##### <span id="ntservice">Running the KCML server as an NT service</span>

This is best done through the Kerridge service administrator. Add a service using the Services\|Add... menu and select KCML as the service provided. Click the Listen radio button and set the port to be the chosen port. Remember to use that port number in the client's endpoint URL.

##### <span id="apache">Invoking KCML from Apache Server</span>

KCML is connected to [Apache](http://www.apache.org) through the [mod_kcml](mod_kcml.html) Apache module. Separate documentation on installing and configuring [mod_kcml](mod_kcml.html) comes with that product.

Running KCML SOAP servers through Apache's [mod_kcml](mod_kcml.html) has several advantages.

- The KCML processes are persistent and can service requests from any client. This gives better performance.
- Apache creates the appropriate number of daemon processes and KCML processes for the current load, adding and removing processes as required.
- Apache offers resilience to crashes, as it will start new processes to replace failed ones.
- In addition to SOAP clients, browsers can access KCML SOAP server methods by URL. SOAP request parameters can be added to the URL. The SOAP response can be returned to the browser as text.
- KCML session variables are implemented by [mod_kcml](mod_kcml.html) and a small cookie on the browser.
- Apache Server can be run on the KCML Database machine or on a machine of its own. Any number of KCML SOAP servers can be connected, on the Web Server machine or any other machines, Unix or NT.

Running KCML SOAP servers through Apache's [mod_kcml](mod_kcml.html) enables the creation of high performance web applications. It allows the integration of a KCML Database and a web site, using (existing) business logic written in KCML.

##### <span id="sessionvariables">KCML session variables</span>

KCML session variables are only implemented when invoking a KCML SOAP server from a browser through the [Apache](http://www.apache.org) module [mod_kcml](mod_kcml.html) They implement a persistent-state in the KCML SOAP server through the use of a browser cookie. The following \$DECLARE calls are used to create/delete sessions and to access the variables of the session.


    $DECLARE 'KCMLObjectSetSessionState(STR(), INT(), STR())="*"
    $DECLARE 'KCMLObjectSetSessionString(STR(), STR(), STR())="*"
    $DECLARE 'KCMLObjectGetSessionString(STR(), STR(), RETURN STR())="*"
    $DECLARE 'KCMLObjectSetSessionNum(STR(), STR(), NUM())="*"
    $DECLARE 'KCMLObjectGetSessionNum(STR(), STR(), RETURN NUM())="*"

The unique session name, and its scope are passed to/from mod_kcml via an HTTP line, eg,


    KcmlSession: id=14-40-19_273-15429 path=/session/test

An example of code to test for the existence of a session and create a new one, if one does not already exist follows. The trace routines are listed [below.](#trace)


    LOCAL DIM rc
    LOCAL DIM line$256
    'TraceMsg(1, "SOAP server: 'testSession_login called")
    REM has the user logged in yet?
    'KCMLObjectGetHttpLine("SOAP", "KcmlSession", BYREF line$)
    IF (STR(line$,, 3) == "id=")
        REM existing session
        'TraceMsg(1, "SOAP server existing session", STR(line$, 4))
    ELSE
        'TraceMsg(1, "SOAP server creating session")
        REM create new session, with scope "/session"
        'TraceMsg(1, "SOAP server new session")
        'KCMLObjectSetSessionState("SOAP", 1, "/session/test")
    END IF

The second parameter to 'KCMLObjectSetSessionState() can be 1 for create or 2 for delete. 1 will create a unique id for a session, create a session and [Apache Server](#apache)'s [mod_kcml](mod_kcml.html) adds a Set-Cookie HTTP line to the response sent to the browser. 2 will delete the session and tell the browser that the cookie has expired.

The third parameter is the scope of the session and the **path=** of the cookie. The browser will only send the cookie - and so the session will only be available for the given path, or subdirectories of it. If you are unsure about this, and only require one session for the site this can be set to "/".

Once a session has been created, session variables can be added to it at any time with the following type of code. The second parameter is the session variables name, the third parameter is the KCML variable.


    REM add and set a couple of session variables for username$ and password$
    'KCMLObjectSetSessionString("SOAP", "user", username$)
    'KCMLObjectSetSessionString("SOAP", "pass", password$)
    'KCMLObjectSetSessionNum("SOAP", "id", idNumber)
    REM add another session variable - just to test
    'KCMLObjectSetSessionString("SOAP", "extra", " ")

Once a session and its session variables have been created the session variables can be accessed with the following type of code.


    REM get the session variables for username$, password$ and extra$
    'KCMLObjectGetSessionString("SOAP", "user", BYREF username$)
    'KCMLObjectGetSessionString("SOAP", "pass", BYREF password$)
    'KCMLObjectGetSessionNum("SOAP", "id", BYREF idNumber)
    'KCMLObjectGetSessionString("SOAP", "extra", BYREF extra$)

The session variables are held by [Apache Server](#apache)'s [mod_kcml](mod_kcml.html) on the Web Server machine. The session variables are not sent to the browser and back in the cookie as this would be slower and could have security implications. The cookie's name and unique short value is all that is used.

The current implementation only supports string and numeric session parameters.

##### <span id="soapstyle">SOAP message style</span>

The WSDL specification allows for two message styles

- RPC or remote procedure call
- Document

The RPC style is the default for the KCML SOAP server. It exposes KCML DEFSUB statements as external methods that the client can invoke passing arguments and getting a response. Usually the messages have the types of the arguments specified in the XML rather than inferred from the WSDL. This style is called RPC/encoded and is again the default for KCML.

However many applications today just want to pass XML over SOAP and for that the Document style is to be preferred. This is the style used by Microsoft .NET exclusively. The messages correspond to XML documents specified in a schema section of the WSDL and do not map onto method arguments. Generally there will be one XML argument and one XML return value. Document style can be encoded but this style is deprecated and the Document/literal style where the WSDL defines the document is the normal style.

To use Document/literal with the KCML SOAP server the DEFSUB name must match the pattern interface_wdl_method rather than the RPC encoded pattern interface_method.

If the DEFSUB returns a string and the method name has a prefix of "xml" then KCML will type the method as returning xsd:anyType in the schema of the WSDL rather than xsd:string. The prefix is not exposed in the WSDL. A similar convention applies to any string argument to the DEFSUB.


    PUBLIC DEFSUB soapserver_wdl_xmlGetPurchaseOrder$(xmlPO$)

##### <span id="soapbody">SOAP Body</span>

If SOAP is being used as a general messaging transport the contents of the request message, the response message or both may be arbitrarily complex. To allow an application the ability to parse the XML directly it can get the whole of the Body section from the request with a \$DECLARE call. Similarly it can specify the entire body for the response over riding the normal method return.


    $DECLARE 'KCMLObjectGetBody(STR(), RETURN STR())="*"
    $DECLARE 'KCMLObjectSetBody(STR(), STR())="*"

##### <span id="soapheader">SOAP Header</span>

The SOAP specification allows for an optional \<Header\> section in front of the \<Body\> section of both the request and the response. The KCML SOAP server exposes two \$DECLARE calls to get any header from the request and to add such a section in the response.


    $DECLARE 'KCMLObjectGetHeader(STR(), RETURN STR())="*"
    $DECLARE 'KCMLObjectSetHeader(STR(), STR())="*"

If there was no header section in the request then 'KCMLObjectGetHeader() will return an empty string.

##### <span id="development">Developing KCML SOAP server programs</span>

KCML SOAP server programs can be developed on the KCML Database machine using the normal development environment of KClient and the KCML Workbench. Obviously the network connection, [Apache Server](#apache)'s [mod_kcml](mod_kcml.html) and any XML or HTML produced can't be tested this way, but the KCML Database and (existing) business logic can. STR([\$MACHINE]($MACHINE.htm), 58,1) is set by the -b switch, so application programs can tell if they are in development/debug mode or are running as a SOAP server. See code below.

KCML session variables are implemented. They are held by KCML rather than by [mod_kcml](mod_kcml.html) and work as the KCML session persists.

The implemented SOAP server runs as a daemon process, so producing a trace log of its activity can be useful for finding subtle problems with its logic. Suitable trace routines are listed [below.](#trace)


    DIM _SoapServer$1=HEX(01), mode$1
    mode$ = STR($MACHINE, 58, 1) AND _SoapServer$
    REM check to see if we are running as a SOAP server
    IF (mode$ == _SoapServer$)
        REM SOAP server mode
        REM SOAP server initialisation code
        REM enable trace for tests
        TraceLevel = 6
        'TraceMsg(1, "SOAP server daemon started")
        REM specify interface and action
        'KCMLObjectExport("SOAP", "testSession", "/session/test")
        REM go to sleep waiting for a request
        $BREAK !
        REM asked to terminate, or socket closed
        REM SOAP server shutdown code
        'TraceMsg(1, "SOAP server daemon stopped running")
        'TraceClose()
    ELSE
        REM debug/develop, enable forms emulation mode
        STR($OPTIONS, 45, 1) = AND HEX(08)
        REM open the main logic testing form
        testSession_formLogin.Open()
        END IF
        REM Terminate
    ENDIF
    $END 

##### <span id="trace">Trace routines</span>


    REM Global variables and their default values for trace routines
    DIM TraceStream=0, TraceLevel=6, TraceFile$256="/disk4/tmp/kcmlSOAP.log", TraceMode$="a+"
    ...

    ...
    REM debug trace message routines
    DEFSUB 'TraceMsg(level, message$, arg1$ = " ", arg2$ = " ", arg3$ = " ", arg4$ = " ", arg5$ = " ", arg6$ = " ", arg7$ = " ", arg8$ = " ", arg9$ = " ")
        LOCAL DIM stamp$20
        IF (level <= TraceLevel)
            IF (TraceStream == 0)
                GOSUB 'TraceOpen()
            END IF
            stamp$ = BIN(VAL("0") + level) & " " & STR(TIME,, 2) & ":" & STR(TIME, 3, 2) & ":" & STR(TIME, 5, 2) & " (......) "
            CONVERT #PART TO STR(stamp$, 13, 6), (######)
            PRINT #TraceStream, stamp$,message$,arg1$,arg2$,arg3$,arg4$,arg5$,arg6$,arg7$,arg8$,arg9$
        END IF
    END SUB

    DEFSUB 'TraceOpen()
        IF (TraceStream <> 0)
            CLOSE #TraceStream
        END IF
        TraceStream = OPEN TraceFile$, TraceMode$
        'TraceMsg(1, "SOAP server daemon trace started")
    END SUB

    DEFSUB 'TraceClose()
        IF (TraceStream <> 0)
            'TraceMsg(1, "SOAP server daemon trace stopped")
            CLOSE #TraceStream
            TraceStream = 0
        END IF
    END SUB

##### <span id="security">SOAP security</span>

SOAP is essentially a Web application, so all the security fundamentals that apply to Web applications apply to SOAP servers. The SOAP specification makes no direct reference to authentication or authorization and these are presumed to be layered into the transport or handled by the application. Clearly the client must be able to support what the server uses.

The typical approach would be to use use SSL to authenticate the server and to provide encryption on the HTTP transport which will, in turn, permits authentication of the client using standard HTTP basic authentication. Basic authentication is the only widely supported authentication scheme but because the passwords are not strongly encrypted, it should not be used without SSL. The virtual directory used for the endpoint should be configured as requiring basic authentication so the KCML [Connection Manager](#cm), Apache or MS IIS will check for the presence of authentication header lines in the incoming request and send a suitable 401 error if missing or incorrect.

- For the Connection Manager you should add a soapauth directive to the service with a value of TRUE.
- On Apache you need to set the AuthName, AuthType, AuthUserFile and AuthUserGroup directives for the virtual directory.
- On IIS5 you right click the directory, select Properties and change the Anonymous Access and Authentication properties of the directory.

The SOAP client will need to specify the username and password as properties e.g. with the KCML SOAP client using [CREATE](CREATE.htm)


    OBJECT s = CREATE "SOAP", "http://someserver/someservice?WSDL","Auth=fred:secretpwd"

Other clients will have similar properties.

The KCML program should check the request's HTTP headers looking for the **Authorization** line using the **'KCMLObjectGetUsername()** \$DECLARE.


    $DECLARE 'KCMLObjectGetUsername(STR(),RETURN STR(),INT())="*"
    DIM user$32,rc
    rc = 'KCMLObjectGetUsername("SOAP", user$, FALSE)

The name will be blank if BASIC authentication is not in use. Remember don't use this simple scheme unless you are encrypting the link with SLL. This need only be done once as the user name and other details inferred from it should be transferred to a session variable. To be extra secure you should then blank any variables used in determining the userid as this KCML instance will be reused by other clients.

The last argument is a boolean flag which, if TRUE, will cause KCML to check the userid and password against the password file for the server. This can be used if you cannot use authentication on the web server or if you are connecting directly to a KCML SOAP server without using a web server. If the supplied userid and password are incorrect the function will delay for a short period. The return values of the 'KCMLObjectGetUsername() call are:

| Value | Meaning                                                       |
|-------|---------------------------------------------------------------|
| 0     | Found a user name and if requested, successfully validated it |
| 1     | Invalid userid and password                                   |
| 2     | Password expired or must be set interactively                 |
| 3     | Missing BASIC authorization HTTP header                       |
| 4     | Buffer too small for username                                 |
| 5     | Not running as a SOAPserver                                   |
| 6     | Wrong parameters supplied to \$DECLARE                        |
| 7     | Unknown error                                                 |
