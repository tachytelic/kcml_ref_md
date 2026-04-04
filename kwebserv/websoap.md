<span id="soap"></span>

SOAP services

A Connection Manager [service](systemconf.htm#services) can define an optional list of SOAP services. Each SOAP service has the following attributes:

| Name          | Optional | Purpose                                           |
|---------------|----------|---------------------------------------------------|
| URL           | No       | Base URL of the SOAP service                      |
| Start program | No       | Pathname of the KCML SOAP server program          |
| User ID       | Yes      | UNIX user account used to execute the SOAP server |
| Environment   | Yes      | List of environment variables                     |

The URL that is used to connect to the SOAP service will be of the form **http://hostname:790/serviceName/baseUrl**. When a HTTP request is made to the connection manager, and the URL matches the above patten, KCML will be executed in [SOAP server](mk:@MSITStore:kcmlrefman.chm::/soapserver.htm) mode via the [-b flag](mk:@MSITStore:kcmlrefman.chm::/kcml.htm). If the URL of the HTTP request is not of the form **http://hostname:790/serviceName/baseUrl**, then it is passed on to the built in [web server](aliases.htm).

The file name of the KCML program that will service SOAP requests is defined in the **Start program** field. The Connection Manager will use this to set the [\$SOAPSTART](mk:@MSITStore:kcmlrefman.chm::/EnvVars.htm#SOAPSTART) environment variable. The set of environment variables that the SOAP server program inherits will be taken from the service's \<environment\> section as well as the \<general\> list of variables. The SOAP service can define extra environment variables, these will override any previous values.

The Connection Manager will also set the \$PATH_INFO, \$SERVER_NAME, \$SERVER_PORT, \$QUERY_STRING CGI environment variables, so that the SOAP server program can reconstruct URLs.\
For example:


    soapUrl$ = "http://" & ENV("SERVER_NAME") & ":" & ENV("SERVER_PORT") & "/" & ENV("SERVICE") & "/" & ENV("PATH_INFO") & "?" & ENV("QUERY_STRING")

On Unix systems, an optional **User ID** can be set. The will cause the SOAP server to be executed under the user's account, instead of being executed by the **root** user.

The list of SOAP services can be defined in an XML include file. When using the [Display/Update services](systemconf.htm#services) page, you can reference an include file by setting the **URL** to *include* and the **Start program** to the pathname of the include file. The Connection Manager wille expand any environment variables that are in the include file's pathname.

**For systems that use the \<soapstart\> tag, see [Converting SOAP services](oldsoap.htm)**

##### See Also:

[KCML SOAP servers](mk:@MSITStore:kcmlrefman.chm::/soapserver.htm) [Connection Manager Environment variables](webenvvar.htm) [Serving web pages](aliases.htm)
