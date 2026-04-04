CREATE

------------------------------------------------------------------------

<div class="Generalform">

General Form:

<div class="indent">

OBJECT *object_name* = CREATE *strexpr1* \[\[, *strexpr2*\] ...\]\

</div>

</div>

------------------------------------------------------------------------

The CREATE statement is used to instantiate a distributed object and return an object reference. KCML will act as a client to the object and can call methods exposed by it. There is no event or callback mechanism. No mechanism is provided to access properties or attributes directly though generally this can be done with accessor functions.

The type of object to create is specified with *strexpr1* and must be one of the following case insensitive strings

| *strexpr1* | Standard              | Object is accessed | Server OS       |
|------------|-----------------------|--------------------|-----------------|
| serverCOM  | [COM](ObjCOM.htm)     | by server          | Windows only    |
| clientCOM  | [COM](ObjCOM.htm)     | by client          | Unix or Windows |
| CORBA      | [CORBA](ObjCorba.htm) | by server          | Unix or Windows |
| SOAP       | [SOAP](ObjSoap.htm)   | by server          | Unix or Windows |
| Dynamic    | [KIDL](DynObj.htm)    | by server          | Unix or Windows |

There will be at least one, and maybe more, strings after the initial *strexp1* to specify the class of object and any further information required. The number and meaning depends on the type of object.

Creating COM objects

For [COM](ObjCOM.htm) objects the alpha expression *strexpr2* on the right must be either a ProgId or a string ClassId defining the object in the appropriate registry. For example


    OBJECT Doc = CREATE "ClientCOM","Word.Basic"
    OBJECT rsTable = CREATE "ServerCOM", "ADODB.Recordset"
    OBJECT rsTable = CREATE "ServerCOM","{00000535-0000-0010-8000-00AA006D2EA4}"

See the page on [COM automation](comautomation.htm) for more details about using COM objects in a KCML program.

Creating CORBA objects

For [Corba](ObjCorba.htm) objects the alpha expression *strexpr2* must be either the object name in the naming service, or an *Interoperable Object Reference* (IOR). KCML must know how to find the naming service with which the object is registered. There are two ways of specifying the location of the naming service, either using the [command line switch](kcml.htm) '-q' to KCML, or specifying additional arguments to CREATE. The exact syntax of the parameters depends on the ORB KCML is using.

Note that you can currently only connect to one ORB, so if you have already called CREATE before, or used the -q option, the additional arguments to CREATE are ignored.

An example using MICO would be:


    OBJECT Add = CREATE "Corba","Add", "-ORBNamingAddr", "inet:evb:9876" 

Or KCML could be started with "`kcml -q -ORBNamingAddr inet:evb:9876`", and the object created using only the name:


    OBJECT Add = CREATE "Corba","Add"
    OBJECT Add = CREATE "Corba","kerridge/my_context/Add/Object/"

The two object names above are equivalent, as KCML assumes a context name of "kerridge", with a type of "my_context" unless both the name and type are given, so if the object name is "Add", with a type of "Object", the name should be "Add/Object/"

Creating SOAP objects

For [SOAP](ObjSoap.htm) objects *strexpr2* represents the URL of the WSDL file describing the SOAP service. [WSDL](http://www.w3.org/TR/wsdl) is a schema language that describes SOAP services and the owner of the service should publish a WSDL schema describing the services on the site. The URL can be of type http:// or file://. If the string does not start with one of these prefixes it will be assumed to be a local file. KCML will attempt to connect to that server and fetch the WSDL file and use it to get the details it need to make procedure calls.

If a proxy server must be used to cross a firewall the proxy location should be specified with the environment variable HTTP_PROXY or with the Proxy keyword in the options string (see below). The proxy string has the format \[user\[:password\]@\]proxyserver\[:port\]. Not all proxy servers require a user and password. See below for an example.

The KCML SOAP client does support SSL/TLS encryption natively by using the *https* protocol prefix in the endpoint URL. It can also use an SSL tunnel like [stunnel](http://www.stunnel.org) to access an SSL site. This might run on the same server or on a different machine in your local network. The tunnel will listen out on one address and if connected to locally will open an SSL connection to the remote end point as specified in the tunnel configuration. The URL for the WSDL and the end points specified in the WSDL can be transparently remapped using the TUNNEL option.

An optional further string *strexpr3* can be used to specify options as a comma separated list of keyword and value pairs. The keywords themselves are case insensitive though their value may not be. Boolean options can be specified using 0, F or N for false and 1, T or Y for true.

<span id="createopts"></span>

| Keyword | Purpose | Example |
|----|----|----|
| AUTH | Basic authentication in the form username:password that may be required by the SOAP end point. | AUTH=soapuser:zrma78 |
| PROXY | The location of an HTTP proxy server and optionally any authentication required. Format is \[user\[:password\]@\]proxyserver\[:port\] | PROXY=proxy:8080 |
| TUNNEL | Allows mapping of a server and port combination to another server and port specified as TUNNEL=old\|new. Port numbers are optional and if omitted default to http i.e. 80. This can be used to redirect the SOAP request through an SSL tunnel. Both the WSDL URL and any endpoints in the WSDL are remapped. There may be more than one TUNNEL option specified. | TUNNEL=www.somesite.com:https\|localhost:4001 |
| MPOST | Boolean flag which if set to 1 specifies that the HTTP M-POST method should be used rather than the default POST. This may be needed to traverse certain firewalls. | MPOST=1 |
| RETRY | Integer value which specifies the number of times the client should retry a method call in the event of getting no response from the server. NOTE Retry can have unexpected side effects at the server. For example if the request increments a data value at the server before it fails, the retry could cause the data value to be incremented more then once. | RETRY=3 |
| DOC | (Deprecated) Use LIT=Y. Boolean flag which if set to 1 specifies that the SOAP client should operate in document mode. On method calls, in this mode, single scalar strings are passed to and from the server. The strings represent documents that the user is responsible for creating and decoding of received documents. KCML provides only the transport and error handling. | DOC=Y |
| LIT | Boolean flag which if set to 1 specifies that the SOAP client should operate in literal document mode. On method calls, in this mode, single scalar strings are passed to and from the server. The strings represent documents that the user is responsible for creating and decoding of received documents. KCML provides only the transport and error handling. | LIT=Y |
| WSS | Specifiy OASIS Web Services Security options. | See [here.](ObjSoap.htm#WSS) |

Creating Dynamic objects

[Dynamic objects](DynObj.htm) are shared libraries which expose interfaces described by a KCML specific XML interface description [language](dynidl.htm). Some examples available on the KCML website are the [Xerces](http://xml.apache.org/xerces-c/index.html) XML DOM parser and the [Xalan](http://xml.apache.org/xalan-c/index.html) XSLT transformer.

The required *strexp2* is the name of the shared library. It is not necessary to specify any extension as .DLL will be assumed for Windows, .so for Unix and .sl for HP-UX. The library, and any dependent libraries, must be available in the current working directory or on the path. On Windows they can also be in the Windows and the system directories. On Unix you should install them into */usr/local/lib*. This directory then needs to be added to the system's search path for shared libraries by setting the appropriate environment variable:

| Operating System | Variable        |
|------------------|-----------------|
| AIX              | LIBPATH         |
| HP-UX            | SHLIB_PATH      |
| All others       | LD_LIBRARY_PATH |

It is crucially important that the dependent libraries are available as this is the most likely reason for being unable to open a library.

To use dynamic objects on Unix platforms it may be necessary to set the [USEMALLOC](EnvVars.htm#USEMALLOC) environment variable before running KCML. This tells KCML to allocate memory in a way that will be consistent with the methods used in the library. This happens automatically on NT systems and this environment variable is unnecessary. CREATE will throw an O30.18 error on these Unix platforms if the variable is not set.

There are some examples of using Xerces DOM [here](xerces.htm)

Syntax examples:

OBJECT x = CREATE "clientCOM", "Excel.Application"\
OBJECT c = CREATE "Corba", "Add"\
OBJECT s = CREATE "SOAP", "http://services.xmethods.net/soap/urn:xmethods-CurrencyExchange.wsdl", "PROXY=fred:secret@firewall.bloggs.com:8080"\
OBJECT x = CREATE "Dynamic", "dyndom"
