### SOAP support in KCML

[SOAP](http://www.w3.org/TR/SOAP/), or Simple Object Access Protocol, is an emerging standard for performing remote procedure calls across the Web. Originally proposed by DevelopMentor, Microsoft and UserLand, it has been enthusiastically adopted by other manufacturers such as IBM and the standard is now under the control of the [W3C](http://www.w3.org). Under the name Web Services it forms a core component of Microsoft .Net. Messages are formatted in XML and sent using standard Internet protocols such as HTTP. KCML 6.0 implements the [SOAP 1.1 specification](http://www.w3.org/TR/SOAP/) and is interoperable with both the [Apache SOAP](http://xml.apache.org/soap/index.html) implementation, the [Microsoft SOAP SDK version 2](http://msdn.microsoft.com/soap/default.asp) implementation, the Microsoft .Net implementation and the [KCML SOAP server](soapserver.htm). KCML now requires a SOAP server to support the [WSDL](http://www.w3.org/TR/wsdl) schema language for describing Web Services and thus will no longer work with the original Microsoft ROPE implementation or the original .NET beta which uses the old SDL schema language.

KCML can act as a client accessing methods exposed by other servers over the Web by HTTP. To do this it needs a URL for the [WSDL](#WSDL) description of the service required. This is in a standard URL format such as "http://www.stockquoteserver.com/stockquote.wsdl" and is passed as the second parameter to [CREATE](CREATE.htm) e.g.


    OBJECT s = CREATE "SOAP", "http://www.stockquoteserver.com/stockquote.wsdl"

This will be fetched by KCML when processing the CREATE statement. The schema file can be specified with an HTTP URL as in the example or it can be a local file which can be handy if the server does not publish WSDL on its site.

If the SOAP server is another KCML process then it's end point can be used, with the parameter ?WSDL and the [KCML SOAP server](soapserver.htm) will create the WSDL and return it. e.g.


    OBJECT s = CREATE "SOAP", "http://www.stockquoteserver.com/stockquote?WSDL"

To get documentation on a KCML SOAP server just point your browser at the end point URL and the server will return a page describing the web services available at that endpoint.

If the request has to cross a firewall then you need to specify the address of the proxy server using either the conventional [HTTP_PROXY](EnvVars.htm#HTTP_PROXY) environment variable or the PROXY keyword in the options string.

An optional third parameter to CREATE allows options such as the proxy server details to be supplied. See the [CREATE documentation](CREATE.htm#createopts) for a list of the available options.


    DIM wsdl$ = "http://localhost/soapdemo/services.asp"
    OBJECT s = CREATE "SOAP", wsdl$
    a$ = s.GetServerTime$()
    OBJECT s = NULL

You must free the client SOAP object when you are finished with it so that KCML can free up memory used to hold the WSDL schema.

There are some examples of calling web services from KCML on this [page](ExSOAPclient.htm).

<span id="WSDL"></span>

##### The role of WSDL

WSDL or Web Services Description Language is a [W3C](http://www.w3.org) standard defining how Web Services expose their methods. The KCML SOAP client uses WSDL to find the server and to discover how to frame the SOAP requests for the available method. The SOAP object browser in the KCML workbench uses WSDL to list the available methods and to enumerate their parameters and parameter types. The formal definition of the language is available [here](http://www.w3.org/TR/wsdl) but it is not necessary to know the language in order to be able to use a web service. Most SOAP implementations, including the KCML server implementation, will automatically generate a WSDL file describing their services. This file can be manually fetched and stored on the KCML client machine or it can be dynamically fetched when the CREATE statement instantiates a SOAP object. The former method will be faster but is less flexible.

If you are using the KCML client to access a Web Service that does not publish WSDL but does document the methods in some ad hoc fashion then you can use KCML's own SOAP server support to generate WSDL by writing stub DEFSUBs for the methods and using the [KCMLObjectExports](soapserver.htm#export) routine with the services actual endpoint to generate a WSDL file which can then be used on the client.

##### Document Based Service

Support for the document based services is provided. This requires the programmer to build and process data that is sent to and from the SOAP server. The methods calls in this mode only accept void or single string arguments. The argument string represents what will be added to the body of a SOAP request, and therefore must be valid XML. This functionality allows document style services, that specify and return variable argument counts, to be used. The return string will consist of the return values of a given method.


    DIM wsdl$ = "http://localhost/soapdemo/services.asp"
    OBJECT s = CREATE "SOAP", wsdl$, "DOC=Y"
    a$ = s.GetSomething$("<type1><arg0>1</arg0><arg1>2</arg1></type1>")
    OBJECT s = NULL

There is an example on this [page](ExSOAPclient.htm).

##### Cookies

HTTP Cookies generated by the server and sent as part of a response will be automatically added to any subsequent requests. They will persist as long as the SOAP Object. *Path* and *Expiry* times will be ignored.

The SOAP object supports the adding HTTP Cookies to requests. This is done using the method *\_AddCookie*. The method takes two arguments. A name/value pair for the cookie. The cookie will be generated for all subsequent requests. Using a blank string for value will remove an already set cookie.


    REM Add cookie
    s._AddCookie("name", "value")
    a$ = s.GetSomething$("<type1><arg0>1</arg0><arg1>2</arg1></type1>")

    REM Remove Cookie
    s._AddCookie("name", "")

##### Error messages

In the event of a problem there are three \$DECLARES implemented for error reporting subsequent to an O30 error. These are available at both the client and server ends of a SOAP interaction. This is in addition to the standard \$ERR mechanism.


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

##### Web Services Security

The SOAP client has partial support of the [OASIS Web Services Security (Version 1.0)](http://www.oasis-open.org/specs/index.php#wssv1.0) specification. This provides a security framework for SOAP messages. The support is limited to outgoing messages signed using RSA keys with x509 certificates as the security token.

Each outgoing message has a header added to the SOAP envelopes header section. This security header contains the certificate and a signature value generated from the SOAP message. The header information can then used by the message recipient to confirm the source of the message.

This support is controlled via the [CREATE](CREATE.htm#soap) "WSS" keyword. The value following the WSS keyword is a comma separated list of tokens and values that must be enclosed in brackets. The general format is shown below:


    WSS=(keyword:'value', keyword:'value', ...)

Supported keywords:\

| Token | Description |
|----|----|
| cfile | x509 Certificate file. The file can be in either PEM or a DER format. |
| pkfile | Private RSA key file. The file can be in either PEM or a DER format. |

\
Example of use in a CREATE statement:\


    OBJECT oSOAP = CREATE "SOAP", "myService.wsdl", "PROXY=user:passwd@proxy, WSS=(cfile:'myCertificate.x509', pkfile:'myPrivateKey.key')"

This is supported on AIX5 and Linux provided [OpenSSL](http://www.openssl.org) version 0.9.7 or later is installed. The OpenSSL libraries are an optional component for AIX5. They can be installed from a set of RPMs on the **Linux Tools for PowerPC** disk.

##### Debugging

KCML adds two properties for each SOAP object to aid debugging. These are **.Response\$** and **.Request\$**. These two scalar string properties provide access to the internal messages sent between the SOAP Client and Server. The **.Request\$** property contains the data sent when making a request of the SOAP server i.e. Invoke a method. The **.Response\$** is the reply received from a SOAP server. The length of each string property can be accessed by calling its numeric equivalent thus the length of the **.Response\$** string can be obtained by referencing **.Response**.

##### Restrictions

- The current implementation does not support passing named arrays or structures. Simple unnamed sequences can be passed in the request and the elements will be unrolled into separate arguments.
- There can only be one endpoint specified in the WSDL.
- The WSDL cannot use the import feature and must be canonically ordered.
- Only UTF-8 encoding is supported.
- Only a limited number of XSD types are supported (string, float, double, int, long, short, boolean, base64Binary, and dateTime)
